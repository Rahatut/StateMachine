from helpers import *

fig, ax = new_ax(11.5, 5.2, (0.2, 13.0), (-3.2, 2.2))

y_top = 1.0
xs = [1.4, 4.0, 6.6, 9.2, 11.8]
# adjust to fit width 11.5 -> recompute
xs = [1.5, 4.05, 6.6, 9.15, 11.7]
labels = [
    "Symbolic\nTrajectory\nGeneration",
    "Validation",
    "Natural-\nLanguage\nRendering",
    "Small\nLanguage\nModel",
    "Evaluation",
]
w, h = 2.0, 1.35
for x, lab in zip(xs, labels):
    fc = ACCENT_FC if lab == "Validation" else BOX_FC
    ec = ACCENT_EDGE if lab == "Validation" else INK
    box(ax, (x, y_top), w, h, lab, fc=fc, ec=ec, fontsize=10)

for i in range(len(xs) - 1):
    arrow(ax, (xs[i] + w / 2, y_top), (xs[i + 1] - w / 2, y_top))

# Symbolic ground truth box below Validation
gt_xy = (4.05, -1.3)
box(ax, gt_xy, 2.6, 1.05, "Symbolic Ground Truth\n(exact final state)", fc=ACCENT_FC, ec=ACCENT_EDGE, fontsize=9.5)
arrow(ax, (4.05, y_top - h / 2), (gt_xy[0], gt_xy[1] + 0.55), color=ACCENT_EDGE)

# Curved dashed arrow from ground truth directly to Evaluation, bypassing renderer/SLM
arrow(ax, (gt_xy[0] + 1.3, gt_xy[1]), (xs[4] - w / 2 + 0.1, y_top - h / 2 - 0.1),
      color=ACCENT_EDGE, rad=-0.28, linestyle=(0, (5, 3)), lw=1.4)

label(ax, (7.9, -1.9), "ground truth compared directly — independent of the\nrenderer and the model's language output",
      fontsize=8.7, color=ACCENT_EDGE, style='italic')

# Title-less; caption handled in LaTeX. Add faint stage numbers
for i, x in enumerate(xs, start=1):
    label(ax, (x, y_top + h / 2 + 0.32), f"{i}", fontsize=9, color='#888888', weight='bold')

save(fig, 'dws_system_overview')
