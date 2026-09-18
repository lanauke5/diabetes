"""Build the three stub hub pages (devices, supplements, complications)
and repair monitoring/a1c-explained.html.

These hubs exist as bare 12-line stubs. We build them in the same visual
language as the nutrition/exercise hubs already on the site, listing the
articles that actually exist in each category folder.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from theme import SITE, CAT_LABEL, CAT_BLURB, cat_colors

ROOT = Path('E:/diabetes')

NAV = [
    ('type-2-diabetes.html', 'Type 2'), ('blood-sugar.html', 'Blood Sugar'),
    ('nutrition.html', 'Nutrition'), ('exercise.html', 'Exercise'),
    ('weight-management.html', 'Weight'), ('monitoring.html', 'Monitoring'),
    ('supplements.html', 'Supplements'), ('complications.html', 'Complications'),
    ('devices.html', 'Devices'), ('reviews.html', 'Reviews'),
    ('prediabetes.html', 'Prediabetes'), ('sleep-stress.html', 'Sleep & Stress'),
]

CSS = """
:root{--ink:#173b3b;--text:#294747;--teal:#5a9898;--teal-dark:#356f70;
--sage:#7c987d;--paper:#f8faf8;--line:#bdd2cf;--muted:#586b6b;--max:1200px}
*{box-sizing:border-box;}html{scroll-behavior:smooth;}
body{margin:0;background:var(--paper);color:var(--text);font-family:"Jost",Arial,sans-serif;
font-size:17px;line-height:1.65;text-rendering:optimizeLegibility;}
h1,h2,h3{font-family:"Cormorant Garamond",Georgia,serif;color:var(--ink);text-wrap:balance;}
a{color:var(--teal-dark);text-underline-offset:.19em;}
a:hover{text-decoration-thickness:.14em;}
a:focus-visible{outline:3px solid #d8a456;outline-offset:4px;border-radius:2px;}
.skip{position:fixed;z-index:1000;top:12px;left:12px;padding:.7rem 1rem;color:#fff;
background:var(--ink);transform:translateY(-160%);text-decoration:none;}
.skip:focus{transform:none;}
.shell{width:min(calc(100% - 48px),var(--max));margin-inline:auto;}
header{background:rgba(255,255,255,.97);border-bottom:1px solid var(--line);
position:sticky;top:0;z-index:10;}
.masthead{display:flex;align-items:center;justify-content:space-between;gap:2rem;
min-height:88px;flex-wrap:wrap;padding-block:.5rem;}
.brand{font-family:"Cormorant Garamond",Georgia,serif;font-size:clamp(1.75rem,3vw,2.2rem);
font-weight:700;color:var(--ink);text-decoration:none;}
.brand span{color:var(--teal);}
nav a{color:var(--ink);text-decoration:none;font-weight:600;font-size:.86rem;margin-left:1.2rem;}
nav a:hover{color:var(--teal-dark);}
.hero{border-bottom:1px solid var(--line);padding:4.5rem 0 3.5rem;
background:linear-gradient(90deg,rgba(223,236,234,.52) 1px,transparent 1px) 0 0/12.5% 100%,#fff;}
.hero h1{font-size:clamp(2.8rem,6vw,5rem);font-weight:600;letter-spacing:-.04em;
line-height:.95;margin:0 0 .7rem;}
.hero p{max-width:60ch;color:#365555;font:500 1.2rem/1.45 "Cormorant Garamond",Georgia,serif;margin:0;}
.breadcrumb{padding:1.2rem 0 .2rem;font-size:.85rem;}
.intro{padding:2.8rem 0 1rem;} .intro h2{font-size:clamp(1.8rem,3vw,2.4rem);margin:0 0 .7rem;}
.intro p{max-width:70ch;margin:0;}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1.2rem;
margin:1.6rem 0 3rem;}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:1.3rem 1.35rem;
text-decoration:none;color:inherit;transition:transform .15s,box-shadow .15s;}
.card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(23,59,59,.09);}
.card h3{margin:0 0 .45rem;font-size:1.25rem;}
.card p{margin:0;font-size:.92rem;color:var(--muted);}
.related{background:#eef4f2;border-top:1px solid var(--line);border-bottom:1px solid var(--line);
padding:2.2rem 0;}
.related-grid{display:flex;flex-wrap:wrap;gap:.7rem 1.4rem;margin-top:.9rem;}
.related-grid a{font-weight:600;font-size:.95rem;}
.medical{padding:2.6rem 0;}
.medical .box{background:#fff8e7;border-left:4px solid #b45309;border-radius:6px;
padding:1.2rem 1.4rem;}
.medical h2{color:#7c2d12;margin:0 0 .4rem;font-size:1.2rem;}
.medical p{margin:0;color:#5a3a1a;font-size:.94rem;}
.footer{background:#102f30;color:#d8e4de;padding:2.8rem 0 2rem;}
.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:2rem;}
.footer a{color:#d8e4de;text-decoration:none;font-size:.88rem;}
.footer a:hover{color:#fff;text-decoration:underline;}
.footer p{margin:0 0 .5rem;font-size:.88rem;}
.footer-bottom{margin-top:1.8rem;padding-top:1.1rem;border-top:1px solid #275051;
font-size:.8rem;color:#a8c4c0;}
@media(max-width:820px){.footer-grid{grid-template-columns:1fr 1fr;}}
@media(max-width:640px){nav a{margin-left:0;margin-right:.8rem;}
.masthead{flex-direction:column;align-items:flex-start;gap:.4rem;}
.footer-grid{grid-template-columns:1fr;}}
"""


def slug_title(slug):
    return ' '.join(w.capitalize() for w in slug.replace('-', ' ').split())


def list_articles(cat):
    out = []
    for p in sorted((ROOT / cat).glob('*.html')):
        out.append((p.stem, slug_title(p.stem)))
    return out


def render_hub(cat, featured_slug=None):
    label = CAT_LABEL[cat]
    blurb = CAT_BLURB[cat]
    articles = list_articles(cat)
    if featured_slug and (ROOT / cat / (featured_slug + '.html')).exists():
        articles = [a for a in articles if a[0] != featured_slug] + [(featured_slug, slug_title(featured_slug))]
        featured = (featured_slug, slug_title(featured_slug))
    else:
        featured = articles[0] if articles else None

    cards = ''.join(
        f'<a href="{cat}/{slug}.html" class="card"><h3>{slug_title(slug)}</h3>'
        f'<p>{blurb}</p></a>' for slug, _ in articles)

    nav = ''.join(f'<a href="{href}">{txt}</a>' for href, txt in NAV)
    feat = ''
    if featured:
        feat = (f'<section class="shell" aria-label="Featured article"><h2>Featured</h2>'
                f'<article style="background:#fff;border:1px solid var(--line);border-radius:8px;'
                f'padding:1.6rem 1.8rem;margin:1.2rem 0 2rem;">'
                f'<h3><a href="{cat}/{featured[0]}.html" style="color:var(--ink);text-decoration:none;">'
                f'{featured[1]}</a></h3><p>{blurb}</p></article></section>')

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{label} Hub | NaturalHealthOne</title>
<meta name="description" content="{blurb}">
<meta name="theme-color" content="#173b3b">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}/{cat}.html">
<meta property="og:type" content="website">
<meta property="og:title" content="{label} Hub | NaturalHealthOne">
<meta property="og:description" content="{blurb}">
<meta property="og:url" content="{SITE}/{cat}.html">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<a href="#main" class="skip">Skip to content</a>
<header aria-label="Primary"><div class="shell masthead">
<a href="index.html" class="brand">Natural<span style="color:var(--teal)">Health</span>One</a>
<nav aria-label="Sections">{nav}</nav>
</div></header>
<main id="main">
<section class="hero" aria-label="Category header"><div class="shell">
<nav aria-label="Breadcrumb" class="breadcrumb"><a href="index.html">Home</a> / {label}</nav>
<h1>{label} Hub</h1><p>{blurb}</p></div></section>
<section class="shell intro" aria-label="Introduction">
<h2>Why {label.lower()} guides matter</h2>
<p>{blurb} Each guide below focuses on one question, explains what the evidence can support, and ends with the details worth bringing to your healthcare team.</p>
</section>
{feat}
<section class="shell" aria-label="Articles">
<h2>All {label.lower()} guides</h2>
<div class="cards">
{cards}
</div>
</section>
<section class="related" aria-label="Related categories"><div class="shell">
<h2>Related categories</h2>
<div class="related-grid">
<a href="blood-sugar.html">Blood Sugar</a>
<a href="monitoring.html">Monitoring</a>
<a href="nutrition.html">Nutrition</a>
<a href="exercise.html">Exercise</a>
<a href="weight-management.html">Weight Management</a>
<a href="sleep-stress.html">Sleep &amp; Stress</a>
</div>
</div></section>
<section class="medical" aria-label="Medical safety note"><div class="shell"><div class="box">
<h2>Medical safety note</h2>
<p>These guides are for educational purposes only and do not replace professional medical advice. Always discuss changes with your healthcare provider, especially if you use insulin or other glucose-lowering medications.</p>
</div></div></section>
</main>
<footer class="footer" aria-label="Footer"><div class="shell footer-grid">
<div><a href="index.html" class="brand" style="color:#fff;">NaturalHealthOne</a>
<p>Evidence-based diabetes education. No invented reviewers or claims.</p></div>
<div><p style="font-weight:700;color:#fff;">Trust</p>
<a href="editorial-policy.html">Editorial Policy</a><br>
<a href="medical-disclaimer.html">Medical Disclaimer</a><br>
<a href="medical-reviewers.html">Medical Review Board</a><br>
<a href="contact.html">Contact</a></div>
<div><p style="font-weight:700;color:#fff;">Legal</p>
<a href="privacy-policy.html">Privacy Policy</a><br>
<a href="terms.html">Terms of Use</a><br>
<a href="medical-review-policy.html">Review Policy</a></div>
</div>
<div class="shell footer-bottom">
<p>Natural Health One &copy; 2026. Content is informational and not medical advice.
<a href="medical-disclaimer.html">Full disclaimer</a>.</p>
</div></footer>
</body></html>
"""


def main():
    built = []
    for cat, featured in [('devices', 'best-glucose-meters'),
                          ('supplements', 'diabetes-supplement-guide'),
                          ('complications', 'diabetes-complications-guide')]:
        html = render_hub(cat, featured)
        (ROOT / f'{cat}.html').write_text(html, encoding='utf-8')
        built.append(f'{cat}.html')
    print('Built hubs:', ', '.join(built))


if __name__ == '__main__':
    main()
