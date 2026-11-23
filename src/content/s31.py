TEMPLATE = """Account:
Reporting week:
Measure results: [measure name, value, source reference]
Completed work: [source-supported statements]
Risks or issues: [description and source reference]
Security incident reported: Yes / No
Missing or conflicting information: [describe, or None]"""

INSTR = """Use only the supplied account inputs and approved Project
knowledge.
For each account, produce the required report fields and keep
every source reference.
Do not infer a missing measure, cause, owner, action or date.
Flag for human review when a security incident is reported,
required evidence is missing, or sources conflict.
For routine accounts, return a spreadsheet-ready measure table
and a report-ready narrative under the approved headings."""

SESSION = {
    "id": 31,
    "slug": "optimising-workflows",
    "short": "Optimising workflows",
    "lead": "A faster workflow that produces something nobody can use is not optimised. Get it right first. Then take out the work that never needed doing.",
    "body": [
        ("h", "Optimise for useful results first"),
        ("defs", [
            ("Effectiveness", "The workflow reliably produces an output that serves its purpose, is supported by evidence and gets the review it needs. See [[effectiveness]]."),
            ("Efficiency", "Getting that result with less unnecessary time, cost, duplication and human effort. See [[efficiency]]."),
        ]),
        ("p", "A faster workflow is not optimised if its output cannot be used, introduces unsupported claims or skips a control."),
        ("p", "Look at the workflow end to end: collecting inputs, preparing context, using Claude, checking the result, handing it to the next person, and handling exceptions. A short interaction with Claude can still be a poor process if a colleague has to keep cleaning up the output or rebuilding evidence that was left out."),
        ("pull", "Remove avoidable work. Keep the evidence, the review and the accountability."),
        ("p", "Measure both operations and quality:"),
        ("table", ["Measure", "What it tells you"], [
            ["Turnaround time", "How long it takes from start to finish"],
            ["Total user effort", "How much human time goes in"],
            ["Correction rate", "The share of outputs needing substantive repair"],
            ["Review burden", "Time reviewers spend checking routine work, as opposed to real exceptions"],
            ["Cost", "What the usage costs"],
            ["Failure rate", "How often it produces something unusable"],
            ["User satisfaction", "Whether the people receiving it find it useful"],
        ]),
        ("p", "See [[correction-rate]] and [[review-burden]]."),

        ("h", "Worked example: the weekly patch compliance report"),
        ("p", "Every week you produce a patch compliance report from updates sent in by six customer account teams. The report has a summary per account, a table of agreed measures, stated risks and an appendix of source references. The stable materials are the approved report structure, the measure definitions, the writing standard and the escalation rule. Three things must go to a human reviewer before publication: a reported security incident, missing evidence for a required measure, and a conflict between source updates."),
        ("p", "The baseline process looks like this:"),
        ("list", [
            "A separate chat for each account.",
            "The same stable references uploaded every time.",
            "Updates pasted in whatever format each team used.",
            "Results copied into a spreadsheet and manually reshaped into the report structure.",
            "The most capable model used for everything, including routine formatting.",
            "No defined exception route. If Claude notices a security issue, you have to spot it while assembling the report.",
        ]),
        ("p", "That is repeated context, duplicated transformation, inconsistent input, more capability than the task needs, reformatting downstream, and an unreliable control on the highest-consequence items."),

        ("h", "Find waste without removing controls"),
        ("p", "Map each handoff and ask three questions. What is stable? What changes each cycle? What has to stay visible for review?"),
        ("defs", [
            ("Stable", "The report structure, approved terminology, measure definitions and escalation criteria."),
            ("Changes each cycle", "This week's account updates and the supporting records they cite."),
        ]),
        ("p", "Keeping the two apart ends the repeated uploads and still preserves the evidence for each cycle. The stable material goes into a [[project]] as curated knowledge: selected, maintained references people can inspect and update. It is not an unfiltered archive of every past report."),
        ("p", "A standard [[input-template|input template]] reduces variation before Claude sees anything. It makes omissions visible, supports batching and gives extraction a predictable structure."),
        ("doc", "Standard account input template", TEMPLATE),
        ("p", "A template does not make a claim true because it sits in a required field. The account team still has to supply current source information, and a reviewer still handles the designated exceptions."),
        ("p", "[[batching|Batching]] means processing several similar, low-risk inputs together under the same rules. It suits routine account summaries with complete templates and no security incident, missing evidence or conflict. It is not a reason to mix exceptions in with ordinary work. Exceptions need focused human attention and a clear decision record."),

        ("h", "Task tiers and better handoffs"),
        ("p", "Assign work to tiers by consequence, ambiguity and the reasoning needed. Do not assign by a preference for one model."),
        ("table", ["Tier", "Work", "Control"], [
            ["Low risk", "Extract submitted measures and format complete routine updates", "Completeness check"],
            ["Standard", "Write the consolidated narrative from validated account summaries", "Normal review"],
            ["High consequence", "Ambiguous conflicts, security-related content, material decisions", "Human review, whatever model is used"],
        ]),
        ("p", "Keep the higher-cost capability for work that needs its extra reasoning or synthesis. Routine formatting, field validation and repetitive extraction generally do not. That cuts cost without treating a cheaper model as a substitute for controls. The review requirement follows the consequence of the case, not the price of the model."),
        ("p", "Optimise the downstream handoff too. If the next person needs a spreadsheet-ready measure table and a report-ready narrative, ask for exactly those. Fixed headings and source-reference fields remove the copy, reformat and reconcile work. The output format is an interface between people and steps."),

        ("h", "The redesigned workflow"),
        ("p", "One Project holds the approved report structure, measure definitions, writing standard and escalation rule. Each account sends the standard template with its current evidence."),
        ("prompt", "Project instructions", INSTR),
        ("steps", [
            ("Batch the routine accounts", "Complete templates only, for extraction and formatting."),
            ("Check completeness", "All accounts and all required fields are present."),
            ("Consolidate", "Use the standard tier to write the narrative from the validated summaries."),
            ("Route the flags", "Any flagged account leaves the batch and goes to the designated reviewer with its evidence. It is added back only after that review."),
            ("Approve release", "You confirm completeness and that flags were resolved through the proper route."),
        ]),
        ("table", ["Measure", "Baseline", "Improved"], [
            ["Quality", "Mixed inputs and manual copying cause omissions and inconsistent wording", "Templates, fixed headings and source references support consistent checking"],
            ["Elapsed time", "Repeated uploads, separate transformations and reformatting", "Stable context, batching and ready-to-use output cut routine steps"],
            ["User effort", "You rebuild context and restructure every result", "You focus on validation, exceptions and release"],
            ["Review risk", "Security and evidence issues can be buried in manual consolidation", "Defined flags pull exceptions out for human review before publication"],
        ]),
        ("note", "Optimisation result", "Repeated preparation and rework are gone. Current evidence, traceable sources and human control over exceptions are all still there."),

        ("h", "Keep it working"),
        ("p", "Do not assume the workflow stays effective. Templates drift, measure definitions change, and people start sending incomplete material. Sample the routine outputs, inspect how exceptions were handled, and compare current measures with the baseline. If satisfaction drops or corrections rise, find the failing handoff before changing models or adding more instructions."),
        ("list", [
            "Keep Project knowledge to approved, stable, current references.",
            "Update the input template when an approved report requirement changes.",
            "Test routine and exception inputs separately after changing instructions or templates.",
            "Check that reviewers receive the source evidence they need.",
            "Measure whether the saved effort shows up downstream, not only during Claude use.",
        ]),
    ],
    "takeaways": [
        "Effectiveness comes first. Faster is not better if the result is unsafe, unsupported or unusable.",
        "Separate stable context from what changes each cycle. Reuse the first, supply the second.",
        "A standard input template makes gaps visible and makes batching possible.",
        "Batch routine work. Route security, evidence and conflict exceptions to a human.",
        "Review follows the consequence of the case, not the price of the model. Measure the whole workflow.",
    ],
    "practice": "Map a recurring report you produce. Mark each step as stable context, variable input, transformation, review or handoff. Find one step you repeat every cycle that could be done once.",
    "quiz": [
        {"q": "A redesigned workflow is twice as fast, and reviewers now spend longer fixing unsupported claims in the output. Is it optimised?", "options": [
            ("Yes. Speed is the measure.", False, "Efficiency only counts once the result is useful."),
            ("Yes, provided cost also fell.", False, "Cheap and fast does not help if the output cannot be used."),
            ("No. Effectiveness comes first, and the effort has only moved downstream.", True, "A faster process that produces unusable or unsupported output is not optimised."),
            ("It cannot be assessed.", False, "Correction rate and review burden assess exactly this."),
        ]},
        {"q": "Which material belongs in the Project as stable context, not re-supplied every week?", "options": [
            ("This week's account updates.", False, "Those change every cycle."),
            ("The supporting records for this week's figures.", False, "Current evidence is supplied each cycle."),
            ("The approved report structure and measure definitions.", True, "They stay the same between cycles, so they are curated once and maintained."),
            ("Every past report ever produced.", False, "An unfiltered archive is not curated knowledge."),
        ]},
        {"q": "An account's template reports a security incident. What happens to it?", "options": [
            ("It is batched with the others to keep things moving.", False, "Exceptions need focused attention and are not mixed with routine work."),
            ("It is removed from the batch and sent to the designated human reviewer with its evidence.", True, "A reported security incident is one of the three defined exception conditions."),
            ("It is left out of the report.", False, "It is reviewed and then included, not dropped."),
            ("It is sent to the most capable model in place of a reviewer.", False, "Review follows consequence. A stronger model is not a substitute."),
        ]},
        {"q": "What should decide how much human review a task gets?", "options": [
            ("The price of the model used.", False, "A cheaper or dearer model does not change the consequence."),
            ("How long the output is.", False, "Length is not risk."),
            ("Whether the user is senior.", False, "Seniority is not a risk measure."),
            ("The consequence and ambiguity of the case.", True, "High-consequence work needs human review whatever capability is selected."),
        ]},
        {"q": "Which TWO does a standard input template give you?", "multi": True, "options": [
            ("It makes omissions visible before Claude receives the material.", True, "An empty required field is obvious."),
            ("It makes any statement in a required field true.", False, "A template structures claims. It does not verify them."),
            ("It gives extraction a predictable structure, which supports batching.", True, "Consistent inputs can be processed together under the same rules."),
            ("It removes the need for a reviewer on exceptions.", False, "Designated exceptions still go to a human."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Optimising workflows", "sub": "Session 31 of 31. Troubleshooting and optimisation.", "notes": "Last session of the programme. It pulls together Projects, model choice, templates, handoffs and review."},
        {"t": "cards", "h": "Two words the exam keeps apart", "cols": 2, "cards": [
            ("Effectiveness", "The output serves its purpose, is supported by evidence and gets the review it needs."),
            ("Efficiency", "Getting there with less unnecessary time, cost, duplication and effort."),
        ], "notes": "Effectiveness first. Always."},
        {"t": "big", "h": "Remove avoidable work. Keep the evidence, the review and the accountability.", "p": "Faster is not better if nobody can use the result.", "notes": "If a question offers 'skip the review to save time', it is the wrong answer."},
        {"t": "list", "h": "The weekly patch report, as it is today", "items": [
            ("Six separate chats", "One per account."),
            ("Same references uploaded six times", "Every week."),
            ("Six different input formats", "Whatever each team sent."),
            ("Manual copy into the spreadsheet", "Then reshaped again for the report."),
            ("The biggest model for everything", "Including formatting."),
            ("No exception route", "You have to spot the security incident yourself."),
        ], "notes": "Ask who recognises this. Then ask which one is the dangerous one. It is the last."},
        {"t": "cards", "h": "Stable or variable?", "cols": 2, "cards": [
            ("Stable: put it in the Project", "Report structure, terminology, measure definitions, escalation rule."),
            ("Variable: supply it each week", "This week's account updates and the records they cite."),
        ], "notes": "Curated, not an archive of every old report."},
        {"t": "code", "h": "One template for all six accounts", "label": "Standard input template", "pre": TEMPLATE, "notes": "Gaps become visible. Batching becomes possible. It does not make what is typed in true."},
        {"t": "cards", "h": "Tiers follow consequence", "cols": 3, "cards": [
            ("Low risk", "Extract and format complete routine updates."),
            ("Standard", "Consolidate validated summaries into the narrative."),
            ("High consequence", "Conflicts, security content, material decisions. Human review, whatever the model."),
        ], "notes": "Review follows the consequence of the case, not the price of the model."},
        {"t": "steps", "h": "The redesigned week", "steps": ["Batch routine accounts", "Check completeness", "Consolidate", "Route the flags", "Approve release"], "notes": "Flagged accounts leave the batch, go to a reviewer with evidence, and come back only after review."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
