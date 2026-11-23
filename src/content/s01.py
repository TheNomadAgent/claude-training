RECORD = """Patch cycle status record: November
Approved by the change manager

Completed
- 42 of 46 Windows servers patched and rebooted.
- Post-patch service checks passed on all 42.

Changed
- The remaining 4 servers moved to Sunday 02:00 to 04:00.
- The original window for all 46 was Saturday 22:00 to 02:00.

Unchanged
- The patch compliance report is still due to the customer on Wednesday.

Asked about, nothing recorded
- No reason for moving the 4 servers is recorded.
- No owner for the Sunday window is recorded."""

BAD_OUT = """Patching update

Patching is progressing well. Four servers were deferred {{due to application compatibility issues}} and {{will be completed by the application team}} on Sunday. {{No customer impact is expected.}}"""

GOOD_PROMPT = """Objective
Draft a stakeholder update on the November patch cycle.

Audience
The customer's service owner and their department leads. Not technical.

Source facts
Use only the status record below as the factual basis.

[paste the approved status record here]

Requirements
- Use these headings: Completed, Changed, Unchanged, Not yet known.
- State that 42 of 46 servers are patched and passed service checks.
- State that the remaining 4 moved from the Saturday window to
  Sunday 02:00 to 04:00.
- State that the compliance report is still due on Wednesday.
- Under Not yet known, say that no reason for the move and no owner
  for the Sunday window were recorded.
- Do not add causes, owners, impact statements, dates or next steps
  that are not in the record.
- Plain, factual tone for a routine email. No acronyms.
- Keep it in proportion to the record. Do not pad it."""

TECH = """Using only the information below, write a troubleshooting note.

Observations
After Tuesday's patch reboot, the print spooler service on one print
server stops within two minutes of starting. No event logs supplied yet.

Hypotheses
A printer driver updated by the patch is crashing the spooler.
A stuck job in the spool folder is crashing the spooler.

Verification steps
Check the System and Application event logs for spooler crash entries.
Check the spool folder for old jobs.

Keep observations, hypotheses and verification steps under separate
headings. Do not state a root cause."""

