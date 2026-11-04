# Research summary

Everything we know for this article. Sources are in `assets/sources.csv`, which has an `access` column for how much of each one we actually read.

> **Reading status.** This environment's network blocked PubMed Central, Scribd, Thread Reader and most journal sites. Almost everything about the paper, the 1987 letters and Hickel's threads comes from **search snippets and abstracts**. Items marked ⚠️ must be checked against the original before publishing. See "Must check before publishing" at the bottom.

## Core question

Does Cereseto & Waitzkin (1986) show that socialism leads to better health? Our thesis:

1. **The design can't answer that question.** Comparing countries "at the same GDP" conditions on a variable the economic system itself affects. That is post-treatment, or collider, bias.
2. **The data were weak.** Socialist health statistics and GNP figures from the early 1980s were unreliable, and the health statistics were biased in the regimes' favour.
3. **Asked properly, the answer is mixed.** Industrialised socialist countries fell behind their neighbours on both income and health from about 1965. Poor Asian socialist countries (and Cuba, which was already a leader before 1959) did well on basic health. But non-socialist low-income countries such as Sri Lanka, Kerala and Costa Rica did just as well.

## The claim

**Hickel, 22 May 2022 thread** ⚠️ (verbatim from search index):
> "Using World Bank data, it finds that at any level of development, socialist countries outperformed capitalist countries on key social indicators, in 28 of 30 direct comparisons."
> "Socialist states had lower infant mortality, lower child death rate, longer life expectancy, better literacy, better secondary education, better food access, more doctors and nurses, and better physical quality of life."

He also cites Lena & London (1993) as confirmation, and concludes the lesson is universal public services.

**Hickel, 9 October 2021 thread** ⚠️, citing Sen (1981):
> "Sen found that this fact holds even when you correct for GDP. In other words, socialist policy delivers better social outcomes at any given level of GDP." … "Five years later, Cereseto and Watkin [sic] confirmed Sen's results."

This is the best hook: he says "correct for GDP" explicitly.

**"At any level of development" is false.** The study had no high-income socialist countries.

## The paper

**Citation:** Cereseto S, Waitzkin H. *Economic development, political-economic system, and the physical quality of life.* AJPH 1986;76(6):661–666.

**Companion version:** Int J Health Serv 16(4):643–658, which reports **30 of 36** comparisons instead of 28 of 30. A 1988 reprint appeared in J Public Health Policy 9:104–120.

**Data:** World Bank, 123 countries (about 97% of world population). Countries grouped by 1981 GNP per capita into low, lower-middle, upper-middle and high income. Source possibly World Development Report 1983 ⚠️.

**Outcomes:** infant mortality, child death rate, life expectancy, population per physician and per nurse, literacy, secondary enrolment, calorie supply, and the composite PQLI.

**Method:** compare socialist and capitalist group means within each income band. As far as we can tell from snippets, there was no regression and no adjustment for anything else.

**Strata** (OCR of Table 1, seen in snippets only) ⚠️:

| Band | Socialist | Capitalist | Mean GNP/cap (soc vs cap) |
|---|---|---|---|
| Low | **1** (almost certainly China, $300) | 33 | $300 vs $299 |
| Lower-middle | 4 | 28 | $1,040 vs $1,080 |
| Upper-middle | 8 | 20 | $4,129 vs $4,018 |
| High | **0** | ? | — |

**Implications:**
- About 13 socialist countries in total.
- "28 of 30" is roughly 10 correlated indicators × 3 bands, so it is not 30 independent tests.
- All low-income comparisons rest on **China alone**.
- The upper-middle socialist group is reportedly USSR, Czechoslovakia, GDR, Hungary, Yugoslavia, Romania, Bulgaria and Poland ⚠️ (r/badeconomics).

**Third category:** the paper has one for "postrevolutionary" countries where socialism was "not consolidated". Poor socialist-oriented states (Angola, Mozambique, Ethiopia…) may have been sorted there, which keeps them out of the socialist group ⚠️.

**The authors' 1987 reply to critics** (Kwon, Zilberg): the association holds "if GNP/c and political-economic system are controlled" ⚠️. In other words, they doubled down on the very move we criticise.

## Argument 1: conditioning on GDP is the wrong comparison

**The causal structure:**
- System → GDP. Well supported: Germany, Korea, Austria/Czechoslovakia, Finland/Estonia, Cuba (see Argument 3).
- GDP → health.
- Other things (history, schooling, industrial base, location) → both GDP and health.

