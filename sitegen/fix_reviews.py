"""Fill the ten hand-written reviews/ pages with real editorial content.

The pages were created with a full bespoke design (hero, verdict, criteria
grid, blockquote, fit list, checklist, CTA, disclosure, sidebar) but every
text node was left empty, and an ad-injection pass then wrote duplicate
300x250 blocks and up to six leaderboard units into each page.

This script replaces only the empty body region of each page with real
content, and rewrites the ad markup to the spec used everywhere else on the
site: one 300x250 block floated after the opening paragraph, and a maximum
of two 728x90 leaderboards per page. It keeps each page's own CSS and design.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from theme import AD_RECT
import content_reviews

ROOT = Path('E:/diabetes')
REVIEW_DIR = ROOT / 'reviews'

LEADER = (
    '<div class="ad-leaderboard">\n'
    '<iframe src="https://worldppc.click/ads.php?publisher_id=3&amp;website_id=1'
    '&amp;type=text&amp;size=728x90" width="728" height="90" frameborder="0" '
    'scrolling="no" loading="lazy" title="Advertisement"></iframe>\n'
    '</div>'
)

# Every page carries its article column between a grid wrapper
# (`.page-grid` or `.layout`) and the rail that follows it. We rewrite that
# whole span, so the exact scaffolding the injection pass left behind does
# not matter.
GRID_RE = re.compile(
    r'(?s)<div class="(page-grid|layout)">(.*?)'
    r'(?=<aside\b(?![^>]*class="(?:pullquote|disclosure)"))')
GRID_CLASS_RE = re.compile(r'<div class="(page-grid|layout)">')


def bare_aside_repl(m):
    """Rebuild a sidebar whose opening tag a leaderboard pass dissolved."""
    attrs = ' '.join(m.group(2).split())
    return '</div>' + m.group(1) + f'<aside {attrs}>' + m.group(3)


BARE_ASIDE_RE = re.compile(
    r'(?s)</div>([ \t]*\n[ \t\n]*)'
    r'((?:class="[^"]*"[ \t]*|aria-label="[^"]*"[ \t]*){1,2})>'
    r'([ \t]*\n[ \t]*)')


# Every leaderboard-shaped div the injection pass could have written, with or
# without the class, with or without inline styles, comment markers included.
LEADER_RE = re.compile(
    r'(?s)(<!-- Ad(?: Block)? 728x90[^>]*-->\s*)?<div[^>]*(?:class="ad-leaderboard"'
    r'|style="width:728px)[^>]*>.*?</div>')


def esc(text):
    return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def build_body(slug, info):
    """Return the article column content: prose, verdict, criteria, CTA."""

    def sec_id(h2):
        return re.sub(r'[^a-z0-9]+', '-', h2.lower()).strip('-')

    out = [f'      <p class="opening">{esc(info["opening"])}</p>',
           f'      {AD_RECT}',
           '      <div class="ad-clearfix"></div>\n']

    for h2, texts in info['sections']:
        sid = sec_id(h2)
        out.append(f'      <section aria-labelledby="{sid}-heading">'
                   f'<h2 id="{sid}-heading">{esc(h2)}</h2>')
        for t in texts:
            out.append(f'        <p>{esc(t)}</p>')
        out.append('      </section>\n')

    criteria = '\n'.join(
        f'        <section class="criterion"><h3>{esc(t)}</h3><p>{esc(d)}</p></section>'
        for t, d in info['criteria'])
    fit = '\n'.join(
        f'        <li><strong>{esc(t)}:</strong> {esc(d)}</li>'
        for t, d in info['fit'])
    checklist = '\n'.join(f'        <li>{esc(i)}</li>' for i in info['checklist'])
    cta = info['cta']

    out.append(f'''      <section class="verdict" aria-labelledby="review-heading">
        <h2 id="review-heading">The short version</h2>
        <p>{esc(info['verdict'])}</p>
      </section>

      <section aria-labelledby="criteria-heading">
        <h2 id="criteria-heading">What we actually compare</h2>
        <p>These are the criteria that decide whether a product earns a place in your routine. They are deliberately not about brands.</p>
        <div class="criteria">
{criteria}
        </div>
      </section>

      <div class="ad-clearfix"></div>
      {LEADER}

      <blockquote><p>{esc(info['quote'])}</p></blockquote>

      <section aria-labelledby="fit-heading">
        <h2 id="fit-heading">Which approach fits which person</h2>
        <ul class="fit-list">
{fit}
        </ul>
      </section>

      <section aria-labelledby="guidance-heading">
        <h2 id="guidance-heading">What to bring to your next appointment</h2>
        <ol class="checklist">
{checklist}
        </ol>
        <p>None of this replaces your clinician. It makes the time you get more useful.</p>
      </section>

      <div class="ad-clearfix"></div>
      {LEADER}

      <section class="cta" aria-labelledby="cta-heading">
        <h2 id="cta-heading">{esc(cta['heading'])}</h2>
        <p>{esc(cta['body'])}</p>
        <a class="cta-link" href="{esc(cta['href'])}">{esc(cta['link'])}</a>
      </section>
      <p class="disclosure"><strong>{esc(info['disclosure'])}</strong></p>''')
    return '\n'.join(out) + '\n'


def fix_page(path, info):
    html = path.read_text(encoding='utf-8')

    # 1. Strip every injected ad unit and placeholder. The body rebuild below
    #    re-inserts the correct number in the correct places. Order matters:
    #    the leaderboard pass can dissolve a neighbouring opening tag, so it
    #    runs first and the repair below restores it.
    html = LEADER_RE.sub('', html)
    html = re.sub(r'(?s)<div class="ad-block"[^>]*>.*?</div>\s*</div>', '', html)
    html = re.sub(r'(?s)<div class="ad-block clearfix"></div>', '', html)
    html = re.sub(r'(?s)<div class="ad"[^>]*>.*?</div>', '', html)
    html = re.sub(r'(?s)\s*<div class="ad-placeholder"[^>]*>.*?</div>', '', html)
    html = re.sub(r'(?s)<div class="ad-slot"></div>', '', html)
    html = re.sub(r'(?s)<div class="ad-clearfix"></div>', '', html)
    # Empty scaffolding left by the injection pass.
    html = re.sub(r'<p></p>', '', html)
    html = re.sub(r'(?s)<div class="notice"[^>]*>.*?</div>', '', html)
    # A leaderboard swallowed the sidebar's opening tag, leaving its
    # attributes bare in the source. Reattach them to a real <aside> element.
    html = BARE_ASIDE_RE.sub(bare_aside_repl, html)
    html = re.sub(r'(?s)<section[^>]*>\s*</section>', '', html)
    html = re.sub(r'(?s)<div[^>]*>\s*</div>', '', html)
    # 2. Replace the whole article column with real content. The old column
    #    may be the original empty one or a column this script already built,
    #    so either way we swap the region between the grid wrapper and the
    #    sidebar with freshly built content.
    m = GRID_RE.search(html)
    if not m:
        raise SystemExit(f'{path.name}: article column not found')
    html = (html[:m.start()]
            + f'<div class="{m.group(1)}">\n{build_body(path.stem, info)}\n      </div>\n\n      '
            + html[m.end():])

    # 3. Fill the hero and sidebar text nodes.
    html = re.sub(r'(<p class="section-name">).*?(</p>)',
                  lambda m: f'{m.group(1)}{esc(info["section"])}{m.group(2)}', html)
    html = re.sub(r'(<h1 id="article-title">).*?(</h1>)',
                  lambda m: f'{m.group(1)}{esc(info["title"])}{m.group(2)}', html)
    html = re.sub(r'(<p class="deck">).*?(</p>)',
                  lambda m: f'{m.group(1)}{esc(info["deck"])}{m.group(2)}', html)
    html = re.sub(r'(class="byline">By <strong>NaturalHealthOne Editorial Team</strong>'
                  r'&nbsp;\|&nbsp; Updated )[^<]*(</p>)',
                  lambda m: f'{m.group(1)}September 18, 2026{m.group(2)}', html)
    html = re.sub(r'(?s)(<section class="side-note">)\s*<h2>.*?</h2>\s*<p>.*?</p>',
                  lambda m: f'{m.group(1)}<h2>Read the label</h2>\n'
                            f'          <p>{esc(info["side_note"])}</p>', html, count=1)

    # 4. Tidy whitespace the injections left behind. A bare attribute line
    #    collapses to a single newline, so restore the two-newline gap that
    #    the step-1 repair produced before this pass runs.
    html = re.sub(r'\n{3,}', '\n\n', html)
    html = re.sub(r'(?s)</div>\n\n(?!\s*<aside|\s*<section|\s*</main|\s*<section)',
                  '</div>\n\n', html)
    html = re.sub(r'(?s)</div>\n      <aside',
                  '</div>\n\n      <aside', html)

    path.write_text(html, encoding='utf-8')


def main():
    written, skipped = [], []
    for path in sorted(REVIEW_DIR.glob('*.html')):
        info = content_reviews.REVIEWS.get(path.stem)
        if info is None:
            skipped.append(path.name)
            continue
        fix_page(path, info)
        written.append(path.name)

    print(f'Wrote {len(written)} review pages')
    for w in written:
        print('  +', w)
    if skipped:
        print(f'Skipped {len(skipped)}:')
        for s in skipped:
            print('  -', s)


if __name__ == '__main__':
    main()
