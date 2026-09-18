"""Editorial content for the hand-written reviews/ pages.

The ten review pages share one design but were left with empty bodies after an
ad-injection pass. This module holds the actual article content for each page.
"""

REVIEWS = {
    'glucose-meter-review': {
        'section': 'Independent device guide / Blood glucose meters',
        'title': 'Choosing a glucose meter that fits real life',
        'deck': 'Accuracy matters, but so do strip prices, readable results, a manageable blood sample, and a routine you can sustain.',
        'verdict': (
            'The best meter for you is the one you will actually use correctly twice a day. '
            'That is usually a mid-range model with cheap strips, a backlight, and a small '
            'blood sample requirement, not the most feature-rich device on the shelf.'),
        'opening': (
            'A glucose meter is the one device most people with diabetes use every single day, '
            'and most of us choose it backwards. We compare features and read marketing claims, '
            'when the things that decide whether the meter helps us are far more ordinary: how '
            'much the strips cost over a year, whether we can read the screen without glasses, '
            'and how big a blood drop it needs.'),
        'sections': [
            ('Accuracy is the floor, not the whole house', [
                'Every meter sold is regulated against reference standards, but allowed error margins mean two correct meters can still disagree by a meaningful amount on the same drop of blood.',
                'That gap is normal, and it is why a single reading should inform a conversation rather than trigger a decision.']),
            ('The real cost is the strips', [
                'Meters are often cheap or even free, because the ongoing purchase is the strips. Over a year of testing twice daily, strip price dominates the total by a wide margin.',
                'Before you buy anything, check what your insurer or health system prefers, because coverage rules often make one choice far cheaper than the rest.']),
            ('The features worth paying for', [
                'A backlight, a small blood sample requirement, and simple data export are genuinely useful in daily life. A large memory or a connected app helps only if you will actually review the data.',
                'The truth is, most people never look at stored readings at all, so paying for unlimited memory is paying for a feature that goes unused.']),
            ('Keeping the readings trustworthy', [
                'Wash hands before testing, store strips inside their date range, keep the lancet fresh, and run control solution checks on a schedule.',
                'A meter you use correctly twice a day beats an advanced one you avoid because it is fiddly.']),
        ],
        'quote': 'A meter you use correctly twice a day beats an advanced one you avoid.',
        'criteria': [
            ('Accuracy standards', 'Ask which meters meet the tighter accuracy standards in your region. This is the first question, not the last one.'),
            ('Annual strip cost', 'Strip price, not meter price, decides the real cost of testing. Compare a full year, not a box.'),
            ('Sample size and screen', 'A small blood drop and a readable, backlit screen change how often you actually test.'),
            ('Data export', 'Exporting readings to your care team matters far more than how many readings the meter can store.'),
        ],
        'fit': [
            ('If you test often', 'Prioritise cheap strips and a small blood sample. Those two factors shape every single day of use.'),
            ('If you test rarely', 'Simplicity beats features. A meter you understand without re-reading the instructions will be used correctly.'),
            ('If you use insulin', 'Accuracy standards and fast, confirmable readings matter most, so ask your clinician or pharmacist which meters qualify.'),
            ('If you share data', 'Choose simple export over large memory, because a summary your clinician can read beats a log only you can see.'),
        ],
        'checklist': [
            'Ask which meters meet the tighter accuracy standards in your region.',
            'Compare a full year of strip cost, not the meter price.',
            'Check coverage through your insurer or health system.',
            'Wash hands and use a fresh lancet for every test.',
            'Run control solution checks on a regular schedule.',
            'Learn to export readings before your next appointment.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Devices hub',
            'href': '../devices.html',
        },
        'disclosure': (
            'How we evaluate meters: we compare published accuracy standards, ongoing '
            'consumable cost, usability, and data handling. We do not rank brands, accept '
            'payment for placement, or invent test results. Prices and coverage change, and '
            'so do device approvals, so confirm the details that matter to you before buying.'),
        'side_note': ('Approved uses and limitations differ by model and country. Consult the '
                      'current instructions for use, regulator information, and your care '
                      'team rather than relying on a comparison page alone.'),
    },

    'cgm-review': {
        'section': 'Independent device guide / Continuous glucose monitors',
        'title': 'Choosing a CGM beyond the headline features',
        'deck': 'Sensor wear, alert design, access, skin tolerance, and a plan for unexpected readings matter as much as data frequency.',
        'verdict': (
            'A continuous glucose monitor is a question-answering tool, not a permanent '
            'answer. It is most valuable when you define one specific question first, such '
            'as what a usual breakfast does, and then stop wearing it once that question is '
            'answered.'),
        'opening': (
            'A continuous glucose monitor changes how you see glucose, because it replaces '
            'isolated dots with a curve, and that curve explains more in a week than a month '
            'of fingersticks ever will. But the decision to wear one is not really about the '
            'sensor. It is about whether you have a question worth answering, and whether you '
            'can get one through coverage or at a price you can sustain.'),
        'sections': [
            ('What a sensor actually measures', [
                'A CGM estimates glucose in the fluid under your skin, not in your blood. That fluid lags blood by several minutes, and the gap is widest exactly when glucose is moving fastest.',
                'This is why a sensor can show a direction that looks different from a fingerstick taken at the same moment, and why both can be telling the truth.']),
            ('The alert question nobody asks first', [
                'Alert design matters more than most people expect, because alerts you cannot tune get turned off, and alerts that cry wolf get ignored.',
                'Before committing to a system, ask how alerts are set, whether you can adjust them, and what happens at night.']),
            ('Skin tolerance and wear length', [
                'Some people react to the adhesive, and a sensor that itches its way off after two days never delivers a usable pattern.',
                'Wear length also changes the value per sensor, so compare cost per day rather than cost per box.']),
            ('When a fingerstick still wins', [
                'Before treating a suspected low or a rapid change, confirm with a fingerstick. That is not a flaw of the technology, it is how it is designed to be used.',
                'And if your fingersticks already answer your questions, adding a sensor may add cost without adding any insight.']),
        ],
        'quote': 'Define one question before you start, and stop when that question is answered.',
        'criteria': [
            ('Lag and accuracy', 'Sensors read interstitial fluid, which lags blood. Ask about accuracy during rapid change, not just at rest.'),
            ('Alert flexibility', 'Alerts you cannot tune get muted. Ask how they are set, and what happens overnight.'),
            ('Cost per day', 'Compare cost per day of wear, accounting for sensor life, not the price of a single box.'),
            ('Coverage rules', 'Coverage often depends on diagnosis and insulin use, so ask what applies to you before assuming anything.'),
        ],
        'fit': [
            ('If you use insulin', 'Alert design and accuracy during rapid change matter most, because that is where treatment decisions happen.'),
            ('If you have type 2 without insulin', 'A short defined window of wear often answers the real question, then you can stop.'),
            ('If you have sensitive skin', 'Test adhesive tolerance on one sensor before committing to a long-term supply.'),
            ('If you are paying yourself', 'Compare cost per day, and set a clear stopping point so the purchase has an endpoint.'),
        ],
        'checklist': [
            'Ask whether a sensor is covered for your situation, and for how long.',
            'Define the one question you want answered before you start.',
            'Ask about accuracy limits during rapid glucose change.',
            'Check how alerts are set and whether you can adjust them.',
            'Confirm unfamiliar readings with a fingerstick before acting.',
            'Bring the summary and the pattern to your next visit.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Devices hub',
            'href': '../devices.html',
        },
        'disclosure': (
            'How we evaluate CGMs: we compare accuracy claims against published clinical '
            'behaviour, alert design, wear length, cost per day, and access. We do not rank '
            'brands, accept payment for placement, or claim to have tested devices '
            'ourselves. Indications and coverage rules differ by country and change often, '
            'so confirm the current situation before you commit.'),
        'side_note': ('CGM indications, compatible devices, interfering substances, imaging '
                      'precautions, and treatment-decision rules vary by system and can '
                      'change. Use the current official instructions.'),
    },

    'continuous-monitor-review': {
        'section': 'Independent device guide / Continuous monitoring',
        'title': 'What a continuous monitor actually teaches you',
        'deck': 'The curve is the point: how readings rise, fall, and repeat tells you more than any single number ever could.',
        'verdict': (
            'A continuous monitor does not give you more data, it gives you a shape. '
            'Learning to read that shape, the rise after meals, the drag of a bad night, '
            'the flat stretch of a good week, is what makes the device worth wearing.'),
        'opening': (
            'Most people buy a continuous monitor hoping for better numbers, and what they '
            'get instead is better questions. The first few days of wearing a sensor usually '
            'reveal that a food you blamed was innocent, and a habit you never thought about '
            'was moving glucose all along. Here is how to get that insight without drowning '
            'in data.'),
        'sections': [
            ('From dots to a curve', [
                'A fingerstick is a photograph, and a sensor is a film. The photograph tells you where you are, and the film shows you how you got there and where you are heading.',
                'Most of the useful information in diabetes care lives in the direction and the shape, not in the value at one instant.']),
            ('The pattern is what repeats', [
                'A single high reading after a meal is a data point. The same rise after three similar meals is a finding, and that distinction is the whole point of wearing a sensor.',
                'Look for what repeats, and treat the repetition as the signal rather than reacting to each spike.']),
            ('Reading the overnight stretch', [
                'The flat or restless overnight stretch tells you about sleep, stress, and the dawn phenomenon, and it is usually the least examined part of the day.',
                'A morning reading alone cannot separate these, which is why the overnight curve is often where the real answer hides.']),
            ('Knowing when to stop', [
                'Wearing a sensor forever is not the goal. Answering a defined question, then returning to fingersticks or a routine visit, is often the better use of the device.',
                'Some people stay on a sensor long after it has stopped teaching them anything, and the cost keeps arriving monthly.']),
        ],
        'quote': 'A single high reading is a data point. The same rise three times is a finding.',
        'criteria': [
            ('Curve quality', 'How the sensor behaves during rapid change matters more than how many points it collects per hour.'),
            ('Trend arrows', 'Readable trend direction, shown clearly and without jargon, is what turns data into a decision.'),
            ('Reporting', 'A summary your clinician can actually read in two minutes beats a detailed report nobody opens.'),
            ('Wear comfort', 'A sensor that irritates its way off your arm after two days produces no pattern at all.'),
        ],
        'fit': [
            ('If you are new to monitoring', 'Start with a short window, and write down one question before you apply the first sensor.'),
            ('If you already log readings', 'The sensor fills the gaps between checks, which is usually where the explanation lives.'),
            ('If you feel overwhelmed', 'Ask for the summary view, not the minute-by-minute chart, and review it weekly rather than hourly.'),
            ('If you have answered your question', 'Stop, or take a break. A sensor that teaches nothing new is a cost without a return.'),
        ],
        'checklist': [
            'Write down one question before you start wearing a sensor.',
            'Review the curve weekly rather than reacting hour by hour.',
            'Look for what repeats across three similar days or meals.',
            'Check the overnight stretch, not just the post-meal peaks.',
            'Ask your clinician how to read the trend arrows correctly.',
            'Agree in advance when you will stop or reassess wearing it.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Monitoring hub',
            'href': '../monitoring.html',
        },
        'disclosure': (
            'How we evaluate monitoring tools: we look at how well a device supports pattern '
            'recognition, how honestly it communicates its own accuracy limits, and what '
            'the reporting looks like in practice. We do not rank brands or accept payment '
            'for placement, and we have not been given devices to test. Confirm current '
            'indications and prices yourself.'),
        'side_note': ('Reading a trend is a learned skill. If a curve worries you, ask your '
                      'care team to walk you through it before you change anything.'),
    },

    'insulin-pen-review': {
        'section': 'Independent device guide / Insulin pens',
        'title': 'Choosing an insulin pen that fits your hands and routine',
        'deck': 'Dose dial feel, grip, needle length, readability, and carrying conditions matter more than the brand name on the barrel.',
        'verdict': (
            'The right pen is the one you can dial accurately with cold hands, in poor '
            'lighting, on a busy morning. That is a usability question, not a brand '
            'question, and the answer is genuinely individual.'),
        'opening': (
            'An insulin pen looks like the simplest object in a diabetes kit, and it is the '
            'one you will handle thousands of times. Here is what surprises most people: '
            'the difference between pens is rarely about the insulin inside, which your '
            'clinician decides. It is about the dial, the grip, the numbers, and whether '
            'you can actually tell what dose you set.'),
        'sections': [
            ('The dial is the daily interface', [
                'A dial with a clear click at each unit, and numbers large enough to read without searching for glasses, prevents the most common dosing errors.',
                'If the dial feels vague, you will second-guess it, and second-guessing a dose is a daily source of stress.']),
            ('Grip and hand strength', [
                'Pen shape and surface change how easy it is to hold and push, and this matters far more for people with arthritis, neuropathy, or reduced grip strength.',
                'A pen that is hard to press leads to skipped or partial doses, which is a clinical problem disguised as a comfort complaint.']),
            ('Needle length and technique', [
                'Shorter needles work for most adults, and the technique, pinching the skin, injecting slowly, holding for a count, matters more than the length.',
                'Needle reuse is the most common mistake, because a needle blunts after one use and hurts more with each reuse.']),
            ('Storage and carrying', [
                'Pens in use can be kept at room temperature for a defined number of days, and spare pens belong in the fridge. Insulated bags matter only when heat or freezing is a real risk.',
                'Check the leaflet for the specific room-temperature limit, because it is not the same for every pen.']),
        ],
        'quote': 'A pen you can dial with cold hands in poor lighting is the one that fits real life.',
        'criteria': [
            ('Dose clarity', 'Clear clicks and large, well-printed numbers are what prevent dosing errors in ordinary conditions.'),
            ('Grip and push force', 'If the plunger is hard to press, doses get skipped. Try the action, not just the shape.'),
            ('Room-temperature limit', 'How many days a pen in use lasts out of the fridge differs, and it changes your travel and storage plan.'),
            ('Needle compatibility', 'Standard needles fit most pens, but confirm length and fitting rather than assuming.'),
        ],
        'fit': [
            ('If you have arthritis or weak grip', 'Test the plunger force and the grip surface before committing, because this decides whether doses happen.'),
            ('If you inject away from home', 'Check the room-temperature limit and carry an insulated bag only when heat is a real risk.'),
            ('If your dose is small', 'A pen that dials in half-unit steps and shows clear clicks makes small dosing far less anxious.'),
            ('If you travel often', 'Spare pens stay cool, used pens stay usable, and airport security rules for needles vary by country.'),
        ],
        'checklist': [
            'Ask which pens are compatible with your prescribed insulin.',
            'Test the dial and the plunger before you settle on a pen.',
            'Check the room-temperature storage limit for that specific pen.',
            'Ask which needle length suits your injection sites and technique.',
            'Use a fresh needle every time and dispose of it safely.',
            'Bring your pen to an appointment and show your technique.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Devices hub',
            'href': '../devices.html',
        },
        'disclosure': (
            'How we evaluate pens: we compare usability, dosing accuracy in ordinary '
            'conditions, storage requirements, and needle compatibility. We do not rank '
            'brands, accept payment for placement, or recommend switching insulin. Which '
            'insulin you use is a clinical decision only your prescriber can make.'),
        'side_note': ('Never change your pen, needle length, or injection technique based on '
                      'an article alone. Bring the pen to your next appointment and show '
                      'exactly what you do.'),
    },

    'diabetes-app-review': {
        'section': 'Independent device guide / Diabetes apps',
        'title': 'Diabetes apps: what they help with, and what they quietly cost',
        'deck': 'A good app turns scattered readings into a pattern. A bad one turns them into anxiety, and the difference is in the design.',
        'verdict': (
            'The best diabetes app for you is the one you will still open in month three, '
            'with privacy terms you have actually read and export that does not lock your '
            'data away. Most apps fail on one of those two points.'),
        'opening': (
            'There is a diabetes app for everything now, and most of them promise the same '
            'thing: that logging your life will finally make it make sense. Some of them '
            'genuinely help. Here is the part most reviews skip, that a third app in a '
            'month does not produce more insight, it just produces more typing, and in '
            'some cases it produces new anxiety about numbers you cannot act on.'),
        'sections': [
            ('What a good app actually does', [
                'It reduces the work of noticing patterns, by remembering context alongside numbers and showing you the repetition instead of making you hunt for it.',
                'The useful question is always the same: does this tool save you time at your appointments, or does it just give you more to explain?']),
            ('The privacy question that matters', [
                'Health data can be shared with insurers, employers, or advertising networks, depending on the terms you agreed to, and most terms are not written to be understood.',
                'Look for clear statements about whether data is sold or used for advertising, and whether you can delete everything and leave.']),
            ('Coaching, subscription, and the fine print', [
                'Human coaching inside an app is sometimes included in care programs at no cost, and sometimes a subscription that adds up to hundreds a year.',
                'Ask your health system first, because the same service is often available free through a program you already qualify for.']),
            ('Export and lock-in', [
                'If you cannot export your own log as a simple file, you do not own it. This matters most when you switch devices, clinicians, or apps.',
                'An app that holds your data hostage is not a tool, it is a trap dressed up as a dashboard.']),
        ],
        'quote': 'If you cannot export your own log, you do not own it.',
        'criteria': [
            ('Privacy terms', 'Clear language about selling data, advertising use, and deletion is more important than any chart style.'),
            ('Context capture', 'Logging sleep, stress, and activity beside a reading is what makes the pattern interpretable.'),
            ('Export', 'A simple file export means your history survives a device change or a new clinician.'),
            ('Ongoing cost', 'Compare against programs you may already qualify for through your health system.'),
        ],
        'fit': [
            ('If you log nothing today', 'A simple app with reminders beats a powerful one you abandon in a week.'),
            ('If you already keep a log', 'Choose the app that imports your existing data rather than making you retype it.'),
            ('If you feel anxious about readings', 'Turn off constant notifications and review the summary weekly instead.'),
            ('If you change devices often', 'Export before you commit, because switching later without it costs your entire history.'),
        ],
        'checklist': [
            'Read what the app says about selling or advertising your data.',
            'Check whether you can export your log as a simple file.',
            'Ask your health system whether coaching or logging is already covered.',
            'Log context, not just numbers, because context is the usable part.',
            'Turn off notifications that make you react instead of review.',
            'Bring the summary, not the raw log, to your next appointment.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Monitoring hub',
            'href': '../monitoring.html',
        },
        'disclosure': (
            'How we evaluate apps: we read privacy terms, test export, and compare cost '
            'against what health systems already provide. We do not rank apps, accept '
            'payment for placement, or claim clinical superiority for any tool. Privacy '
            'policies and prices change frequently, so re-check before you trust an app '
            'with health data.'),
        'side_note': ('An app is a notebook with a chart, not a clinician. If reading your '
                      'own data makes you anxious, say so at your next appointment; '
                      'scaling back logging is a reasonable choice.'),
    },

    'fitness-tracker-review': {
        'section': 'Independent device guide / Fitness trackers',
        'title': 'Fitness trackers for diabetes: what helps, what is noise',
        'deck': 'Step counts, heart rate trends, and sleep data can support a real care plan, and the marketing around them mostly cannot.',
        'verdict': (
            'A tracker helps when it makes movement impossible to ignore. It fails when it '
            'turns every walk into a performance, or when sleep data you cannot act on '
            'becomes a nightly source of worry.'),
        'opening': (
            'The promise of a fitness tracker is seductive precisely because movement is '
            'one of the most reliable levers on glucose. Here is what gets lost: the '
            'tracker does not move you. It only counts. The people it helps most are the '
            'ones who use the count to protect daily walking from being crowded out, not '
            'the ones who chase a streak for its own sake.'),
        'sections': [
            ('What the count is good for', [
                'A step count is an honest proxy for ordinary daily movement, and protecting it protects one of the most reliable influences on insulin sensitivity.',
                'Working muscles take up glucose with less insulin, which is why a walking habit is worth far more than the occasional hard workout.']),
            ('Sleep data, useful and useless', [
                'Sleep quality moves the next day glucose, so a tracker that reveals a pattern of fragmented nights has real clinical value.',
                'But a nightly score you cannot act on can become its own source of stress, which is the exact problem you were trying to solve.']),
            ('Heart rate and stress hints', [
                'Resting heart rate trends can hint at fitness changes, illness, or persistent stress, and they are a prompt to ask a question, not a diagnosis.',
                'No consumer device can read stress or recovery from your wrist, whatever the marketing implies.']),
            ('Battery, comfort, and water resistance', [
                'The features that decide whether you keep wearing it are boring: charge it once a week or every night, and whether it survives a shower.',
                'A tracker in a drawer collects no data at all, so comfort and battery matter more than sensor count.']),
        ],
        'quote': 'The tracker does not move you. It only counts.',
        'criteria': [
            ('Daily movement tracking', 'Reliable step counting and reminders to move are what actually support a glucose-relevant habit.'),
            ('Sleep insight', 'Sleep quality shifts the next day glucose, so usable sleep reporting earns its place.'),
            ('Battery life', 'Weekly charging beats nightly, because a dead tracker collects nothing.'),
            ('Comfort and durability', 'You will only keep wearing what you forget is on your wrist.'),
        ],
        'fit': [
            ('If you sit for long stretches', 'Move reminders are the single most useful feature, because they interrupt the sitting, not the schedule.'),
            ('If you suspect poor sleep', 'Sleep reporting gives you two weeks of evidence to bring to a conversation.'),
            ('If you are easily demotivated', 'Hide the streaks and the comparisons, and keep one number you can actually influence.'),
            ('If you want training data', 'A tracker is a general tool; for structured training, your clinician and a plan matter more than the device.'),
        ],
        'checklist': [
            'Note your typical daily step count before setting any target.',
            'Protect walking time on busy days rather than chasing streaks.',
            'Record sleep quality beside your morning readings.',
            'Ask whether a sleep evaluation is warranted if nights stay fragmented.',
            'Use heart rate trends as a prompt to ask, never as a diagnosis.',
            'Bring two weeks of movement data to your next appointment.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Exercise hub',
            'href': '../exercise.html',
        },
        'disclosure': (
            'How we evaluate trackers: we compare what a device measures reliably against '
            'what actually influences glucose, plus battery, comfort, and data export. We '
            'do not rank brands, accept payment for placement, or treat step targets as '
            'clinical advice. Consumer sensors are not medical devices, and their accuracy '
            'varies more than their marketing suggests.'),
        'side_note': ('Consumer trackers are not medical devices. Their heart rate and '
                      'sleep estimates are useful prompts for conversation, not '
                      'measurements to act on alone.'),
    },

    'smart-scale-review': {
        'section': 'Independent device guide / Smart scales',
        'title': 'Smart scales and weight trends, without the false precision',
        'deck': 'Body fat estimates from a scale are rough. The trend in morning weight over weeks is what carries real signal.',
        'verdict': (
            'A smart scale earns its place by making the trend visible and the daily noise '
            'easy to ignore. It fails when its body fat percentage becomes a number you '
            'react to each morning.'),
        'opening': (
            'Weight is one physiological factor among many, and the scale industry has '
            'spent decades convincing people it is a moral scorecard. So here is the '
            'honest version: your weight trend over weeks carries real information about '
            'your metabolic picture, and your weight on any single morning carries almost '
            'none. A good scale helps you see the difference.'),
        'sections': [
            ('Why daily weight is mostly noise', [
                'Water, glycogen, salt, hormones, and a large meal shift the number by more than any real fat change, and they do it within hours.',
                'Looking at the trend across weeks is the only way to see past that noise, and it is the whole reason to own a connected scale.']),
            ('Body fat percentage, honestly', [
                'Scale-based body fat estimates use a weak electrical signal and a population formula, so they are approximate and easily confused by hydration.',
                'Two scales can disagree by several points on the same person on the same day, so track direction at most, and never compare between devices.']),
            ('What a trend can tell your clinician', [
                'A steady downward or stable trend alongside improving glucose tells a meaningful story about whether a plan is sustainable.',
                'A jagged, yo-yo pattern tells a different story, often about a plan that is too aggressive to maintain.']),
            ('The habit that makes it work', [
                'Weigh once, first thing in the morning, on the same day each week, and record it without reacting to it.',
                'Daily weighing is fine for data, but only if you can look at the week rather than the day.']),
        ],
        'quote': 'Your weight trend over weeks carries real information. Any single morning carries almost none.',
        'criteria': [
            ('Trend reporting', 'A clear weekly and monthly chart is the entire value, because that is where the signal lives.'),
            ('Consistency', 'Same time, same conditions, same scale. Comparability is worth more than precision.'),
            ('App and export', 'Being able to share a trend with your care team is what turns data into a conversation.'),
            ('Body fat honesty', 'Treat the percentage as a rough direction at best, never as a daily target.'),
        ],
        'fit': [
            ('If daily weighing upsets you', 'Switch to weekly, or stop weighing and let your clinician track it at visits.'),
            ('If you are building muscle', 'Weight may hold steady while your shape and glucose both improve, so ignore the scale number alone.'),
            ('If you share data', 'Pick a scale whose app exports a simple trend, because that is what your clinician can use.'),
            ('If you just want a number', 'Any reliable scale works; you do not need a connected one.'),
        ],
        'checklist': [
            'Weigh at the same time and under the same conditions.',
            'Look at the weekly and monthly trend, not the daily number.',
            'Record weight beside glucose readings for context.',
            'Ask your clinician what trend is realistic for your plan.',
            'Mention fluid retention, swelling, or sudden changes promptly.',
            'Bring the trend, not the daily readings, to appointments.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Weight Management hub',
            'href': '../weight-management.html',
        },
        'disclosure': (
            'How we evaluate scales: we compare trend reporting, app export, build '
            'quality, and how honestly the device communicates its own accuracy limits. '
            'We do not rank brands, accept payment for placement, or treat body fat '
            'percentages as measurements. Weight is one factor among many, and no scale '
            'tells you anything about your worth.'),
        'side_note': ('Weight is one physiological factor among many, not a measure of '
                      'effort or character. If the number affects your mood for the day, '
                      'that is a signal to change the habit, not yourself.'),
    },

    'foot-care-review': {
        'section': 'Independent device guide / Foot care for diabetes',
        'title': 'Foot care products: where they help, where they hide risk',
        'deck': 'Daily inspection, moisturising the right places, and well-fitted shoes prevent harm. Home surgery kits cause it.',
        'verdict': (
            'Most diabetes foot problems are prevented by boring daily habits and '
            'well-fitted footwear, not by buying more products. The single most useful '
            'purchase is often a long-handled mirror, because it lets you actually see the '
            'parts you cannot reach.'),
        'opening': (
            'Foot care is the least glamorous part of diabetes self-care and the one with '
            'the highest stakes, because reduced sensation means a small problem can go '
            'unnoticed for days. Here is what actually helps, and the one category of '
            'product that causes more harm than it prevents.'),
        'sections': [
            ('Why daily looking matters more than buying', [
                'When sensation is reduced, your eyes replace your nerves as the warning system, and a daily thirty-second check is what catches a blister before it becomes a wound.',
                'No cream, insole, or gadget substitutes for noticing.']),
            ('Moisturise the right places, not all of them', [
                'Dry skin on the heel cracks and opens a door to infection, so moisturise the tops and soles.',
                'Between the toes should stay dry, because moisture there encourages fungal breakdown, and that is one of the few foot rules with no exceptions.']),
            ('The products that quietly cause harm', [
                'Callus shavers, chemical peels, and corn removal kits are sold for home use, and on feet with reduced sensation or circulation they are a direct route to a wound.',
                'A pedicure at a salon is not a substitute for a podiatry visit, and instruments that are not sterile are a real risk.']),
            ('Footwear and professional review', [
                'Well-fitted shoes with enough depth and a smooth lining prevent the friction that starts most problems, and professional fitting costs less than one wound.',
                'Ask how often your feet should be professionally reviewed, because that interval depends on your risk level, not on how things feel.']),
        ],
        'quote': 'When sensation is reduced, your eyes replace your nerves as the warning system.',
        'criteria': [
            ('Daily inspection', 'A long-handled or magnifying mirror is the highest-value purchase in foot care, full stop.'),
            ('Moisturiser choice', 'A simple fragrance-free cream for tops and soles, and nothing between the toes.'),
            ('Footwear fit', 'Depth, lining seams, and width matter more than the brand or the price.'),
            ('Professional care', 'How often your feet are reviewed is a clinical decision based on your risk level.'),
        ],
        'fit': [
            ('If you cannot see your feet', 'A long-handled mirror or a phone photo is not optional, it is your warning system.'),
            ('If you have dry, cracking heels', 'Moisturise tops and soles daily, and ask your podiatrist rather than filing aggressively.'),
            ('If you have reduced sensation', 'Never buy a blade, a callus shaver, or a chemical peel for your own feet.'),
            ('If you are buying shoes', 'Get fitted at the end of the day, and check the lining for seams that press.'),
        ],
        'checklist': [
            'Check every foot daily, including between the toes and the heel.',
            'Use a mirror or a phone photo for areas you cannot see.',
            'Moisturise tops and soles, and keep between the toes dry.',
            'Never use blades, shavers, or chemical peels on your feet.',
            'Report cuts, blisters, colour change, or numbness the same day.',
            'Ask how often professional foot review is right for you.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Devices hub',
            'href': '../devices.html',
        },
        'disclosure': (
            'How we evaluate foot care products: we separate prevention, which is backed '
            'by clear clinical practice, from products that quietly transfer risk to '
            'people with reduced sensation. We do not rank brands, accept payment for '
            'placement, or sell anything. Foot care is a clinical matter, and the most '
            'important step is a professional review at the interval your clinician sets.'),
        'side_note': ('If you find a cut, blister, colour change, or area of numbness, '
                      'contact your care team the same day rather than treating it at '
                      'home. Waiting is the mistake almost everyone makes.'),
    },

    'diabetes-supplement-review': {
        'section': 'Independent guide / Diabetes supplements',
        'title': 'Diabetes supplements: how to read past the label',
        'deck': 'Most supplements for blood sugar have weak evidence, and the strongest ones still cannot replace prescribed care.',
        'verdict': (
            'The honest answer about diabetes supplements is that a few have modest '
            'evidence, most do not, and none is a substitute for the care your clinician '
            'prescribes. The most useful skill is not choosing a supplement, it is reading '
            'a label well enough to know which claims to distrust.'),
        'opening': (
            'Walk into any pharmacy and the supplement aisle will promise steadier blood '
            'sugar in a bottle. The truth is that supplement regulation is far lighter '
            'than drug regulation, which means the burden of evaluating the evidence falls '
            'on you. Here is how to do that without needing a research degree.'),
        'sections': [
            ('Why supplement claims are so easy to make', [
                'In many countries, supplements are regulated as food rather than medicine, so claims can be phrased loosely and the ingredient list is not always verified by a third party.',
                'This is why a bottle can look as convincing as a medication while being held to a completely different standard.']),
            ('The ingredients with the most evidence', [
                'A small number of ingredients have been studied in trials, but the results are mixed, the effects are generally modest, and they rarely justify the marketing language around them.',
                'Even the better-studied options interact with medications, and an interaction with a glucose-lowering drug is not a minor concern.']),
            ('The claims that should end the conversation', [
                'Any product that promises to replace medication, reverse a condition, or deliver a guaranteed result is not telling you something true.',
                'That language is not a grey area; it is the clearest available signal that the marketing is stronger than the evidence.']),
            ('What actually belongs in the conversation', [
                'If you take a supplement, bring the actual bottle to your appointment so doses and interactions can be checked against your medications.',
                'The risk worth worrying about is not that a supplement does nothing, it is that it does something that conflicts with your care.']),
        ],
        'quote': 'The risk is not that a supplement does nothing, it is that it does something that conflicts with your care.',
        'criteria': [
            ('Evidence strength', 'Look for trials in people, not in cells or animals, and look for replications rather than a single study.'),
            ('Interactions', 'Any supplement that can lower glucose can interact with prescribed medication, so the interaction check is the real question.'),
            ('Third-party testing', 'Independent verification of contents matters because the label is not guaranteed.'),
            ('Claim language', 'Promises of reversal, cure, or replacement of medication should end your interest immediately.'),
        ],
        'fit': [
            ('If your glucose is well managed', 'A supplement adds risk and cost without an obvious benefit worth either.'),
            ('If you are considering stopping medication', 'Do not. That is the single most dangerous reason to buy a supplement.'),
            ('If you already take one', 'Bring the bottle, including the dose, to your next appointment and ask about interactions.'),
            ('If you are on a tight budget', 'Sleep, movement, and food consistency outperform any supplement per dollar spent.'),
        ],
        'checklist': [
            'Bring the actual bottle and label to your next appointment.',
            'Ask about interactions with your specific medications.',
            'Ask whether the evidence is in people or only in cells and animals.',
            'Look for independent third-party testing of contents.',
            'Report any new symptoms after starting a supplement.',
            'Never stop or reduce prescribed medication to replace it.',
        ],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Supplements hub',
            'href': '../supplements.html',
        },
        'disclosure': (
            'How we evaluate supplements: we look at the strength and reproducibility of '
            'human evidence, interaction risk, and whether claims match what is legal to '
            'say. We do not sell supplements, take payment for placement, or recommend '
            'specific brands. Supplement regulation and formulations change, so check the '
            'current situation and your own medications before taking anything.'),
        'side_note': ('Supplements are not regulated like medications, so the label is a '
                      'claim, not a guarantee. Verify the evidence independently, and '
                      'always check interactions with your prescribed care.'),
    },

    'blood-sugar-support-review': {
        'section': 'Independent guide / Blood sugar support formulas',
        'title': 'Blood sugar support formulas: what the label cannot tell you',
        'deck': 'Proprietary blends hide doses, ingredient lists change, and the strongest claims usually have the weakest evidence.',
        'verdict': (
            'A blood sugar support formula is only as good as what it actually contains, '
            'and proprietary blends are designed to keep you from knowing that. If you '
            'cannot see the dose of each ingredient, you cannot evaluate the risk.'),
        'opening': (
            'The supplement drawer fills up for a reason. Blood sugar feels personal, it '
            'changes without warning, and a product that promises steadiness offers '
            'something care does not always feel like it provides. Here is why that '
            'promise is worth examining closely before you spend money on it.'),
        'sections': [
            ('Why proprietary blends hide the useful information', [
                'A proprietary blend lists ingredients but not individual doses, so the ingredient with the most evidence can be present in a trivial amount while the label still features it.',
                'That is a feature of the label, not a flaw, and it is the main reason such products cannot be properly evaluated.']),
            ('Why formulas change without notice', [
                'Because many of these products are regulated as food rather than medicine, formulations can be altered and the version you read about last year may not be the one in the bottle.',
                'A review that describes a formula is describing a moving target, which is another reason to verify the current label yourself.']),
            ('The interaction you are not warned about', [
                'Several common ingredients can lower glucose, and when that effect meets a prescribed glucose-lowering medication, the result can be a low you did not expect.',
                'This is not theoretical, and it is exactly why the conversation with your clinician has to come first.']),
            ('What actually steadies blood sugar', [
                'Consistent meals, daily movement, protected sleep, and taking medication as prescribed are boring, and they are also the things that reliably move the pattern.',
                'None of them comes in a capsule, and all of them are free of interaction risk.']),
        ],
        'quote': 'If you cannot see the dose of each ingredient, you cannot evaluate the risk.',
        'criteria': [
            ('Per-ingredient doses', 'A transparent label shows the amount of every ingredient. A blend does not, and that gap is the whole evaluation.'),
            ('Human evidence', 'Look for trials in people with the actual ingredient at the stated dose, not borrowed from a different extract.'),
            ('Interaction risk', 'Glucose-lowering ingredients plus prescribed medication is the combination that needs professional review.'),
            ('Brand transparency', 'A company that will not tell you what is in the bottle is telling you something anyway.'),
        ],
        'fit': [
            ('If your glucose fluctuates a lot', 'The answer is a conversation about your pattern, not a blend, because the pattern is what your clinician can act on.'),
            ('If you take glucose-lowering medication', 'Interaction risk is the first and last question before adding any formula.'),
            ('If you want to try one anyway', 'Choose full per-ingredient dosing, and bring the bottle to your next appointment.'),
            ('If you are spending real money', 'Compare the cost against what consistent food, movement, and sleep would do for the same pattern.'),
        ],
        'checklist': [
            'Check whether the label shows a dose for every ingredient.',
            'Look for human trials rather than cell or animal studies.',
            'Bring the bottle to your appointment before you start taking it.',
            'Ask specifically about interactions with your medications.',
            'Report unexpected lows or new symptoms promptly.',
            'Keep the original label so you can compare it with the next batch.'],
        'cta': {
            'heading': 'Bring these details to your next visit',
            'body': 'Each item gives your clinician the context needed to turn a general guide into advice that fits your situation.',
            'link': 'Explore the Supplements hub',
            'href': '../supplements.html',
        },
        'disclosure': (
            'How we evaluate formulas: we read labels for per-ingredient dosing, check '
            'whether claims match the available human evidence, and flag interaction risk '
            'with prescribed care. We do not sell these products, take payment for '
            'placement, or rank brands. Formulations change, and so does the evidence, so '
            'treat any evaluation as a point in time.'),
        'side_note': ('A label is a marketing document until proven otherwise. The dose of '
                      'each ingredient is the only part that can be evaluated, and if it is '
                      'missing, so is the evidence.'),
    },
}
