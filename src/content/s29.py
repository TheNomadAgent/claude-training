SOURCES = """Backup Operations Standard, effective 1 April 2026
Section 4.2: daily backups of production servers must be retained
for 35 days. This standard replaces earlier retention procedures.

Backup Procedure, revised 15 June 2024
Section 3.1: daily backups of production servers are retained
for 30 days.

Backup team note, 8 April 2026
We have been keeping dailies for 42 days on the new storage
lately.

Original prompt
How long are daily backups of production servers retained?"""

INSTR = """For backup retention questions, treat the current Backup
Operations Standard as authoritative. When sources conflict,
prefer the most recent approved standard in effect. Treat team
notes as non-authoritative context. State the retention period,
name the governing source, and do not infer exceptions that are
not supplied."""

OUT = """Daily backups of production servers must be retained for 35 days,
under Section 4.2 of the Backup Operations Standard, effective
1 April 2026. The team note describes dailies currently being
kept for 42 days. That is not the approved retention requirement."""

SESSION = {
    "id": 29,
    "slug": "diagnosing-poor-outputs",
    "short": "Diagnosing poor outputs",
    "lead": "When Claude gives a bad answer, the instinct is to rewrite the whole prompt. Treat it like any other fault: reproduce it, isolate the cause, change one thing, test again.",
    "body": [
        ("h", "Start with the symptom and the standard"),
        ("p", "An underperforming prompt is not always a badly written prompt. A result can fail because the task is unclear, context is missing, the sources conflict, a source is weak, or the request is beyond what Claude should decide or do. Changing everything at once hides the real cause and makes any improvement impossible to verify."),
        ("p", "Begin by describing the observable [[symptom]]: different answers to the same question, required fields missing, unsupported claims in a summary, the wrong format. Then define [[acceptance-criteria]], the conditions a usable result has to meet. For a factual workplace answer that might be the correct value, a named authoritative source, an explanation of uncertainty where sources disagree, and no invented policy."),
        ("pull", "Diagnose against a defined standard before you change the prompt, the sources or the tool."),
        ("p", "This also stops a wrong default assumption. A poor result does not show that the product has a fault. Most problems can be investigated first through the task, the prompt, the material available and the workflow. Technical escalation is appropriate only after controlled testing shows that configuration and sources do not explain it."),

        ("h", "Worked example: three answers to one question"),
        ("p", "Your team's Project answers internal questions about backups. It holds one current standard, one obsolete procedure and one informal note that disagrees with both. No instruction says which source wins. Asked the same question in separate chats, it gives different answers."),
        ("doc", "What is in the Project", SOURCES),
        ("p", "One chat says 35 days. Another says 30, or describes 42 as the retention period. The outputs conflict, but the conflict was already in the material. The prompt does not say which document governs, whether dates matter, or that an informal practice is different from a required standard."),

        ("h", "Classify the plausible cause"),
        ("p", "Classifying a failure limits unnecessary changes. More than one category can apply. Test the smallest plausible explanation first."),
        ("table", ["Category", "What to inspect", "Typical correction"], [
            ["Unclear task", "Missing outcome, audience, scope or acceptance criteria", "State the deliverable and the decision boundary"],
            ["Missing or conflicting context", "Absent facts, inconsistent documents, competing instructions", "Supply the facts and define source priority"],
            ["Unsuitable format", "Prose where a table, checklist or extraction was needed", "Specify the output structure"],
            ["Poor source quality", "Outdated, informal, incomplete or unapproved material", "Replace, remove or clearly label the source"],
            ["Context overload", "Too much unrelated or duplicated material", "Cut the input back to relevant authoritative evidence"],
            ["Wrong feature or model", "The task needs a different workflow, capability or depth", "Pick a better-suited feature or model"],
            ["Policy restriction or unsupported capability", "A prohibited action, outside access or final authority is being asked for", "Redesign the task and add human review or expertise"],
        ]),
        ("p", "A prompt can have a defect even when Claude is accurately reflecting contradictory sources. And excellent instructions cannot make an obsolete source authoritative. See [[context-overload]] for the fifth row."),
        ("p", "A policy restriction limits what the organisation lets Claude receive, produce or decide. An unsupported capability is something Claude cannot reliably do from the material and access it has, such as verifying an event nobody told it about or giving an approval that needs an authorised person. More forceful wording fixes neither."),

        ("h", "Reproduce before you repair"),
        ("p", "Use a small representative input. The single controlled question is ideal here because it removes everything unrelated. Record the original prompt, the sources available, the output and the acceptance criteria. Run the same test in separate [[fresh-chat|fresh chats]] with the Project configuration unchanged."),
        ("steps", [
            ("Confirm the authoritative answer", "35 days, in the current standard."),
            ("Run the original prompt", "Record the answer and the reasoning it cites."),
            ("Test with the current standard alone", "If it returns 35 days, the question itself is understandable."),
            ("Put the old procedure and the note back", "If the conflict returns, look at currency, authority and missing instructions."),
            ("Apply the smallest correction", "Then rerun the identical prompt."),
        ]),
        ("p", "That order separates prompt clarity from source conflict. Compare a case that worked with one that did not and look at what differed: sources, wording, attachments, format, earlier conversation, instructions. Do not assume a cause because something changed at the same time. Test it directly."),

        ("h", "Apply a narrow correction and retest"),
        ("p", "The controlled tests point to two causes: an obsolete source is still available, and the Project has no authority rule. The 42-day note is not false as a report of what the team is doing. It cannot establish the official requirement. So the narrow fix is to remove the obsolete procedure, keep the note only if it is useful context, and add a short instruction that separates approved standards from informal notes."),
        ("prompt", "Added Project instruction", INSTR),
        ("p", "Then use the **same** test question, not an easier one, and the same rubric: states 35 days, names the current standard, separates the informal practice if it mentions it, invents no exceptions. That is what makes the before and after comparison mean something."),
        ("out", "After the correction", OUT, "good"),
        ("note", "Diagnosis result", "The task was not rewritten. A superseded source was removed and an explicit authority rule was added."),

        ("h", "Know when another response is needed"),
        ("defs", [
            ("Restart", "When the conversation has collected irrelevant instructions or material that interfere with a focused test."),
            ("Replace a source", "When it is obsolete, incomplete or not approved for the decision."),
            ("Update Project instructions", "When a stable rule such as source priority or output format should govern repeated work."),
            ("Choose another feature or model", "When the task needs something different, such as structured extraction in place of open drafting. A different option will not repair weak evidence."),
            ("Ask a human expert", "When the materials do not establish the answer, policy interpretation needs an authorised owner, or an error would be costly."),
            ("Escalate a technical problem", "After a controlled test documents the prompt, sources, configuration, expected result, actual result and repeated behaviour."),
        ]),
        ("p", "That record gives support staff evidence to work with, and stops ordinary prompt or knowledge defects being logged as product failures."),
    ],
    "takeaways": [
        "State the observable symptom and the acceptance criteria before revising anything.",
        "Classify the cause: task, context, format, source quality, overload, fit, or a restriction.",
        "Reproduce with the smallest representative test and keep its inputs.",
        "Make one narrow change and rerun the same test against the same rubric.",
        "A poor answer is not evidence of an outage. Escalate only with a documented, repeatable test.",
    ],
    "practice": "Take a recent AI answer that disappointed you. Write the symptom in one sentence and three acceptance criteria. Then pick the most likely category from the table and the one change you would test first.",
    "quiz": [
        {"q": "A Project gives three different answers to the same factual question in separate chats. What should you do first?", "options": [
            ("Rewrite the whole prompt with more emphasis.", False, "Changing everything at once hides the cause."),
            ("Report a product outage.", False, "A poor result is not evidence of a technical fault."),
            ("Describe the symptom, define what a correct answer must contain, and reproduce it with a controlled test.", True, "Diagnosis starts from an observable symptom and a defined standard."),
            ("Switch to a larger model.", False, "A different model does not repair conflicting sources."),
        ]},
        {"q": "The question returns the right answer when only the current standard is available, and conflicting answers when an obsolete procedure and a team note are added back. What does that show?", "options": [
            ("The question is badly worded.", False, "It worked with the current standard alone, so the question is understandable."),
            ("The cause is the source set and the lack of an authority rule.", True, "The conflict returns with the conflicting sources, which isolates the cause."),
            ("Claude is malfunctioning.", False, "It is reflecting a conflict that exists in the material."),
            ("The team note should become the standard.", False, "An informal note cannot establish the official requirement."),
        ]},
        {"q": "After making a correction, how should you retest?", "options": [
            ("With an easier question, to confirm it works.", False, "An easier question does not show the original defect is fixed."),
            ("With several other changes at the same time.", False, "Then you cannot tell which change helped."),
            ("By reading the instruction again.", False, "Reading is not testing."),
            ("With the identical question and the same rubric.", True, "That is what makes the before and after comparison meaningful."),
        ]},
        {"q": "A request asks Claude to give a final approval that policy reserves for an authorised person. Which diagnosis fits?", "options": [
            ("Unsuitable format.", False, "Changing the layout does not change who may approve."),
            ("Context overload.", False, "The amount of input is not the issue."),
            ("Policy restriction or unsupported capability. Redesign the task and add human review.", True, "More forceful wording cannot fix a request Claude should not fulfil."),
            ("Unclear task. Add more emphasis.", False, "The task is clear. It is one Claude should not perform."),
        ]},
        {"q": "Which TWO belong in the record when you escalate a suspected technical problem?", "multi": True, "options": [
            ("The prompt, sources and configuration used.", True, "Support needs the exact inputs to reproduce it."),
            ("How frustrated you are.", False, "Not evidence."),
            ("The expected result, the actual result and whether it repeats.", True, "That shows what failed and that it is reproducible."),
            ("A guess at which data centre is at fault.", False, "Speculation is not part of a controlled test record."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Diagnosing poor outputs", "sub": "Session 29 of 31. Troubleshooting and optimisation.", "notes": "Final content domain, 10% of the exam. This is the session your team already knows how to do. It is fault-finding."},
        {"t": "big", "h": "Reproduce. Isolate. Change one thing. Retest.", "p": "The same discipline you would use on a server. Do not rewrite the whole prompt.", "notes": "Nobody here rebuilds a server because one service will not start."},
        {"t": "ask", "h": "How long are daily backups of production servers retained?",
         "pre": "Backup Operations Standard, effective 1 April 2026: 35 days\nBackup Procedure, revised 15 June 2024: 30 days\nBackup team note, 8 April 2026: \"keeping dailies for 42 days lately\"",
         "answer": "35 days. The Project gave all three in different chats, because nothing told it which source wins.",
         "notes": "The conflict was in the material before Claude ever saw the question."},
        {"t": "cards", "h": "Symptom first, then the standard", "cols": 2, "cards": [
            ("Symptom", "What you can observe. \"Different answers to the same question in separate chats.\""),
            ("Acceptance criteria", "What a good answer must contain. Correct value, named source, no invented exceptions."),
        ], "notes": "Without acceptance criteria you cannot tell whether your fix worked."},
        {"t": "list", "h": "Seven places the fault can be", "items": [
            ("Unclear task", "State the deliverable."),
            ("Missing or conflicting context", "Supply facts, set source priority."),
            ("Unsuitable format", "Specify the structure."),
            ("Poor source quality", "Replace, remove or label."),
            ("Context overload", "Cut to what is relevant."),
            ("Wrong feature or model", "Choose a better fit."),
            ("Restriction or unsupported capability", "Redesign. Add a human."),
        ], "notes": "Test the smallest plausible explanation first. More than one can apply."},
        {"t": "steps", "h": "The controlled test", "steps": ["Confirm the right answer", "Run the original prompt", "Current standard only", "Add the others back", "Smallest fix, same test"], "notes": "Step 3 clears the prompt. Step 4 convicts the sources."},
        {"t": "code", "h": "The whole fix", "label": "Added Project instruction", "pre": INSTR, "notes": "Plus removing the obsolete procedure. The task itself was not rewritten."},
        {"t": "big", "h": "A bad answer is not an outage.", "p": "Escalate a technical problem only with a documented, repeatable test.", "notes": "Prompt, sources, configuration, expected, actual, repeats. Same as any good ticket."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
