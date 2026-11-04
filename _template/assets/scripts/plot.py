"""Starter visualisation script. Reads from data/processed/, writes to figures/."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ASSETS = Path(__file__).resolve().parent.parent
DATA = ASSETS / "data" / "processed"
FIGURES = ASSETS / "figures"


def main() -> None:
    # df = pd.read_csv(DATA / "example.csv")
    # fig, ax = plt.subplots(figsize=(8, 5))
    # ax.plot(df["x"], df["y"])
    # fig.savefig(FIGURES / "example.png", dpi=200, bbox_inches="tight")
    pass


if __name__ == "__main__":
    main()
