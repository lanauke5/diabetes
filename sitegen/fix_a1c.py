"""Repair monitoring/a1c-explained.html.

The page had real editorial content but a broken article body: the article
element was never closed, empty duplicate card markup was glued onto the
end of the article, and the ad blocks sat in place of body text. We keep
the page's own design and replace only the broken body region with real
A1C content followed by the existing ad markup.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import AD_RECT, AD_LEADER

ROOT = Path('E:/diabetes')
FILE = ROOT / 'monitoring' / 'a1c-explained.html'

SECTIONS = [
    ('What the A1C test actually measures', [
        'A1C, also called glycated hemoglobin or HbA1c, reflects the proportion of your hemoglobin that carries glucose. Because red blood cells live for roughly three months, the result approximates your average glucose over that window.',
        'It is not a snapshot. It is a moving average, which is why it can disagree with any single reading you take today and still be correct.']),
    ('Why A1C and daily readings can disagree', [
        'A meter tells you what glucose is right now. A1C tells you what it has been averaging. Both can be right while looking contradictory.',
        'This is the single most common source of confusion about the test, and it is not a sign that either measurement is wrong.']),
    ('What the result can and cannot tell you', [
        'A1C is useful for tracking the overall pattern over months, and for comparing the effect of a change in plan.',
        'It cannot show the daily highs and lows that matter for how you feel, and it says nothing about the cause of the pattern.']),
    ('The conditions that change interpretation', [
        'Anemia, recent blood loss or transfusion, hemoglobin conditions, pregnancy, and kidney disease can all make A1C misleading.',
        'This is why these details belong in the conversation, not just the number.']),
    ('Turning a result into a conversation', [
        'Bring the date of the test, a recent log or sensor summary, and any context like illness or medication changes.',
        'A result with context becomes a plan. A result without context becomes a worry.']),
]

SAFETY = ('Do not change medication, insulin, or a monitoring plan based on an A1C result '
          'without a qualified clinician. Tell your care team about pregnancy, anemia, '
          'hemoglobin conditions, kidney disease, recent blood loss, or transfusion, because '
          'they can affect interpretation. This article is educational only; read our full '
          'medical disclaimer.')


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('"', '&quot;'))


def main():
    html = FILE.read_text(encoding='utf-8')

    parts = []
    first = True
    for h2, paras in SECTIONS:
        parts.append(f'<h2>{esc(h2)}</h2>')
        for p in paras:
            cls = 'drop-cap' if first else ''
            first = False
            parts.append(f'<p class="{cls}">{esc(p)}</p>')
    body = '\n'.join(parts)

    items = [
        'Record the date of your last A1C.',
        'Bring a meter log or CGM summary if you have one.',
        'Note recent illness, travel, stress, or sleep changes.',
        'List prescribed medicines and recent changes.',
        'Mention anemia, bleeding, transfusion, or pregnancy.',
        'Ask what pattern to track before the next visit.',
    ]
    checklist = '\n'.join(
        f'          <span class="check-item" role="listitem">{esc(i)}</span>' for i in items)

    related = [
        ('Blood Glucose Monitoring Guide', 'blood-glucose-monitoring-guide.html',
         'Choose meaningful check times and make everyday measurements less confusing.'),
        ('Continuous Glucose Monitoring', 'continuous-glucose-monitoring-guide.html',
         'Understand sensor readings, trend direction, and useful questions for your team.'),
        ('How to Read Blood Sugar Trends', 'how-to-read-blood-sugar-trends.html',
         'Move beyond isolated values and notice the patterns that repeat.'),
    ]
    cards = '\n'.join(
        f'''        <article class="card">
          <div class="card-image" aria-hidden="true"></div>
          <div class="card-body"><small>Monitoring</small><h3>{esc(t)}</h3><p>{esc(d)}</p><a href="{href}">Read the guide</a></div>
        </article>''' for t, href, d in related)

    new_body = f'''      <p class="drop-cap">An A1C result is one of the most talked-about numbers in diabetes care, and one of the easiest to misunderstand when you see it without context. It is an average, not a verdict, and what it means depends heavily on the details you bring with it.</p>
{AD_RECT}
{body}
      <div class="ad-clearfix"></div>
{AD_LEADER}
      <blockquote class="pull-quote"><p>&#8220;A meter tells you what glucose is right now. A1C tells you what it has been averaging. Both can be right.&#8221;</p></blockquote>
      <div class="ad-clearfix"></div>
{AD_LEADER}
'''

    # Replace the broken body region with clean content + ads.
    import re
    pattern = re.compile(
        r'(?s)<p class="drop-cap"></p>.*?<!-- Ad Block 728x90 Slot 2 -->.*?<p></p>')
    if not pattern.search(html):
        raise SystemExit('Could not locate the broken body region')
    html = pattern.sub(lambda m: new_body, html)

    # Drop the empty duplicate cards that were glued onto the article end.
    html = re.sub(r'(?s)</article><article class="card">.*?</article>\s*(?=<aside class="safety-note")',
                  '\n      </article>', html, count=1)

    FILE.write_text(html, encoding='utf-8')
    print('Repaired a1c-explained.html')


if __name__ == '__main__':
    main()
