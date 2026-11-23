RECORD = """Approved criteria
1. Role relevance
2. Feasibility
3. Expected team benefit
4. Budget fit

Application fields
- Certification requested and cost
- Current role and accounts supported
- Why it is needed
- Study plan
- Supporting documents

Not supplied
- Previous funding history
- The applicant's reputation
- Performance ratings
- Whether anyone helped write the application
- Reasons for missing detail"""

BAD = """For each application, give a readiness score from 1 to 5.
Use writing quality, number of attachments, number of
certifications already held, how visible the person is in team
channels, and how sophisticated the study plan looks.
Rank all applications from strongest to weakest and recommend
funding for the top ones."""

GOOD = """Using only the application materials provided, create one
evidence sheet per application. For each approved criterion, list
the relevant submitted evidence and name the field it came from.
Do not score, rank, recommend, or infer the applicant's quality.
Do not use writing style, attachment count, certifications
already held or visibility as criteria. Where relevant
information is absent, write "Not supplied". Use neutral
language."""

FLOW = """1. Claude creates a neutral evidence sheet from each application.
2. A panel member compares each sheet with the original.
3. The panel discusses and applies the four approved criteria.
4. The panel records each decision and the criterion-based reason.
5. Applicants get an outcome notice that explains how AI was used.
6. Applicants can ask for a factual error to be corrected or
   raise a concern about the process. Someone who was not on the
   panel checks the record and documents the response."""

