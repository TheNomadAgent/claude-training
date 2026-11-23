RULES = """Routing rules
1. Password reset or account unlock, caller verified:
   Service Desk queue.
2. Software request for an item in the approved catalogue:
   Fulfilment queue.
3. Privileged access request, firewall change, data restore, or
   access to another person's mailbox: Specialist Review queue.
   Do not state that the request will be granted.
4. Conflicting requester, asset or approval details:
   Specialist Review queue.

Pilot ticket T-17
Request: "Please install the PDF editor on my laptop."
Asset record: laptop LT-2231, assigned to the requester.
Catalogue: PDF editor is an approved item."""

PILOT = """Using only the ticket and records supplied:
1. Assign one queue: Service Desk, Fulfilment or Specialist Review.
2. Draft a reply of no more than 60 words.
3. State only facts found in the records.
4. Do not promise access, approve a change or confirm a restore.
5. If a risk trigger or a conflict in the records is present, route
   to Specialist Review and say the request needs review."""

SESSION = {
    "id": 13,
    "slug": "quality-speed-cost",
    "short": "Quality, speed and cost",
    "lead": "There is no best model. There is the cheapest approach that reliably meets what a particular service needs, and you find it by defining the need first and testing second.",
    "body": [
        ("h", "Start with the service requirement"),
        ("p", "A model is only useful when its output meets the needs of a specific service. Before comparing anything, define four things. Together they are the [[service-requirement]]."),
        ("defs", [
            ("Minimum acceptable quality", "What the output has to get right."),
            ("Turnaround", "How quickly it is needed."),
            ("Volume", "How many, how often."),
            ("Consequence", "What happens if an error reaches a customer or a decision maker."),
        ]),
        ("p", "Quality depends on the task. For routine classification it may mean the right queue and a draft with nothing unsupported in it. For a high-consequence exception it may mean recognising uncertainty, keeping the source facts intact and escalating instead of proposing something unsafe. A fluent answer is not an acceptance criterion."),
        ("pull", "Choose the least costly approach that reliably meets the defined service requirement."),

        ("h", "Worked example: service desk triage"),
        ("p", "A service desk lead wants help triaging requests. About 1,800 a month are routine. About 90 are exceptions: privileged access, firewall changes, data restores, access to someone else's mailbox, or records that conflict. Routine tickets need a queue and a first-draft reply within two business hours."),
        ("doc", "Rules and a sample ticket", RULES),

        ("h", "Define acceptance before comparing models"),
        ("p", "[[acceptance-criteria|Acceptance criteria]] let reviewers judge output against evidence. Without them the comparison comes down to one model \"seeming better\"."),
        ("table", ["Work type", "Acceptance criteria", "Consequence of an error"], [
            ["Routine", "At least 95% routed correctly. At least 95% of drafts factually supported. No prohibited commitments. Two-hour turnaround", "Modest. A reviewer corrects the queue or draft before it is sent"],
            ["Exception", "Every listed trigger goes to Specialist Review. No output grants access, approves a change or resolves conflicting records", "High. An unsafe exception costs far more than a routine redo"],
        ]),
        ("p", "For exceptions, a better draft may help the specialist. It does not remove the human decision."),
        ("note", "What quality is not", "A requested heading, a polished tone or a long explanation does not establish quality. Measure against the factual, routing, safety and turnaround criteria for the task."),

        ("h", "Count total cost, not only usage cost"),
        ("p", "What you pay to run the model is one part. [[total-cost|Total cost]] also includes reviewer time, rework after a caught error, delay from slow processing, and the impact of failures that get past review. A cheap model that needs constant correction can be the expensive option. A stronger model can earn its price if it cuts specialist effort or prevents a serious failure."),
        ("p", "For the pilot, reviewer time is costed at $1.00 a minute and a routine correction at $2.00."),
        ("table", ["Cost element", "Faster model", "Higher-capability model"], [
            ["Usage per ticket", "$0.02", "$0.16"],
            ["Average review time", "0.5 minute", "0.4 minute"],
            ["Correction rate in the pilot", "4.5%", "3%"],
            ["Estimated total per routine ticket", "**$0.61**", "**$0.62**"],
        ]),
        ("p", "The usage price differs by a factor of eight. The total differs by one cent. That is why a price-list comparison is not enough. The faster model is right for routine tickets only because the task is constrained, the data is there, and a short review catches errors before a reply goes out. If corrections or review time rise, test again."),

        ("h", "Pilot the same work against one rubric"),
        ("p", "A [[pilot]] should reflect real demand, not one impressive answer. The lead samples 100 routine tickets and 20 exceptions. Both approaches get the same records and the same instructions. Two reviewers score the outputs without knowing which model produced which. That [[blind-comparison]] stops expectations about the \"better\" model from swaying the score."),
        ("prompt", "Pilot instruction", PILOT),
        ("table", ["Pilot result", "Faster model", "Higher-capability model"], [
            ["Routine tickets routed correctly", "95 of 100", "98 of 100"],
            ["Routine drafts factually supported", "96 of 100", "99 of 100"],
            ["Average time to generate", "15 seconds", "45 seconds"],
            ["Exceptions sent to Specialist Review", "16 of 20", "20 of 20"],
            ["Specialist preparation time per exception", "6 minutes", "3.5 minutes"],
        ]),
        ("p", "The faster model meets the routine threshold, just, and stays suitable with review. It fails the exception requirement: four risk-triggering tickets were not escalated. The stronger model handles exceptions better and saves the specialist time. Using it on every routine ticket would add little measurable value."),

        ("h", "Escalation thresholds and tiers"),
        ("p", "The finished design does not ask a model whether a case \"feels difficult\". It uses an [[escalation-threshold]]: any privileged access request, firewall change, restore, access to another person's mailbox, or conflicting field is escalated automatically. So is a routine ticket with required data missing. These are observable conditions a reviewer can audit."),
        ("steps", [
            ("Tier 1: faster model", "Classifies routine tickets and prepares first drafts when the asset record and catalogue entry are present. A reviewer checks before sending."),
            ("Tier 2: higher-capability model", "Prepares a structured summary and draft for escalated tickets, from the supplied records only."),
            ("Tier 3: specialist", "Reviews every escalated ticket and makes any access, change or restore decision."),
        ]),

        ("h", "Keep the decision honest over time"),
        ("p", "A tiered design is not permanent proof the choice is still right. Ticket patterns, policies, data quality, reviewer capacity and model behaviour all move. Keep a sample of reviewed outputs and rerun the same rubric periodically, and always after changing instructions, records or rules."),
        ("p", "Do not pick a model from one demonstration, from maximum capability, or from the lowest listed price. The question is whether the approach meets the service requirement at an acceptable total cost, with the right human review."),
    ],
    "takeaways": [
        "Define quality, turnaround, volume and consequence before comparing models.",
        "Set measurable acceptance criteria. Fluency and polish are not criteria.",
        "Total cost includes review, rework, delay and escaped failures as well as usage.",
        "Pilot on representative work with one rubric, blind where you can.",
        "Tier by risk with observable escalation triggers, and retest when things change.",
    ],
    "practice": "Take one repetitive task your team could hand to an AI tool. Write its four service requirements and two acceptance criteria you could measure. Then list the conditions that should always send a case to a person.",
    "quiz": [
        {"q": "What should be defined before comparing models for a task?", "options": [
            ("Which model is newest.", False, "Newness says nothing about fit for the service."),
            ("Minimum quality, turnaround, volume and the consequence of an error.", True, "These four make up the service requirement that every option is then tested against."),
            ("The listed price per request only.", False, "Usage price is one part of cost and says nothing about quality."),
            ("Which model writes most fluently.", False, "Fluency is not an acceptance criterion."),
        ]},
        {"q": "Model A costs $0.02 per ticket and Model B costs $0.16. After adding review time and corrections, they come to $0.61 and $0.62. What does this show?", "options": [
            ("Model A is always the better choice.", False, "Only for work where it meets the quality bar. The totals are nearly equal."),
            ("Model B is overpriced.", False, "Its total cost is almost the same once review and rework are counted."),
            ("Comparing usage price alone is incomplete. Total cost includes review and rework.", True, "An eightfold price gap shrank to one cent when the cost of human time and corrections was included."),
            ("Review time should be removed to save money.", False, "Review is what makes the cheaper model safe to use."),
        ]},
        {"q": "In a pilot, a faster model routes 95% of routine tickets correctly but sends only 16 of 20 risk-triggering exceptions to specialist review. The requirement is that every exception is escalated. What is the right conclusion?", "options": [
            ("It is suitable for everything, since 95% meets the threshold.", False, "It meets the routine threshold and fails the exception requirement."),
            ("It is unsuitable for anything.", False, "It meets the routine criteria with review in place."),
            ("Lower the exception requirement to 80%.", False, "The requirement reflects the consequence of an unsafe exception. Missing four of twenty is the finding, not a reason to move the bar."),
            ("Use it for reviewed routine work, and send exceptions to a stronger model and a specialist.", True, "A tiered design puts each kind of work where its criteria are met."),
        ]},
        {"q": "Which TWO are good escalation triggers?", "multi": True, "options": [
            ("\"Escalate if the request seems complicated.\"", False, "\"Seems complicated\" is a judgement nobody can audit."),
            ("\"Escalate any privileged access request.\"", True, "It is an observable condition a reviewer can check."),
            ("\"Escalate if the model is not confident.\"", False, "Stated confidence is not a reliable or checkable signal."),
            ("\"Escalate when requester and asset records conflict.\"", True, "A conflict between fields is visible in the data."),
        ]},
        {"q": "Why score pilot outputs without knowing which model produced them?", "options": [
            ("So expectations about a model cannot influence the scores.", True, "A blind comparison keeps reviewers judging the output against the rubric."),
            ("To make the pilot faster.", False, "It does not speed anything up."),
            ("Because reviewers are not allowed to know.", False, "It is a method choice, not a rule about access."),
            ("To hide which model costs more.", False, "Cost is measured separately and openly."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Quality, speed and cost", "sub": "Session 13 of 31. Product and model selection.", "notes": "Session 12 was which family. Today is how you prove the choice with numbers."},
        {"t": "big", "h": "There is no best model.", "p": "There is the cheapest approach that reliably meets what this service needs.", "notes": "Ask who has chosen a tool because a demo looked good."},
        {"t": "cards", "h": "Define the service requirement first", "cols": 2, "cards": [
            ("Quality", "What must the output get right?"),
            ("Turnaround", "How fast is it needed?"),
            ("Volume", "How many, how often?"),
            ("Consequence", "What happens if an error gets through?"),
        ], "notes": "Then turn these into acceptance criteria you can measure. Fluent is not a criterion."},
        {"t": "ask", "h": "Model A is $0.02 a ticket. Model B is $0.16. Which is cheaper?",
         "pre": "                        Model A      Model B\nUsage per ticket         $0.02        $0.16\nReview time              0.5 min      0.4 min\nCorrection rate          4.5%         3%\n\nReviewer time: $1.00 a minute. A correction: $2.00.",
         "answer": "A is $0.61 and B is $0.62 all in. An eightfold price gap becomes one cent once people's time is counted.",
         "notes": "Work it on the board: 0.02 + 0.50 + 0.09, and 0.16 + 0.40 + 0.06."},
        {"t": "list", "h": "Total cost has five parts", "items": [
            ("Usage", "What you pay to run the model."),
            ("Review", "Time a person spends checking."),
            ("Rework", "Fixing errors that were caught."),
            ("Delay", "Slow processing holding things up."),
            ("Escaped failures", "Errors that got past review."),
        ], "notes": "The last one is usually the biggest and the hardest to price."},
        {"t": "ask", "h": "The faster model hit 95% on routine tickets. Good to go?",
         "pre": "                              Faster     Stronger\nRoutine routed correctly      95/100     98/100\nExceptions escalated          16/20      20/20\n\nRequirement: every exception goes to a specialist.",
         "answer": "For routine work with review, yes. For exceptions, no. Four risky tickets slipped through.",
         "notes": "The answer is a tiered design, not picking one winner."},
        {"t": "compare", "h": "Escalation triggers you can audit",
         "left_label": "Cannot be checked", "left": "Escalate if the request seems complicated.\nEscalate if the model is not confident.",
         "right_label": "Observable", "right": "Escalate any privileged access request.\nEscalate any firewall change or data restore.\nEscalate when requester and asset records conflict.\nEscalate when required data is missing.",
         "notes": "If a reviewer cannot look at the ticket and see whether the rule fired, it is not a threshold."},
        {"t": "steps", "h": "Three tiers", "steps": ["Faster model: routine", "Stronger model: prepares exceptions", "Specialist: decides"], "notes": "And retest with the same rubric whenever instructions, records or rules change."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
