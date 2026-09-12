from helpers import *

fig, ax = new_ax(13.6, 7.4, (-1.3, 13.6), (-5.3, 2.3))

xs = [0.0, 2.35, 4.7, 7.05, 9.4, 11.75]
steps = [
    ("$t_0$: PUT", "Ball → Room A"),
    ("$t_1$: MOVE", "Ball → Room B"),
    ("$t_2$: MOVE", "Ball → Room C"),
    ("$t_3$: MOVE", "Ball → Room A"),
    ("$t_4$: REMOVE", "Ball"),
    ("$t_5$: PUT", "Ball → Room D"),
]
w, h = 1.95, 1.15
cy = 1.2

for i, (x, (op, res)) in enumerate(zip(xs, steps)):
    highlight = (i == 3) or (i == 5)
    fc = ACCENT_FC if highlight else BOX_FC
    ec = ACCENT_EDGE if highlight else INK
    box(ax, (x, cy), w, h, f"{op}\n{res}", fontsize=9.3, fc=fc, ec=ec)
    if i > 0:
        arrow(ax, (xs[i - 1] + w / 2, cy), (x - w / 2, cy))

label(ax, (xs[3], cy - h / 2 - 0.32), "revision: revisits Room A", fontsize=8.3, color=ACCENT_EDGE, style='italic')

# Query / gold state box under the last step
arrow(ax, (xs[5], cy - h / 2), (xs[5], -1.05), rad=0.0)
box(ax, (xs[5] - 1.2, -1.75), 5.0, 1.1, "Query: \u201cWhere is the Ball?\u201d\nGold state (symbolic): Room D",
    fontsize=9.7, fc=ACCENT_FC, ec=ACCENT_EDGE)

# Rendered narrative box spanning the width
arrow(ax, (xs[5] - 1.2, -1.75 - 0.55), (xs[5] - 1.2, -2.75))
box(ax, (5.2, -3.85), 11.8, 1.7,
    "Rendered narrative (example)\n\u201cThe ball was placed in Room A, then moved to Room B and on to\n"
    "Room C. It was later brought back to Room A before being taken away.\n"
    "It was finally placed in Room D.\u201d",
    fontsize=9, fc=ALT_FC, ec='#666666')

label(ax, (5.2, -4.95), "Gold answer is computed from the symbolic trace above — never from this text.",
      fontsize=8.5, color='#555555', style='italic')

save(fig, 'dws_example_trajectory')
