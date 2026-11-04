"""Re-analysis with modern Gapminder data.

1. The paper's design, redone for 1983: life expectancy vs GDP per capita, socialist countries highlighted.
2. The 'same GDP' gap for every year 1900-2019, split into the Soviet bloc and Asia + Cuba.
3. Natural comparisons (neighbours with similar starting points): life expectancy and GDP over time.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.nonparametric.smoothers_lowess import lowess

import style

GROUP_LABEL = {"soviet_bloc": "USSR & Eastern Europe", "asia_cuba": "China, Vietnam, Laos, Cambodia, N. Korea, Cuba"}


def load():
    p = pd.read_csv(style.PROCESSED / "panel.csv")
    p = p[p.group.isin(["capitalist", "soviet_bloc", "asia_cuba"])].copy()  # drop ambiguous cases
    p["lg"] = np.log(p.gdp_pcap)
    return p


def same_gdp_gap(d, groups):
    """Paper-style estimate: life expectancy gap at the same GDP (quadratic in log GDP)."""
    d = d[d.group.isin(["capitalist", *groups])].dropna(subset=["lex", "lg"]).copy()
    d["soc"] = (d.group != "capitalist").astype(int)
    r = smf.ols("lex ~ soc + lg + I(lg**2)", d).fit(cov_type="HC1")
    return r.params.soc, r.bse.soc, int(r.nobs)


def fig_1983(p):
    d = p[p.year == 1983].dropna(subset=["lex", "lg"])
    cap = d[d.group == "capitalist"]
    curve = lowess(cap.lex, cap.lg, frac=0.5)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(cap.gdp_pcap, cap.lex, s=30, color=style.CAPITALIST, alpha=0.55, edgecolor="white", lw=0.8,
               label="Capitalist", zorder=2)
    ax.plot(np.exp(curve[:, 0]), curve[:, 1], color=style.CAPITALIST, lw=2, label="Capitalist average at each GDP")
    for g, marker in [("soviet_bloc", "o"), ("asia_cuba", "D")]:
        s = d[d.group == g]
        ax.scatter(s.gdp_pcap, s.lex, s=46, marker=marker, color=style.SOCIALIST, edgecolor="white", lw=1,
                   label=GROUP_LABEL[g], zorder=3)
    for name in ["China", "Cuba", "Vietnam", "North Korea", "Russia", "Czech Republic", "Hungary", "Poland", "Lao", "Estonia"]:
        r = d[d.name == name].iloc[0]
        ax.annotate(name, (r.gdp_pcap, r.lex), xytext=(5, -3), textcoords="offset points", fontsize=9, color=style.TEXT_2)
    ax.set_xscale("log")
    ax.set_xlabel("GDP per capita, 1983 (log scale, 2017 PPP $)")
    ax.set_ylabel("Life expectancy at birth, 1983 (years)")
    ax.set_title("1983: the paper's comparison, redone with today's data")
    ax.legend(loc="lower right", fontsize=9)
    style.save(fig, "02_preston_curve_1983.png")


def fig_gap_over_time(p):
    rows = []
    for year in range(1900, 2020):
        d = p[p.year == year]
        for g in ["soviet_bloc", "asia_cuba"]:
            est, se, n = same_gdp_gap(d, [g])
            rows.append({"year": year, "group": g, "gap": est, "se": se, "n": n})
    res = pd.DataFrame(rows)
    res.to_csv(style.PROCESSED / "same_gdp_gap_by_year.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), sharey=True)
    for ax, g, start in [(axes[0], "soviet_bloc", 1945), (axes[1], "asia_cuba", 1949)]:
        r = res[(res.group == g) & (res.year >= 1950)]
        ax.fill_between(r.year, r.gap - 1.96 * r.se, r.gap + 1.96 * r.se, color=style.SOCIALIST, alpha=0.18, lw=0)
        ax.plot(r.year, r.gap, color=style.SOCIALIST)
        ax.axhline(0, color=style.TEXT_2, lw=1)
        ax.axvline(1983, color=style.TEXT, lw=1, ls="--")
        ax.text(1984, -5.5, "paper's data\n(c. 1983)", fontsize=9, color=style.TEXT)
        ax.set_title(GROUP_LABEL[g], fontsize=11)
        ax.set_xlim(1950, 2019)
        ax.set_ylim(-6, 14)
    axes[0].set_ylabel("Life expectancy gap vs capitalist\ncountries at the same GDP (years)")
    fig.suptitle("The 'same GDP' advantage: where it comes from and when", x=0.01, ha="left",
                 fontsize=13, fontweight="bold", color=style.TEXT)
    fig.tight_layout()
    style.save(fig, "03_same_gdp_gap_over_time.png")
    return res


def fig_pairs(p):
    pairs = [
        ("Finland vs Estonia", ["fin"], ["est"]),
        ("Austria vs Czechia & Hungary", ["aut"], ["cze", "hun"]),
        ("Spain, Portugal, Italy, Greece\nvs Poland, Bulgaria, Romania", ["esp", "prt", "ita", "grc"], ["pol", "bgr", "rou"]),
        ("India vs China", ["ind"], ["chn"]),
    ]
    fig, axes = plt.subplots(2, 4, figsize=(15, 7), sharex=True)
    for j, (title, cap, soc) in enumerate(pairs):
        for i, var in enumerate(["lex", "gdp_pcap"]):
            ax = axes[i, j]
            for codes, colour, label in [(cap, style.CAPITALIST, "Capitalist"), (soc, style.SOCIALIST, "Socialist")]:
                s = p[p.country.isin(codes) & p.year.between(1920, 2019)]
                s = s.groupby("year")[var].mean()  # simple average if several countries
                ax.plot(s.index, s.values, color=colour, label=label)
            ax.axvspan(1945 if j < 3 else 1949, 1989 if j < 3 else 2019, color=style.SOCIALIST, alpha=0.06, lw=0)
            if var == "gdp_pcap":
                ax.set_yscale("log")
                ax.set_yticks([1000, 3000, 10000, 30000])
                ax.set_yticklabels(["1k", "3k", "10k", "30k"])
            if i == 0:
                ax.set_title(title, fontsize=11)
                ax.set_ylim(20, 85)
        axes[0, 0].set_ylabel("Life expectancy (years)")
        axes[1, 0].set_ylabel("GDP per capita (log, 2017 PPP $)")
    axes[0, 0].legend(loc="lower right", fontsize=9)
    fig.suptitle("Neighbours that started in similar places: health and income", x=0.01, ha="left",
                 fontsize=13, fontweight="bold", color=style.TEXT)
    fig.tight_layout()
    style.save(fig, "04_natural_comparisons.png")


def main():
    style.setup()
    p = load()
    fig_1983(p)
    res = fig_gap_over_time(p)
    fig_pairs(p)

    d = p[p.year == 1983]
    print("\n1983 'same GDP' gap (years of life expectancy):")
    for groups in [["soviet_bloc", "asia_cuba"], ["soviet_bloc"], ["asia_cuba"]]:
        est, se, n = same_gdp_gap(d, groups)
        print(f"  {'+'.join(groups):25s} {est:+.2f} (se {se:.2f}, n={n})")
    print("\nGap by decade:")
    print(res[res.year.isin([1913, 1938, 1950, 1960, 1965, 1970, 1975, 1980, 1983, 1989])]
          .pivot(index="year", columns="group", values="gap").round(1))


if __name__ == "__main__":
    main()