**What "comparing at the same GDP" estimates.** At best it is the *controlled direct effect*: the effect of the system with income held fixed. But the system's main effect on health plausibly runs *through* income. So even with perfect data, this comparison ignores the main channel.

**Why it is worse than just "the wrong question".** GDP is a collider: system → GDP ← other advantages.
- A socialist country that reaches a given GDP *despite* a growth-sapping system must have stronger other advantages than a capitalist country at the same GDP.
- Those advantages also improve health.
- So the comparison credits socialism with health that really comes from the country's history.
- Montgomery, Nyhan & Torres (2018): post-treatment bias "can affect our estimates in any direction and can be of any size".

**Our simulation** (`scripts/01_simulation.py`, `figures/01_simulation.png`):
- 123 countries, 20% socialist.
- Socialism lowers log GDP by 0.6 and has **zero** direct effect on health.
- True total effect: −3.0 years.

| | Result |
|---|---|
| Raw comparison | −3.1 years on average (correct) |
| "Same GDP" regression | **+1.5 years** on average |
| Share of 2,000 simulated worlds showing a socialist advantage | **97%** |
| Paper-style band comparisons won by socialist countries | 66% |

**Analogy for readers:** comparing smokers and non-smokers *with the same lung function* tells you nothing about whether smoking is bad for you. The smokers who still have good lungs are unusual in other ways.

**Earlier robustness critique:** Burkett (1985, J Comp Econ) used extreme-bounds analysis over disputed control sets. The bounds include zero for many countries, so the result is fragile to the choice of controls even before the mediator problem.

**No published paper in this debate calls GDP a mediator by name, as far as we found.** That is a gap our article fills.

## Argument 2: the data

### Health statistics were biased in the regimes' favour

**Soviet definition of a live birth.**
- Only breathing counted.
- Babies under 28 weeks, under 1,000 g or under 35 cm counted as live births only if they survived 7 days.
- Anderson & Silver (1986): reported Soviet infant mortality should be raised by about **22–25%** to match the WHO definition, even with complete registration.

**Misreporting.**
- Velkoff & Miller (1995): early neonatal deaths were recorded as stillbirths. Hospitals were judged on infant mortality, so they had an incentive to misclassify.
- Underreporting was worse in the Central Asian republics.

**Size of the bias across the region** (HMD notes): from about 0% in Central Europe to 25% or more in South-Eastern Europe and the former USSR.
- GDR: a heartbeat without breathing counted as a stillbirth.
- Romania: babies under 1,000 g had to survive 15 days to count.

**Suppression.**
- The USSR stopped publishing infant mortality and life expectancy in the mid-1970s; publication was banned from 1974 to 1986.
- Davis & Feshbach (1980): infant mortality rose from 22.9 (1971) to about 31.1 (1976, estimated).
- So the World Bank's figures for the USSR around 1981 must have been **estimates or carried forward**.

**Cuba.**
- Gonzalez & Gilleskie (2017): late-fetal mortality was about 6× early-neonatal mortality, suggesting reclassification. Adjusted infant mortality is about **2× the reported figure**.
- *Fair point to include:* even after adjustment, Cuba is still slightly better than countries at similar development.
- Berdine, Geloso & Powell (2018): doctors face infant-mortality targets with penalties, and there are coercive abortions after abnormal ultrasounds.
- Mesa-Lago: official statistics tended "to deflate prerevolutionary figures and to inflate revolutionary achievements".

**Literacy:** mostly census self-reports or official claims. Eberstadt says Cuban literacy figures were redefined. We have no solid source on 1980s Eastern European literacy statistics.

### GNP figures for planned economies were guesses

- **Different accounting.** Socialist countries reported net material product, which leaves out most services. Prices and exchange rates were set by the state, so converting to dollars is guesswork.
- **World Bank estimates.** The Bank's own project (Marer 1985) put USSR 1980 GNP per capita at **$2,700–5,700**. It made **no estimate for Bulgaria or Cuba**, and said it could not estimate most planned economies' per-capita GNP.
- **Overstatement.**
  - The CIA put Soviet output per head equal to Spain's; Nordhaus & Hewett (1990) say Western estimates overstated Soviet growth.
  - Late-1980s estimates ranged from 12% to 57% of US income (Harrison).
  - The *CIA World Factbook 1987* famously showed East Germany richer per head than West Germany.
