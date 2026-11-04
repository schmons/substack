"""Simulation: why comparing countries 'at the same GDP' can invent a socialist health advantage.

Causal story (DAG):
    U (historical development: schooling, sanitation, industry) -> GDP, health
    S (socialist system)                                       -> GDP (lowers it)
    GDP                                                        -> health
    S -> health directly: ZERO by construction.

So the true total effect of socialism on health is NEGATIVE (it works only through
lower GDP). The paper's design compares socialist and capitalist countries within
GDP bands. GDP is caused by both S and U, so within a band, socialist countries are
the ones with more U (they reached that GDP *despite* socialism). U also improves
health, so they look healthier. This is collider / post-treatment bias.
"""
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

import style

RNG = np.random.default_rng(1986)
N_COUNTRIES = 123      # same as the paper
SHARE_SOCIALIST = 0.2
SOCIALISM_ON_LOG_GDP = -0.6   # socialism cuts GDP per capita by ~45%
U_ON_LOG_GDP = 0.8
LOG_GDP_ON_HEALTH = 5.0       # years of life expectancy per log-point of GDP
U_ON_HEALTH = 3.0
DIRECT_EFFECT = 0.0           # socialism has no direct effect on health


def simulate(rng):
    u = rng.normal(size=N_COUNTRIES)
    s = (rng.random(N_COUNTRIES) < SHARE_SOCIALIST).astype(float)
    log_gdp = 8.5 + U_ON_LOG_GDP * u + SOCIALISM_ON_LOG_GDP * s + rng.normal(0, 0.6, N_COUNTRIES)
    health = 25 + LOG_GDP_ON_HEALTH * log_gdp + U_ON_HEALTH * u + DIRECT_EFFECT * s + rng.normal(0, 2.5, N_COUNTRIES)
    return u, s, log_gdp, health


def estimates(s, log_gdp, health):
    total = sm.OLS(health, sm.add_constant(s)).fit().params[1]
    adjusted = sm.OLS(health, sm.add_constant(np.column_stack([s, log_gdp]))).fit().params[1]
    # The paper's version: 4 GDP bands, count bands where socialist mean is higher
    bands = np.quantile(log_gdp, [0.25, 0.5, 0.75])
    band = np.digitize(log_gdp, bands)
    wins = cells = 0
    for b in range(4):
        hs, hc = health[(band == b) & (s == 1)], health[(band == b) & (s == 0)]
        if len(hs) and len(hc):
            cells += 1
            wins += hs.mean() > hc.mean()
    return total, adjusted, wins, cells


def main():
    style.setup()
    true_total = SOCIALISM_ON_LOG_GDP * LOG_GDP_ON_HEALTH

    # One example world for the scatter
    u, s, log_gdp, health = simulate(np.random.default_rng(7))

    # Many worlds for the sampling distribution
    res = np.array([estimates(*simulate(RNG)[1:]) for _ in range(2000)])
    total, adjusted, wins, cells = res.T
    print(f"true total effect: {true_total:.1f} years; true direct effect: {DIRECT_EFFECT}")
    print(f"mean raw estimate: {total.mean():.2f}; mean GDP-adjusted estimate: {adjusted.mean():.2f}")
    print(f"share of worlds where adjusted estimate > 0: {(adjusted > 0).mean():.1%}")
    print(f"GDP-band comparisons won by socialist countries: {wins.sum() / cells.sum():.1%}")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw={"width_ratios": [1.2, 1]})

    gdp = np.exp(log_gdp)
    for flag, colour, label in [(0, style.CAPITALIST, "Capitalist"), (1, style.SOCIALIST, "Socialist")]:
        m = s == flag
        ax1.scatter(gdp[m], health[m], s=36, color=colour, edgecolor="white", linewidth=1, label=label, zorder=3)
        fit = np.polyfit(log_gdp[m], health[m], 1)
        xs = np.linspace(log_gdp.min(), log_gdp.max(), 50)
        ax1.plot(np.exp(xs), np.polyval(fit, xs), color=colour, lw=2)
    ax1.set_xscale("log")
    ax1.set_xlabel("GDP per capita (log scale, simulated $)")
    ax1.set_ylabel("Life expectancy (simulated years)")
    ax1.set_title("One simulated world: socialist countries sit above the line")
    ax1.legend(loc="upper left")
    ax1.text(0.98, 0.04, "By construction, socialism has\nno direct effect on health and\nmakes countries poorer.",
             transform=ax1.transAxes, ha="right", va="bottom", color=style.TEXT_2, fontsize=10)

    bins = np.linspace(min(total.min(), adjusted.min()), max(total.max(), adjusted.max()), 60)
    ax2.hist(total, bins=bins, color=style.MUTED, alpha=0.9, label="Raw comparison", rwidth=0.9)
    ax2.hist(adjusted, bins=bins, color=style.SOCIALIST, alpha=0.9, label="'Same GDP' comparison", rwidth=0.9)
    ax2.axvline(true_total, color=style.TEXT, lw=1.5, ls="--")
    ax2.annotate("true effect\nof socialism", xy=(true_total, ax2.get_ylim()[1] * 0.55), xytext=(-12, 0),
                 textcoords="offset points", ha="right", va="center", color=style.TEXT, fontsize=10)
    ax2.axvline(0, color=style.TEXT_2, lw=1)
    ax2.set_xlabel("Estimated effect of socialism on life expectancy (years)")
    ax2.set_ylabel("Number of simulated worlds")
    ax2.set_title("2,000 simulated worlds")
    ax2.legend(loc="upper left")

    fig.tight_layout()
    style.save(fig, "01_simulation.png")


if __name__ == "__main__":
    main()
