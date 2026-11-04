---
title: "Same GDP, Better Health? How a 1986 Paper Fooled Itself"
subtitle: "Comparing socialist and capitalist countries 'at the same income' answers the wrong question, and the data don't hold up either."
status: researching   # idea | researching | drafting | editing | published
created: 2026-11-04
target_publish:
published_url:
tags: [causal-inference, bad-science, health, economics, socialism]
---

# Same GDP, Better Health?

## One-sentence pitch

A widely shared 1986 paper (cited by Jason Hickel) claims socialist countries have better health than capitalist ones "at the same level of economic development". Comparing countries at the same GDP is a textbook causal-inference mistake that can manufacture exactly this result, and when you redo the analysis with today's data the effect mostly disappears or reverses.

## Outline

1. **Hook: the claim.**
   - Hickel (2021): "socialist policy delivers better social outcomes at any given level of GDP." (2022): "at any level of development, socialist countries outperformed capitalist countries … in 28 of 30 direct comparisons." *(verify both verbatim)*
   - The source is Cereseto & Waitzkin (1986), AJPH: 123 countries, World Bank data, socialist countries better in "28 of 30 comparisons" within income groups.
   - It sounds clean: like for like, same income, different system.

2. **What the paper did, in one paragraph.**
   - Grouped countries into four GNP-per-capita bands and compared averages within each band.
   - About 13 socialist countries in total. Low-income band: China alone vs 33 capitalist countries. High-income band: no socialist countries at all, so "at any level of development" is simply false.
   - "28 of 30" ≈ 10 correlated indicators × 3 bands, not 30 independent tests.
   - Their answer to critics in 1987: the result holds "if GNP/c and political-economic system are controlled". That defence is the problem.

3. **The core mistake: you can't hold GDP fixed when the system changes GDP.**
   - The economic system is the "treatment"; GDP is one of its main *outcomes*.
   - Comparing at the same GDP asks: "Among countries that ended up equally rich, who is healthier?" It doesn't ask "What did the system do to health?"
   - Analogy: comparing smokers and non-smokers *with the same lung function* and finding smokers have fewer heart attacks.
   - It's worse than just "the wrong question". GDP is driven by the system *and* by things like history, schooling and infrastructure. A socialist country that reached the same GDP *despite* a growth-sapping system must have had a lot going for it, and those same advantages improve health. (Collider bias.)
   - **Figure 1 (simulation):** in a world where socialism has *zero* direct effect on health and makes countries poorer, the "same GDP" comparison finds a socialist health advantage in ~97% of simulated worlds.

4. **Redoing their comparison with today's data.**
   - **Figure 2:** 1983 life expectancy vs GDP. Eastern Europe sits *on or below* the capitalist curve. The advantage comes entirely from China, Vietnam, North Korea and Cuba.
   - The paper-style "same GDP" gap in 1983: +0.9 years overall (not significant); −0.9 for the USSR & Eastern Europe; +7.1 for Asia + Cuba.
   - Why it differs from 1986: GDP figures for planned economies were guesses, since there were no market prices. The result depends on which guess you use.
   - Earlier warning sign: Burkett (1985) showed the result is fragile to the choice of controls.
   - **Figure 3:** the Soviet-bloc "advantage" was +3.5 years in the 1950s and shrank to below zero by the 1980s. Whatever was going on, it wasn't a stable feature of the system.

5. **Asking the right question: what happened to similar countries?**
   - **Figure 4:** neighbours with similar starting points (Finland/Estonia, Austria/Czechia & Hungary, Southern vs Eastern Europe).
     - Life expectancy tracked closely until about 1965, then stalled in the East for 25 years while the West kept rising.
     - Income diverged from the start. That lost income is exactly what the "same GDP" comparison hides.
   - **The honest part:** poor Asian socialist countries (China especially) did make large early health gains compared with, for example, India. *Except* during the 1959–61 famine, which killed tens of millions.
     - But the 1985 Rockefeller "Good Health at Low Cost" study found the same at low income in Sri Lanka, Kerala and Costa Rica, none of them communist.
     - What these cases share is primary care, schooling (especially for girls) and public health. Not ownership of the means of production.
   - Cuba led Latin America in health *before* 1959. After 1960 it was only 5th of 20 on infant-mortality reduction (McGuire & Frankel). Costa Rica overtook it.

6. **And the data themselves.**
   - Soviet infant-mortality definitions, underreporting, and publication stopped in the 1970s.
   - Cuba's infant-mortality figures.
   - Soviet live-birth definition: reported infant mortality ~22–25% too low (Anderson & Silver). Publication banned 1974–86, so the 1981 numbers were estimates.
   - Cuba: adjusted infant mortality ~2× reported (Gonzalez & Gilleskie), though still a bit better than peers.
   - GNP for planned economies: guesswork (USSR $2,700–5,700; none for Cuba or Bulgaria). Concede that overstated GNP actually works *against* the socialist group.

7. **What good evidence would look like.**
   - Compare on *pre-treatment* characteristics, not post-treatment ones.
   - Natural experiments (Germany, Korea).
   - Trajectories rather than a single snapshot.
   - Honest uncertainty about the data.

8. **Conclusion.**
   - The claim isn't crazy: some socialist countries did well on basic health at low incomes.
   - But the 1986 paper can't show that socialism *caused* better health, because its design cannot answer that question.
   - Bigger lesson: "controlling for" a variable is not a neutral act. Ask whether the thing you control for is caused by the thing you're studying.

## Draft

*(to write)*
