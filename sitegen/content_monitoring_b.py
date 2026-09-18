"""Monitoring article content (part 2 of 2)."""

MONITORING_B = {
    'how-to-check-blood-sugar': {
        'deck': 'A fingerstick takes thirty seconds. Doing it consistently well is what makes the number usable.',
        'sections': [
            ('Before you start', [
                'Wash your hands with warm water and soap, then dry them fully. Traces of food, lotion, or hand sanitizer can distort the reading noticeably.',
                'Have everything ready: meter, strip, lancet device, and a safe place to dispose of used lancets.']),
            ('Where to prick', [
                'Use the side of the fingertip rather than the pad, which hurts more and is more sensitive. Rotate fingers and sites between tests.',
                'Avoid calloused areas and using the same exact spot repeatedly, which leads to soreness and harder sampling.']),
            ('Getting the drop right', [
                'A small drop is usually enough; do not squeeze hard. Compressing the finger can express fluid that dilutes the sample.',
                'If blood does not flow, warm your hand first or let it hang down briefly rather than forcing it.']),
            ('After the reading', [
                'Press a clean tissue to the site, record the number with its context, and store the used lancet in a proper sharps container.',
                'If the result disagrees strongly with how you feel, wash again and retest once before drawing conclusions.']),
        ],
        'safety': 'This article describes standard technique and cannot replace the training your clinician or diabetes educator provides. Never treat a suspected low or high without confirming, and contact your care team if you feel unwell.',
        'checklist': [
            'Wash and fully dry hands before every test.',
            'Prick the side of the fingertip, not the center pad.',
            'Rotate fingers and sites to avoid soreness.',
            'Use a fresh lancet and a properly stored strip each time.',
            'Record the reading with time, food, and activity context.',
            'Retest once if the number does not match your symptoms.'],
    },
    'how-to-read-blood-sugar-trends': {
        'deck': 'Isolated readings create worry. Trends are where the useful information actually lives.',
        'sections': [
            ('One reading tells you almost nothing', [
                'Glucose moves constantly through the day. A single value is a snapshot of one moment, shaped by what you ate, when, how you slept, and what you did.',
                'The question worth asking is not whether one number is good, but whether a pattern repeats.']),
            ('Look for repetition, not perfection', [
                'A spike after a particular meal once is data. The same spike after the same meal three times is a finding you can act on with your care team.',
                'Most patterns need five to ten consistent entries before they are worth interpreting.']),
            ('The four patterns worth watching', [
                'Overnight and early morning values, post-meal peaks, patterns after activity, and readings during illness or stress. These are the areas where glucose behavior changes most.',
                'Each one points to a different question, and to different conversations with your clinician.']),
            ('When a change deserves attention', [
                'A reading that breaks a stable pattern for several days, or a shift that comes with symptoms, is worth reporting sooner rather than later.',
                'A single odd reading, especially with an obvious cause, usually is not.']),
        ],
        'safety': 'Trends inform conversations; they do not set your treatment. Do not change insulin or medication doses based on self-identified patterns. Report sustained pattern changes or symptoms to your clinician.',
        'checklist': [
            'Record readings at consistent times for two weeks.',
            'Group entries by situation: morning, post-meal, activity.',
            'Look for a pattern that repeats at least three times.',
            'Note sleep, stress, and illness alongside the numbers.',
            'Ask your clinician which pattern to watch first.',
            'Report a sustained break in a stable pattern promptly.'],
    },
    'questions-about-glucose-monitoring': {
        'deck': 'The questions people ask most about glucose monitoring, with answers that respect what the evidence can support.',
        'sections': [
            ('How often should I check?', [
                'It depends entirely on your treatment. People using insulin generally check more often than those on lifestyle measures alone.',
                'Ask your clinician for a written schedule rather than deciding yourself. Testing without purpose tends to increase anxiety without improving control.']),
            ('Why do my readings vary so much?', [
                'Glucose is meant to move. Food, timing, activity, sleep, stress, illness, and even hydration all shift it within a single day.',
                'Variation is not failure. The question is whether the variation follows a pattern you can describe.']),
            ('Why did my reading not match how I felt?', [
                'Perceived symptoms and actual glucose do not always agree, and meters carry an allowed error margin.',
                'When the two disagree strongly, wash your hands and retest before acting on the number.']),
            ('Do I need a continuous monitor?', [
                'Not necessarily. A sensor is most valuable for answering a defined question over a defined period, and coverage rules differ widely.',
                'If fingersticks answer your questions, a sensor may add cost without adding insight. Ask your clinician what it would change for you.']),
        ],
        'safety': 'These answers are educational and cannot account for your diagnosis, medications, or targets. Ask your own clinician before changing any monitoring habit, and seek urgent care for severe symptoms.',
        'checklist': [
            'Ask for a written testing schedule and your targets.',
            'Bring your log with context, not just numbers, to visits.',
            'Ask what a normal day-to-day range looks like for you.',
            'Ask whether a change in pattern would change your plan.',
            'Confirm your technique and meter accuracy once a year.',
            'Ask whom to contact between appointments if readings shift.'],
    },
    'when-to-check-blood-sugar': {
        'deck': 'When you check matters as much as whether you check. Timing is what turns a number into information.',
        'sections': [
            ('Why timing is the whole point', [
                'A reading means little without its context. The same value means something different before a meal, two hours after it, at 3 a.m., or after a long walk.',
                'Testing at random times produces numbers that cannot be compared to each other, which is how monitoring becomes anxiety without insight.']),
            ('The standard checkpoints', [
                'First thing in the morning before food, just before a main meal, and two hours after starting that meal are the most commonly used windows.',
                'Your own schedule may differ, and if you use insulin or certain medications it almost certainly does. Follow the plan your clinician sets.']),
            ('Situations that call for an extra check', [
                'Before and after new or intense activity, during illness, after a medication change, before driving if you are at risk of lows, and before bed when overnight lows are a concern.',
                'These are the moments where a reading can genuinely change what you do next.']),
            ('When checking less is better', [
                'If testing has become a source of distress with no change in plan, discuss reducing frequency with your clinician rather than quitting silently.',
                'The right frequency is the one you can sustain and that informs actual decisions.']),
        ],
        'safety': 'This article describes general timing principles, not your schedule. Never change insulin or medication timing based on general guidance. If you experience symptoms of a low or feel unwell, check immediately and follow your care plan.',
        'checklist': [
            'Ask your clinician for your personal check schedule.',
            'Hold chosen times steady for one to two weeks.',
            'Add checks around new activity, illness, or medication change.',
            'Check before driving if you are at risk of lows.',
            'Record the context, not just the value, every time.',
            'Tell your team if checking is causing persistent distress.'],
    },
}
