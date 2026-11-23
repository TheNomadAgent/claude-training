POLICY = """Server Backup Standard, 5.2 Restore testing

Each team that operates production servers must complete a
quarterly restore test.

The test record must identify each server by hostname, name the
backup job used, and state whether the restore succeeded. The team
lead must keep the record for 24 months.

When a restore fails, the team lead must notify the backup service
owner using the internal incident form."""

OUT = """Under Server Backup Standard {{5.2(b)}}, teams operating production
servers must complete a quarterly restore test. Records must list
hostnames, backup job names and restore results, and must be kept
for 24 months.

Failed restores must be reported to the backup service owner
{{within 5 business days}} through the internal incident form.
{{Failure to comply may result in an audit finding and monthly
testing, because untested backups have historically caused data
loss.}}

Inference: The requirement likely applies only to servers that hold
customer data.

Unresolved question: Does "quarterly" mean a calendar quarter or
every 90 days?"""

FIXED = """Teams that operate production servers must complete a quarterly
restore test. The test record must identify each server by hostname,
name the backup job used, and state whether the restore succeeded.
The team lead must keep the record for 24 months.

When a restore fails, the team lead must notify the backup service
owner using the internal incident form.

Inference, not a policy statement: Teams may need a way to collect
backup job names before the test so the record can be completed.

Unresolved question: Does "quarterly" mean a calendar quarter or
every 90 days? The excerpt does not define the term."""

