"""East vs West Germany: the closest thing to a natural experiment.

Data:
- Life expectancy: Human Mortality Database (HMD) East Germany (DEUTE) and West Germany (DEUTW), 1956-2017
  (release of Dec 2018, copied from a public GitHub repo because mortality.org was not reachable).
- GDP per capita 1950-1989: Conference Board Total Economy Database (2015), 1990 international $, as shown in
  Our World in Data's chart "The two Germanies". Values are read back from the chart's SVG (accurate to ~1%).
- Peer countries: Gapminder (see 02_prepare_data.py).

Outputs: data/processed/germany.csv, figures/05_germany.png, figures/06_germany_peers.png
"""
import math
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import style

WEST_POP, EAST_POP = 62.0, 16.5  # millions, 1980s
RECONSTRUCTED_RATIO_1989 = 8322 / 25160  # Heske reconstruction vs West, 1995 EUR (Post-Communist Economies, 2013)


def read_hmd(code):
    d = pd.read_csv(style.RAW / "hmd" / f"{code}.E0per.txt", sep=r"\s+", skiprows=2)
    d.columns = ["year", "female", "male", "total"]
    return d.astype(float).astype({"year": int}).set_index("year")


def read_owid_svg():
    """Recover the plotted points from OWID's reference SVG using the axis tick positions."""
    svg = (style.RAW / "owid" / "the-two-germanies-planning-and-capitalism.svg").read_text()
    ticks_x = {int(t): float(x) for x, t in re.findall(r'<text x="([\d.]+)"[^>]*text-anchor="middle"[^>]*>(\d{4})</text>', svg)}
    ticks_y = {int(v.replace(",", "")): float(y) for y, v in re.findall(r'y="([\d.]+)" dy="\.32em"[^>]*>\$([\d,]+)</text>', svg)}
    (y1, x1), (y2, x2) = sorted(ticks_x.items())[:2]
    px_per_year = (x2 - x1) / (y2 - y1)
    (v1, p1), (v2, p2) = sorted(ticks_y.items())[:2]
    px_per_decade = (p1 - p2) / math.log10(v2 / v1)
    out = {}
    for name, key in [("West-Germany", "gdp_west"), ("East-Germany", "gdp_east")]:
        block = re.search(r'<g id="datapoints__%s"[^>]*>(.*?)</g>' % name, svg, re.S).group(1)
        pts = re.findall(r'cx="([\d.]+)"\s+cy="([\d.]+)"', block)
        out[key] = {round(y1 + (float(x) - x1) / px_per_year): v1 * 10 ** ((p1 - float(y)) / px_per_decade) for x, y in pts}
    return pd.DataFrame(out)


def build():
    east, west = read_hmd("DEUTE"), read_hmd("DEUTW")
    d = pd.DataFrame({"lex_east": east.total, "lex_west": west.total,
                      "lex_east_male": east.male, "lex_west_male": west.male})
    d = d.join(read_owid_svg(), how="outer")
    d.index.name = "year"
    d["lex_gap"] = d.lex_west - d.lex_east
    d["gdp_ratio"] = d.gdp_east / d.gdp_west
    d.round(3).to_csv(style.PROCESSED / "germany.csv")
    return d


def peers(d, panel, year, band=0.15):
    """Capitalist countries with East Germany's GDP per capita (Gapminder units).

    Gapminder has no separate East/West series, so we split unified Germany's GDP using the TED East/West ratio.
    """
    r = d.loc[year, "gdp_ratio"]
    deu = panel[(panel.country == "deu") & (panel.year == year)].gdp_pcap.item()
    west = deu / ((WEST_POP + EAST_POP * r) / (WEST_POP + EAST_POP))
    east = r * west
    p = panel[(panel.year == year) & (panel.group == "capitalist") & panel.gdp_pcap.between(east * (1 - band), east * (1 + band))]
    return p.sort_values("lex"), east, west


