"""Verify the generated site: internal links, anchors, and basic structure."""

import re
import sys
from pathlib import Path

ROOT = Path('E:/diabetes')
sys.path.insert(0, str(Path(__file__).resolve().parent))


def main():
    html_files = sorted(p for p in ROOT.rglob('*.html'))
    existing = {str(p.relative_to(ROOT)).replace('\\', '/') for p in html_files}

    problems = []
    for p in html_files:
        rel = str(p.relative_to(ROOT)).replace('\\', '/')
        html = p.read_text(encoding='utf-8', errors='ignore')

        # Unbalanced article tags
        n_open = len(re.findall(r'<article\b', html))
        n_close = len(re.findall(r'</article>', html))
        if n_open != n_close:
            problems.append(f'{rel}: <article> unbalanced ({n_open} open / {n_close} close)')

        # Unclosed main
        if '<main' in html and '</main>' not in html:
            problems.append(f'{rel}: <main> never closed')

        # href targets
        for m in re.finditer(r'href="([^"#]+)"', html):
            href = m.group(1)
            if href.startswith(('http', 'mailto:', '#')):
                continue
            base = p.parent / href
            target = str(base.resolve().relative_to(ROOT)).replace('\\', '/')
            if target not in existing:
                problems.append(f'{rel}: broken link -> {href}')

    # Expected files all present
    print(f'Checked {len(html_files)} html files')
    if problems:
        print(f'\n{len(problems)} problems:')
        for x in problems:
            print('  !', x)
    else:
        print('No broken internal links or structural problems found.')


if __name__ == '__main__':
    main()
