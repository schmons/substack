# Data

| File | Source (URL) | Collected on | Licence | Notes |
|------|--------------|--------------|---------|-------|
| `raw/gapminder/lex.csv` | Gapminder Fasttrack, https://github.com/open-numbers/ddf--gapminder--fasttrack | 2026-11-04 | CC BY 4.0 | Life expectancy at birth, 1800–2100. Post-1950 mostly UN WPP; pre-1950 Gapminder estimates (rough). |
| `raw/gapminder/gdp_pcap.csv` | same | 2026-11-04 | CC BY 4.0 | GDP per capita, 2017 PPP $. World Bank, back-extended with Maddison Project growth rates. |
| `raw/gapminder/child_mortality_0_5_year_olds_dying_per_1000_born.csv` | same | 2026-11-04 | CC BY 4.0 | Under-5 deaths per 1,000 births. Not used in figures yet. |
| `raw/gapminder/pop.csv` | same | 2026-11-04 | CC BY 4.0 | Population. |
| `raw/gapminder/countries.csv` | same | 2026-11-04 | CC BY 4.0 | Country names and regions. |
| `socialist_countries.csv` | Hand-coded by us | 2026-11-04 | — | Which countries count as socialist, and when. See below. |
| `processed/panel.csv` | Made by `scripts/02_prepare_data.py` | — | — | One row per country-year, 1900–2023, UN member states only. |
| `processed/same_gdp_gap_by_year.csv` | Made by `scripts/03_reanalysis.py` | — | — | The paper-style "same GDP" gap for every year. |

## Classification

- **Main groups:** `soviet_bloc` (USSR successor states, Eastern Europe, Mongolia) and `asia_cuba` (China, North Korea, Vietnam, Laos, Cambodia, Cuba).
- **Left out of the main analysis:** `yugoslavia` (market socialism, non-aligned) and `afro_marxist` (Angola, Mozambique, Ethiopia, Benin, Congo, Afghanistan, Nicaragua). Both are ambiguous cases, kept for sensitivity checks.
- **Not the paper's list.** We could not read the full paper, so this is our own list of Marxist–Leninist one-party states around 1983.

## Known problems

- **Today's borders.** Gapminder has no separate series for East Germany, Czechoslovakia, the USSR or Yugoslavia. We use the successor states (Russia, Czech Republic, …), so the USSR counts as 15 countries in unweighted comparisons.
- **GDP estimates for planned economies are uncertain.** They had no market prices, and modern figures differ a lot from 1980s World Bank estimates.
- **Health statistics from these regimes are known to be unreliable.** See `research-summary.md`.