- **⚠️ Be honest about direction.** If socialist GNP was *overstated*, socialist countries were compared with *richer* capitalist peers. That works *against* finding a socialist advantage, so on this point the paper is conservative.
  - For China, an exchange-rate GNP of $300 probably *understated* real income, which works the other way.
  - The net effect is unclear. Don't lean on GNP error; lean on the design problem and the biased health data.

### Our own replication with modern data

We used Gapminder data (`scripts/03_reanalysis.py`, `04_robustness.py`) with our own list of socialist countries, since we couldn't read the paper's.

**1983 "same GDP" gap in life expectancy** (quadratic in log GDP), from `data/processed/robustness_1983.csv`:

| Specification | Gap (years) | SE |
|---|---|---|
| All socialist (paper-style) | **+0.9** | 1.1 |
| USSR & Eastern Europe only | **−0.9** | 0.8 |
| China, Vietnam, Laos, Cambodia, N. Korea, Cuba only | **+7.1** | 2.9 |
| + region fixed effects | −1.9 | 1.2 |
| Population-weighted (China dominates) | +6.3 | 1.9 |
| Including Yugoslavia & Afro-Marxist states | −0.2 | 1.1 |
| No GDP adjustment (raw) | +3.6 | 1.3 |
| Log child mortality | −0.06 (n.s.) | 0.12 |

- **With modern GDP estimates, Eastern Europe sits on or below the capitalist curve** (Figure 2). The paper's result rests on the Asian countries and Cuba.
- **The answer flips with the GDP numbers.** Modern GDP figures for the USSR and Eastern Europe are reconstructed and much higher than the 1980s World Bank estimates, and the 1983 result changes with them. That is a point in itself: the conclusion depends on which guess about planned-economy GDP you use.
- **The Soviet-bloc gap over time** (Figure 3): about +3.5 years in the 1950s, falling steadily to about −1.5 by 1989. Not a stable feature of "the system".
- **⚠️ Gapminder limits:** no separate GDR, Czechoslovakia, USSR or Yugoslavia (we use successor states, so the USSR counts as 15 countries); pre-1950 values are rough.

## Argument 3: asking the right question gives a mixed answer

### Europe: caught up, then stalled for 25 years

**Figure 4** (Gapminder):
- Finland vs Estonia, Austria vs Czechia & Hungary, and Spain/Portugal/Italy/Greece vs Poland/Bulgaria/Romania all show life expectancy tracking until about 1965.
- After that it was **flat in the East until 1989** while the West kept rising.
- Income diverged from the start.

**Life expectancy (Gapminder):**

| | 1965 | 1989 |
|---|---|---|
| Finland | 69.4 | 75.1 |
| Estonia | 70.5 | 70.3 |
| Austria | 69.9 | 75.6 |
| Czech Republic | 70.3 | 71.5 |
| Spain | 70.8 | 76.8 |
| Poland | 69.7 | 71.4 |

**GDP per capita, 1989 (Gapminder, 2017 PPP):** Finland $37k vs Estonia $22k; Austria $39k vs Czech Republic $25k.

**Maddison, as % of Germany:** Austria 67 vs Czechoslovakia 62 in 1937; 99 vs 53 in 1989.

**Literature:**
- Mackenbach (2013): countries that did and didn't join the Soviet bloc diverged after about 1960. Before that, infectious-disease control advanced under all regimes.
- Aburto & van Raalte (2018): Central and Eastern European male life expectancy was stuck at 65–70 from the 1960s to the mid-1980s.
- Bobak & Marmot (1996): the East–West divide was driven by adult chronic disease.
- Around 1990, Central and Eastern European male life expectancy was about 7 years below Western Europe's.
- Hungary trailed Austria by 7.3 years (men) and 5.3 years (women) in 1989–90.
- Eberstadt: the USSR was the first industrialised country with a peacetime fall in life expectancy.

**Germany:**
- The GDR was ahead in the mid-1960s and the FRG ahead from the mid-1970s.
- The 1990 gap was 3.4 years (men) and about 2.7 (women).
- After reunification the East gained 6–7 years by 2009, and the female gap was gone by 2013 (INED).
- ⚠️ Becker, Mergele & Woessmann (2020): East and West already differed before the division, and about a fifth of the East's population moved West before 1961, a selective group. So it is not a clean experiment.

**Counterpoint to include:** Brainerd (2010) finds real, large Soviet gains in infant mortality and height from 1945 to 1970, comparing well with European peers. Then stagnation.

### Poor Asian countries and Cuba: the strongest pro-socialist evidence

