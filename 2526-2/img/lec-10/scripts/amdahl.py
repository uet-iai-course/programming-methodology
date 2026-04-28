"""
Sinh SVG biểu đồ Định luật Amdahl cho slide lec-10.

Công thức: speedup(s, n) = 1 / (s + (1 - s) / n)
- s: tỷ lệ phần tuần tự (không song song được)
- n: số lõi
- speedup tối đa khi n → ∞ là 1/s

Vẽ 3 đường cong cho s ∈ {5%, 10%, 25%}, trục x = số lõi (1..16),
trục y = speedup. Đầu ra: 2526-2/img/lec-10/amdahl.svg

Chạy:
    cd 2526-2/img/lec-10/scripts
    python3 amdahl.py
"""
from __future__ import annotations

import os
from pathlib import Path

# ----- Tham số -----
N_MAX = 16                                # Số lõi tối đa trên trục x
S_VALUES = [(0.05, "#2e7d32", r"s=5%"),   # (s, màu, nhãn)
            (0.10, "#1565c0", r"s=10%"),
            (0.25, "#c62828", r"s=25%")]
Y_MAX = 20                                # Speedup tối đa hiển thị trên trục y

# Khung SVG (logic coordinates) — tỷ lệ rộng/cao tương đối
SVG_W = 480
SVG_H = 320

# Padding chừa trục + nhãn
PAD_L = 56          # lề trái cho nhãn trục y
PAD_R = 80          # lề phải cho legend
PAD_T = 24          # lề trên
PAD_B = 50          # lề dưới cho nhãn trục x

# Vùng vẽ (data area)
PLOT_X = PAD_L
PLOT_Y = PAD_T
PLOT_W = SVG_W - PAD_L - PAD_R
PLOT_H = SVG_H - PAD_T - PAD_B


def speedup(s: float, n: float) -> float:
    """Công thức Amdahl: 1 / (s + p/n) với p = 1 - s."""
    return 1.0 / (s + (1.0 - s) / n)


def x_to_px(n: float) -> float:
    """Map số lõi (1..N_MAX) → toạ độ x trong SVG."""
    return PLOT_X + (n - 1) / (N_MAX - 1) * PLOT_W


def y_to_px(speedup_val: float) -> float:
    """Map speedup (0..Y_MAX) → toạ độ y trong SVG (đảo chiều: y=0 ở đỉnh)."""
    return PLOT_Y + PLOT_H - (speedup_val / Y_MAX) * PLOT_H


def build_path(s: float) -> str:
    """Sinh path 'M x0 y0 L x1 y1 L x2 y2 ...' cho đường cong speedup theo s."""
    points = []
    # Vẽ ở các giá trị n = 1, 2, ..., N_MAX (đường gấp khúc — đủ mượt khi N_MAX nhỏ)
    for i in range(N_MAX):
        n = 1 + i  # n = 1..N_MAX
        sp = speedup(s, n)
        x = x_to_px(n)
        y = y_to_px(min(sp, Y_MAX))
        cmd = "M" if i == 0 else "L"
        points.append(f"{cmd} {x:.1f},{y:.1f}")
    return " ".join(points)


def build_svg() -> str:
    parts: list[str] = []

    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {SVG_W} {SVG_H}" '
        f'style="font-family: serif; max-width: 100%; height: auto;">'
    )

    # ----- Trục x, y -----
    # Trục x (dưới)
    parts.append(
        f'<line x1="{PLOT_X}" y1="{PLOT_Y + PLOT_H}" '
        f'x2="{PLOT_X + PLOT_W}" y2="{PLOT_Y + PLOT_H}" '
        f'stroke="#333" stroke-width="1.5"/>'
    )
    # Trục y (trái)
    parts.append(
        f'<line x1="{PLOT_X}" y1="{PLOT_Y}" '
        f'x2="{PLOT_X}" y2="{PLOT_Y + PLOT_H}" '
        f'stroke="#333" stroke-width="1.5"/>'
    )

    # ----- Tick + nhãn trục x -----
    x_ticks = [1, 4, 8, 12, 16]
    for n in x_ticks:
        x = x_to_px(n)
        parts.append(
            f'<line x1="{x:.1f}" y1="{PLOT_Y + PLOT_H}" '
            f'x2="{x:.1f}" y2="{PLOT_Y + PLOT_H + 4}" stroke="#333"/>'
        )
        parts.append(
            f'<text x="{x:.1f}" y="{PLOT_Y + PLOT_H + 18}" '
            f'text-anchor="middle" font-size="13" fill="#555">{n}</text>'
        )
    parts.append(
        f'<text x="{PLOT_X + PLOT_W / 2:.1f}" y="{PLOT_Y + PLOT_H + 38}" '
        f'text-anchor="middle" font-size="14" fill="#333">Số lõi (n)</text>'
    )

    # ----- Tick + nhãn trục y -----
    y_ticks = [0, 5, 10, 15, 20]
    for sp in y_ticks:
        y = y_to_px(sp)
        parts.append(
            f'<line x1="{PLOT_X - 4}" y1="{y:.1f}" '
            f'x2="{PLOT_X}" y2="{y:.1f}" stroke="#333"/>'
        )
        parts.append(
            f'<text x="{PLOT_X - 8}" y="{y + 4:.1f}" '
            f'text-anchor="end" font-size="13" fill="#555">{sp}</text>'
        )
    # Nhãn trục y (dọc)
    parts.append(
        f'<text x="14" y="{PLOT_Y + PLOT_H / 2:.1f}" '
        f'text-anchor="middle" font-size="14" fill="#333" '
        f'transform="rotate(-90 14 {PLOT_Y + PLOT_H / 2:.1f})">Speedup</text>'
    )

    # ----- Đường gridline (mờ) ngang -----
    for sp in y_ticks[1:]:  # bỏ y=0 (trùng trục x)
        y = y_to_px(sp)
        parts.append(
            f'<line x1="{PLOT_X}" y1="{y:.1f}" '
            f'x2="{PLOT_X + PLOT_W}" y2="{y:.1f}" '
            f'stroke="#eee" stroke-width="1"/>'
        )

    # ----- Đường cong cho từng s -----
    legend_y = PLOT_Y + 16
    for s, color, label in S_VALUES:
        d = build_path(s)
        parts.append(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5"/>'
        )
        # Đường ngang đứt nét cho asymptote 1/s nếu nằm trong khung
        asymptote = 1.0 / s
        if asymptote <= Y_MAX:
            y_asym = y_to_px(asymptote)
            parts.append(
                f'<line x1="{PLOT_X}" y1="{y_asym:.1f}" '
                f'x2="{PLOT_X + PLOT_W}" y2="{y_asym:.1f}" '
                f'stroke="{color}" stroke-width="1" stroke-dasharray="3,3" opacity="0.4"/>'
            )

        # Legend item
        legend_x = PLOT_X + PLOT_W + 12
        parts.append(
            f'<line x1="{legend_x}" y1="{legend_y - 4}" '
            f'x2="{legend_x + 18}" y2="{legend_y - 4}" '
            f'stroke="{color}" stroke-width="2.5"/>'
        )
        parts.append(
            f'<text x="{legend_x + 22}" y="{legend_y}" '
            f'font-size="13" fill="{color}" font-weight="bold">{label}</text>'
        )
        legend_y += 22

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    out_path = script_dir.parent / "amdahl.svg"
    out_path.write_text(build_svg(), encoding="utf-8")
    print(f"✓ Sinh xong {out_path.relative_to(script_dir.parent.parent.parent)}")


if __name__ == "__main__":
    main()
