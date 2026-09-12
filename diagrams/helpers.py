from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon


INK = "#20252b"
BOX_FC = "#f4f6f8"
ACCENT_FC = "#dcecf2"
ACCENT_EDGE = "#137c8b"
ACCEPT_FC = "#e4f1e8"
ACCEPT_EDGE = "#2f7d4a"
REJECT_FC = "#f8e4e1"
REJECT_EDGE = "#b34b43"
ALT_FC = "#f7f1df"


def new_ax(width, height, xlim, ylim):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    return fig, ax


def box(ax, center, width, height, text, fc=BOX_FC, ec=INK, fontsize=10,
        text_color=INK, style="round,pad=0.03,rounding_size=0.08", linestyle="-"):
    patch = FancyBboxPatch(
        (center[0] - width / 2, center[1] - height / 2),
        width,
        height,
        boxstyle=style,
        facecolor=fc,
        edgecolor=ec,
        linewidth=1.2,
        linestyle=linestyle,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        center[0],
        center[1],
        text,
        ha="center",
        va="center",
        color=text_color,
        fontsize=fontsize,
        linespacing=1.15,
        zorder=3,
    )
    return patch


def diamond(ax, center, width, height, text, fc=BOX_FC, ec=INK, fontsize=10):
    points = [
        (center[0], center[1] + height / 2),
        (center[0] + width / 2, center[1]),
        (center[0], center[1] - height / 2),
        (center[0] - width / 2, center[1]),
    ]
    patch = Polygon(points, closed=True, facecolor=fc, edgecolor=ec,
                    linewidth=1.2, zorder=2)
    ax.add_patch(patch)
    ax.text(center[0], center[1], text, ha="center", va="center",
            color=INK, fontsize=fontsize, linespacing=1.15, zorder=3)
    return patch


def arrow(ax, start, end, color=INK, rad=0.0, linestyle="-", lw=1.2, mscale=10):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        connectionstyle=f"arc3,rad={rad}",
        mutation_scale=mscale,
        linewidth=lw,
        linestyle=linestyle,
        color=color,
        shrinkA=4,
        shrinkB=4,
        zorder=1,
    )
    ax.add_patch(patch)
    return patch


def label(ax, position, text, fontsize=10, color=INK, **kwargs):
    return ax.text(position[0], position[1], text, fontsize=fontsize,
                   color=color, zorder=4, **kwargs)


def save(fig, name):
    output_dir = Path(__file__).resolve().parent.parent / "report" / "images" / "thesis_figures"
    output_dir.mkdir(parents=True, exist_ok=True)
    for extension in ("png", "pdf"):
        fig.savefig(output_dir / f"{name}.{extension}", dpi=300,
                    bbox_inches="tight", facecolor="white")
    plt.close(fig)