"""Shared config for the NaturalHealthOne site generator."""

SITE = 'https://diabetes.naturalhealthone.com'

THEMES = {
    'sage':   {'accent': '#7a9e82', 'dark': '#4a7252', 'light': '#c0d8c4'},
    'teal':   {'accent': '#5a9898', 'dark': '#356f70', 'light': '#b0d4d4'},
    'amber':  {'accent': '#c4a054', 'dark': '#8a6c30', 'light': '#e8d4a0'},
    'purple': {'accent': '#8878a8', 'dark': '#585078', 'light': '#c8c0e0'},
    'blue':   {'accent': '#5f91a0', 'dark': '#376775', 'light': '#b8d4dc'},
    'rose':   {'accent': '#c4856a', 'dark': '#9b5e4a', 'light': '#e8c4b0'},
}

CAT_THEME = {
    'best': 'rose', 'complications': 'rose', 'devices': 'teal',
    'exercise': 'blue', 'prediabetes': 'sage', 'sleep-stress': 'purple',
    'supplements': 'amber', 'type-2-diabetes': 'sage', 'weight-management': 'rose',
    'nutrition': 'sage', 'monitoring': 'teal', 'blood-sugar': 'teal',
    'reviews': 'rose',
}

CAT_LABEL = {
    'best': 'Best', 'complications': 'Complications', 'devices': 'Devices',
    'exercise': 'Exercise', 'prediabetes': 'Prediabetes', 'sleep-stress': 'Sleep & Stress',
    'supplements': 'Supplements', 'type-2-diabetes': 'Type 2 Diabetes',
    'weight-management': 'Weight Management', 'nutrition': 'Nutrition',
    'monitoring': 'Monitoring', 'blood-sugar': 'Blood Sugar', 'reviews': 'Reviews',
}

CAT_BLURB = {
    'best': 'Compare diabetes products by fit, safety, and cost—not the loudest marketing claim.',
    'complications': 'Know what deserves attention, and how everyday care supports long-term health.',
    'devices': 'Compare diabetes tools by fit, safety, cost, and the life you actually lead.',
    'exercise': 'Find safer, more sustainable ways to bring movement into diabetes care.',
    'prediabetes': 'Understand risk and practical next steps without panic or all-or-nothing rules.',
    'sleep-stress': 'Explore how rest, stress hormones, and routines shape the glucose picture.',
    'supplements': 'Read supplement evidence carefully and keep prescribed care at the center.',
    'type-2-diabetes': 'Build a clearer understanding of type 2 diabetes and the choices around care.',
    'weight-management': 'Approach weight and metabolic health with context, dignity, and no quick-fix promises.',
    'nutrition': 'Understand how food choices shape glucose, insulin demand, and daily energy.',
    'monitoring': 'Turn numbers into patterns, and patterns into better questions for your care team.',
    'blood-sugar': 'Understand everyday glucose patterns with context, not judgment.',
    'reviews': 'How to evaluate diabetes products instead of trusting the loudest claim.',
}

# Hub pages that list each category (top level of the site).
HUBS = [
    'type-2-diabetes', 'prediabetes', 'blood-sugar', 'nutrition', 'exercise',
    'weight-management', 'monitoring', 'supplements', 'sleep-stress',
    'complications', 'devices', 'best', 'reviews',
]

# Hubs that are still bare stubs and must be (re)built.
STUB_HUBS = ['devices', 'supplements', 'complications']

AD_RECT = (
    '<div class="ad-block">'
    '<div class="ad-label">Advertisement</div>'
    '<div class="ad-slot">'
    '<script async src="https://worldppc.click/ads.php?publisher_id=3&amp;website_id=1'
    '&amp;type=banner&amp;size=300x250&amp;format=js"></script>'
    '</div></div>'
)

AD_LEADER = (
    '<div class="ad-leaderboard">'
    '<iframe src="https://worldppc.click/ads.php?publisher_id=3&amp;website_id=1'
    '&amp;type=text&amp;size=728x90" width="728" height="90" frameborder="0" '
    'scrolling="no" loading="lazy" title="Advertisement"></iframe>'
    '</div>'
)


def cat_colors(cat):
    return THEMES[CAT_THEME.get(cat, 'teal')]
