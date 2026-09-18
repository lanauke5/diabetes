"""Regenerate article-manifest.json from the actual files on disk."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import SITE, CAT_LABEL
import generate_articles as gen

ROOT = Path('E:/diabetes')

CATS = ['type-2-diabetes', 'prediabetes', 'blood-sugar', 'nutrition', 'exercise',
        'weight-management', 'monitoring', 'supplements', 'sleep-stress',
        'complications', 'devices', 'best', 'reviews']


def main():
    articles = []
    for cat in CATS:
        cat_dir = ROOT / cat
        if not cat_dir.is_dir():
            continue
        for path in sorted(cat_dir.glob('*.html')):
            slug = path.stem
            info = gen.ALL_CONTENT.get(slug, {})
            articles.append({
                'slug': slug,
                'title': gen.slug_title(slug),
                'category': cat,
                'categoryLabel': CAT_LABEL.get(cat, cat),
                'url': f'{SITE}/{cat}/{path.name}',
                'path': f'{cat}/{path.name}',
                'description': info.get('deck', ''),
                'updated': '2026-09-18',
                'readTime': '6 min read',
                'generated': bool(info),
            })

    hubs = []
    for cat in CATS:
        if (ROOT / f'{cat}.html').exists():
            hubs.append({'slug': cat, 'title': CAT_LABEL.get(cat, cat),
                         'url': f'{SITE}/{cat}.html'})

    manifest = {
        'site': SITE,
        'generated_at': '2026-09-18',
        'generated_from': 'sitegen content modules',
        'articleCount': len(articles),
        'hubCount': len(hubs),
        'articles': articles,
        'hubs': hubs,
    }

    out = ROOT / 'article-manifest.json'
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False),
                   encoding='utf-8')
    print(f'Wrote {out} with {len(articles)} articles and {len(hubs)} hubs')


if __name__ == '__main__':
    main()
