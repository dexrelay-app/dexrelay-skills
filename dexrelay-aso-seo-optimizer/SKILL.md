---
name: dexrelay-aso-seo-optimizer
description: Research and optimize product naming, App Store metadata, SEO copy, website positioning, domain fit, and iOS launch details for apps or websites. Use when Codex needs to name a new product, improve an existing name, draft App Store or TestFlight metadata, compare ASO/SEO options, evaluate competitor language, inspect App Store/web/Reddit demand signals, or recommend domain-friendly titles based on the problem the product solves.
---

# DexRelay ASO SEO Optimizer

Build a market-informed naming and metadata recommendation for an app or website. Start from the product itself, verify demand and competition online, and return a ranked package that is ready for App Store Connect, TestFlight, landing pages, and SEO work.

If `app-marketing-context.md` exists in the repo root, read it first and treat it as the marketing source of truth. If it does not exist and the task is substantial, create it in the repo root using [references/app-marketing-context-template.md](./references/app-marketing-context-template.md). When the user asks to apply the skill to the current app, leave behind durable repo artifacts instead of only returning chat output.

## Workflow

1. Understand the product before naming it.
2. Build or refresh the marketing context.
3. Decide whether this is pre-launch positioning, a live-listing optimization, or both.
4. Research the market with live data.
5. Build a keyword and intent map.
6. Generate multiple strong options instead of locking onto one early.
7. Score options for clarity, intent match, differentiation, and distribution fit.
8. Deliver fill-ready metadata, not just brainstormed names.
9. Save durable outputs when the task is repo-backed.

## Step 1: Inspect The Product

Read local context first. Prefer source files, README files, PRDs, landing-page copy, screenshots, app strings, and configuration that reveal:

- the user problem
- target audience
- platform: iOS app, website, or both
- core actions and features
- emotional tone: utility, premium, playful, technical, consumer, B2B
- monetization and acquisition constraints

If the repo is sparse, infer from the best available artifacts and state assumptions clearly.

## Step 2: Build Or Refresh Marketing Context

Before producing recommendations, organize the product into a concise context:

- current working name
- app or website URL if it exists
- target user and user problem
- core value proposition
- competitors or substitutes
- monetization model
- primary market and language
- launch stage
- growth goal: downloads, signups, revenue, activation, retention, brand

If the user did not provide this explicitly, infer from local files first, then fill gaps with research. Use [references/app-marketing-context-template.md](./references/app-marketing-context-template.md) as the section structure. For repo work, prefer creating or updating `app-marketing-context.md` so later ASO turns can start from the same source of truth.

## Step 3: Choose The Right ASO Mode

Decide early which path fits the product:

- **Pre-launch ASO**: no public listing yet, or the product is still in TestFlight. Focus on positioning, keyword territory, metadata drafts, category framing, and launch-readiness gaps.
- **Live-listing optimization**: public App Store page exists. Audit the current listing, compare it to competitors, and recommend deltas.
- **Shared brand work**: App Store plus website/landing page need one coherent story.

When a live or imminent App Store launch is involved, use the scoring structure in [references/aso-audit-framework.md](./references/aso-audit-framework.md) to produce at least a compact audit snapshot. If there is no live listing, adapt the same framework into a pre-launch readiness audit and mark unverified fields clearly.

## Step 4: Research The Market

Use live web research whenever evaluating current names, competition, App Store positioning, Reddit language, SEO viability, or domain availability.

Research at least these sources when relevant:

- App Store search results and competing app metadata
- direct web competitors and landing pages
- Reddit threads where target users describe the problem in their own words
- search-result snippets or keyword tools if available through the current environment
- domain registration or resolver signals for candidate names

When the space is crowded or the naming choice is high stakes, structure the findings with [references/competitor-analysis-template.md](./references/competitor-analysis-template.md).

Capture:

- recurring keywords
- category conventions
- overused naming patterns
- gaps where a sharper title could stand out
- evidence of user language that should influence title/subtitle/tagline choices

Do not present availability or ranking claims as facts unless checked. Distinguish verified findings from inference.

## Step 5: Build A Keyword And Intent Map

Before drafting final metadata, expand the keyword space with the process in [references/keyword-research-playbook.md](./references/keyword-research-playbook.md).

At minimum, produce:

- 3 to 5 primary keywords or intents
- 5 to 10 secondary keywords
- long-tail or audience-specific phrases when relevant
- a note on which terms belong in title, subtitle, keyword field, website H1, and meta title

If the data is weak, score opportunity with informed judgment and label it as inferred rather than verified.

## Step 6: Generate Candidate Sets

Produce multiple naming directions, not minor spelling variants. Include a mix such as:

- direct and descriptive
- brandable but still intuitive
- SEO-forward
- ASO-forward
- premium or emotional
- domain-friendly compact names

For each candidate, evaluate:

