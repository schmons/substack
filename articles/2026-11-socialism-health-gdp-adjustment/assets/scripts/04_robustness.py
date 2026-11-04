"""Robustness of the 1983 'same GDP' gap to reasonable analysis choices. Writes data/processed/robustness_1983.csv."""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

import style


def gap(d, formula="lex ~ soc + lg + I(lg**2)", weights=None):
    d = d.dropna(subset=["lex", "lg"])
    model = smf.wls(formula, d, weights=d[weights]) if weights else smf.ols(formula, d)
    r = model.fit(cov_type="HC1")
    return r.params.soc, r.bse.soc, int(r.nobs)


def main():
    p = pd.read_csv(style.PROCESSED / "panel.csv")
    p["lg"] = np.log(p.gdp_pcap)
    p["lu"] = np.log(p.u5mr.where(p.u5mr > 0))
    d = p[p.year == 1983].copy()

    core = ["soviet_bloc", "asia_cuba"]
    def sample(soc_groups, drop=("yugoslavia", "afro_marxist")):
        s = d[~d.group.isin([g for g in drop if g not in soc_groups])].copy()
        s["soc"] = s.group.isin(soc_groups).astype(int)
        return s

    rows = []
    def add(label, est):
        rows.append({"specification": label, "gap_years": round(est[0], 2), "se": round(est[1], 2), "n": est[2]})

    add("Paper-style: GDP (quadratic), all core socialist", gap(sample(core)))
    add("USSR & Eastern Europe only", gap(sample(["soviet_bloc"]).query("group != 'asia_cuba'")))
    add("Asia + Cuba only", gap(sample(["asia_cuba"]).query("group != 'soviet_bloc'")))
    add("+ region fixed effects", gap(sample(core), "lex ~ soc + lg + I(lg**2) + C(world_6region)"))
    add("Population-weighted (China dominates)", gap(sample(core), weights="pop"))
    add("Including Yugoslavia & Afro-Marxist states", gap(sample(core + ["yugoslavia", "afro_marxist"])))
    add("No GDP adjustment (raw difference)", gap(sample(core), "lex ~ soc"))
    s = sample(core).query("u5mr > 0")
    est = gap(s.assign(lex=s.lu), "lex ~ soc + lg + I(lg**2)")
    rows.append({"specification": "Outcome: log child mortality (negative = better)", "gap_years": round(est[0], 2),
                 "se": round(est[1], 2), "n": est[2]})

    out = pd.DataFrame(rows)
    out.to_csv(style.PROCESSED / "robustness_1983.csv", index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
