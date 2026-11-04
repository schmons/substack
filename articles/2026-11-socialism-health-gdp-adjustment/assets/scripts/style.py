"""Shared chart style for this article (static PNGs for Substack)."""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

ASSETS = Path(__file__).resolve().parent.parent
RAW = ASSETS / "data" / "raw"
PROCESSED = ASSETS / "data" / "processed"
FIGURES = ASSETS / "figures"

# Reference palette (dataviz skill), light mode.
SURFACE = "#ffffff"
TEXT = "#0b0b0b"
TEXT_2 = "#52514e"
MUTED = "#a3a29c"
GRID = "#e6e5e0"
CAPITALIST = "#2a78d6"  # slot 1, blue
SOCIALIST = "#eb6834"   # slot 2, orange
THIRD = "#1baf7a"       # slot 3, aqua


def setup() -> None:
    mpl.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "font.size": 11,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": TEXT_2,
        "axes.titlecolor": TEXT,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "xtick.color": TEXT_2,
        "ytick.color": TEXT_2,
        "legend.frameon": False,
        "lines.linewidth": 2,
    })


def save(fig, name: str) -> None:
    FIGURES.mkdir(exist_ok=True)
    fig.savefig(FIGURES / name, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("saved", FIGURES / name)
