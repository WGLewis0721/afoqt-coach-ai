# AFOQT Overview (Form T family)

Quick heads up: this app is set up by default for the **cyber / software officer** path, not for rated aircrew (pilots, etc.). If that's you, jump to `CYBER_TRACK.md` for the specifics — this page is the big picture.

## What this test actually is

The AFOQT is a long, timed test with a bunch of different sections (the Air Force calls them "subtests"). It does two jobs at once: it helps decide whether you can commission as an officer at all (through OTS, AFROTC, or some Guard/Reserve paths), and it helps sort people into flying-related jobs — Pilot (including RPA), Combat Systems Officer, and Air Battle Manager.

Here's what to expect, plain and simple:

- About 516 multiple-choice questions, spread across 12 sections.
- The whole appointment takes about five hours once you count paperwork and breaks. The actual timed testing is roughly 3.5 hours of that.
- A lot of test sites now use the computer version (eAFOQT). Same strict timing, just on a screen.
- No calculator. Ever. And no penalty for a wrong answer — so always answer every question, even a guess.
- Your official score is a **percentile**, from 1 to 99 — not a percent-correct grade. A score of 60 means you did better than 60% of the people who've taken it, not that you got 60% of questions right.

## The one officially blessed practice tool

If you want to see what the real test screens look like, there's exactly one Air Force-endorsed practice tool: OATTS (Official AFOQT & TBAS Test-familiarization Software), at https://af-oatts.github.io/. Think of it this way: use this app to actually learn the material, build drills, and track your progress — and use OATTS to get comfortable with the real screens and timing, plus TBAS familiarization.

## The sections, in the order you'll take them

Here's the full lineup — what each section is called, its short code, how many questions, how many minutes you get, and roughly how many seconds that gives you per question:

| # | Subtest | Code | Items | Minutes | Sec/item | Scored composites |
|---|---------|------|------:|--------:|---------:|-------------------|
| 1 | Verbal Analogies | VA | 25 | 8 | ~19 | Verbal, Academic, ABM, CSO* |
| 2 | Arithmetic Reasoning | AR | 25 | 29 | ~70 | Quant, Academic, CSO* |
| 3 | Word Knowledge | WK | 25 | 5 | ~12 | Verbal, Academic, CSO†, ABM* |
| 4 | Math Knowledge | MK | 25 | 22 | ~53 | Quant, Academic, Pilot, CSO, ABM |
| 5 | Reading Comprehension | RC | 25 | 24 | ~58 | Verbal, Academic, ABM* |
| 6 | Situational Judgment | SJ | 16 | 35 | generous | none (officer research / judgment) |
| 7 | Self-Description Inventory | SDI | ~240 | 45 | ~11 | none (personality; not graded right/wrong) |
| 8 | Physical Science | PS | 20 | 10 | ~30 | CSO* |
| 9 | Table Reading | TR | 40 | 7 | ~10.5 | Pilot, CSO, ABM |
| 10 | Instrument Comprehension | IC | 25 | 5 | ~12 | Pilot, ABM |
| 11 | Block Counting | BC | 30 | 5 | ~10 | CSO, ABM |
| 12 | Aviation Information | AI | 20 | 8 | ~24 | Pilot, ABM |

A quick honesty note: \*different public sources don't fully agree on exactly which subtests feed CSO and ABM. This app uses the Wikipedia / Form T research mapping below and flags where sources disagree. Don't take any of this as gospel over your official score report — confirm with your testing office.

Sources also disagree on the Reading Comprehension time (24 vs 38 minutes) and the SJ item count (16 vs 50). This app trains you to the **faster** published times, so if the real thing turns out slower, that's a nice surprise instead of a nasty one. And if the pamphlet at your actual test site says something different, always go with the pamphlet.

## How the composite scores are built

| Composite | Subtests summed (Form T research / Wikipedia) |
|-----------|-----------------------------------------------|
| Pilot | MK + TR + IC + AI |
| CSO | VA + AR + MK + PS + TR + BC |
| ABM | VA + WK + RC + TR + IC + AI |
| Academic Aptitude | VA + AR + WK + MK + RC |
| Verbal | VA + WK + RC |
| Quantitative | AR + MK |

Heads up: some commercial prep sites list CSO as just WK + MK + TR + BC. Either way, MK, TR, and the verbal trio (VA/WK/RC) are safe bets to study — they show up no matter which recipe is right.

## What actually counts as "good enough" (policy as commonly published 2025–2026)

For a regular line-officer commission, the typical floor is:
- Verbal: **15**
- Quantitative: **10**

For rated jobs, the typical floors are (confirm these for your specific accession source):
- Pilot / RPA: Pilot composite **25**
- CSO: CSO composite **25**
- ABM: ABM composite **25**

Important distinction: those are just the minimums to be *eligible* — not what actually gets you picked. In public reporting, people who are actually competitive for pilot slots often cluster in the Pilot 70–90+ range. If you're not going rated, boards care more about your Verbal, Quant, and Academic Aptitude scores, plus GPA, your fitness test, your commander's ranking, and how the board sees your whole package.

One more wrinkle: some Guard/Reserve units still reference older combined Pilot+CSO rules. If that might apply to you, confirm locally.

## How many times you can take it

The commonly published rules:
- You get a limited number of lifetime attempts — often 2, with a third possible by waiver.
- There's usually a waiting period between attempts, often 90 days (though some sources still say 150). AFROTC guidance has used 90.
- A third attempt may require you to show proof of extra coursework or skill-building since your last try.
- Under current DAFMAN language, your best composite across attempts can become your score of record — this is called super-scoring.

Always double-check these with whichever office owns your package. Policy on this stuff changes.

## PCSM — this only matters if you're going rated

If you're chasing a pilot or RPA slot, you'll also run into PCSM (Pilot Candidate Selection Method), which combines:
1. Your AFOQT Pilot composite
2. TBAS (Test of Basic Aviation Skills) results
3. Your logged flying hours (civilian hours are capped in the official formula)

PCSM gets its own separate percentile. This app doesn't calculate it for you.

## How to actually use this app

1. Pick a target track on the dashboard.
2. Take a baseline mixed quiz so you know where you stand.
3. Study your weak spots in Coach mode (it's a local AI tutor grounded in these files).
4. Run timed drills at the real test's pace.
5. Track your readiness section by section — not just by how you *feel*.
