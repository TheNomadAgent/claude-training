PROMPT = """Draft the weekly customer service report from the intake records
below.

Use these headings: On Track, At Risk, Blocked, Proposed
Commitments, Proposed Escalations, Missing Information.

Use only facts in the records. Keep each item's stated status,
owner, blocker and next step. Do not create commitments,
escalations, dates, causes or actions that were not supplied. Put
any blank required field under Missing Information. Mark every
proposed commitment and escalation "Pending service manager
approval".

Intake records:
[paste the completed records here]"""

OUT = """At Risk
- [Work item]: Status: At Risk. Owner: [stated owner].
  Blocker: [stated blocker]. Next step: [stated next step].

Proposed Commitments
- [Stated commitment]. Pending service manager approval.

Missing Information
- [Work item]: next step was not supplied."""

SESSION = {
    "id": 17,
    "slug": "process-improvements",
    "short": "Process improvements",
    "lead": "Adding AI to a messy process gives you a faster messy process. Map what really happens, fix the inputs, and then decide which part a tool should help with.",
    "body": [
        ("h", "Improve the process, not just the tool use"),
        ("p", "A [[process]] is the repeatable sequence of people, information, decisions and tools that produces an outcome. Improving it means changing that sequence to cut effort, delay, error or risk while keeping the controls that good work needs. Claude can support a better process. Dropped into a badly defined one, it makes inconsistent work happen faster."),
        ("p", "Start from the current state, not an imagined ideal. A [[current-state|current-state map]] shows where information starts, who changes it, where it waits, which systems hold it and how exceptions are handled. It also separates work that adds value from work caused by unclear inputs or repeated reformatting."),
        ("pull", "Standardise the work before deciding which parts to assist or automate."),

        ("h", "Worked example: the weekly service report"),
        ("p", "Every Monday a coordinator builds a customer service report from engineers' updates. The updates arrive by chat, by email and in a shared spreadsheet, in whatever form each engineer likes. The coordinator retypes them, picks status labels and rewrites the wording for the customer. The service manager must approve any commitment or escalation before it goes out."),
        ("table", ["Element", "What happens today"], [
            ["Trigger", "The Monday report deadline"],
            ["Intake", "Free-form updates by chat, email or spreadsheet"],
            ["Coordinator's work", "Collects messages, retypes details, chooses labels, rewrites prose"],
            ["Handoffs and systems", "Three intake places, one report document, then the service manager"],
            ["Waiting", "Chasing missing details. Waiting for approval"],
            ["Exceptions", "An update with no status, owner or next step. A proposed commitment or escalation"],
            ["Outcome", "An approved report sent to the customer"],
        ]),
        ("p", "The map records facts without blaming anyone. It shows the coordinator never receives a consistent source record. So any later request for Claude to write the report has to be built on structured, complete inputs, not on guesses about what a vague message meant."),

        ("h", "Find friction and rework"),
        ("p", "[[friction|Friction]] is effort, delay, confusion or failure that makes the process harder. [[rework|Rework]] is work done again because the first version was incomplete, inconsistent or wrong for its next use."),
        ("list", [
            "**Repeated summarising**: the same update is reworded, then reworded again after review.",
            "**Manual reformatting**: details copied from three places into one document.",
            "**Inconsistent labels**: similar situations get different status words because none are defined.",
            "**Missing information**: no owner or next step, so a chase-up cycle starts.",
            "**Double entry**: written once at intake and again in the report.",
            "**Delayed review**: nothing goes out until the service manager has looked.",
        ]),
        ("note", "A control is not waste", "The approval delay may be a deliberate accountability control. The service manager is the person authorised to decide whether a commitment can be made. Removing that review would save time and raise the risk of sending an unsupported promise. Before changing a control, find out why it exists and who is authorised to change it."),

        ("h", "Four kinds of change"),
        ("table", ["Change", "Meaning", "In this report"], [
            ["Elimination", "Stop work that has no purpose", "Drop the duplicate copying once a structured intake is the source"],
            ["Simplification", "Reduce steps, choices or variation", "One intake form and defined status labels"],
            ["Augmentation", "A tool helps a person do judgement-based work", "Claude drafts a faithful report for the coordinator to check"],
            ["Automation", "A system performs a repeatable action with little human involvement", "Completed intake records flow into the report workspace"],
        ]),
        ("p", "These combine, and the order matters. Standardising intake is simplification. It makes [[augmentation]] more reliable because Claude gets consistent fields. [[automation|Automatic]] routing might help afterwards. Routing inconsistent free-form messages faster would fix neither the missing details nor the clashing labels."),

        ("h", "Prioritise by value and safety"),
        ("p", "Rank options on more than time saved: **value** to the report and its readers, **feasibility** with the people and tools you have, **risk** if it goes wrong, **frequency** of the benefit, and **reversibility** if it turns out to be a mistake."),
        ("table", ["Opportunity", "Value", "Feasibility", "Risk", "Reversible", "Priority"], [
            ["Standardise intake fields and labels", "High", "High", "Low", "Yes", "First"],
            ["Claude drafts the report", "High", "High once intake is standard", "Moderate", "Yes", "Second"],
            ["Remove the service manager's approval", "Some time saved", "Not authorised", "High", "Hard to undo", "Do not pursue"],
        ]),

        ("h", "The improved workflow"),
        ("p", "One intake record per work item, with required fields: work item, status, progress this week, blocker, owner, next step, proposed commitment, proposed escalation. Status is limited to On Track, At Risk or Blocked. If a fact is missing, the record says so. Nobody, human or AI, is invited to infer it."),
        ("prompt", "Report drafting prompt", PROMPT),
        ("out", "Shape of the draft", OUT, "good"),
        ("p", "This is not full automation. Engineers still supply the accountable source information. The coordinator checks the draft against the records for faithful grouping, dropped fields and unsupported wording. The service manager reviews everything marked pending and approves, changes or removes it."),

        ("h", "Measure whether it worked"),
        ("p", "Show the improvement against a [[baseline]]: a measure taken before the change. Capture a few weekly cycles under the old process, then the same measures afterwards, comparing like with like."),
        ("table", ["Measure", "Defined as"], [
            ["Coordinator preparation time", "Minutes from collecting updates to submitting a draft for review"],
            ["Missing required fields", "Count of incomplete updates at draft time"],
            ["Revision cycles", "Number of rewrites after the first draft"],
            ["Approval quality", "Commitments or escalations sent back for correction"],
        ]),
        ("p", "Time saved is not enough. A faster process with more missing information or more corrections has moved the work, not improved it."),
    ],
    "takeaways": [
        "Map the current process before changing it: trigger, steps, handoffs, waiting, exceptions and outcome.",
        "Friction and rework are candidates for improvement. Approvals and checks may be controls, not waste.",
        "Elimination, simplification, augmentation and automation solve different problems.",
        "Standardise inputs first. It makes Claude's drafting more dependable and easier to review.",
        "Measure against a baseline, and look at completeness and rework as well as speed.",
    ],
    "practice": "Pick a report or handover your team produces every week. Sketch its current-state map in seven lines. Circle one step that is rework and say which of the four change types would address it.",
    "quiz": [
        {"q": "A team wants to add Claude to a reporting process where updates arrive in three places with no set format. What should happen first?", "options": [
            ("Automate the routing of updates.", False, "Routing inconsistent messages faster does not fix missing details or clashing labels."),
            ("Standardise the intake fields and status labels.", True, "Consistent, complete inputs make any later assistance more reliable and easier to check."),
            ("Have Claude infer the missing details.", False, "That builds guesses into the report."),
            ("Remove the approval step to save time.", False, "The approval is an accountability control."),
        ]},
        {"q": "The report cannot be sent until a manager approves any commitments in it. This adds a day. How should an improvement review treat that step?", "options": [
            ("As waste to remove.", False, "It may be a deliberate control, and the manager holds the authority for commitments."),
            ("As a control. Find out why it exists and who can change it before touching it.", True, "Do not optimise away approvals, privacy protections or quality checks just because they add time."),
            ("As something Claude can do in the manager's place.", False, "Claude cannot hold the manager's authority."),
            ("As irrelevant to the process map.", False, "Waiting and approvals are part of the current state."),
        ]},
        {"q": "Using one intake form with three defined status labels, in place of free-form updates, is an example of which change type?", "options": [
            ("Elimination.", False, "Nothing is being stopped. Variation is being reduced."),
            ("Augmentation.", False, "No tool is assisting a judgement task here."),
            ("Automation.", False, "No system is performing the action without a person."),
            ("Simplification.", True, "It reduces steps, choices and variation."),
        ]},
        {"q": "After a change, the report is produced 30% faster but twice as many items come back from approval for correction. What is the right reading?", "options": [
            ("A clear success.", False, "Speed improved and quality got worse."),
            ("The work has shifted to reviewers. It has not improved overall.", True, "Time saved in one place and added in another is not an improvement."),
            ("The approval step should be removed.", False, "The approval step is what revealed the problem."),
            ("The baseline was wrong.", False, "Nothing suggests the baseline is at fault."),
        ]},
        {"q": "Which TWO belong on a current-state process map?", "multi": True, "options": [
            ("Where work waits, such as for clarification or approval.", True, "Delay often sits in waiting, not in doing."),
            ("How the process should ideally look next year.", False, "That is a future state. The map records what happens now."),
            ("How exceptions are handled.", True, "Exceptions show where the process breaks or needs judgement."),
            ("Which model family to use.", False, "Tool choice comes after the process is understood."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Process improvements", "sub": "Session 17 of 31. Workflow integration and solution design.", "notes": "ITIL people will recognise most of this. The AI-specific point is the order: fix the inputs before adding the tool."},
        {"t": "big", "h": "AI on a messy process gives you a faster messy process.", "p": "Standardise the work before deciding what to assist or automate.", "notes": "Ask for a process where they think AI would just speed up the mess."},
        {"t": "steps", "h": "Map what happens today", "steps": ["Trigger", "Intake", "Work", "Handoffs", "Waiting", "Exceptions", "Outcome"], "notes": "Current state, not ideal state. Record facts, not blame."},
        {"t": "list", "h": "Friction and rework in the weekly report", "items": [
            ("Repeated summarising", "Reworded, then reworded after review."),
            ("Manual reformatting", "Three places copied into one."),
            ("Inconsistent labels", "No defined status words."),
            ("Missing information", "A chase-up cycle every week."),
            ("Double entry", "Written at intake and again in the report."),
        ], "notes": "Then ask: is the approval delay friction? Next slide."},
        {"t": "big", "h": "A control is not waste.", "p": "Before removing an approval, find out why it exists and who is authorised to change it.", "notes": "The manager is the person authorised to make a commitment to the customer. That step costs time on purpose."},
        {"t": "cards", "h": "Four kinds of change", "cols": 2, "cards": [
            ("Elimination", "Stop work with no purpose. Drop the duplicate copying."),
            ("Simplification", "Fewer steps and less variation. One form, three labels."),
            ("Augmentation", "A tool helps a person. Claude drafts, the coordinator checks."),
            ("Automation", "A system does it. Records flow into the report workspace."),
        ], "notes": "The exam asks which type a given change is. Order matters: simplify before you augment."},
        {"t": "list", "h": "Rank by more than time saved", "items": [
            ("Value", "Benefit to the report and its readers."),
            ("Feasibility", "Do you have the people, data and tools?"),
            ("Risk", "What if it goes wrong?"),
            ("Frequency", "How often does the benefit land?"),
            ("Reversibility", "Can you go back?"),
        ], "notes": "Standardise intake first. Claude drafting second. Removing approval: do not pursue."},
        {"t": "ask", "h": "The report is 30% faster. Twice as many items come back from approval. Success?",
         "answer": "No. The work moved to the reviewers. Measure completeness and rework against a baseline, not only speed.",
         "notes": "Four measures: preparation time, missing fields, revision cycles, approval quality."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
