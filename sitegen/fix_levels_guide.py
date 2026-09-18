"""Repair blood-sugar/blood-sugar-levels-guide.html.

The page is the category's flagship guide, but an ad-injection pass emptied
its article body and replaced the prose with duplicate 300x250 blocks and six
leaderboard units. The design (hero, comparison CTA, related cards,
newsletter, footer) survived intact, so this script rebuilds only the article
column and restores the single 300x250 plus two leaderboards the spec allows.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from theme import AD_RECT, AD_LEADER

ROOT = Path('E:/diabetes')
FILE = ROOT / 'blood-sugar' / 'blood-sugar-levels-guide.html'

DECK = ('The useful part of a glucose reading isn\'t the judgment. It\'s the '
        'context you can bring to the next decision.')

OPENING = (
    'Most people start checking their blood sugar because a number came back '
    'from a lab, and then keep checking without anyone explaining what the '
    'daily numbers are for. Here is the short version: a reading is not a '
    'verdict on your day. It is a question about what happened in the hours '
    'before it, and the value of checking rises sharply once you start '
    'answering that question instead of just collecting the number.')

SECTIONS = [
    ('What a single reading can and cannot tell you', [
        'One value is a snapshot. It cannot tell you whether glucose is rising, falling, or holding steady, and it cannot tell you what drove it.',
        'This is why two people with the same fasting number can have completely different days, and why a single reading should never be the basis of a decision about medication.']),
    ('Why timing matters more than the number', [
        'The same value means different things at different times. A reading two hours after a meal answers a question about that meal, while a fasting reading answers a question about the night before.',
        'Checking at random times produces numbers that are not comparable with each other, which is the most common reason a log feels useless.']),
    ('The pattern is what your clinician can act on', [
        'Individual readings vary for dozens of reasons, including stress, sleep, illness, and hydration. A pattern across two weeks is far more stable than any single day.',
        'A repeating high after a particular meal, or a consistent morning rise, is a finding. Fifty unrelated numbers in a log are just noise.']),
    ('Fasting, post-meal, and the dawn phenomenon', [
        'Fasting glucose reflects overnight physiology, including the natural hormone rise before waking that doctors call the dawn phenomenon.',
        'Post-meal glucose reflects what a specific meal actually did. Both matter, and neither one alone describes your overall control.']),
    ('Turning readings into better conversations', [
        'Bring the context, not just the numbers: what you ate, when you slept, whether you were ill or stressed, and what activity you did.',
        'A clinician with two weeks of readings and their context can adjust a plan. A clinician with a single high number can only guess.']),
]

QUOTE = ('A reading is a question about the hours before it, not a verdict '
         'on your day.')

SAFETY = (
    'Blood glucose targets are individual. They depend on your diagnosis, '
    'medications, pregnancy, other health conditions, and your risk of low '
    'glucose. Do not change insulin, medication, or a monitoring plan based '
    'on a general guide. If you have symptoms that concern you, contact your '
    'clinician, and for severe symptoms such as confusion, chest pain, or '
    'difficulty breathing, contact local emergency services immediately.')

CHECKLIST = [
    'Ask your clinician what your personal targets are.',
    'Check at consistent times so readings are comparable.',
    'Record what you ate, when you slept, and your activity.',
    'Note illness, stress, and any medication changes.',
    'Look at the two-week pattern, not single days.',
    'Bring the log with its context, not just the numbers.',
]


def esc(text):
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def build_body():
    parts = [f'      <p class="drop-cap">{esc(OPENING)}</p>',
             f'      {AD_RECT}',
             '      <div class="ad-clearfix"></div>\n']

    for h2, texts in SECTIONS:
        sid = re.sub(r'[^a-z0-9]+', '-', h2.lower()).strip('-')
        parts.append(f'      <section aria-labelledby="{sid}-heading">'
                     f'<h2 id="{sid}-heading">{esc(h2)}</h2>')
        for t in texts:
            parts.append(f'        <p>{esc(t)}</p>')
        parts.append('      </section>\n')

    parts.append(f'''      <div class="ad-clearfix"></div>
      {AD_LEADER}

      <blockquote class="pull-quote"><p>&#8220;{esc(QUOTE)}&#8221;</p></blockquote>

      <aside class="safety-note" aria-labelledby="safety-title">
        <h2 id="safety-title">Keep the next step safe</h2>
        <p>{esc(SAFETY)} Read our <a href="../medical-disclaimer.html">full medical disclaimer</a>.</p>
      </aside>

      <div class="ad-clearfix"></div>
      {AD_LEADER}

      <section class="cta-section" aria-labelledby="checklist-title">
        <h2 id="checklist-title">Bring these details to your next visit</h2>
        <p>Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.</p>
        <div class="checklist" role="list">
{chr(10).join(f'          <span class="check-item" role="listitem">{esc(i)}</span>' for i in CHECKLIST)}
        </div>
        <a class="button" href="../blood-sugar.html">Explore the Blood Sugar hub</a>
      </section>''')

    return '\n'.join(parts) + '\n'


# The article column sits between the grid wrapper and the related-cards
# section. We rewrite that whole span.
GRID_RE = re.compile(
    r'(?s)<div class="article-wrap">(.*?)'
    r'(?=<section class="related-section")')


def main():
    html = FILE.read_text(encoding='utf-8')

    # Strip every injected ad unit so the counts come out at spec.
    html = re.sub(
        r'(?s)(<!-- Ad Block 728x90[^>]*-->\s*)?'
        r'<div[^>]*(?:class="ad-leaderboard"|style="width:728px)[^>]*>.*?</div>',
        '', html)
    html = re.sub(r'(?s)<div class="ad-block"[^>]*>.*?</div>\s*</div>', '', html)
    html = re.sub(r'(?s)<div class="ad-block clearfix"></div>', '', html)
    html = re.sub(r'(?s)<div class="ad-slot"></div>', '', html)
    html = re.sub(r'(?s)<div class="ad-clearfix"></div>', '', html)
    html = re.sub(r'<p></p>', '', html)
    # Empty scaffolding the injection pass left behind.
    html = re.sub(r'(?s)</article><article class="card">.*?</article>\s*(?=<aside class="safety-note")',
                  '\n      </article>', html, count=1)

    m = GRID_RE.search(html)
    if not m:
        raise SystemExit('article column not found')
    html = (html[:m.start()]
            + '<div class="article-wrap">\n' + build_body()
            + '      </div>\n\n    ' + html[m.end():])
    # The original column was already followed by its own closing tag, so
    # drop the duplicate that the rebuild introduced.
    html = re.sub(r'(?s)</div>\s*\n\s*\n\s*</div>\s*\n\s*\n\s*(?=<section class="related-section")',
                  '</div>\n\n    ', html, count=1)

    # The deck in the hero.
    html = re.sub(r'(<p class="hero-deck">).*?(</p>)',
                  lambda mm: f'{mm.group(1)}{esc(DECK)}{mm.group(2)}', html)
    # Refresh the date stamp.
    html = re.sub(r'<time datetime="[^"]*">[^<]*</time>',
                  '<time datetime="2026-09-18">Updated September 18, 2026</time>',
                  html)

    html = re.sub(r'\n{3,}', '\n\n', html)
    FILE.write_text(html, encoding='utf-8')
    print('Repaired blood-sugar-levels-guide.html')


if __name__ == '__main__':
    main()
