"""Supplements article content."""

SUPPLEMENTS = {
    'berberine-guide': {
        'deck': 'Berberine has some of the most studied evidence among diabetes supplements, with real caveats.',
        'sections': [
            ('What the evidence shows', [
                'Several trials suggest berberine can modestly lower glucose and HbA1c, with effect sizes that are meaningful but not equivalent to prescribed medication.',
                'The evidence base is smaller and shorter than the trials behind approved drugs, which is the honest framing.']),
            ('Why mechanism matters here', [
                'Berberine appears to activate an enzyme involved in cellular energy sensing, which is the same pathway several prescription drugs target.',
                'This is not an inert substance, and that is exactly why it needs the same caution as a drug.']),
            ('The interactions that deserve attention', [
                'Berberine can interact with medications metabolized by the liver, including some antibiotics and blood pressure drugs.',
                'This is why the pharmacy conversation is not optional, even for a naturally occurring compound.']),
            ('The honest bottom line', [
                'It may help some people, it is not a replacement for prescribed care, and it should never be started without telling your clinician.',
                'If you take it, monitoring glucose more closely is how you learn whether it is doing anything.']),
        ],
        'safety': 'Berberine is not a replacement for prescribed medication and can interact with other drugs. Never start it without telling your clinician and pharmacist. Do not stop prescribed medication to take a supplement.',
        'checklist': [
            'Tell your clinician and pharmacist before starting.',
            'Ask about interactions with your current medications.',
            'Do not stop or reduce prescribed medication.',
            'Check glucose more often while taking it.',
            'Report any new symptoms promptly.',
            'Ask your clinician if it is appropriate for you at all.'],
    },
    'chromium-and-blood-sugar': {
        'deck': 'Chromium is heavily marketed for glucose. The evidence is far weaker than the claims.',
        'sections': [
            ('What the evidence shows', [
                'Some studies suggest a modest benefit in glucose metabolism, while others find none. Overall the evidence is mixed and the effects, where present, are small.',
                'This is why strong marketing claims about chromium should be read with suspicion.']),
            ('Why it became popular', [
                'Chromium is involved in insulin action, which is a real biological connection.',
                'A plausible mechanism is not the same as a proven benefit at supplement doses, which is the gap that marketing exploits.']),
            ('The risk profile', [
                'At typical doses it appears safe for most people, but high doses and long-term use have not been well studied.',
                'It can also interact with some medications, including antacids and thyroid drugs.']),
            ('The honest bottom line', [
                'It is unlikely to harm most people and unlikely to transform glucose control either.',
                'The money is better spent on food and activity, which have far stronger evidence.']),
        ],
        'safety': 'This article is educational and is not medical advice. Tell your clinician about any chromium supplement you take, especially if you take thyroid medication or antacids. Do not stop prescribed medication.',
        'checklist': [
            'Tell your clinician about any supplement you take.',
            'Do not expect meaningful glucose changes alone.',
            'Ask about interactions with your medications.',
            'Avoid high doses without clinical reason.',
            'Prioritize food and activity over supplements.',
            'Do not stop prescribed medication.'],
    },
    'cinnamon-and-blood-sugar': {
        'deck': 'Cinnamon is one of the most popular diabetes supplements, and one of the most overrated.',
        'sections': [
            ('What the evidence shows', [
                'Studies are inconsistent. Some show a small effect on fasting glucose, many show none, and the overall quality of the evidence is limited.',
                'This is why cinnamon cannot be recommended as a glucose treatment, regardless of its popularity.']),
            ('Why it remains popular', [
                'It is cheap, pleasant, and natural, and the claims spread faster than the studies that contradict them.',
                'A food-like substance with a plausible story is the perfect condition for exaggerated claims.']),
            ('A safety detail worth knowing', [
                'Cassia cinnamon, the common and cheap variety, contains coumarin, which can harm the liver in higher amounts.',
                'Ceylon cinnamon has far less coumarin, if cinnamon is used at all.']),
            ('The honest bottom line', [
                'Use it as a spice if you enjoy it, not as a treatment.',
                'The glucose benefit, if any, is small enough that it should not change your care plan.']),
        ],
        'safety': 'This article is educational and is not medical advice. Cinnamon is not a treatment for diabetes. If you consume it regularly, prefer Ceylon cinnamon to limit coumarin intake, and tell your clinician about all supplements.',
        'checklist': [
            'Treat cinnamon as a spice, not a treatment.',
            'Prefer Ceylon cinnamon over Cassia if used often.',
            'Tell your clinician about any supplement use.',
            'Do not expect a meaningful glucose effect.',
            'Do not stop prescribed medication.',
            'Report any new symptoms promptly.'],
    },
    'diabetes-supplement-guide': {
        'deck': 'How to evaluate any diabetes supplement, using the same standard you would apply to a drug.',
        'sections': [
            ('Why supplements need the same scrutiny as drugs', [
                'A substance that changes physiology carries risk, whether it is sold as a drug or as a supplement.',
                'This is why the question is always what it does, at what dose, and how it interacts with your care.',
                'Natural does not mean safe, and traditional does not mean proven.']),
            ('What the label does not tell you', [
                'Supplement regulation is weaker than drug regulation in most countries, so contents and doses may not match the label.',
                'Independent testing is the only way to verify what is actually in a product.']),
            ('The red flags that indicate a problem', [
                'Claims that a product will fix the condition, promises of replacing medication, testimonial-driven marketing, and pressure to buy now.',
                'Any of these warrants walking away, regardless of how compelling the story is.']),
            ('The conversation worth having', [
                'Tell your clinician and pharmacist everything you take, including products you assume are harmless.',
                'The interaction risk is real, and it is the main reason supplements belong in the medical record.']),
        ],
        'safety': 'This article is educational and is not medical advice. Never start or stop a supplement without telling your clinician, and never replace prescribed medication with a supplement. Tell your pharmacist about everything you take.',
        'checklist': [
            'List every supplement for your clinician and pharmacist.',
            'Ask what each one actually does at that dose.',
            'Ask about interactions with your medications.',
            'Treat cure claims and urgency as red flags.',
            'Prefer independently tested products.',
            'Never replace prescribed medication.'],
    },
    'fiber-supplements-and-blood-sugar': {
        'deck': 'Fiber supplements are the closest thing to a sensible supplement for glucose, with clear limits.',
        'sections': [
            ('Why fiber is the exception', [
                'Fiber is the part of carbohydrate that does not become glucose, and it slows the absorption of what it travels with.',
                'This is a direct mechanism on post-meal glucose, unlike most supplements with speculative effects.']),
            ('What the evidence supports', [
                'Certain soluble fibers can modestly reduce post-meal glucose and improve cholesterol.',
                'The effect is real but modest, and it works best alongside dietary change rather than instead of it.']),
            ('How to use them sensibly', [
                'Start with a small amount and increase gradually, and take with adequate water.',
                'Taking fiber supplements with medications can reduce their absorption, so timing matters.']),
            ('Why food is still better', [
                'Whole foods provide fiber along with nutrients and satiety, which an isolated powder does not.',
                'Supplements can fill a gap; they cannot replace a diet.']),
        ],
        'safety': 'This article is educational and is not medical advice. Fiber supplements can reduce absorption of some medications, so discuss timing with your pharmacist. Increase intake gradually with adequate water.',
        'checklist': [
            'Ask your pharmacist about timing with medications.',
            'Start small and increase gradually.',
            'Take with adequate water.',
            'Track post-meal readings to see the effect.',
            'Prioritize whole-food fiber sources.',
            'Tell your clinician about all supplement use.'],
    },
    'how-to-evaluate-diabetes-supplements': {
        'deck': 'A practical framework for judging any supplement claim, so marketing stops making the decision.',
        'sections': [
            ('Ask what it claims to do', [
                'Does it claim to lower glucose, cure the condition, or replace medication? The strength of the claim should match the strength of the evidence.',
                'Cure and replacement claims are the clearest signal that a product is being marketed dishonestly.']),
            ('Ask who benefits from the claim', [
                'If the only source of the evidence is the seller, that is not evidence.',
                'Look for independent reviews and trials not funded by the manufacturer.']),
            ('Ask what it might harm', [
                'Every substance that has an effect also has a risk, and interaction with your prescribed medications is the most common one.',
                'A pharmacist is the right person to check this.']),
            ('Ask what you are giving up', [
                'Money and attention spent on a supplement are not spent on food, activity, or care.',
                'This is the most overlooked cost.']),
        ],
        'safety': 'This article is educational and is not medical advice. Never start or stop a supplement without telling your clinician or pharmacist, and never replace prescribed medication with a supplement.',
        'checklist': [
            'Match the claim to the strength of the evidence.',
            'Check who funded the evidence.',
            'Ask your pharmacist about interactions.',
            'Treat cure or replacement claims as red flags.',
            'Consider what else the money could buy.',
            'List every supplement for your clinician.'],
    },
    'magnesium-and-blood-sugar': {
        'deck': 'Magnesium has a real role in glucose metabolism, and correcting a genuine deficiency makes sense.',
        'sections': [
            ('What the evidence shows', [
                'Low magnesium is associated with reduced insulin sensitivity, and correcting a deficiency can improve glucose metabolism.',
                'The key word is deficiency. Supplementing when levels are normal may add little.']),
            ('Who is most likely to be deficient', [
                'People with poor dietary intake, certain medication use, alcohol intake, and some medical conditions.',
                'A blood test is the way to find out, rather than guessing from a list of vague symptoms.']),
            ('What to know about dosing and forms', [
                'Different forms are absorbed differently, and high doses can cause diarrhea and interact with some medications.',
                'More is not better, and the cheapest form is often not the best absorbed.']),
            ('The honest bottom line', [
                'If you are deficient, correcting it is worthwhile. If not, it is an expense without a benefit.',
                'Ask your clinician for a test before supplementing.']),
        ],
        'safety': 'This article is educational and is not medical advice. High magnesium intake can cause diarrhea and interact with medications. Ask your clinician for a test before supplementing, and tell your pharmacist about all supplements.',
        'checklist': [
            'Ask for a magnesium test before supplementing.',
            'Tell your clinician about all supplement use.',
            'Ask your pharmacist about interactions.',
            'Prefer well-absorbed forms if supplementing.',
            'Do not take high doses without reason.',
            'Prioritize magnesium-rich foods.'],
    },
    'omega-3-and-diabetes': {
        'deck': 'Omega-3 is heavily marketed for heart health in diabetes. The evidence is narrower than the claims.',
        'sections': [
            ('What omega-3 actually is', [
                'A type of fat found in oily fish and some plants, with a role in inflammation and heart health.',
                'The body cannot make enough of it, so it must come from food or a supplement.']),
            ('What the evidence shows', [
                'Eating fish is consistently associated with better cardiovascular outcomes, while supplement trials have had mixed results.',
                'This is why the food is better supported than the pill, despite the marketing emphasis.']),
            ('What it does not do', [
                'Omega-3 does not lower glucose or HbA1c in any meaningful way. It is not a diabetes treatment.',
                'Any benefit is to cardiovascular risk, not to glucose itself.']),
            ('The honest bottom line', [
                'If you do not eat fish, a supplement may fill that gap. If you do, the pill adds little.',
                'Discuss it with your clinician, especially if you take blood thinners.']),
        ],
        'safety': 'This article is educational and is not medical advice. Omega-3 can interact with blood-thinning medications. Tell your clinician about all supplement use, and do not stop prescribed medication.',
        'checklist': [
            'Tell your clinician about all supplement use.',
            'Ask about interactions, especially with blood thinners.',
            'Prefer oily fish over supplements if possible.',
            'Do not expect a glucose benefit.',
            'Discuss the right dose if you supplement.',
            'Do not stop prescribed medication.'],
    },
    'supplement-interactions-and-diabetes': {
        'deck': 'The biggest supplement risk is not the supplement. It is how it interacts with your prescribed care.',
        'sections': [
            ('Why interactions are the real risk', [
                'Many supplements are processed by the same liver pathways as prescription drugs, so they can raise or lower drug levels.',
                'This can make a medication too weak to work, or too strong to tolerate.']),
            ('The products that most often cause problems', [
                'Anything marketed for glucose, blood thinning, blood pressure, or energy, and any product with multiple ingredients.',
                'Multi-ingredient blends are the hardest to evaluate because the combined effects are unknown.']),
            ('Why timing can matter', [
                'Fiber supplements and some minerals can reduce absorption of medications taken at the same time.',
                'Spacing doses by a couple of hours is a simple way to avoid this.']),
            ('The conversation that prevents the problem', [
                'Bring every bottle, including products you assume are harmless, to your clinician and pharmacist.',
                'An interaction you mention is one they can manage.']),
        ],
        'safety': 'This article is educational and is not medical advice. Bring every supplement and medication to your clinician and pharmacist for review. Never stop prescribed medication without asking first.',
        'checklist': [
            'Bring every bottle to your clinician and pharmacist.',
            'Ask specifically about interactions.',
            'Ask about timing, not just products.',
            'Be cautious with multi-ingredient blends.',
            'Report new symptoms after starting anything.',
            'Keep the list updated at every visit.'],
    },
    'vitamin-d-and-diabetes': {
        'deck': 'Vitamin D is genuinely important for health. Its role in glucose is weaker than the marketing suggests.',
        'sections': [
            ('What the evidence shows', [
                'Low vitamin D is associated with reduced insulin sensitivity, but supplementing to raise levels has produced inconsistent effects on glucose.',
                'Association and benefit are different things, and this is where most supplement marketing blurs the line.']),
            ('Why testing matters before supplementing', [
                'If you are deficient, correcting it is worthwhile for bone and general health, whatever it does for glucose.',
                'If you are not deficient, supplementation is an expense with unclear benefit.']),
            ('How to get it without a bottle', [
                'Safe sun exposure, oily fish, eggs, and fortified foods. In many climates, winter makes dietary sources important.',
                'Food and sunlight are the sources the body is designed to use.']),
            ('The honest bottom line', [
                'Ask for a test, correct a genuine deficiency, and do not expect a glucose transformation.',
                'This is the sensible version of the vitamin D story.']),
        ],
        'safety': 'This article is educational and is not medical advice. Very high vitamin D intake can cause harm. Ask your clinician for a test before supplementing, and tell them about all supplements you take.',
        'checklist': [
            'Ask for a vitamin D test before supplementing.',
            'Correct a deficiency if one is found.',
            'Do not expect a glucose benefit alone.',
            'Include fish, eggs, and fortified foods.',
            'Avoid very high doses without reason.',
            'Tell your clinician about all supplement use.'],
    },
}
