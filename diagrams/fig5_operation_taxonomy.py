from helpers import *

core_xs = [-0.35, 1.7, 3.75]
struct_xs = [5.4, 7.45, 9.5, 11.55, 13.6]
core_cx = sum(core_xs) / len(core_xs)
struct_cx = sum(struct_xs) / len(struct_xs)
root_cx = (core_cx + struct_cx) / 2

fig, ax = new_ax(15.7, 5.4, (-1.6, 14.8), (1.9, 8.6))

box(ax, (root_cx, 7.7), 5.4, 0.85, "DWS-Bench Operation Vocabulary  (8 operations)", fc=ACCENT_FC, ec=ACCENT_EDGE, fontsize=10.3)

box(ax, (core_cx, 5.9), 4.6, 0.95, "Core State Operations\n(used throughout RQ1\u2013RQ4)", fontsize=9.3)
box(ax, (struct_cx, 5.9), 7.2, 0.95, "Structural Operation Families\n(RQ5 pilot)", fontsize=9.3)

arrow(ax, (root_cx - 1.2, 7.7 - 0.425), (core_cx + 0.3, 5.9 + 0.475))
arrow(ax, (root_cx + 1.2, 7.7 - 0.425), (struct_cx - 0.3, 5.9 + 0.475))

leaf_w, leaf_h = 1.95, 1.35
core_ops = [
    ("PUT", "establishes an\nentity's state"),
    ("MOVE", "changes an\nentity's location"),
    ("REMOVE", "removes entity\nfrom active state"),
]
struct_ops = [
    ("SPLIT", "splits one entity\ninto parts"),
    ("MERGE", "merges entities\ninto one"),
    ("SWAP", "exchanges locations\nof two entities"),
    ("UNDO", "reverses a prior\nhistory step"),
    ("REDO", "reapplies an\nundone step"),
]

for x, (name, desc) in zip(core_xs, core_ops):
    arrow(ax, (core_cx, 5.9 - 0.475), (x, 4.35 + leaf_h / 2))
    box(ax, (x, 4.35), leaf_w, leaf_h, f"{name}\n{desc}", fontsize=8.7)

for x, (name, desc) in zip(struct_xs, struct_ops):
    arrow(ax, (struct_cx, 5.9 - 0.475), (x, 4.35 + leaf_h / 2))
    box(ax, (x, 4.35), leaf_w, leaf_h, f"{name}\n{desc}", fontsize=8.7)

# cross-cutting note: UNDO / REDO also feed the revision factor V
undo_x, redo_x = struct_xs[3], struct_xs[4]
note_cy = 4.35 - leaf_h / 2 - 0.95
box(ax, ((undo_x + redo_x) / 2, note_cy), 4.0, 0.75, "also contribute to the\nrevision factor  $V$  (RQ2)", fc='white', ec=ACCENT_EDGE, fontsize=8.5, text_color=ACCENT_EDGE, style="round,pad=0.02,rounding_size=0.10", linestyle=(0, (3, 2)))
arrow(ax, (undo_x, 4.35 - leaf_h / 2), (undo_x, note_cy + 0.5), color=ACCENT_EDGE, linestyle=(0, (3, 2)), lw=1.0)
arrow(ax, (redo_x, 4.35 - leaf_h / 2), (redo_x, note_cy + 0.5), color=ACCENT_EDGE, linestyle=(0, (3, 2)), lw=1.0)

save(fig, 'dws_operation_taxonomy')
