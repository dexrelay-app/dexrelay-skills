# ASO Audit Framework

Use this when the product has a live App Store listing, a TestFlight page that is about to become public, or a launch is close enough that a readiness audit is useful.

## Modes

- **Live listing audit**: score the existing surface.
- **Pre-launch readiness audit**: score the draft surface and mark missing public evidence as `Not yet live`.

## Scorecard

Score each area from 0 to 10. Convert to a weighted overall score only when enough evidence exists.

| Area | Weight | What to check |
| --- | --- | --- |
| Title | 20 | primary keyword fit, readability, character usage, differentiation |
| Subtitle | 15 | secondary keyword coverage, no repetition, value proposition |
| Keyword field | 15 | coverage, no wasted repeats, relevance, character efficiency |
| Description | 5 | hook quality, benefits, proof, scannability, CTA |
| Screenshots | 15 | first-three story, caption clarity, consistency, feature prioritization |
| Preview video | 5 | hook, clarity without sound, usefulness |
| Ratings and reviews | 15 | average rating, recent trend, review count, response quality |
| Icon | 5 | distinctiveness, category fit, small-size legibility |
| Keyword rankings | 10 | visibility on target terms, competitor gap |
| Conversion signals | 5 | promo text, update notes, events, custom pages, pricing clarity |

## Quick-Win Structure

Return findings in three buckets:

### Quick wins

- changes that can be made today
- mostly metadata, copy, ordering, or clarity fixes

### High-impact changes

- changes for this week
- often screenshots, launch assets, positioning shifts, rating-prompt fixes, or keyword refocusing

### Strategic recommendations

- changes for this month
- distribution, launch sequencing, localization, pricing, or product-surface gaps

## Pre-Launch Adaptation

When there is no public listing yet:

- keep title, subtitle, keyword field, description, screenshots, icon, and conversion signals
- replace ratings/reviews with **social proof readiness**
- replace keyword rankings with **keyword territory readiness**
- call out missing assets explicitly instead of inventing scores

## Output Snippet

Use a compact scorecard when the full audit would be overkill:

```text
ASO readiness score: 72/100

Title: 8/10
Subtitle: 7/10
Keyword field: 6/10
Description: 7/10
Screenshots: Not yet reviewed
...
```
