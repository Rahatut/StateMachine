from helpers import *

sym_xs = [0.0, 2.3, 4.6, 6.9, 9.2]
surf_xs = [11.2, 13.5]
sym_cx = sum(sym_xs) / len(sym_xs)
surf_cx = sum(surf_xs) / len(surf_xs)
root_cx = (sym_cx + surf_cx) / 2

fig, ax = new_ax(15.0, 5.0, (-1.3, 14.8), (3.7, 8.6))

box(ax, (root_cx, 7.7), 5.6, 0.85, "DWS-Bench Complexity Factors", fc=ACCENT_FC, ec=ACCENT_EDGE, fontsize=10.3)

box(ax, (sym_cx, 5.95), 9.6, 0.95, "Symbolic Complexity\n(changes the canonical world state)", fontsize=9.3)
box(ax, (surf_cx, 5.95), 3.1, 0.95, "Surface Complexity\n(rendering only)", fontsize=9.3)

arrow(ax, (root_cx - 1.0, 7.7 - 0.425), (sym_cx + 0.3, 5.95 + 0.475))
arrow(ax, (root_cx + 1.0, 7.7 - 0.425), (surf_cx - 0.3, 5.95 + 0.475))

leaf_w, leaf_h = 2.2, 1.15
sym_factors = [
    ("$E$", "Entity count", "world size"),
    ("$T$", "Update depth", "temporal dependency"),
    ("$D$", "Distractor count", "interference"),
    ("$V$", "Revision count", "state overwrite"),
    ("$U$", "Total updates", "trajectory size"),
]
surf_factors = [
    ("$N$", "Narrative count", "surface noise"),
    ("$L$", "Word-count proxy", "context length"),
]

for x, (sym, name, role) in zip(sym_xs, sym_factors):
    arrow(ax, (sym_cx, 5.95 - 0.475), (x, 4.55 + leaf_h / 2))
    box(ax, (x, 4.55), leaf_w, leaf_h, f"{sym} — {name}\n({role})", fontsize=8.0)

for x, (sym, name, role) in zip(surf_xs, surf_factors):
    arrow(ax, (surf_cx, 5.95 - 0.475), (x, 4.55 + leaf_h / 2))
    box(ax, (x, 4.55), leaf_w, leaf_h, f"{sym} — {name}\n({role})", fontsize=8.0)

save(fig, 'dws_factor_taxonomy')