def fig_trends(d):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.8))
    for ax in (ax1, ax2):
        ax.axvspan(1949, 1990, color=style.SOCIALIST, alpha=0.06, lw=0)
    l = d.dropna(subset=["lex_east"])
    ax1.plot(l.index, l.lex_west, color=style.CAPITALIST, label="West Germany")
    ax1.plot(l.index, l.lex_east, color=style.SOCIALIST, label="East Germany")
    ax1.set_title("Life expectancy at birth (years)")
    ax1.annotate("level until\nthe mid-1970s", (1966, 70.6), xytext=(1958, 74), fontsize=9, color=style.TEXT_2,
                 arrowprops=dict(arrowstyle="-", color=style.MUTED))
    gap89 = d.loc[1989, "lex_gap"]
    ax1.annotate(f"gap of {gap89:.1f} years\nby 1989", (1989, 74.7), xytext=(1976, 78.5), fontsize=9, color=style.TEXT_2,
                 arrowprops=dict(arrowstyle="-", color=style.MUTED))
    ax1.annotate(f"gap closes after\nreunification ({d.loc[2017, 'lex_gap']:.1f} in 2017)", (2010, 79.6), xytext=(1995, 72),
                 fontsize=9, color=style.TEXT_2, arrowprops=dict(arrowstyle="-", color=style.MUTED))
    ax1.legend(loc="upper left")
    ax1.set_xlim(1955, 2018)

    g = d.dropna(subset=["gdp_east"])
    ax2.plot(g.index, g.gdp_west, color=style.CAPITALIST, label="West Germany")
    ax2.plot(g.index, g.gdp_east, color=style.SOCIALIST, label="East Germany")
    ax2.set_yscale("log")
    ax2.set_yticks([2000, 4000, 8000, 16000])
    ax2.set_yticklabels(["$2k", "$4k", "$8k", "$16k"])
    ax2.minorticks_off()
    ax2.set_title("GDP per capita (log scale, 1990 int. $)")
    ax2.text(1951, 15500, f"Total Economy Database: East Germany at\n{g.gdp_ratio.min():.0%}–{g.gdp_ratio.max():.0%} of West German income", fontsize=9,
             color=style.TEXT_2)
    # Post-1990 reconstruction (Heske series, as compared in Post-Communist Economies 2013): 1989 East = 8,322 vs West = 25,160 EUR (1995 prices)
    recon = RECONSTRUCTED_RATIO_1989 * g.loc[1989, "gdp_west"]
    ax2.scatter([1989], [recon], s=60, facecolor="white", edgecolor=style.SOCIALIST, lw=2, zorder=3)
    ax2.annotate(f"post-1990 reconstruction:\n~{RECONSTRUCTED_RATIO_1989:.0%} of West (1989)", (1989, recon), xytext=(1972, 3300),
                 fontsize=9, color=style.TEXT_2, arrowprops=dict(arrowstyle="-", color=style.MUTED))
    ax2.text(1951, 13300, "1936: East about equal\nto West per head (CIA).\nGap opened 1945–50.", fontsize=9,
             color=style.TEXT_2, va="top")
    ax2.set_xlim(1950, 1991)
    fig.suptitle("East vs West Germany: same people, same history, different system", x=0.01, ha="left",
                 fontsize=13, fontweight="bold", color=style.TEXT)
    fig.text(0.01, -0.03, "Sources: Human Mortality Database (life expectancy); Conference Board Total Economy Database via "
             "Our World in Data (GDP, 1950–89); reconstruction: Post-Communist Economies (2013). Shaded: GDR 1949–90.", fontsize=8.5, color=style.TEXT_2)
    fig.tight_layout()
    style.save(fig, "05_germany.png")


def fig_peers(d, panel, year=1983):
    p, east_gdp, _ = peers(d, panel, year)
    east, west = d.loc[year, "lex_east"], d.loc[year, "lex_west"]
    rows = [(n, v, style.MUTED) for n, v in zip(p.name, p.lex)]
    rows += [("East Germany", east, style.SOCIALIST), ("West Germany", west, style.CAPITALIST)]
    rows.sort(key=lambda r: r[1])

    fig, ax = plt.subplots(figsize=(9, 5.5))
    for i, (n, v, c) in enumerate(rows):
        ax.plot([55, v], [i, i], color=style.GRID, lw=1, zorder=1)
        ax.scatter(v, i, s=70, color=c, edgecolor="white", lw=1, zorder=3)
        ax.text(v + 0.4, i, f"{v:.1f}", va="center", fontsize=9, color=style.TEXT_2)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows])
    for t, r in zip(ax.get_yticklabels(), rows):
        if r[0] in ("East Germany", "West Germany"):
            t.set_fontweight("bold")
    ax.axvline(p.lex.mean(), color=style.TEXT_2, lw=1, ls="--")
    ax.text(p.lex.mean() - 0.3, len(rows) - 0.4, "average of\nGDP peers", ha="right", va="top", fontsize=9, color=style.TEXT_2)
    ax.set_xlim(55, 80)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel(f"Life expectancy at birth, {year} (years)")
    ax.set_title(f"Who East Germany gets compared with when you 'hold GDP fixed' ({year})")
    vs_peers, vs_west = east - p.lex.mean(), east - west
    fig.text(0.01, -0.04,
             f"Grey: capitalist countries within 15% of East Germany's GDP per capita. East Germany vs these peers: {vs_peers:+.1f} years. "
             f"East Germany vs West Germany: {vs_west:+.1f} years.\nSources: Gapminder (peers), Human Mortality Database (Germanies), "
             "Total Economy Database (East/West GDP ratio).", fontsize=8.5, color=style.TEXT_2)
    style.save(fig, "06_germany_peers.png")
    return p, vs_peers, vs_west


def main():
    style.setup()
    d = build()
    panel = pd.read_csv(style.PROCESSED / "panel.csv")
    fig_trends(d)
    p, vs_peers, vs_west = fig_peers(d, panel)
    print(d.loc[[1956, 1960, 1965, 1970, 1975, 1980, 1985, 1989, 1990, 2000, 2017], ["lex_east", "lex_west", "lex_gap", "gdp_ratio"]].round(2))
    print(f"\n1983 peers: {', '.join(p.name)}")
    print(f"East Germany vs GDP peers: {vs_peers:+.1f} years; vs West Germany: {vs_west:+.1f} years")


if __name__ == "__main__":
    main()