SESSION = {
    "id": 28,
    "slug": "ethics-fairness-and-accountability",
    "short": "Ethics, fairness and accountability",
    "lead": "A score out of five looks objective. Whether it is depends entirely on what went into it, and Claude will happily score things nobody should be scored on.",
    "body": [
        ("h", "Ethics goes beyond compliance"),
        ("p", "Complying with law, policy and approval rules is necessary. It is not the whole ethical test. A process can follow every stated rule and still hand out benefits unfairly, shut out people who cannot use its format, or make a consequential decision impossible to question. Ethical judgement asks whether the process treats the people it affects with care and respect."),
        ("p", "Claude produces text, summaries, classifications and suggested structures from what it is given. It does not hold responsibility for a decision and does not live with the consequences. The people who design, approve and use an AI-assisted process stay accountable for its criteria, its inputs, its decisions and its effects."),
        ("pull", "AI can support judgement. Accountable people make consequential decisions and stand behind them."),
        ("p", "Fairness does not mean treating everyone identically. It means relevant criteria, applied consistently, with attention to unequal barriers, in a process that can notice when neutral-looking rules produce unequal effects. Think also about the people who are not in the room: unsuccessful applicants, the customers a team supports, and the staff who have to explain the outcome."),

        ("h", "Worked example: allocating certification funding"),
        ("p", "A panel has to allocate a limited certification budget across 46 applications from engineers. The panel has asked Claude to organise the submitted evidence before members review each one."),
        ("doc", "What the panel has", RECORD),
        ("p", "Some applications are short, written in a non-standard style or thin on context. Those applicants may have been on call that week, be writing in a second language, or never have filled in a form like this before. The application is the record of what was claimed. It establishes nothing hidden about the applicant's quality or likely success. A polished application may reflect help or practice. A short one may reflect time, language or circumstance, and not a weaker case."),

        ("h", "Proxy criteria create hidden risk"),
        ("p", "A proxy is a stand-in measure used to infer something that was not measured directly. Proxies look objective because they are countable or easy to compare. They can end up measuring access to resources, cultural norms or past advantage in place of the approved criterion. Polished writing is not feasibility. Being loud in the team channel is not expected team benefit."),
        ("prompt", "The panel's first idea", BAD),
        ("p", "This brings in criteria the panel never approved and asks Claude to infer qualities the record does not support. The proxies can disadvantage people with less time, less familiarity with formal writing or a quieter communication style. Missing context makes the inference less reliable, and ranking makes it more likely that an early presentation choice shapes who gets the money."),
        ("note", "Automation bias", "[[automation-bias|Automation bias]] is the tendency to accept a system's recommendation because it looks systematic, polished or numerical. A score and a ranking create confidence that the inputs may not deserve."),

        ("h", "Test the process for fairness"),
        ("p", "Evaluate the workflow, not only individual outputs."),
        ("steps", [
            ("Compare each AI task with the approved criteria", "Claude may extract a cost or find a statement about accounts supported. It should not turn missing information, writing style or visibility into a judgement about readiness."),
            ("Look at who gains and who carries the burden", "A ranking can steer scarce funding to people already able to produce extensive paperwork."),
            ("Check accessibility", "Forms, outcome notices and correction routes should not assume everyone can work through a complex process or write in one preferred style."),
        ]),
        ("p", "[[transparency|Transparency]] matters when AI involvement materially affects what people receive, how they are assessed or how they can respond. How much to disclose depends on what the audience expects, what the rules require and what is at stake. Here applicants should be told that Claude organised the submitted information, that panel members applied the approved criteria, and that no automated ranking decided the awards."),
        ("p", "[[contestability|Contestability]] means a person has a practical way to identify and challenge an error or a process problem. \"Decisions are final\" does not provide one. A real route says what can be corrected, how to raise a concern, who reviews it, and whether that reviewer can change the record or reconsider the decision."),

        ("h", "Use Claude for bounded evidence organisation"),
        ("p", "The narrowest useful change is to take out automated scoring, ranking, recommendation and proxy-based inference. Claude can still save the panel real effort by producing a consistent evidence sheet per application. A blank field or \"Not supplied\" is more accurate than a plausible guess."),
        ("prompt", "Revised prompt", GOOD),
        ("p", "The panel then applies the approved criteria itself. Meaningful [[human-gate|human oversight]] is more than somebody clicking approve. Reviewers need the authority to reject Claude's organisation of the material, access to the original application, enough time to compare the two, and permission to ask for clarification where the process allows it."),
        ("doc", "Revised review workflow", FLOW),
        ("p", "The independent check in step 6 supports accountability, because the person looking at a challenge can examine the evidence and the process. They are not just restating the original result."),

        ("h", "Maintain accountability over time"),
        ("p", "Ethical controls need upkeep. A sound prompt can be changed, reviewers can drift into trusting tidy outputs, and recurring complaints can reveal a barrier nobody anticipated. Keep the approved criteria, prompt, evidence sheets, decision reasons, notices and correction records available for review. Look at correction requests and outcomes for patterns from time to time, and adjust the instructions, the accessibility support or the review practice when the evidence shows the process is not working as intended."),
        ("p", "Accountability cannot be transferred to a prompt, a score or a workflow diagram."),
    ],
    "takeaways": [
        "Compliance is necessary and not sufficient. Also assess fairness, access and the effect on people.",
        "Proxies such as writing polish or visibility measure advantage, not the approved criterion.",
        "Scores and rankings invite automation bias. Remove them when the inputs do not justify them.",
        "Reviewers need the original material, the authority and the time to reject what Claude organised.",
        "Disclose material AI involvement and give people a practical route to correct errors or challenge the process.",
    ],
    "practice": "Think of a decision your team makes about people or priorities, such as who goes on a course or which request is done first. List the approved criteria. Then list two proxies that could creep in if an AI tool were asked to \"rank\" the options.",
    "quiz": [
        {"q": "What is a proxy criterion?", "options": [
            ("A criterion the panel formally approved.", False, "A proxy stands in for an approved criterion. It is not one."),
            ("A stand-in measure used to infer something that was not measured directly.", True, "For example, treating polished writing as if it measured feasibility."),
            ("A backup reviewer.", False, "That is not what the term means here."),
            ("A network device.", False, "Wrong kind of proxy."),
        ]},
        {"q": "A panel wants Claude to score applications from 1 to 5 using writing quality and number of attachments, then rank them. What is the main problem?", "options": [
            ("Claude cannot produce numbers.", False, "It can. That is exactly the danger."),
            ("Five points is too few for a scale.", False, "The scale is not the issue."),
            ("It uses criteria nobody approved, which can disadvantage people with less time or writing experience, and a ranking invites automation bias.", True, "The proxies measure resources and style, and the score makes them look objective."),
            ("It would take too long.", False, "Speed is not the concern."),
        ]},
        {"q": "Which statement best describes meaningful contestability?", "options": [
            ("\"All decisions are final.\"", False, "That closes off any challenge."),
            ("\"Contact us if you have questions.\"", False, "It names no route, reviewer or possible outcome."),
            ("The process says what can be corrected, how to raise it, who reviews it and whether they can change the outcome.", True, "A practical route is specific about each of those."),
            ("Applicants can read the prompt that was used.", False, "That may help transparency. It is not a way to challenge an error."),
        ]},
        {"q": "Which TWO are required for human oversight to be meaningful?", "multi": True, "options": [
            ("Access to the original application, not only Claude's sheet.", True, "The reviewer must be able to compare the summary with the source."),
            ("A reviewer who signs off quickly so the process is not delayed.", False, "Speed without scrutiny is a rubber stamp."),
            ("Authority to reject what Claude produced.", True, "Without the power to reject, the review changes nothing."),
            ("A numerical score to make the decision easier.", False, "A score invites automation bias."),
        ]},
        {"q": "A process follows every stated policy rule. Is it therefore ethical?", "options": [
            ("Yes. Compliance is the complete test.", False, "Compliance is necessary and not sufficient."),
            ("Yes, provided AI was involved.", False, "AI involvement does not make a process fair."),
            ("Only if everyone was treated identically.", False, "Fairness needs relevant criteria and attention to unequal barriers, not identical treatment."),
            ("Not necessarily. It can still distribute benefits unfairly, exclude people or be impossible to question.", True, "Ethical judgement looks at the effect on people, beyond whether the rules were followed."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Ethics, fairness and accountability", "sub": "Session 28 of 31. Governance and responsible use.", "notes": "Last governance session. The scenario is deliberately close to home: who gets the cert budget."},
        {"t": "big", "h": "AI can support judgement. People make the decision and stand behind it.", "p": "Following the rules is necessary. It is not the whole test.", "notes": "A process can be compliant and still unfair, inaccessible or impossible to challenge."},
        {"t": "code", "h": "The panel's first idea", "label": "Proposed prompt", "pre": BAD, "notes": "Ask the room what is wrong before moving on. Every input here is a proxy."},
        {"t": "list", "h": "What those inputs really measure", "items": [
            ("Writing quality", "Time, practice, first language."),
            ("Number of attachments", "Admin effort."),
            ("Certifications already held", "Past opportunity."),
            ("Visibility in team channels", "Personality and shift pattern."),
            ("Sophisticated study plan", "Experience with forms like this."),
        ], "notes": "None of these is role relevance, feasibility, team benefit or budget fit."},
        {"t": "big", "h": "A score looks objective. That is the problem.", "p": "Automation bias: accepting a recommendation because it looks systematic or numerical.", "notes": "Once the ranked list exists, the panel will anchor on it."},
        {"t": "compare", "h": "Same tool, different role",
         "left_label": "Claude judges", "left": "Score each application 1 to 5.\nRank strongest to weakest.\nRecommend funding for the top ones.",
         "right_label": "Claude organises", "right": "One evidence sheet per application.\nEvidence listed under each approved criterion.\n\"Not supplied\" where it is missing.\nNo score, rank or recommendation.",
         "notes": "The admin saving is still there. The decision stays with the panel."},
        {"t": "cards", "h": "Two things applicants are owed", "cols": 2, "cards": [
            ("Transparency", "Tell them Claude organised the information, people applied the criteria, and no automated ranking decided anything."),
            ("Contestability", "What can be corrected, how to raise it, who reviews it, and whether they can change the result."),
        ], "notes": "'Decisions are final' is not contestability."},
        {"t": "ask", "h": "What makes human oversight more than clicking approve?",
         "answer": "Authority to reject the output, the original material, enough time, and the ability to ask for clarification.",
         "notes": "Same test as session 25."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
