"""Generate the article HTML for the NaturalHealthOne diabetes site.

Reads the content modules in sitegen/ and writes complete article pages,
preserving the existing ad markup and on-disk layout conventions of each
category folder.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from theme import (SITE, CAT_THEME, CAT_LABEL, CAT_BLURB, AD_RECT, AD_LEADER,
                   cat_colors)

import content_monitoring_a
import content_monitoring_b
import content_type2_a
import content_type2_b
import content_nutrition
import content_exercise_weight
import content_sleep_a
import content_sleep_b
import content_prediabetes
import content_complications
import content_supplements
import content_devices_best
import content_blood_sugar

ROOT = Path('E:/diabetes')

ALL_CONTENT = {}
ALL_CONTENT.update(content_monitoring_a.MONITORING_A)
ALL_CONTENT.update(content_monitoring_b.MONITORING_B)
ALL_CONTENT.update(content_type2_a.TYPE2_A)
ALL_CONTENT.update(content_type2_b.TYPE2_B)
ALL_CONTENT.update(content_nutrition.NUTRITION)
ALL_CONTENT.update(content_exercise_weight.EXERCISE)
ALL_CONTENT.update(content_exercise_weight.WEIGHT)
ALL_CONTENT.update(content_sleep_a.SLEEP_STRESS)
ALL_CONTENT.update(content_sleep_b.SLEEP_STRESS_B)
ALL_CONTENT.update(content_prediabetes.PREDIABETES)
ALL_CONTENT.update(content_complications.COMPLICATIONS)
ALL_CONTENT.update(content_supplements.SUPPLEMENTS)
ALL_CONTENT.update(content_devices_best.DEVICES)
ALL_CONTENT.update(content_devices_best.BEST)
ALL_CONTENT.update(content_blood_sugar.BLOOD_SUGAR)

# Categories whose articles use the custom dark-teal design rather than
# the rose/cream article template.
CUSTOM_CATEGORIES = {'monitoring', 'blood-sugar'}

CSS_ADS = """
.ad-block { float: left; margin: 0 36px 24px 0; width: 300px; flex-shrink: 0; }
.ad-label { font-size: 9px; letter-spacing: 0.18em; text-transform: uppercase;
  color: #718583; text-align: center; margin-bottom: 4px; font-family: 'Jost', sans-serif; }
.ad-slot { width: 300px; height: 250px; background: #F0EAE4; border: 1px solid #c9d9d1;
  display: flex; align-items: center; justify-content: center; overflow: hidden; }
.ad-clearfix { clear: both; }
.ad-leaderboard { width: 728px; height: 90px; margin: 1.5rem auto; background: #F0EAE4;
  border: 2px dashed #5A9898; display: flex; align-items: center; justify-content: center;
  overflow: hidden; max-width: 100%; }
.ad-leaderboard iframe { border: 0; overflow: hidden; width: 728px; height: 90px; max-width: 100%; }
@media (max-width: 700px) {
  .ad-block { float: none; margin: 24px auto; display: block; }
}
"""

CSS_BASE = """
body { font-family: Georgia, "Times New Roman", serif; color: #3a2e2e;
  background: #fff5f3; margin: 0; padding: 0; line-height: 1.7; }
a { color: {accent}; text-decoration: none; }
a:hover { text-decoration: underline; }
header { border-bottom: 2px solid {accent}; padding: 1rem 0; background: #fff0eb; }
.container { max-width: 780px; margin: 0 auto; padding: 0 1.5rem; }
nav.back { font-size: .9rem; margin: 1rem 0; }
h1 { font-family: system-ui, sans-serif; color: {dark}; font-size: 2.2rem;
  margin: 1rem 0 .4rem; line-height: 1.15; }
.meta { font-family: system-ui, sans-serif; font-size: .85rem; color: {dark};
  margin-bottom: 1.25rem; }
h2 { font-family: system-ui, sans-serif; color: {dark}; font-size: 1.4rem;
  margin-top: 2rem; }
p { margin: 0 0 1.1rem; }
.drop-cap::first-letter { float: left; font-size: 4rem; line-height: .8;
  padding-right: .5rem; color: {accent}; font-family: Georgia, serif; font-weight: bold; }
.pull-quote { border-left: 4px solid {accent}; padding: 1rem 1.5rem; margin: 1.75rem 0;
  background: #fff0eb; font-style: italic; font-size: 1.15rem; color: #5a3a2a;
  font-family: Georgia, serif; line-height: 1.5; }
.checklist-cta { border: 2px solid {light}; border-radius: 8px; padding: 1.5rem;
  margin: 2rem 0; background: #fff8f5; }
.checklist-cta h2 { margin-top: 0; }
.checklist-cta ul { margin: 0 0 1rem; padding-left: 1.2rem; }
.checklist-cta li { font-family: system-ui, sans-serif; font-size: .92rem;
  margin-bottom: .45rem; }
.checklist-cta .btn { display: inline-block; background: {accent}; color: #fff;
  padding: .55rem 1rem; border-radius: 4px; font-weight: bold;
  font-family: system-ui, sans-serif; font-size: .9rem; }
.cards { display: flex; gap: 1rem; flex-wrap: wrap; margin: 1.5rem 0; }
.card { border: 1px solid {accent}; border-radius: 8px; padding: 1rem;
  background: #fff8f5; flex: 1; min-width: 200px; }
.card h3 { font-family: system-ui, sans-serif; color: {dark}; font-size: 1rem;
  margin: 0 0 .3rem; }
.card p { font-family: system-ui, sans-serif; font-size: .88rem; color: #5a3a2a;
  margin: 0 0 .5rem; }
footer { background: #3a2e2e; color: #fff; padding: 2rem 0; text-align: center;
  font-size: .85rem; font-family: system-ui, sans-serif; line-height: 1.6; }
footer a { color: #e8c4b0; }
"""


def esc(text):
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def slug_title(slug):
    return ' '.join(w.capitalize() for w in slug.replace('-', ' ').split())


def read_time_for(info):
    """Body word count divided by 200, rounded up, per the spec."""
    words = 0
    for _, texts in info['sections']:
        for t in texts:
            words += len(t.split())
    words += len(info['deck'].split())
    words += len(info['safety'].split())
    for i in info['checklist']:
        words += len(i.split())
    return f'{max(1, -(-words // 200))} min read'


def related_cards(cat, slug, n=3):
    files = sorted(p.name for p in (ROOT / cat).glob('*.html'))
    files = [f for f in files if f != slug + '.html']
    out = []
    for f in files[:n]:
        stem = Path(f).stem
        if stem in ALL_CONTENT:
            out.append((slug_title(stem), f, ALL_CONTENT[stem]['deck']))
        else:
            out.append((slug_title(stem), f, 'Continue with a practical, evidence-aware guide in this category.'))
    while len(out) < n:
        out.append((CAT_LABEL[cat] + ' Hub', '../' + cat + '.html', CAT_BLURB[cat]))
    return out


def render_article(cat, slug, info):
    colors = cat_colors(cat)
    css = (CSS_BASE.replace('{accent}', colors['accent'])
           .replace('{dark}', colors['dark'])
           .replace('{light}', colors['light']) + CSS_ADS)
    title = slug_title(slug)
    label = CAT_LABEL[cat]

    paras = []
    first = True
    for h2, texts in info['sections']:
        paras.append(f'<h2>{esc(h2)}</h2>')
        for t in texts:
            cls = 'drop-cap' if first else ''
            first = False
            paras.append(f'<p{cls and " " + cls}>{esc(t)}</p>')

    body = '\n'.join(paras)
    read_time = read_time_for(info)

    quote = info['sections'][1][1][0] if len(info['sections']) > 1 else info['deck']
    items = ''.join(f'<li>{esc(i)}</li>' for i in info['checklist'])
    cards = related_cards(cat, slug)
    cards_html = ''.join(
        f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p>'
        f'<a href="{f}">Read the guide</a></div>' for t, f, d in cards)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)} | NaturalHealthOne</title>
<meta name="description" content="{esc(info['deck'])}" />
<meta name="theme-color" content="{colors['dark']}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{SITE}/{cat}/{slug}.html" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{esc(title)} | NaturalHealthOne" />
<meta property="og:description" content="{esc(info['deck'])}" />
<meta property="og:url" content="{SITE}/{cat}/{slug}.html" />
<meta property="og:site_name" content="NaturalHealthOne" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,500;1,600&amp;family=Jost:wght@0,300;0,400;0,500;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<header><div class="container"><a href="../index.html">NaturalHealthOne</a> | <a href="../medical-disclaimer.html">Medical Disclaimer</a> | <a href="../{cat}.html">{label}</a></div></header>
<main class="container">
<nav class="back"><a href="../{cat}.html">&larr; {label} Hub</a></nav>
<h1>{esc(title)}</h1>
<p class="meta">Category: {label} &bull; By Editorial Team &bull; Updated 2026-09-18 &bull; {read_time}</p>

{AD_RECT}

{body}

<div class="ad-clearfix"></div>
{AD_LEADER}

<blockquote class="pull-quote">"{esc(quote)}"</blockquote>

<section class="checklist-cta" aria-labelledby="checklist-title">
<h2 id="checklist-title">Bring these details to your next visit</h2>
<ul>
{items}
</ul>
<a href="../{cat}.html" class="btn">Explore more {label} guides</a>
</section>

<h2>Related guides</h2>
<div class="cards">
{cards_html}
</div>

<aside class="checklist-cta" style="border-color:{colors['accent']}" aria-labelledby="safety-title">
<h2 id="safety-title">Keep the next step safe</h2>
<p>{esc(info['safety'])} Read our <a href="../medical-disclaimer.html">full medical disclaimer</a>.</p>
</aside>

{AD_LEADER}
</main>

<footer>
<p><strong>Medical Disclaimer</strong></p>
<p>This content is for educational purposes only and does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider before making changes to your diabetes management plan.</p>
<p>&copy; 2026 Natural Health One. All rights reserved.</p>
</footer>
</body>
</html>
"""


def render_custom(cat, slug, info):
    """ monitoring/ and blood-sugar/ use the dark editorial design. """
    colors = cat_colors(cat)
    title = slug_title(slug)
    label = CAT_LABEL[cat]
    c = colors

    paras = []
    first = True
    for h2, texts in info['sections']:
        paras.append(f'<h2>{esc(h2)}</h2>')
        for t in texts:
            cls = 'drop-cap' if first else ''
            first = False
            paras.append(f'<p{cls and " " + cls}>{esc(t)}</p>')

    body = '\n'.join(paras)
    read_time = read_time_for(info)
    items = ''.join(f'<span class="check-item" role="listitem">{esc(i)}</span>'
                    for i in info['checklist'])
    cards = related_cards(cat, slug)
    cards_html = ''.join(
        f'<article class="card"><div class="card-image" aria-hidden="true"></div>'
        f'<div class="card-body"><small>{label}</small><h3>{esc(t)}</h3>'
        f'<p>{esc(d)}</p><a href="{f}">Read the guide</a></div></article>'
        for t, f, d in cards)

    css = f"""
:root {{
  --ink:#173b3b; --text:#415857; --light-mid:#718583; --paper:#f8faf8;
  --white:#fff; --border:#c9d9d1; --mist:#e7f0ef;
  --accent:{c['accent']}; --accent-dark:{c['dark']}; --accent-light:{c['light']};
  --hero-bg:linear-gradient(135deg,#1a2c2c,#2a4040,#3a5858); --max:1200px;
}}
* {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{ margin:0; color:var(--text); background:var(--paper);
  font-family:"Jost",Arial,sans-serif; font-size:16px; line-height:1.85;
  text-rendering:optimizeLegibility; }}
a {{ color:var(--accent-dark); text-underline-offset:.18em; }}
a:hover {{ text-decoration-thickness:.14em; }}
a:focus-visible {{ outline:3px solid #d8a456; outline-offset:4px; border-radius:2px; }}
.skip-link {{ position:fixed; z-index:100; top:12px; left:12px; padding:.7rem 1rem;
  color:#fff; background:var(--ink); transform:translateY(-180%); text-decoration:none; }}
.skip-link:focus {{ transform:translateY(0); }}
.shell {{ width:min(calc(100% - 48px),var(--max)); margin-inline:auto; }}
.topbar {{ color:#e9f1ed; background:var(--ink); }}
.topbar .shell {{ min-height:40px; display:flex; align-items:center;
  justify-content:space-between; gap:.6rem 1.5rem; padding-block:.45rem;
  font-size:.73rem; }}
.topbar p {{ margin:0; }} .topbar strong {{ color:#fff; }}
.topbar a {{ color:#fff; font-weight:600; white-space:nowrap; }}
.site-header {{ border-bottom:1px solid var(--border); background:rgba(255,255,255,.97); }}
.masthead {{ min-height:88px; display:flex; align-items:center;
  justify-content:space-between; gap:1.5rem 2.5rem; }}
.brand {{ color:var(--ink); font:700 clamp(1.8rem,3vw,2.2rem)/.9 "Cormorant Garamond",Georgia,serif;
  text-decoration:none; }}
.brand em {{ color:var(--accent-dark); font-style:italic; }}
.brand small {{ display:block; margin-top:.38rem; color:var(--light-mid);
  font:600 .59rem/1 "Jost",Arial,sans-serif; letter-spacing:.09em; text-transform:uppercase; }}
.primary-nav ul {{ display:flex; flex-wrap:wrap; justify-content:flex-end;
  gap:.35rem 1.05rem; margin:0; padding:0; list-style:none; }}
.primary-nav a {{ color:var(--ink); font-size:.79rem; font-weight:600; text-decoration:none; }}
.primary-nav a:hover {{ color:var(--accent-dark); }}
.article-hero {{ background:var(--hero-bg); color:#eef5f3; padding:clamp(2.5rem,6vw,4rem) 0; }}
.hero-inner {{ }} .eyebrow {{ margin:0 0 .55rem; color:var(--accent-light);
  font-size:.72rem; font-weight:700; letter-spacing:.18em; text-transform:uppercase; }}
.article-hero h1 {{ margin:0 0 .7rem; color:#fff;
  font:600 clamp(2.6rem,6vw,4.2rem)/.95 "Cormorant Garamond",Georgia,serif;
  letter-spacing:-.03em; text-wrap:balance; }}
.hero-deck {{ max-width:60ch; margin:0; font:400 clamp(1.05rem,2vw,1.3rem)/1.5
  "Cormorant Garamond",Georgia,serif; color:#d7e6e2; }}
.byline {{ display:flex; flex-wrap:wrap; gap:.4rem 1rem; margin-top:1.4rem;
  font-size:.76rem; color:#b6cfc9; }}
.article-wrap {{ display:grid; grid-template-columns:minmax(0,1fr) 320px;
  gap:2.5rem; width:min(calc(100% - 48px),var(--max)); margin:2.5rem auto 0;
  align-items:start; }}
.article-copy {{ font-size:1.02rem; }}
.article-copy h2 {{ margin:2.4rem 0 .9rem; color:var(--ink);
  font:600 clamp(1.5rem,3vw,1.9rem)/1.1 "Cormorant Garamond",Georgia,serif;
  letter-spacing:-.015em; text-wrap:balance; }}
.article-copy p {{ max-width:68ch; }}
.drop-cap::first-letter {{ float:left; margin:.13em .14em 0 0; color:var(--accent-dark);
  font:600 4.2rem/.71 "Cormorant Garamond",Georgia,serif; }}
.pull-quote {{ margin:2.35rem 0; max-width:62ch; padding:.35rem 0 .35rem 1.5rem;
  border-left:4px solid var(--accent); color:var(--ink);
  font:italic 500 clamp(1.35rem,2.6vw,1.65rem)/1.3 "Cormorant Garamond",Georgia,serif; }}
.pull-quote p {{ margin:0; }}
.safety-note {{ margin-top:2.6rem; padding:1.25rem 1.35rem;
  border-left:5px solid var(--accent-dark); background:#e9f3f2; }}
.safety-note h2 {{ margin:0 0 .35rem; color:var(--ink);
  font:600 1.15rem/1.15 "Jost",Arial,sans-serif; }}
.safety-note p {{ margin:0; font-size:.91rem; line-height:1.65; }}
.cta-section {{ margin-top:2.8rem; padding:clamp(1.45rem,4vw,2.2rem);
  border:2px solid var(--accent-light); background:#f4faf9; }}
.cta-section h2 {{ margin:0 0 .8rem; color:var(--ink);
  font:400 clamp(1.8rem,4vw,2.4rem)/1.05 "Cormorant Garamond",Georgia,serif;
  letter-spacing:-.025em; }}
.cta-section > p {{ max-width:62ch; margin:.8rem 0 1.15rem; font-size:.93rem; }}
.checklist {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr));
  gap:.62rem 1.15rem; margin:0 0 1.45rem; }}
.check-item {{ position:relative; display:block; padding-left:1.7rem;
  font-size:.84rem; line-height:1.45; }}
.check-item::before {{ position:absolute; top:.15rem; left:0; width:.85rem; height:.85rem;
  border:1px solid var(--accent-dark); background:var(--white); content:""; }}
.check-item::after {{ position:absolute; top:.28rem; left:.22rem; width:.4rem; height:.2rem;
  border-bottom:2px solid var(--accent-dark); border-left:2px solid var(--accent-dark);
  transform:rotate(-45deg); content:""; }}
.button {{ display:inline-flex; align-items:center; justify-content:center;
  min-height:46px; padding:.65rem 1rem; color:var(--white); background:var(--accent-dark);
  font-size:.82rem; font-weight:700; text-decoration:none; }}
.button:hover {{ color:var(--ink); background:var(--accent-light); }}
.related-section {{ width:min(calc(100% - 48px),var(--max)); margin:0 auto;
  padding:3rem 0 4rem; }}
.section-kicker {{ margin:0 0 .45rem; color:var(--accent-dark); font-size:.72rem;
  font-weight:600; letter-spacing:.16em; text-transform:uppercase; }}
.related-section h2 {{ margin:0; color:var(--ink);
  font:400 clamp(2rem,4vw,2.6rem)/1 "Cormorant Garamond",Georgia,serif;
  letter-spacing:-.025em; }}
.cards {{ display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:1.5rem; }}
.card {{ overflow:hidden; border:1px solid var(--border); background:var(--white); }}
.card-image {{ height:120px; background:linear-gradient(135deg,#1f5050,#5d9796 57%,#b5dbd7); }}
.card:nth-child(2) .card-image {{ background:linear-gradient(135deg,#384d55,#7897a0 55%,#cadade); }}
.card:nth-child(3) .card-image {{ background:linear-gradient(135deg,#3f5a4e,#80a391 58%,#cee0d5); }}
.card-body {{ padding:1.1rem 1.15rem 1.25rem; }}
.card small {{ color:var(--accent-dark); font-size:.69rem; font-weight:700;
  letter-spacing:.13em; text-transform:uppercase; }}
.card h3 {{ margin:.42rem 0 .5rem; color:var(--ink);
  font:500 1.35rem/1.05 "Cormorant Garamond",Georgia,serif; }}
.card p {{ margin:0 0 .65rem; font-size:.85rem; line-height:1.55; }}
.card a {{ font-size:.82rem; font-weight:700; }}
.site-footer {{ color:#d8e4de; background:#102f30; margin-top:0; }}
.footer-grid {{ display:grid; grid-template-columns:1.4fr repeat(3,1fr); gap:2rem;
  padding-block:2.6rem 1.4rem; }}
.footer-brand {{ margin:0 0 .5rem; font:700 1.5rem/1 "Cormorant Garamond",Georgia,serif;
  color:#fff; }} .footer-brand em {{ color:var(--accent-light); font-style:italic; }}
.footer-description {{ margin:0; font-size:.84rem; line-height:1.6; }}
.footer-heading {{ margin:0 0 .6rem; font-size:.7rem; font-weight:700;
  letter-spacing:.14em; text-transform:uppercase; color:#9fbcb8; }}
.footer-links {{ margin:0; padding:0; list-style:none; }}
.footer-links a {{ color:#d8e4de; font-size:.85rem; text-decoration:none; }}
.footer-links a:hover {{ color:#fff; text-decoration:underline; }}
.footer-bottom {{ display:flex; justify-content:space-between; flex-wrap:wrap;
  gap:.6rem 1.5rem; padding-block:1.2rem 2rem; border-top:1px solid #275051;
  font-size:.78rem; color:#a8c4c0; }}
.footer-bottom p {{ margin:0; }}
@media (max-width:1000px) {{ .article-wrap {{ grid-template-columns:1fr; }} }}
@media (max-width:820px) {{
  .cards {{ grid-template-columns:repeat(2,1fr); }}
  .footer-grid {{ grid-template-columns:repeat(2,1fr); }}
  .checklist {{ grid-template-columns:1fr; }}
}}
@media (max-width:700px) {{
  .shell, .article-wrap, .related-section {{ width:min(calc(100% - 32px),var(--max)); }}
  .topbar .shell {{ align-items:flex-start; flex-direction:column; gap:.15rem; }}
  .footer-bottom {{ align-items:flex-start; flex-direction:column; }}
  .ad-block {{ float:none; margin:24px auto; display:block; }}
}}
@media (max-width:580px) {{
  .cards, .footer-grid {{ grid-template-columns:1fr; }}
  .primary-nav ul {{ gap:.45rem .8rem; }}
  .primary-nav a {{ font-size:.73rem; }}
}}
.ad-block {{ float:left; margin:0 36px 24px 0; width:300px; flex-shrink:0; }}
.ad-label {{ font-size:9px; letter-spacing:.18em; text-transform:uppercase;
  color:#718583; text-align:center; margin-bottom:4px; font-family:'Jost',sans-serif; }}
.ad-slot {{ width:300px; height:250px; background:#F0EAE4; border:1px solid #c9d9d1;
  display:flex; align-items:center; justify-content:center; overflow:hidden; }}
.ad-clearfix {{ clear:both; }}
.ad-leaderboard {{ width:728px; height:90px; margin:1.5rem auto; background:#F0EAE4;
  border:2px dashed #5A9898; display:flex; align-items:center; justify-content:center;
  overflow:hidden; max-width:100%; }}
.ad-leaderboard iframe {{ border:0; overflow:hidden; width:728px; height:90px; max-width:100%; }}
"""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | NaturalHealthOne</title>
<meta name="description" content="{esc(info['deck'])}">
<meta name="theme-color" content="{c['dark']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}/{cat}/{slug}.html">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(title)} | NaturalHealthOne">
<meta property="og:description" content="{esc(info['deck'])}">
<meta property="og:url" content="{SITE}/{cat}/{slug}.html">
<meta property="og:site_name" content="NaturalHealthOne">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,500;1,600&amp;family=Jost:wght@0,300;0,400;0,500;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>
<a class="skip-link" href="#article">Skip to article</a>
<div class="topbar"><div class="shell"><p><strong>NaturalHealthOne</strong> &middot; Clear, evidence-aware diabetes education for everyday decisions.</p><a href="../medical-disclaimer.html">Medical disclaimer</a></div></div>
<header class="site-header"><div class="shell masthead">
<a class="brand" href="../index.html" aria-label="NaturalHealthOne Diabetes home">NaturalHealth<em>One</em><small>Diabetes &amp; metabolic health</small></a>
<nav class="primary-nav" aria-label="Primary navigation"><ul>
<li><a href="../index.html">Home</a></li>
<li><a href="../type-2-diabetes.html">Type 2</a></li>
<li><a href="../prediabetes.html">Prediabetes</a></li>
<li><a href="../blood-sugar.html">Blood sugar</a></li>
<li><a href="../nutrition.html">Nutrition</a></li>
<li><a class="active" href="../{cat}.html" aria-current="page">{label}</a></li>
<li><a href="../reviews.html">Reviews</a></li>
</ul></nav>
</div></header>
<main id="article">
<section class="article-hero" aria-labelledby="page-title">
<div class="shell hero-inner">
<p class="eyebrow">{label}</p>
<h1 id="page-title">{esc(title)}</h1>
<p class="hero-deck">{esc(info['deck'])}</p>
<div class="byline"><span>By NaturalHealthOne Editors</span><span><time datetime="2026-09-18">Updated September 18, 2026</time></span><span>{read_time}</span></div>
</div>
</section>
<div class="article-wrap">
<article class="article-copy">
{AD_RECT}
{body}
<div class="ad-clearfix"></div>
{AD_LEADER}
<aside class="safety-note" aria-labelledby="safety-title">
<h2 id="safety-title">Keep the next step safe</h2>
<p>{esc(info['safety'])} Read our <a href="../medical-disclaimer.html">full medical disclaimer</a>.</p>
</aside>
<section class="cta-section" aria-labelledby="checklist-title">
<h2 id="checklist-title">Bring these details to your next visit</h2>
<p>Each item gives your clinician the context needed to turn a general article into advice that fits your situation.</p>
<div class="checklist" role="list">
{items}
</div>
<a class="button" href="../{cat}.html">Explore the {label} hub</a>
</section>
</article>
<aside class="safety-note" aria-labelledby="related-title">
<h2 id="related-title">Keep reading</h2>
<p>Three more practical, evidence-aware guides from the {label.lower()} category.</p>
</aside>
</div>
<section class="related-section" aria-labelledby="related-h">
<p class="section-kicker">Related guides</p>
<h2 id="related-h">More in {label}</h2>
<div class="cards">
{cards_html}
</div>
</section>
</main>
<footer class="site-footer" role="contentinfo">
<div class="shell footer-grid">
<div><p class="footer-brand">NaturalHealth<em>One</em></p>
<p class="footer-description">Independent education for diabetes, blood sugar, and everyday care, without hype or hidden promises.</p></div>
<nav aria-label="Footer topics"><p class="footer-heading">Topics</p><ul class="footer-links">
<li><a href="../type-2-diabetes.html">Type 2 diabetes</a></li>
<li><a href="../prediabetes.html">Prediabetes</a></li>
<li><a href="../blood-sugar.html">Blood sugar</a></li>
<li><a href="../nutrition.html">Nutrition</a></li>
<li><a href="../monitoring.html">Monitoring</a></li></ul></nav>
<nav aria-label="Footer trust links"><p class="footer-heading">Trust</p><ul class="footer-links">
<li><a href="../about.html">About</a></li>
<li><a href="../editorial-policy.html">Editorial policy</a></li>
<li><a href="../medical-disclaimer.html">Medical disclaimer</a></li>
<li><a href="../contact.html">Contact</a></li></ul></nav>
<nav aria-label="Footer legal links"><p class="footer-heading">Legal</p><ul class="footer-links">
<li><a href="../privacy-policy.html">Privacy policy</a></li>
<li><a href="../terms.html">Terms of use</a></li>
<li><a href="../medical-review-policy.html">Review policy</a></li></ul></nav>
</div>
<div class="shell footer-bottom">
<p>&copy; 2026 NaturalHealthOne. This site is for educational purposes only and is not medical advice, diagnosis, or treatment.</p>
<p>For emergencies, contact local emergency services.</p>
</div>
</footer>
</body>
</html>
"""


def main():
    cats = ['best', 'blood-sugar', 'complications', 'devices', 'exercise',
            'nutrition', 'prediabetes', 'sleep-stress', 'supplements',
            'type-2-diabetes', 'weight-management', 'monitoring']

    written, skipped = [], []
    for cat in cats:
        cat_dir = ROOT / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob('*.html')):
            slug = path.stem
            if slug not in ALL_CONTENT:
                skipped.append(f'{cat}/{path.name} (no content defined)')
                continue
            if cat in CUSTOM_CATEGORIES:
                html = render_custom(cat, slug, ALL_CONTENT[slug])
            else:
                html = render_article(cat, slug, ALL_CONTENT[slug])
            path.write_text(html, encoding='utf-8')
            written.append(f'{cat}/{path.name}')

    print(f'Wrote {len(written)} articles')
    for w in written:
        print('  +', w)
    if skipped:
        print(f'\nSkipped {len(skipped)} (no content module):')
        for s in skipped:
            print('  -', s)


if __name__ == '__main__':
    main()
