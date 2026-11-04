"""Build one country-year panel from the raw Gapminder files + our socialist classification."""
import pandas as pd

import style

FILES = {
    "lex": "lex.csv",
    "gdp_pcap": "gdp_pcap.csv",
    "u5mr": "child_mortality_0_5_year_olds_dying_per_1000_born.csv",
    "pop": "pop.csv",
}


def main():
    raw = style.RAW / "gapminder"
    panel = None
    for name, file in FILES.items():
        d = pd.read_csv(raw / file)
        d.columns = ["country", "year", name]
        panel = d if panel is None else panel.merge(d, on=["country", "year"], how="outer")

    countries = pd.read_csv(raw / "countries.csv")[["country", "name", "un_state", "world_4region", "world_6region"]]
    panel = panel.merge(countries, on="country")
    panel = panel[(panel.un_state == True) & panel.year.between(1900, 2023)].drop(columns="un_state")

    soc = pd.read_csv(style.ASSETS / "data" / "socialist_countries.csv")
    panel = panel.merge(soc[["country", "group", "start", "end"]], on="country", how="left")
    panel["group"] = panel["group"].fillna("capitalist")
    panel["socialist_now"] = (panel.start <= panel.year) & (panel.end.isna() | (panel.year < panel.end))

    style.PROCESSED.mkdir(exist_ok=True)
    panel.to_csv(style.PROCESSED / "panel.csv", index=False)
    print(panel.shape, panel.country.nunique(), "countries")
    print(panel.groupby("group").country.nunique())


if __name__ == "__main__":
    main()
