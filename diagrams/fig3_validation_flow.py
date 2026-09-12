from helpers import *

cx = 0.0
w = 5.6
gap = 0.55

blocks = [
    (0.9, "Candidate symbolic trajectory\n(post-generation)", 9.8),
    (1.7, "A — World & Operation Validity\n• entities / locations in the predefined world\n• every operation valid under the\n   simulator's transition rules", 9),
    (2.1, "B — QuerySpec Compliance\n• trajectory satisfies its QuerySpec\n• target dependency chain has requested depth\n• distractor conditions satisfy their definitions\n• revision conditions satisfy the operational definition", 9),
    (1.5, "C — Symbolic Consistency\n• final symbolic state is internally consistent\n• realized factors (E,T,D,N,V,U,L) recorded", 9),
    (1.1, "D — Rendering Admissibility\n• rendered instance meets all admissibility\n   constraints, incl. word-count tolerance", 9),
]

top_y = 14.6
centers = []
y = top_y
for h, text, fs in blocks:
    cy = y - h / 2
    centers.append(cy)
    y = cy - h / 2 - gap

diamond_h = 1.6
diamond_cy = y - diamond_h / 2
y2 = diamond_cy - diamond_h / 2 - gap
accept_h = 0.9
accept_cy = y2 - accept_h / 2

fig, ax = new_ax(7.4, 15.6, (-4.2, 3.9), (accept_cy - 0.9, top_y + 0.5))

for i, (h, text, fs) in enumerate(blocks):
    box(ax, (cx, centers[i]), w, h, text, fontsize=fs)
    if i > 0:
        prev_bottom = centers[i - 1] - blocks[i - 1][0] / 2
        this_top = centers[i] + h / 2
        arrow(ax, (cx, prev_bottom), (cx, this_top))

last_bottom = centers[-1] - blocks[-1][0] / 2
arrow(ax, (cx, last_bottom), (cx, diamond_cy + diamond_h / 2))
diamond(ax, (cx, diamond_cy), 3.4, diamond_h, "All checks\npassed?", fontsize=10)

label(ax, (0.35, diamond_cy - diamond_h / 2 + 0.45), "yes", fontsize=9, color=ACCEPT_EDGE, weight='bold')
arrow(ax, (cx, diamond_cy - diamond_h / 2), (cx, accept_cy + accept_h / 2), color=ACCEPT_EDGE)
box(ax, (cx, accept_cy), 4.2, accept_h, "Accepted into frozen benchmark", fc=ACCEPT_FC, ec=ACCEPT_EDGE, fontsize=9.8)

rej_x = -3.0
rej_w, rej_h = 2.0, 0.9
arrow(ax, (cx - 1.7, diamond_cy), (rej_x + rej_w / 2, diamond_cy), color=REJECT_EDGE)
label(ax, ((cx - 1.7 + rej_x + rej_w / 2) / 2, diamond_cy + 0.28), "no", fontsize=9, color=REJECT_EDGE, weight='bold')
box(ax, (rej_x, diamond_cy), rej_w, rej_h, "Rejected\n(discarded)", fc=REJECT_FC, ec=REJECT_EDGE, fontsize=9)

arrow(ax, (rej_x, diamond_cy + rej_h / 2), (cx - 1.6, top_y - 0.45),
      color=REJECT_EDGE, rad=-0.18, linestyle=(0, (4, 3)), lw=1.15)
label(ax, (rej_x - 0.5, (diamond_cy + top_y) / 2 - 0.3), "regenerate", fontsize=8.3, color=REJECT_EDGE, rotation=90)

save(fig, 'dws_validation_flow')
