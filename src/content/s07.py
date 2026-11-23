SHEET = """Monitoring licence comparison sheet

Option A
Monthly cost: $4,500
Licences bought: 150
Covered servers: 150
Cost per covered server: $4,500 / 150 = $30

Option B
Monthly cost: $3,600
Licences bought: 80
Covered servers: 120
Cost per covered server: $3,600 / 120 = $30

Definition: a covered server is a server the monitoring agent
is licensed to run on, whether through its own licence or its
host's licence. It is not the number of licences bought."""

DRAFT = """Choose Option B because it {{covers 150 servers}} for $3,600, or
{{$24 per covered server}}. Option A buys a licence for every server,
while Option B costs less. {{It gives better coverage}} because {{a
covered server counts each licence bought}}. {{This makes it the right
choice.}}"""

CHECK = """Compare the draft recommendation with the licence comparison sheet.
List only:
1. contradictions in numbers or calculations,
2. figures attached to the wrong option,
3. changes to the definition of "covered server",
4. ambiguous references,
5. conclusions the sheet does not support.
Do not recommend an option."""

FIXED = """Option A costs $4,500 a month for 150 licences and covers 150
servers. Option B costs $3,600 a month for 80 licences and covers
120 servers. Each works out at $30 per covered server.

A covered server is one the agent is licensed to run on, through
its own licence or its host's.

The decision owner needs to decide whether covering 30 more servers
under Option A is worth $900 more a month."""

