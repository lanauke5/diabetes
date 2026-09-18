# MASTER PROMPT — diabetes.naturalhealthone.com ARTICLE (NaturalHealthOne)

Adapted from the Artsina beauty template. Every article on this site follows this spec.
The existing generator in `sitegen/` already implements it; hand-written pages must match it.

---

## ARTICLE DETAILS

- **Title:** [ambil dari judul artikel]
- **Category:** salah satu dari 13 kategori di bawah
- **Target length:** 900–1200 words (body text, excluding headline/CTA/related)
- **Target audience:** English-speaking adults (mostly 30–65) living with type 2 diabetes or
  prediabetes — or caring for someone who is. They are tired of hype and clickbait, they want
  practical context they can actually use, and above all they need better questions to bring
  to their healthcare team.
- **Voice:** a health-literate friend who actually reads the research — not a textbook, not a
  clinic handout, and definitely not a hype account.

---

## WRITING STYLE — CRITICAL

- Write like a knowledgeable friend, not a textbook or AI.
- Use contractions naturally (you'll, it's, don't, here's).
- Vary sentence length — mix short punchy sentences with longer ones.
- Include occasional personal-feeling observations ("The truth is...", "Here's what surprises
  most people...", "Most people get this wrong...").
- Use second person "you" throughout — speak directly to the reader.
- **No bullet-point lists in the article body** — write in flowing paragraphs.
- No overly formal transitions ("Furthermore", "Moreover", "In conclusion").
- Use natural transitions ("The thing is...", "That said...", "And here's where it gets
  interesting...").
- Occasional one-sentence paragraphs for emphasis.
- Explain one clinical term plainly each time it appears. Never hide behind jargon, and never
  use jargon to sound authoritative.

---

## MEDICAL SAFETY RULES — CRITICAL

This is a health site, so these rules override everything else:

- Articles are **educational only**. They are not medical advice, diagnosis, or treatment.
- **Never** instruct the reader to start, stop, or change medication, insulin, or a monitoring
  plan. Always route that decision to their clinician.
- Match wording to evidence strength: "may", "can", "is associated with" — never "will",
  "cures", "reverses", or "guarantees".
- Targets are personal. Present published ranges as *group* statistics, then tell the reader
  to ask their clinician for *their* numbers.
- Every article ends with a **safety note** and a link to `medical-disclaimer.html`.
- Emergency language is explicit: chest pain, breathlessness, confusion, severe symptoms →
  contact local emergency services now, not at the next appointment.
- No fear-mongering. Complications articles must make clear that complications are **not
  inevitable** and that ordinary consistent care is what prevents them.
- No weight stigma. Weight is discussed as one physiological factor among many, never as a
  moral failing or the sole cause of the condition.

---

## STRUCTURE

1. **Hook opening** — one punchy paragraph that immediately addresses the reader's pain point
   or curiosity. (NO generic "In today's world..." or "Diabetes is a growing epidemic..."
   openers. Start with the specific frustration: the 6 a.m. reading that makes no sense, the
   log that never helped, the supplement drawer full of promises.)
2. **The core problem or context** — 2 paragraphs explaining why this matters and what is
   really going on.
3. **Main content** — 4–6 paragraphs covering the topic in depth with real, useful information.
4. **Practical takeaway** — 2 paragraphs of actionable advice the reader can apply today.
5. **CTA section** — rotate through the 5 variations below.

---

## CONTENT RULES

- Include **at least 2 specific terms** relevant to the topic — e.g. HbA1c, dawn phenomenon,
  insulin resistance, beta-cell function, glycemic index, continuous glucose monitor, resistant
  starch, sleep apnea, cortisol, diabetic neuropathy, retinopathy, insulin sensitivity,
  postprandial glucose.
- Include **one surprising or counterintuitive fact** — e.g. poor sleep raises glucose the next
  day regardless of what you ate; cinnamon's evidence is far weaker than its marketing;
  a workout does not cancel hours of uninterrupted sitting; a "normal" fasting value says
  nothing about the post-meal spike.
- Reference **one common mistake** readers might be making — e.g. testing at random times so
  no reading is comparable; blaming food for a stress response; stopping a plan after one bad
  week; self-treating a foot wound at home.
- Give **at least one concrete, specific piece of advice** — not vague ("take care of
  yourself") but actionable ("fix your wake time before you change anything else, and hold it
  for two weeks").
- **Do NOT mention specific brand names** unless writing a reviews/ or best/ article — and
  even then, evaluate product *types* and criteria, never invent credentials or rankings.
- **Banned phrases:** "game-changer", "revolutionary", "transformative", "holistic approach",
  "journey", "superfood", "detox", "cleanse", "miracle", "breakthrough", "scientifically
  proven", "reverse your diabetes", "cure".
- Do NOT end sentences with "as well".
- Do NOT start paragraphs with "Additionally" or "Furthermore".

---

## HTML OUTPUT FORMAT

Output the article as a complete HTML page using this exact structure and color scheme.

### HEAD section

- Google Fonts: **Cormorant Garamond** (serif) + **Jost** (sans-serif), weights:
  `Cormorant Garamond:ital,wght@0,400;0,500;0,600;0,700;1,500;1,600` and
  `Jost:wght@0,300;0,400;0,500;0,600;0,700;1,400`.
- Color variables (per category — see COLOR COMBINATIONS below):

```css
:root {
  --ink: #173b3b;
  --text: #415857;
  --light-mid: #718583;
  --paper: #f8faf8;
  --white: #ffffff;
  --border: #c9d9d1;
  --mist: #e7f0ef;
  --accent: #5a9898;
  --accent-dark: #356f70;
  --accent-light: #b0d4d4;
  --hero-bg: linear-gradient(135deg, #1a2c2c, #2a4040, #3a5858);
  --max: 1200px;
}
```

- Full meta block: description, theme-color, robots, canonical
  (`https://diabetes.naturalhealthone.com/{category}/{slug}.html`), Open Graph tags.

### PAGE STRUCTURE

- **Topbar** (dark `--ink` background, promo/strap text + "Medical disclaimer" link)
- **Header** with logo **NaturalHealth*One*** (`<em>` around "One" in accent color) and tagline
  "Diabetes & metabolic health"
- **Navigation:** Home | Type 2 | Prediabetes | Blood sugar | Nutrition | Monitoring | Reviews
  (add "Monitoring" active class on current category; links are relative `../` from article
  pages, plain from hub pages)
- **Skip link** to `#article` for accessibility
- **Article hero** (full-width, dark category gradient — see below)
- **Article body** (`max-width` ~68ch, left column of a grid with a sidebar)
- **Safety note** aside (accent-bordered box)
- **CTA section** (see the 5 variations below)
- **Related articles** (3 cards)
- **Newsletter signup**
- **Footer** (Topics / Trust / Legal columns, disclaimer, "For emergencies, contact local
  emergency services.")

### ARTICLE HERO

- Dark background using `var(--hero-bg)`.
- Article category label (small caps, wide letter-spacing, accent-light).
- Article title — Cormorant Garamond, large, weight 600, with **one word or phrase in italic
  accent color**.
- Byline: "By NaturalHealthOne Editors" + date + read time.
- **Estimated read time:** word count ÷ 200, rounded up ("6 min read").

### ARTICLE BODY TYPOGRAPHY

- Body text: Jost 300, ~16px, line-height 1.85, color `var(--text)`.
- Headings (H2): Cormorant Garamond, ~32px, weight 400/600, color `var(--ink)`,
  `text-wrap: balance`.
- Headings (H3): Cormorant Garamond, ~24px, weight 400, italic.
- Pull quote: Cormorant Garamond italic, ~24px, left border 4px in accent color.
- First paragraph: **drop cap** on the first letter using accent-dark color.
- One pull quote mid-article, pulled from a genuinely quotable line in the body.

---

## CTA INSTRUCTIONS — CRITICAL

Place **ONE** of these CTA variations at the end of the article (rotate through them, and
never repeat the same variation on two adjacent articles in a category):

### CTA VARIATION 1 — Conversation Checklist (default, most used)

- Light cream/mist background with accent border
- Heading: "Bring these details to your next visit"
- 5–6 actionable items styled as **CSS-only checkboxes** (no JS), e.g. record the pattern,
  list medications, note sleep and stress changes, bring the log not just the numbers
- Button: "Explore the [Category] hub" → `../{category}.html`
- Subtext framing: each item gives the clinician the context needed to turn a general article
  into advice that fits the reader's situation.

### CTA VARIATION 2 — Safety Note Box

- Accent-dark left border, pale background
- Heading: "Keep the next step safe"
- 2–3 sentences: do not change medication/insulin from a general article, what to report
  promptly, when to seek urgent care
- Link to `../medical-disclaimer.html`

### CTA VARIATION 3 — Tracking Log Download

- Light background, accent border
- Heading: "Start with one question"
- Short teaser (2 sentences) about tracking one pattern for 1–2 weeks
- Button: "Download the glucose log template" → `#`
- Subtext: "Two weeks of context beats two months of bare numbers."

### CTA VARIATION 4 — Pattern Quiz

- Gradient background (accent color tones)
- Heading: "Find your glucose pattern"
- Short teaser (2 sentences) — explicitly non-diagnostic
- Button: "Take the free quiz" → `#`
- Subtext: "Takes 2 minutes · educational only, not a diagnosis"

### CTA VARIATION 5 — Comparison Table

- Clean white background, bordered table
- Heading: "Quick Comparison: [Option A] vs [Option B]"
  (e.g. Fasting vs Post-meal Glucose, Meter vs CGM, Walking vs Strength Training)
- 4-row comparison table relevant to the article topic
- Button: "See the full comparison guide" → related article URL

---

## RELATED ARTICLES SECTION

- 3 article cards linking to **real files in the same category folder**.
- Titles must be topically related to the main article (never generic "Continue reading").
- Use gradient placeholder images (`div.card-image` with CSS gradients, vary colors per card
  via `:nth-child`).
- Card meta: category small-caps label, title, one-line description, "Read the guide" link.

---

## COLOR COMBINATIONS — choose by article category

Each category maps to a palette; these match `sitegen/theme.py` exactly:

**Type 2 Diabetes / Prediabetes / Nutrition → Sage palette**
```css
--accent: #7a9e82; --accent-dark: #4a7252; --accent-light: #c0d8c4;
--hero-bg: linear-gradient(135deg, #2a3828, #3a5040, #4a6850);
```

**Blood Sugar / Monitoring → Teal palette**
```css
--accent: #5a9898; --accent-dark: #356f70; --accent-light: #b0d4d4;
--hero-bg: linear-gradient(135deg, #1a2c2c, #2a4040, #3a5858);
```

**Exercise → Blue palette**
```css
--accent: #5f91a0; --accent-dark: #376775; --accent-light: #b8d4dc;
--hero-bg: linear-gradient(135deg, #1c2c34, #2c4050, #3c5868);
```

**Weight Management / Complications / Best → Rose palette**
```css
--accent: #c4856a; --accent-dark: #9b5e4a; --accent-light: #e8c4b0;
--hero-bg: linear-gradient(135deg, #2c2420, #4a3530, #6b4840);
```

**Supplements → Amber palette**
```css
--accent: #c4a054; --accent-dark: #8a6c30; --accent-light: #e8d4a0;
--hero-bg: linear-gradient(135deg, #2c2010, #4a3820, #6b5030);
```

**Sleep & Stress → Dusty Purple palette**
```css
--accent: #8878a8; --accent-dark: #585078; --accent-light: #c8c0e0;
--hero-bg: linear-gradient(135deg, #201828, #382840, #504060);
```

**Reviews → Teal palette** (matches the existing hand-written review pages)
```css
--accent: #5a9898; --accent-dark: #3a6868; --accent-light: #b0d4d4;
--hero-bg: linear-gradient(135deg, #1a2c2c, #2a4040, #3a5858);
```

---

## AD PLACEMENT

### 300×250 rectangle — one per article

Place **after the first (drop-cap) paragraph**, floated so body text wraps beside it:

```html
<!-- Ad Block 300x250 -->
<div class="ad-block">
  <div class="ad-label">Advertisement</div>
  <div class="ad-slot">
    <!-- INSERT AD NETWORK CODE HERE -->
    <script async src="https://worldppc.click/ads.php?publisher_id=3&website_id=1&type=banner&size=300x250&format=js"></script>
  </div>
</div>
```

```css
.ad-block { float: left; margin: 0 36px 24px 0; width: 300px; flex-shrink: 0; }
.ad-label { font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;
  color: #718583; text-align: center; margin-bottom: 4px; font-family: 'Jost', sans-serif; }
.ad-slot { width: 300px; height: 250px; background: #F0EAE4; border: 1px solid #c9d9d1;
  display: flex; align-items: center; justify-content: center; overflow: hidden; }
.ad-clearfix { clear: both; }
@media (max-width: 700px) {
  .ad-block { float: none; margin: 24px auto; display: block; }
}
```

- Add `<div class="ad-clearfix"></div>` after the third paragraph to clear the float.
- **Only ONE 300×250 block per article page.**

### 728×90 leaderboard — up to two per article

```html
<div class="ad-leaderboard">
  <iframe src="https://worldppc.click/ads.php?publisher_id=3&website_id=1&type=text&size=728x90"
    width="728" height="90" frameborder="0" scrolling="no" loading="lazy" title="Advertisement">
  </iframe>
</div>
```

```css
.ad-leaderboard { width: 728px; height: 90px; margin: 1.5rem auto; background: #F0EAE4;
  border: 2px dashed #5A9898; display: flex; align-items: center; justify-content: center;
  overflow: hidden; max-width: 100%; }
.ad-leaderboard iframe { border: 0; overflow: hidden; width: 728px; height: 90px; max-width: 100%; }
```

- First leaderboard: mid-article, after the clearfix above.
- Second leaderboard (optional): near the end of the body, before the safety note.
- **Ads must never push the article body out of view.** Article prose comes first; ad blocks
  follow it in the source order.

---

## OUTPUT

- Complete, self-contained HTML file, all CSS inline in a single `<style>` tag.
- No external CSS files except Google Fonts.
- Filename format: `{slug}.html`, placed inside the category folder
  (e.g. `monitoring/when-to-check-blood-sugar.html`).
- All links from article pages to hub pages use `../{category}.html`.
- Canonical URL: `https://diabetes.naturalhealthone.com/{category}/{slug}.html`.
- Date stamp: current date in "Updated September 18, 2026" + `<time datetime="...">` form.
- File must be ready to upload directly to the server.

---

## WORKFLOW FOR NEW ARTICLES

This site is generated, not hand-edited one file at a time:

1. Add a content entry to the matching module in `sitegen/`
   (`content_{category}.py`) — `deck`, `sections` (H2 + paragraphs), `safety`, `checklist`.
2. Run `python sitegen/generate_articles.py` to render every article page.
3. Run `python sitegen/generate_hubs.py` if a hub changed.
4. Run `python sitegen/generate_manifest.py` to refresh `article-manifest.json`.
5. Run `python sitegen/verify.py` — it checks all 155 files for broken internal links,
   unbalanced tags, and unclosed elements. Never publish with a failing verification.
