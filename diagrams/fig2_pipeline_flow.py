from helpers import *

fig, ax = new_ax(7.6, 10.8, (-3.6, 4.6), (2.2, 15.4))

cx = 0.0
w_main = 3.6
h_main = 1.0

ys = {
    'queryspec': 14.4,
    'generator': 12.6,
    'validator': 10.6,
    'record': 8.6,
    'renderer': 6.8,
    'slm': 5.0,
    'evaluator': 3.2,
}

box(ax, (cx, ys['queryspec']), w_main, h_main, "QuerySpec\n(requested structural condition)", fc=ACCENT_FC, ec=ACCENT_EDGE, fontsize=10)
# side note listing target factors
box(ax, (3.55, ys['queryspec']), 1.9, 1.3, "target:\nT, D, E, V, N", fc='white', ec='#888888', fontsize=8.7)
arrow(ax, (cx + w_main/2, ys['queryspec']), (3.55 - 0.95, ys['queryspec']), color='#888888', lw=1.0)

arrow(ax, (cx, ys['queryspec'] - h_main/2), (cx, ys['generator'] + h_main/2))
box(ax, (cx, ys['generator']), w_main, h_main, "Generator\n(constructs candidate symbolic trajectory)", fontsize=10)

arrow(ax, (cx, ys['generator'] - h_main/2), (cx, ys['validator'] + 0.75))
diamond(ax, (cx, ys['validator']), 3.2, 1.5, "Validator\nvalid?", fontsize=10)

# reject loop back to Generator
arrow(ax, (cx + 1.6, ys['validator']), (cx + w_main/2 + 0.05, ys['generator']),
      color=REJECT_EDGE, rad=0.55, lw=1.3)
label(ax, (2.55, ys['validator'] + 0.35), "no", fontsize=9, color=REJECT_EDGE, weight='bold')
label(ax, (3.35, (ys['validator']+ys['generator'])/2 + 0.05), "reject —\nregenerate", fontsize=8.3, color=REJECT_EDGE, ha='left')

label(ax, (cx + 0.3, ys['validator'] - 0.9), "yes", fontsize=9, color=ACCEPT_EDGE, weight='bold')
arrow(ax, (cx, ys['validator'] - 0.75), (cx, ys['record'] + h_main/2), color=ACCEPT_EDGE)

box(ax, (cx, ys['record']), w_main, h_main, "Record realized factors\n(E, T, D, N, V, U, L)", fc=ACCEPT_FC, ec=ACCEPT_EDGE, fontsize=9.8)

arrow(ax, (cx, ys['record'] - h_main/2), (cx, ys['renderer'] + h_main/2))
box(ax, (cx, ys['renderer']), w_main, h_main, "Renderer\n(natural-language narrative)", fontsize=10)

arrow(ax, (cx, ys['renderer'] - h_main/2), (cx, ys['slm'] + h_main/2))
box(ax, (cx, ys['slm']), w_main, h_main, "Small Language Model\n(zero-shot / chain-of-thought)", fontsize=10)

arrow(ax, (cx, ys['slm'] - h_main/2), (cx, ys['evaluator'] + h_main/2))
box(ax, (cx, ys['evaluator']), w_main, h_main, "Evaluator\n(final-answer + step-wise accuracy)", fontsize=9.7)

# ground truth side arrow from record straight to evaluator
arrow(ax, (cx - w_main/2 + 0.05, ys['record'] - 0.15), (cx - w_main/2 - 0.02, ys['evaluator'] + 0.3),
      color=ACCENT_EDGE, rad=0.35, linestyle=(0, (5, 3)), lw=1.3, mscale=11)
label(ax, (-3.15, (ys['record']+ys['evaluator'])/2), "symbolic\nground truth", fontsize=8.3, color=ACCENT_EDGE, ha='center')

save(fig, 'dws_pipeline_flow')