- what job it signals immediately
- likely search intent alignment
- memorability
- pronunciation
- risk of sounding generic or crowded
- risk of App Store confusion with existing products
- fit for website URL and social handles when discoverable

Avoid names that are clever but unclear, overloaded with stopwords, or likely to collide with dominant incumbents.

## Step 7: Optimize For The Surface

Adapt recommendations to the actual launch surface.

### For iOS apps

Prepare the fields most useful for App Store Connect and TestFlight, including:

- app name/title candidates
- subtitle candidates
- keyword themes or keyword list when requested
- short promotional copy angles
- App Store description outline and final draft
- TestFlight beta app description
- TestFlight feedback email suggestion if needed
- What to Test notes
- release notes draft if the version context is available
- category positioning and audience framing

Use [references/metadata-optimization-checklist.md](./references/metadata-optimization-checklist.md) for field-by-field checks and common failure modes. Unless the user asks for fewer, provide one recommended package and two viable alternates with different emphasis such as keyword-forward, brand-forward, or conversion-forward.

Use these iOS constraints unless the current platform documentation proves otherwise:

- App Store title: 30 characters
- App Store subtitle: 30 characters
- iOS keyword field: 100 characters, comma-separated, no spaces
- promotional text: 170 characters

Keyword field rules:

- do not repeat words already used in title or subtitle
- prefer singular forms unless there is a reason not to
- do not include competitor brands
- do not waste space on `app`, `free`, or obvious category words
- prioritize by relevance first, then discoverability

When relevant, note title-length tradeoffs, brand-vs-keyword tradeoffs, and localization opportunities.

### For websites

Prepare:

- product name candidates
- homepage H1 options
- meta title options
- meta description options
- tagline options
- positioning statement
- target keyword themes
- domain recommendations

Prefer names that can work across the product, homepage, and search snippets without feeling forced.

## Step 8: Check Domains And Naming Risk

For the top candidates, check whether plausible domains look usable. Prefer `.com` first, then note stronger alternatives only when necessary. If exact availability cannot be confirmed, report the observed signal precisely, such as:

- exact domain resolves
- registrar shows unavailable
- no obvious active site found, but availability remains unconfirmed

Also flag:

- spelling ambiguity
- trademark-like collision risk based on obvious market evidence
- App Store crowding
- weak SEO distinctiveness

Do not give legal clearance. Provide practical naming risk, not legal advice.

## Step 9: Score, Rank, And Recommend

Always end with a recommendation, not just a list.

Return:

- a top pick with concise rationale
- two or three backup picks
- why each loser lost
- the best metadata package for the top pick
- open questions that would materially change the recommendation

Base the ranking on evidence plus judgment. A slightly less keyword-heavy name may still win if it is more ownable, memorable, and distribution-friendly.

Use the stricter scoring matrix in [references/name-score-matrix.md](./references/name-score-matrix.md) for finalists or whenever the user asks for the best possible option. Prefer a 1-5 score per dimension plus a weighted total. Show the matrix whenever it helps the decision.

## Step 10: Save Durable Outputs

When working inside a repo, prefer leaving behind the artifacts another operator would need:

- `app-marketing-context.md` for the reusable source of truth
- a focused ASO report in `docs/` if the work is substantial
- updated launch metadata drafts in existing marketing docs if the repo already has a canonical location

If you only return chat output, say why no file artifact was created.

## Output Standard

Use the report structure in [references/deliverable-template.md](./references/deliverable-template.md) when delivering substantial work. Trim sections that are irrelevant, but keep the final answer opinionated and decision-ready.

Minimum quality bar:

- show what product understanding was used
- cite current web findings when they matter
- provide at least 5 serious name candidates unless the user asks for fewer
- include a keyword strategy section for iOS or SEO surfaces when those matter
- include an ASO audit or readiness snapshot for App Store work
- include both rationale and risks
- include fill-ready copy for the winning option
- include character counts for App Store title, subtitle, and promotional text when those fields are present
- include a keyword coverage view when recommending iOS metadata
- include a scored finalist table when comparing 3 or more serious contenders

## Practical Heuristics

- Prefer concrete user language over founder-internal jargon.
- Prefer names that say the outcome or job to be done.
- If the market is crowded with generic keyword titles, search for a clearer and more ownable angle.
- If the product is dual-surface, optimize for the shared brand first, then tailor App Store and SEO copy separately.
- If the app solves an urgent problem, clarity beats cleverness.
- If the product is consumer and brand-led, balance distinctiveness with search discoverability.
- Read the codebase or docs before browsing so research is anchored to the actual product.
- Prefer a shared strategic narrative across name, subtitle, H1, and meta title rather than optimizing each field independently.
- When useful, provide 3 variants for title, subtitle, and description angle instead of only one final draft.
- Flag repeated-keyword waste explicitly for iOS metadata.