**China vs India:**
- China's life expectancy was far ahead by the 1970s (Gapminder 1975: 60.8 vs 49.5).
- Drèze & Sen (1989) agree, adding: "There are skeletons in China's cupboard — millions of them from the disastrous famine of 1958–61." Gapminder shows China's life expectancy falling to 26 in 1960.

**Cuba:**
- McGuire & Frankel (2005): Cuba **led** Latin America in mortality decline before 1959. From 1960 to 1995 it ranked only 5th of 20 on infant-mortality reduction and 4th on life-expectancy gains.
- Costa Rica, never socialist, overtook Cuba on life expectancy by the late 1980s (Gapminder 1989: 76.6 vs 75.3).
- Devereux (2021): Cuban GDP per capita grew only about 40% over 1957–2017.

**Good Health at Low Cost** (Rockefeller Foundation, 1985):
- The classic low-income success stories were China, **Kerala, Sri Lanka and Costa Rica**. Only one was socialist.
- What they share: primary care, mass schooling (especially for girls), public health and nutrition.
- So "good health at low income" does not need socialism.
- The 2011 follow-up (Balabanova, McKee, Mills) revisited the same four.

**Fair framing:** some socialist states were very good at "single-goal problems" (vaccination, basic sanitation, primary care) through state capacity and coercion (Geloso, Berdine & Powell 2020). That is real, and it is not the same as "socialism causes better health".

### Other quantitative work

| Study | Finding | Caveat |
|---|---|---|
| Lena & London (1993) | Democracy and left-wing regimes go with better health, net of GNP | About left/right regimes, not economic systems; also conditions on GNP |
| Moon & Dixon (1985) | Democracy goes with better PQLI, controlling for wealth | |
| Sookias et al. (2018) | Former communism *negatively* predicts health and HDI across 44 Eurasian countries | |
| Ross (2006) | How missing autocracies are handled changes regime–health results | |
| Navarro (1992, 1993) | Defends C&W, continent by continent | |

## Arguments against us / open questions

- **The authors would say** they're estimating "efficiency": health per dollar. That is a legitimate descriptive question. But it isn't what Hickel claims ("socialism delivers better outcomes"), and the collider problem means even the "per dollar" number is biased.
- **Overstated socialist GNP biases against the socialist group.** We must concede this.
- **China's early health gains are real and large.** Don't deny them; put them in context with the famine and the non-socialist low-cost success stories.
- **Is the 1950s Soviet-bloc "above the curve" advantage inherited or caused?** We can't tell from Gapminder; pre-war data are rough.
- **Selection into socialism wasn't random**, e.g. Soviet occupation. But that cuts both ways and is mostly about geography.
- **Our replication uses our own list and modern GDP**, not the paper's. It is not a strict replication.

## Quotes worth using

> "at any level of development, socialist countries outperformed capitalist countries … in 28 of 30 direct comparisons." — Hickel, 2022 ⚠️

> "socialist policy delivers better social outcomes at any given level of GDP." — Hickel, 2021 ⚠️

> Post-treatment bias "can affect our estimates in any direction and can be of any size." — Montgomery, Nyhan & Torres, 2018

> "There are skeletons in China's cupboard — millions of them from the disastrous famine of 1958–61." — Drèze & Sen, 1989

> Cuban official statistics tended "to deflate prerevolutionary figures and to inflate revolutionary achievements." — Mesa-Lago

## People to contact / follow up

- Howard Waitzkin (UNM, emeritus): his view now?
- Vincent Geloso (George Mason): Cuba and Soviet data.
- Johan Mackenbach (Erasmus MC): European divergence.
- Roberto Gonzalez: Cuban infant mortality.

## Must check before publishing

1. **Read the paper** (PMC1646771): Table 1 country list per band, GNP sources and footnotes, the "postrevolutionary" category, and exact quotes.
2. **Read the Kwon and Zilberg letters and the reply** (PMC1646820, PMC1646830, PMC1646824).
3. **Hickel's threads verbatim:** x.com/i/status/1528326657500758016 and x.com/i/status/1446769071991705605.
4. **Sen (1981):** what "correct for GDP" meant there.
5. **Optional robustness:** redo Figure 2 with the paper's own 1981 GNP figures (from Table 1) and Maddison GDP. Use Human Mortality Database data for East vs West Germany.

## Dead ends

- **Full texts:** we couldn't fetch any here (network policy). The only reachable data source was GitHub, hence Gapminder.
- **Gapminder country coverage:** it has no series for East Germany, Czechoslovakia, the USSR or Yugoslavia, despite listing them as entities.