SESSION = {
    "id": 7,
    "slug": "finding-inconsistencies",
    "short": "Finding inconsistencies",
    "lead": "Every sentence can look reasonable on its own while the response as a whole is wrong. This session is about checking how the pieces relate.",
    "body": [
        ("h", "Check relationships, not only facts"),
        ("p", "An [[external-error|external factual error]] is a statement that conflicts with a reliable source outside the response, such as a wrong published price. An internal inconsistency is when parts of the same response, or the response and its own source, disagree with each other. A response can have no external errors at all and still be unreliable."),
        ("p", "A recommendation might quote the right monthly cost in one sentence and work out the wrong unit cost in the next. It might attach one option's figure to the other option's name. These matter because readers act on the final line. They rarely re-check the middle."),
        ("pull", "Every conclusion has to keep the figures, definitions and labels the evidence supplied."),
        ("p", "Checking [[internal-consistency]] means tracing the response from top to bottom. Numbers, units, totals, dates, names, terms and the recommendation all get checked together."),

        ("h", "Worked example: two licensing options"),
        ("p", "A customer has to choose between two monitoring licence options. You did the sums and they are on the sheet below. You ask Claude to review a draft recommendation for consistency. The customer's decision owner makes the choice. You and Claude do not."),
        ("doc", "Source sheet", SHEET),
        ("p", "The sheet separates licences bought from covered servers, and that difference matters. Under Option B a host licence covers every virtual server on that host, so 80 licences cover 120 servers."),
        ("p", "What the sheet supports is limited. Option A covers more servers. Option B costs less per month. Both cost the same per covered server. It does not say which of those the decision owner cares about, so on its own it cannot support a final pick."),

        ("h", "Three defects to look for"),
        ("defs", [
            ("Ambiguous reference", "The reader cannot tell what a word points to. \"It\" after two options is the usual culprit. So is an undefined label like \"better coverage\". [[ambiguous-reference|More.]]"),
            ("Terminology shift", "A key term changes meaning part-way through. Treating covered servers as licences bought still sounds coherent, and it answers a different question. [[terminology-shift|More.]]"),
            ("Unsupported conclusion", "The stated facts do not justify the conclusion. A lower monthly cost does not prove more coverage, or that an option is the right one."),
        ]),

        ("h", "Test the draft against the sheet"),
        ("out", "Draft recommendation", DRAFT, "bad"),
        ("table", ["Defect", "What the draft says", "What the sheet says"], [
            ["Wrong label", "Option B covers 150 servers", "150 belongs to Option A. Option B covers 120"],
            ["Wrong calculation", "$24 per covered server", "$3,600 / 120 = $30"],
            ["Terminology shift", "A covered server counts each licence bought", "A covered server is one the agent is licensed to run on"],
            ["Ambiguous reference", "\"It gives better coverage\"", "\"It\" could be either option, and \"better\" has no measure"],
            ["Unsupported conclusion", "\"This makes it the right choice\"", "No selection criterion is stated"],
        ]),
        ("note", "A correct sum can still be wrong", "$3,600 divided by 150 really is $24. The arithmetic is fine. It is attached to the wrong option, so the result is still false."),

        ("h", "Use Claude for a focused check"),
        ("p", "A short verification prompt points Claude at specific kinds of defect and keeps it out of the decision. Treat what comes back as leads. You still confirm each one against the sheet yourself."),
        ("prompt", "Verification prompt", CHECK),
        ("p", "The repair states the verified comparison and names the open question. It does not invent a service requirement or pick a side."),
        ("out", "Corrected result", FIXED, "good"),

        ("h", "A review routine for anything with options or figures"),
        ("steps", [
            ("Match", "Tie every number to its source value, unit, time period and option label."),
            ("Recalculate", "Redo rates, totals, differences and percentages from the inputs shown."),
            ("Trace terms", "Follow dates, names, headings and defined terms through the whole response."),
            ("Pin down references", "Replace vague pronouns and undefined comparison words with specific ones."),
            ("Test the conclusion", "Does the evidence support it, or does it need a criterion nobody stated?"),
            ("Confirm by hand", "Check reported defects against the source before changing a decision record."),
        ]),
    ],
    "takeaways": [
        "A response can be free of outside errors and still contradict itself or its own source.",
        "Match every figure to its option, unit and period, then recalculate.",
        "Watch for a key term changing meaning while the wording stays similar.",
        "Replace unclear pronouns and undefined comparison words.",
        "If a conclusion needs a criterion the evidence does not state, say so and leave the decision to its owner.",
    ],
    "practice": "Find a comparison or options paper, yours or one an AI tool drafted. Pick one defined term and trace every use of it. Then recalculate one unit cost or percentage from the inputs shown.",
    "quiz": [
        {"q": "A draft defines \"availability\" as scheduled uptime at the start, then later uses the same word to mean uptime including planned outages. What defect is this?", "options": [
            ("An external factual error.", False, "Nothing is being compared with an outside source. The problem is inside the draft."),
            ("A terminology shift.", True, "The same term carries two meanings, so the later reasoning no longer rests on the measure that was defined."),
            ("An ambiguous reference.", False, "It is clear what the word refers to each time. What changed is its meaning."),
            ("A formatting problem.", False, "Layout is not the issue. The definition is."),
        ]},
        {"q": "A draft says \"Option B costs $24 per server\". The source shows $3,600 a month and 120 servers for Option B, and 150 servers for Option A. What has gone wrong?", "options": [
            ("Nothing. $3,600 / 150 = $24.", False, "The division is right. The 150 belongs to the other option."),
            ("The source must be out of date.", False, "There is no reason to doubt the source. The draft disagrees with it."),
            ("A correct calculation has been attached to the wrong option's figure.", True, "The sum uses Option A's server count with Option B's cost, so the result does not describe either option."),
            ("The draft has used the wrong currency.", False, "Nothing suggests a currency issue."),
        ]},
        {"q": "After describing two options, a draft says: \"It provides stronger coverage.\" Which TWO problems does this sentence have?", "multi": True, "options": [
            ("\"It\" could refer to either option.", True, "With two options just mentioned, the pronoun does not identify one."),
            ("The sentence is too short.", False, "Length is not a defect."),
            ("\"Stronger coverage\" has no stated measure.", True, "Stronger by what: more servers, more hours, a different standard? Without a measure the claim cannot be checked."),
            ("It uses the passive voice.", False, "It does not, and voice would not be the problem if it did."),
        ]},
        {"q": "A source compares two plans on price and coverage and says nothing about which matters more. A draft concludes: \"Plan X is cheapest and is therefore the right choice.\" What is the main reasoning problem?", "options": [
            ("The conclusion assumes a selection criterion the evidence does not establish.", True, "Cheapest only means right if cost is the deciding factor, and the source never says it is."),
            ("Price should never be used to compare plans.", False, "Price is a legitimate factor. It is just not shown to be the deciding one."),
            ("The draft contains an external factual error.", False, "The price itself may be perfectly correct."),
            ("The draft is internally inconsistent.", False, "It does not contradict itself. It overreaches."),
        ]},
        {"q": "Which prompt is best for a verification pass on a draft comparison?", "options": [
            ("\"Rewrite this so the recommendation is more decisive.\"", False, "That changes the wording and checks nothing."),
            ("\"Choose the strongest option based on the narrative.\"", False, "That asks for a decision, and from the narrative instead of the source."),
            ("\"Summarise the source and add the priorities needed to justify a choice.\"", False, "Adding priorities invents the criteria the decision should rest on."),
            ("\"Compare the draft with the source. List number contradictions, label mismatches, definition changes, ambiguous references and unsupported conclusions. Do not recommend an option.\"", True, "It names the defect types, ties the check to the source and keeps Claude out of the decision."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Finding inconsistencies", "sub": "Session 7 of 31. Output evaluation and validation.", "notes": "Last session was claims that are not in the source. Today: claims that are in the source and got scrambled on the way through."},
        {"t": "big", "h": "Each sentence can be fine while the whole is wrong.", "p": "Readers act on the last line. They rarely re-check the middle.", "notes": "Think of a change record where the rollback step refers to a server name that is not in the implementation steps."},
        {"t": "code", "h": "The source sheet", "label": "Monitoring licence comparison", "pre": SHEET, "notes": "Point at the definition. 80 licences cover 120 servers under option B because a host licence covers its VMs."},
        {"t": "spot", "h": "Find five defects", "reveal_label": "Five defects:",
         "left_label": "What the sheet says", "left": "Option A: $4,500, 150 licences, 150 covered, $30 each\nOption B: $3,600, 80 licences, 120 covered, $30 each\n\nA covered server is one the agent is licensed\nto run on. It is not the number of licences bought.",
         "right_label": "Draft recommendation", "right": DRAFT,
         "reveal": "Wrong label, wrong sum, changed definition, vague \"it\", and a conclusion with no criterion.",
         "notes": "Let them shout them out. $3,600 / 150 really is $24, which is why it looks right."},
        {"t": "cards", "h": "Three defects with names", "cols": 3, "cards": [
            ("Ambiguous reference", "\"It\" after two options. \"Better coverage\" with no measure."),
            ("Terminology shift", "A defined term quietly changes meaning."),
            ("Unsupported conclusion", "The facts do not get you to the recommendation."),
        ], "notes": "The exam uses these names. Make sure they can tell a terminology shift from an ambiguous reference."},
        {"t": "big", "h": "A correct sum on the wrong option is still wrong.", "p": "Recalculate, and check which option each number belongs to.", "notes": "Wintel version: the right free-space figure against the wrong drive letter."},
        {"t": "code", "h": "Ask Claude to check, not to choose", "label": "Verification prompt", "pre": CHECK, "notes": "Claude's findings are leads. Confirm each against the sheet before touching the decision record."},
        {"t": "steps", "h": "Review routine", "steps": ["Match", "Recalculate", "Trace terms", "Pin references", "Test conclusion", "Confirm"], "notes": "Works on any options paper, AI-written or not."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