SESSION = {
    "id": 1,
    "slug": "building-effective-prompts",
    "short": "Building effective prompts",
    "lead": "A prompt is a work order. Claude does the job described, using the facts supplied. Whatever you leave out, it fills with something that sounds reasonable.",
    "body": [
        ("h", "Why a short request goes wrong"),
        ("p", "Most requests start as one line: \"Write a stakeholder update.\" That names an activity. It does not say what happened, who will read it, which facts are the approved ones, or what to do when a detail is missing."),
        ("p", "Claude does not know your environment. Given a gap, it will usually write something plausible to fill it, and the result reads just as smoothly as the parts that are true. That is how a [[hallucination]] ends up in a customer email."),
        ("pull", "A polished sentence does not make an unsupported claim reliable."),
        ("p", "An effective [[prompt]] is not a test of whether Claude can guess your business facts. It is a set of directions that turns a general request into a bounded task, with enough information to do the job and nothing extra."),

        ("h", "The six parts of a prompt"),
        ("defs", [
            ("Objective", "The piece of work to produce. \"Draft a status update on the November patch cycle.\" [[objective|What counts as an objective?]]"),
            ("Relevant context", "The project and setting that give the work meaning. [[context|More on context.]]"),
            ("Authoritative inputs", "The facts Claude may use as evidence. They are [[authoritative]] because your prompt says they are."),
            ("Audience", "Who will read it. The [[audience]] decides vocabulary, detail and tone."),
            ("Constraints", "The boundaries: what must not be claimed, what to do with a gap, which terms to use. [[constraint|See constraint.]]"),
            ("Output format", "The layout you want back: headings, a table, a length. [[format|See output format.]]"),
        ]),
        ("p", "These do different jobs, and the exam likes to check that you can tell them apart. An audience is not a format. Asking for a heading called \"Training\" does not give Claude any facts to put under it."),

        ("h", "Worked example: the patching update"),
        ("p", "You run the monthly patch cycle for a customer and need to send a routine update. The change manager has approved this status record."),
        ("doc", "Approved status record", RECORD),
        ("p", "Here is the one-line version of the request, and what comes back."),
        ("prompt", "First attempt", "Write a stakeholder update about this month's patching."),
        ("out", "What Claude returned", BAD_OUT, "bad"),
        ("p", "It reads fine. Three things in it are not in the record: a cause for the deferral, a team that will do the work, and a statement about customer impact. The record says plainly that no reason and no owner were recorded. Claude was never told to respect that."),
        ("p", "Now the same request with all six parts."),
        ("prompt", "Rebuilt prompt", GOOD_PROMPT),
        ("p", "Each line fixes one weakness. The objective names the deliverable. The audience line stops a technical write-up. \"Use only the status record\" sets the [[evidence-boundary]]. The headings make coverage visible at a glance. The \"do not add\" line blocks the usual inventions, and the \"Not yet known\" instruction gives Claude an acceptable thing to do with the gap."),

        ("h", "Three habits that carry over to every prompt"),
        ("steps", [
            ("Label the evidence", "Put source facts in a clearly marked block or attachment and write your instructions outside it. Claude can then tell evidence from directions, and a reviewer can trace each statement back."),
            ("Say what to do with a gap", "Tell Claude how to handle missing information: name it as not supplied and do not speculate. Asking about a topic does not authorise Claude to make up facts about it."),
            ("Make success checkable", "Swap words like \"high quality\" or \"executive-ready\" for an [[observable|observable requirement]]: which sections, what tone, how long. \"Short enough for a routine email\" is useful. An exact word count can cause padding or cuts."),
        ]),

        ("h", "Using examples without boxing Claude in"),
        ("p", "An example helps when a structure or style is hard to describe. A short sample of the heading pattern is quicker than a paragraph explaining it. The risk is a long, detailed example: Claude may copy its wording, order and length instead of adapting to your facts. Use an example to show the form. Do not use it to sneak in content that is missing from the source."),

        ("h", "Mistakes the exam expects you to spot"),
        ("table", ["Mistake", "What it looks like", "Fix"], [
            ["Hidden assumptions", "Expecting Claude to know a fact you did not state", "State every fact that affects the task"],
            ["Conflicting directions", "\"Keep it brief\" and \"include every detail\"", "Say which one wins, or ask for two outputs"],
            ["Undefined acronyms", "OTIF, CAB, RTO with a mixed audience", "Spell it out on first use"],
            ["Vague quality words", "\"Make it executive-ready\"", "Replace with checkable tone, scope and structure"],
            ["Completing an incomplete record", "Asking for a section the source has no facts for", "Tell Claude to label the unknown"],
        ]),

        ("h", "Technical prompts: same rules, tighter boundary"),
        ("p", "For troubleshooting, the evidence boundary needs more care, because a guess that gets written down as fact sends everyone in the wrong direction. Give Claude the affected service, what was observed, what changed recently, which logs exist and how a fix would be verified. Then keep three things apart: what was seen, what might explain it, and how to check."),
        ("prompt", "Troubleshooting prompt", TECH),
        ("p", "This stops a [[hypothesis]] being promoted to a [[root-cause]] before anything supports it. It is the same discipline as the [[diagnostic-loop]]: collect evidence first, reason second."),
    ],
    "takeaways": [
        "State the objective, context, authoritative inputs, audience, constraints and output format.",
        "Keep source facts in a labelled block, separate from your instructions.",
        "Tell Claude what to do when information is missing. Never leave it to fill the gap.",
        "Write requirements a reviewer can check, in place of words like \"good\" or \"polished\".",
    ],
    "practice": "Find a real request you sent to an AI tool this week. Mark which of the six parts it had. Rewrite it with all six and run both versions. Compare what each one made up.",
    "quiz": [
        {
            "q": "A service desk lead prompts Claude: \"Summarise the outage for the customer.\" The summary states a root cause that appears nowhere in the incident notes. Which change most directly prevents this?",
            "options": [
                ("Add \"be accurate and professional\" to the prompt.", False, "These are vague quality words. They give Claude nothing to check against and do not set a limit on what it may claim."),
                ("Paste the incident notes as a labelled source, tell Claude to use only those notes, and tell it to say when a detail was not supplied.", True, "This sets the evidence boundary and gives Claude an acceptable way to handle the gap, so it has no reason to invent a cause."),
                ("Ask for a longer, more detailed summary.", False, "More length does not add evidence. It usually gives Claude more room to fill with plausible material."),
                ("Ask Claude to draw on what usually causes outages like this.", False, "This invites exactly the problem. A typical cause is not this incident's cause."),
            ],
        },
        {
            "q": "Which option correctly separates audience from output format?",
            "options": [
                ("Audience: three short headed paragraphs. Format: professional.", False, "Headed paragraphs describe layout, which is format. \"Professional\" is tone."),
                ("Audience: department leads with no technical background. Format: three short headed paragraphs.", True, "Audience is who reads it. Format is the shape of what they receive. Each is in the right place here."),
                ("Audience: the November patch cycle. Format: an update.", False, "The patch cycle is the subject, and \"an update\" is the objective. Neither names a reader or a layout."),
                ("Audience: use only the status record. Format: no acronyms.", False, "\"Use only the status record\" sets the authoritative input, and \"no acronyms\" is a constraint."),
            ],
        },
        {
            "q": "A prompt says \"Keep it brief\" and also \"Include every detail from the log\". Which TWO changes properly resolve the conflict?",
            "multi": True,
            "options": [
                ("State the priority: \"Keep it brief. If something has to go, keep changes and risks.\"", True, "Telling Claude which instruction wins removes the conflict and makes the trade-off yours, not its guess."),
                ("Leave both in and trust Claude to find a balance.", False, "Claude will pick a balance, but you will not know which details it dropped or why."),
                ("Ask for two outputs: a short summary, plus the full detail as an appendix.", True, "Splitting the deliverable lets both needs be met without either instruction undercutting the other."),
                ("Add \"use your best judgement\".", False, "This restates the problem. The conflict is still there and the priority is still unstated."),
            ],
        },
        {
            "q": "Stakeholders asked for a Training section in a project update. The approved source record contains no training schedule, owner or dates. What is the best instruction to give Claude?",
            "options": [
                ("\"Estimate likely training dates based on the pilot date.\"", False, "An estimate presented in a status update reads as a commitment. Nothing in the record supports it."),
                ("\"Leave the Training section out.\"", False, "Stakeholders asked about it. Dropping it silently hides the gap instead of reporting it."),
                ("\"Under Training, state that no schedule, owner or dates were supplied.\"", True, "The update stays useful and honest. It reports the gap without presenting a guess as a project fact."),
                ("\"Write a short paragraph on why training matters.\"", False, "Filler makes the section look complete while saying nothing about the actual status."),
            ],
        },
        {
            "q": "An engineer tells Claude that a web service returns HTTP 502 after a configuration change. No logs are available yet. Which prompt design is strongest?",
            "options": [
                ("Ask for the single most likely root cause, stated confidently so the team can act.", False, "With no logs there is no evidence for a root cause. Confidence in the wording does not make it one."),
                ("Paste a root cause analysis from a different incident as a template to follow.", False, "A detailed example from another incident tends to bring its content along, not only its layout."),
                ("Ask Claude to review the logs and report what it finds.", False, "No logs were supplied. Claude cannot inspect what it was not given, and may describe log entries that do not exist."),
                ("Have Claude keep observations, hypotheses and verification steps under separate headings, and tell it not to state a root cause.", True, "This keeps what was seen apart from what might explain it, and gives the team checks to run before anyone commits to a cause."),
            ],
        },
    ],
    "deck": [
        {"t": "title", "h": "Building effective prompts", "sub": "Session 1 of 32. Prompting and task execution.",
         "notes": "Set expectations: 20 minutes of slides, then five questions on their phones. Everything today is in section 1 of the handout."},
        {"t": "big", "h": "A prompt is a work order.", "p": "Claude does the job described, with the facts supplied. Whatever you leave out, it fills with something that sounds reasonable.",
         "notes": "Ask who has had Claude or Copilot confidently tell them something wrong. That is nearly always a missing-input problem, not a model problem."},
        {"t": "spot", "h": "Which parts did Claude make up?",
         "left_label": "What it was given", "left": "Prompt: Write a stakeholder update about this month's patching.\n\nRecord\n- 42 of 46 servers patched, checks passed.\n- Remaining 4 moved to Sunday 02:00 to 04:00.\n- Compliance report still due Wednesday.\n- No reason for the move recorded.\n- No owner for Sunday recorded.",
         "right_label": "What came back", "right": BAD_OUT,
         "reveal": "A cause, an owner and an impact statement. None are in the record.",
         "notes": "Give them 30 seconds to call it out before you press next. The point: nothing in the output looks wrong."},
        {"t": "cards", "h": "Six parts turn a request into a task", "cols": 3, "cards": [
            ("Objective", "The deliverable. \"Draft a status update\", not \"patching\"."),
            ("Context", "The project and setting that give it meaning."),
            ("Authoritative inputs", "The facts Claude is allowed to use."),
            ("Audience", "Who reads it. Sets vocabulary, detail and tone."),
            ("Constraints", "What must not be claimed. What to do with a gap."),
            ("Output format", "Headings, table, length. The shape, not the facts."),
        ], "notes": "One press per card. Stress that audience is not format, and a heading does not supply facts for itself."},
        {"t": "compare", "h": "Same request, rebuilt",
         "left_label": "Before", "left": "Write a stakeholder update about this month's patching.",
         "right_label": "After", "right": "Objective: draft an update on the November patch cycle.\nAudience: the customer's service owner. Not technical.\nSource: use only the status record below.\n\nHeadings: Completed, Changed, Unchanged, Not yet known.\nUnder Not yet known, say no reason and no owner\nwere recorded.\nDo not add causes, owners, impact or next steps.\nPlain tone. No acronyms. Do not pad it.",
         "notes": "Walk the right side line by line and name which of the six parts each line is."},
        {"t": "list", "h": "Three habits for every prompt", "items": [
            ("Label the evidence", "Source facts in a marked block. Instructions outside it."),
            ("Say what to do with a gap", "\"State that it was not supplied. Do not speculate.\""),
            ("Make success checkable", "Sections, tone, length. Not \"make it good\"."),
        ], "notes": "These three are the ones that show up in exam scenarios most often."},
        {"t": "ask", "h": "\"Make it executive-ready.\" What would you write instead?",
         "answer": "Something a reviewer can check: \"Three headed paragraphs. Lead with what changed. No acronyms. Under 150 words.\"",
         "notes": "Take two or three answers from the room before revealing."},
        {"t": "code", "h": "Technical prompts: keep three things apart", "label": "Troubleshooting prompt",
         "pre": "Observations\nSpooler stops within two minutes of starting, since\nTuesday's patch reboot. No event logs supplied yet.\n\nHypotheses\nA driver updated by the patch. A stuck job in the spool folder.\n\nVerification steps\nCheck System and Application logs. Check the spool folder.\n\nKeep the three headings separate. Do not state a root cause.",
         "notes": "This is the diagnostic loop in miniature. A guess written down as fact sends the whole team the wrong way."},
        {"t": "list", "h": "Mistakes to spot in exam questions", "items": [
            ("Hidden assumptions", "A fact you knew and did not state."),
            ("Conflicting directions", "\"Brief\" and \"every detail\" with no priority."),
            ("Undefined acronyms", "Spell it out for a mixed audience."),
            ("Vague quality words", "\"Polished\", \"executive-ready\", \"high quality\"."),
            ("Completing an incomplete record", "A section with no facts behind it."),
        ], "notes": "Quick pass. They will see each of these again in the quiz."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. Then go through any question where the room split."},
    ],
}