SESSION = {
    "id": 6,
    "slug": "detecting-hallucinations",
    "short": "Detecting hallucinations",
    "lead": "Most of a generated summary can be right while one invented deadline rides along with it. The job is to check each claim against the source, not to judge how the whole thing sounds.",
    "body": [
        ("h", "What makes a claim unsupported"),
        ("p", "A [[hallucination]] is generated content presented as fact without adequate support. Whether it sounds reasonable is irrelevant. Whether it is written formally is irrelevant. Whether it might be true somewhere else is irrelevant. The only test is whether the authoritative material you have supports the statement, at the strength and level of detail used."),
        ("p", "In business work these slip into summaries, reports and policy explanations. A summary can state the main rule correctly and add a deadline, a clause number, a penalty or a reason that nobody supplied. That is what makes it risky: nearly all of it checks out."),
        ("pull", "Specificity requires specific evidence."),
        ("p", "Some kinds of claim deserve a closer look because their precision makes them feel authoritative:"),
        ("list", [
            "exact citations and clause numbers",
            "quotations",
            "statistics and dates",
            "names",
            "product capabilities",
            "legal or policy provisions",
            "causes and reasons",
        ]),
        ("p", "Saying a rule exists is one claim. Saying it sits in subsection (b), carries a set penalty and exists for a stated reason is four claims, and each needs its own support."),

        ("h", "Worked example: the restore testing summary"),
        ("p", "You have been asked to check a Claude-written summary before it goes to team leads. This excerpt is the only source you were given, so it is the [[evidence-boundary]]. Common practice and sensible guesses do not count."),
        ("doc", "Source excerpt", POLICY),

        ("h", "Classify each claim"),
        ("p", "Do not form a general impression. Sort every statement into one of four groups."),
        ("defs", [
            ("Supported", "Stated in the source, or an accurate restatement of it."),
            ("Unsupported", "Adds a fact, condition or level of certainty the source does not establish. See [[unsupported-claim]]."),
            ("Inference", "A reasoned interpretation. Acceptable when it is labelled as one. See [[inference]]."),
            ("Unresolved question", "Something the source does not answer. See [[unresolved|unresolved question]]."),
        ]),
        ("p", "Warning signs: a detail you cannot find in the source, wording that differs from the source's own terms, a citation that does not lead to the text it claims, and certainty where the evidence is incomplete."),
        ("out", "Summary to review", OUT, "bad"),
        ("table", ["Claim", "Verdict", "Why"], [
            ["Quarterly restore test for teams with production servers", "Supported", "Stated in the excerpt"],
            ["Record fields and 24-month retention", "Supported", "Stated in the excerpt"],
            ["Section 5.2(b)", "Unsupported", "The source shows 5.2 and no subsection (b)"],
            ["Report within 5 business days", "Unsupported", "No deadline appears anywhere"],
            ["Audit finding and monthly testing", "Unsupported", "No consequence is stated"],
            ["Untested backups have caused data loss", "Unsupported", "A cause presented as history, with nothing behind it"],
            ["Applies only to servers with customer data", "Inference", "Not in the source, and correctly labelled"],
            ["Calendar quarter or every 90 days?", "Unresolved question", "The source uses the word without defining it"],
        ]),
        ("p", "The causal claim is the most dangerous of the four. It reads like background everyone knows, and it gives the rule a reason the policy owner never gave."),

        ("h", "Confidence is not verification"),
        ("p", "Asking Claude whether it is confident checks nothing. Confidence wording is more generated text. It is not a source, a citation check or a policy review. A response can sound certain while resting on an invented detail, and a hedged response can be a perfectly accurate restatement."),
        ("steps", [
            ("Find the source wording", "For each factual statement, locate the exact text that supports it."),
            ("Check the detail", "Does the source support the scope, timing, consequence and cause as claimed?"),
            ("Follow citations", "Confirm a clause number points to the text it is attached to."),
            ("Remove what has no basis", "Take out invented deadlines, penalties and reasons."),
            ("Label the rest", "Mark interpretations as inferences. Keep open questions open."),
            ("Escalate meaning", "Send unresolved questions about what the policy means to whoever owns it."),
        ]),

        ("h", "Fix it without filling the gaps"),
        ("p", "The corrected version keeps everything supported, removes the invented specifics and leaves the uncertainty where a reader can see it. It does not swap one guess for another."),
        ("out", "Revised summary", FIXED, "good"),
        ("note", "Removing beats softening", "\"May be subject to a penalty\" is still an unsupported claim. If nothing supports a detail, take it out. Hedged wording does not make it true."),
        ("p", "Those details may well exist in another document. If so, get that document before treating its contents as established."),
    ],
    "takeaways": [
        "Check each claim against the authoritative source. Do not rate the response as a whole.",
        "Citations, dates, numbers, names, penalties and causes need direct support.",
        "Sort statements into supported, unsupported, inference and unresolved question.",
        "Confidence wording is not evidence. Verify against the source.",
        "Remove unsupported detail. Do not soften it or replace it with a different guess.",
    ],
    "practice": "Take a summary an AI tool wrote for you from a document. Pick the three most specific details in it (a number, a date, a clause or a reason) and find the exact source wording for each. Note any you cannot find.",
    "quiz": [
        {"q": "A Claude-written policy summary cites \"section 7.4(c)\". The policy excerpt you supplied shows section 7.4 with no subsections. How should the citation be classified?", "options": [
            ("Supported, because section 7.4 exists.", False, "The section exists. The subsection does not, and the citation claims it does."),
            ("An inference, because subsections are common in policies.", False, "What policies commonly contain is not evidence about this one, and the citation was not labelled as an inference."),
            ("Unsupported, because the source does not contain that subsection.", True, "A citation has to resolve to the text it points to. This one adds detail the source does not have."),
            ("An unresolved question.", False, "An unresolved question is something the summary leaves open. Here it asserts a specific reference as fact."),
        ]},
        {"q": "Which statement in a generated summary is acceptable even though the source does not state it?", "options": [
            ("\"Late reports attract a $500 penalty.\"", False, "A specific penalty stated as fact with no source basis is an unsupported claim."),
            ("\"Inference, not policy: teams will probably need a shared template for the record.\"", True, "It is clearly labelled as an interpretation, so a reader will not mistake it for the policy text."),
            ("\"The rule was introduced after several failed audits.\"", False, "This asserts a history and a cause the source does not give."),
            ("\"Reports are due within 10 business days.\"", False, "A precise deadline needs precise support. None was supplied."),
        ]},
        {"q": "You ask Claude how confident it is in a summary, and it replies that it is highly confident. What does that tell you?", "options": [
            ("The summary has been verified.", False, "Nothing has been compared with the source."),
            ("Only the uncertain parts need checking.", False, "The response did not identify any, and unsupported details are often stated most confidently."),
            ("The summary is probably accurate enough for internal use.", False, "Confidence wording does not measure accuracy at any level of use."),
            ("Nothing about accuracy. Confidence wording is generated text, not evidence.", True, "Verification means checking each claim against the authoritative source."),
        ]},
        {"q": "Which TWO kinds of detail most need direct evidence, because their precision makes them sound authoritative?", "multi": True, "options": [
            ("A stated cause for why a rule exists.", True, "Causal explanations read as settled background and are a common place for invention."),
            ("A sentence that restates the main rule in plain words.", False, "A faithful restatement is supported by the source."),
            ("An exact deadline or clause number.", True, "Specific figures and references look checked. They need to actually be checked."),
            ("A heading that organises the summary.", False, "A heading is layout, not a factual claim."),
        ]},
        {"q": "A summary contains a penalty amount that does not appear in the source. What is the best correction?", "options": [
            ("Remove it. The detail may exist elsewhere, but this source does not establish it.", True, "Taking it out is more accurate than keeping it in any form without evidence."),
            ("Change it to \"may be subject to a penalty\".", False, "Softer wording still asserts a penalty the source never mentions."),
            ("Replace it with a more typical amount.", False, "That swaps one invention for another."),
            ("Leave it and add a note that Claude is confident.", False, "A confidence note adds no support."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Detecting hallucinations", "sub": "Session 6 of 32. Output evaluation and validation.", "notes": "This domain is 21% of the exam, the biggest one. Today is the skill most of them already half-do: spotting what Claude made up."},
        {"t": "big", "h": "Specificity requires specific evidence.", "p": "A clause number, a deadline, a penalty and a reason are four separate claims. Each one needs its own support.", "notes": "The risk is that most of the summary is right, so the invented parts ride along."},
        {"t": "list", "h": "Details that sound checked and often are not", "items": [
            ("Citations and clause numbers", "Does it lead to that text?"),
            ("Dates and statistics", "Is the figure in the source?"),
            ("Names and capabilities", "Who said it can do that?"),
            ("Causes and reasons", "Did the source give a why?"),
        ], "notes": "Ask for an example of each from something an AI tool has told them."},
        {"t": "spot", "h": "What did Claude add?",
         "left_label": "Source excerpt", "left": POLICY,
         "right_label": "Generated summary", "right": "Under Server Backup Standard {{5.2(b)}}, teams must complete a\nquarterly restore test. Records must be kept for 24 months.\n\nFailed restores must be reported {{within 5 business days}}.\n{{Failure to comply may result in an audit finding and monthly\ntesting, because untested backups have historically caused\ndata loss.}}",
         "reveal": "A subsection, a deadline, a consequence and a cause.",
         "notes": "Give them a minute. The cause is the one people miss, because it sounds like common knowledge."},
        {"t": "cards", "h": "Sort every statement into one of four", "cols": 2, "cards": [
            ("Supported", "In the source, or an accurate restatement."),
            ("Unsupported", "Adds a fact, condition or certainty the source lacks."),
            ("Inference", "An interpretation. Fine when it is labelled as one."),
            ("Unresolved question", "The source does not answer it. Leave it open."),
        ], "notes": "A labelled inference is not a hallucination. An unlabelled one is."},
        {"t": "ask", "h": "\"I am highly confident in this summary.\" What does that tell you?",
         "answer": "Nothing about accuracy. Confidence wording is more generated text. Check each claim against the source.",
         "notes": "This comes up directly in exam questions."},
        {"t": "compare", "h": "Fixing an unsupported detail",
         "left_label": "Softened", "left": "Failure to comply may be subject to a penalty.",
         "right_label": "Removed", "right": "When a restore fails, the team lead must notify the backup\nservice owner using the internal incident form.\n\nUnresolved question: Does \"quarterly\" mean a calendar\nquarter or every 90 days?",
         "notes": "Hedging keeps the invention. Removing it is the accurate fix."},
        {"t": "steps", "h": "Claim by claim", "steps": ["Find wording", "Check detail", "Follow citations", "Remove", "Label", "Escalate"], "notes": "Escalate means: questions about what the policy means go to whoever owns the policy."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
