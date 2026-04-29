# Schema

## Node fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | slug | yes | Unique identifier (lowercase, underscores) |
| `name` | string | yes | Display name |
| `aka` | string | yes | Common aliases, separated by · |
| `cluster` | slug | yes | Primary cluster ID |
| `tags` | list | yes | Multi-dimensional categories for cross-filtering (see tag vocabulary below) |
| `hook` | string | yes | What draws people in — written in second person |
| `cost` | string | yes | What it actually does — evidence-based |
| `tactics` | list | yes | Deception techniques actively used to recruit and retain (see tactics vocabulary below) |
| `risk_level` | int 1–10 | yes | Danger severity (1=low manipulation, 10=direct violence risk) |
| `entry_point` | bool | yes | Common starting identity in pipelines |
| `terminal` | bool | yes | Hard to escape; destination rather than waypoint |
| `trap_depth` | int 1–5 | no | Escape difficulty for terminal nodes: 1=recoverable within months, 5=requires intensive long-term intervention. Omit for non-terminal nodes |
| `target_age` | string | yes | Primary vulnerable age range |
| `target_gender` | enum | yes | `male_heavy`, `female_heavy`, `mixed` |
| `target_socioeconomic` | string | yes | Economic vulnerability profile: `precarious`, `precarious to middle-class`, `middle-class`, `middle-class to affluent`, `affluent`, `mixed` |
| `target_psychology` | list | yes | Psychological vulnerabilities exploited |
| `timeline_entry` | string | yes | Time to get drawn in |
| `timeline_deepening` | string | yes | Time to become identity-fused |
| `timeline_terminal` | string | yes | Time to reach hardest-to-escape state; use `N/A` for non-terminal nodes |
| `pipeline_to` | list | no | Slug IDs of direct downstream nodes — informational; authoritative pipeline data lives in edges.md |
| `intervention_breaking` | string | yes | What might snap someone out |
| `intervention_alternative` | string | yes | Healthier alternative that addresses the same need |
| `intervention_resources` | list | yes | Organizations, hotlines, or tools |
| `evidence_sources` | list | no | Specific sources supporting the `cost` field for this node |

## Edge fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | slug | yes | Unique identifier: `{from}__{to}` (double underscore) |
| `from` | slug | yes | Source node ID |
| `to` | slug | yes | Target node ID |
| `strength` | enum | yes | `high` = well-documented reliable transition · `medium` = common but conditional · `low` = observed but rare or context-dependent |
| `mechanism` | string | yes | What drives the movement between identities — platform, psychological, or social mechanism |
| `bidirectional` | bool | no | Whether flow is documented in both directions (default: false) |

## Cluster fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | slug | yes | Unique identifier |
| `name` | string | yes | Display name |
| `tagline` | string | yes | One-line summary of the promise vs. delivery |
| `color` | hex | yes | UI color code |
| `risk_theme` | string | yes | Primary risk pattern across the cluster |

## Tag vocabulary

Used in `tags` field for cross-cluster filtering. A node may carry multiple tags.

- `masculinity` — male identity/grievance content
- `financial` — money/economic exploitation
- `political` — ideology/policy/activism
- `aesthetic` — lifestyle/visual identity
- `health` — body/fitness/diet
- `conspiracy` — hidden knowledge/anti-system thinking
- `spiritual` — religion/metaphysics/meaning
- `community` — belonging/tribal identity
- `isolation` — loneliness/disconnection as mechanism
- `violence` — direct or indirect violence risk
- `gambling` — addictive risk-taking behaviour exploited as entry point

## Tactics vocabulary

Used in `tactics` field to classify the deception mechanisms deployed by each identity. A node may use multiple tactics.

- `parental anxiety exploitation` — weaponises fear for children's safety or future to bypass critical thinking
- `wellness-to-conspiracy pipeline` — uses legitimate health concern as gateway to medical and institutional distrust
- `conspiracy thinking` — presents unfalsifiable hidden-knowledge framework as superior insight
- `identity fusion` — merges personal identity with group identity so that questioning the group feels like self-destruction
- `fear monetization` — converts ongoing threat anxiety into product sales, subscriptions, or donations
- `pseudo-intellectual cover` — uses dense or academic-sounding language to make extreme positions feel like rigorous analysis
- `dehumanization` — progressively strips out-group members of individuality or humanity to lower inhibition against harm
- `us vs. them framing` — reduces complex social reality to a binary of in-group (enlightened) vs. out-group (enemy or dupe)
- `isolation from support networks` — systematically separates target from friends, family, or institutions that might provide counter-perspective
- `magical thinking` — frames belief or spiritual alignment as a causal mechanism for material or social outcomes
- `irony shield` — deploys humour, memes, and plausible deniability to circulate genuinely harmful content without accountability
- `manufactured urgency` — creates artificial time pressure or crisis framing to prevent deliberate evaluation
- `sunk-cost entrenchment` — deepens commitment by ensuring the target has already sacrificed relationships, money, or reputation for the identity
- `parasocial replacement` — substitutes algorithmically mediated relationship with an influencer or anonymous figure for real community
- `violence` — direct or indirect violence risk