NOTES = """File server migration meeting notes, 14 May

- The migration is 70% complete. Copy testing found orphaned
  permission entries on the legacy shares. The team talked
  through earlier clean-up work and why several share mappings
  were originally chosen.
- Decision: defer the firewall rule review until 28 May.
- Action: prepare remediation options for the orphaned
  permissions. Owner: storage lead. Due: 21 May.
- Risk: if the remediation options are not approved by 21 May,
  migration testing may run past the planned completion date.
- The new monitoring dashboard was demonstrated. No decision or
  action was recorded."""

OLD = """Summarise these meeting notes clearly and thoroughly for the
service managers and the engineering team."""

NEW = """Using only the meeting notes, create two summaries.

Service manager summary:
- Use the headings Decisions, Actions, Risks, Context.
- Include every explicit decision, action, owner, due date
  and risk.
- Limit Context to two bullets at most.

Engineering summary:
- Use the same headings.
- Include brief context that affects current work.
- If a heading has no recorded items, write "None recorded".

Do not infer names, dates, decisions, causes or commitments. For
an action with no owner or due date, write "Not recorded" in
that field."""

CASES = """Case 1: normal
Notes hold one decision, one action with owner and date, one
risk and brief context.
Expected: all fields present. Manager context within two bullets.

Case 2: edge
Notes hold three decisions and two risks, and no actions.
Expected: all decisions and risks present. Actions says
"None recorded".

Case 3: incomplete
Notes hold an action with no owner or due date.
Expected: the action appears. Owner and date are marked
"Not recorded".

Case 4: previously failed
The 14 May notes.
Expected: the deferred firewall review, storage lead, 21 May and
the testing risk all appear. The history is cut to brief context."""

OUT = """Service manager summary

Decisions
- Defer the firewall rule review until 28 May.

Actions
- Prepare remediation options for the orphaned permissions.
  Owner: storage lead. Due: 21 May.

Risks
- If the remediation options are not approved by 21 May,
  migration testing may run past the planned completion date.

Context
- The migration is 70% complete. Copy testing found orphaned
  permission entries on the legacy shares."""

SESSION = {
    "id": 30,
    "slug": "feedback-and-controlled-testing",
    "short": "Feedback and controlled testing",
    "lead": "\"The summary is not useful\" tells you something is wrong. It does not tell you what to change, or how you would know you had fixed it.",
    "body": [
        ("h", "Feedback is evidence, not a revision request"),
        ("p", "Collect evidence before changing a prompt, instruction, source, format, model or review rule. The record should show:"),
        ("list", [
            "the input given to Claude,",
            "the output received,",
            "the behaviour expected,",
            "the actual defect,",
            "the impact on the user,",
            "how often it happens.",
        ]),
        ("p", "Not all feedback carries the same weight."),
        ("defs", [
            ("Factual defect", "A statement that conflicts with the source material supplied."),
            ("Policy defect", "A breach of an explicit handling, approval or formatting rule."),
            ("Stylistic preference", "Tone, length, order or presentation."),
            ("Isolated edge case", "Happens under unusual but legitimate input."),
        ]),
        ("p", "All four can justify an improvement. They should not get the same priority or the same acceptance test."),
        ("pull", "Improve a workflow against repeatable criteria, not against one person's reaction."),

        ("h", "Worked example: one meeting, two audiences"),
        ("p", "You prepare summaries from a recurring migration meeting. Service managers want a short update on decisions, named owners, dates and risks. The engineering team needs the same action information plus brief context for anything that affects current work. Claude must not infer anything that is not in the notes."),
        ("p", "Feedback on three recent summaries: managers say long background paragraphs bury what needs their attention. Engineers say a decision to defer a firewall review was left out, an action had no owner, and a stated due date was missing. Those are different problems. Too much detail is a presentation issue. Leaving out explicit decisions, owners, dates and risks is a completeness defect."),
        ("doc", "Source notes", NOTES),
        ("p", "The notes support only what they say. They name no person, do not say who approves the remediation options, and give no revised completion date. A reliable summary keeps those limits and does not turn likely assumptions into commitments."),

        ("h", "Turn comments into acceptance criteria"),
        ("p", "Vague feedback becomes testable once it describes an observable result. \"Make it shorter\" will not do, because two readers can disagree about whether it is. These are the [[acceptance-criteria]] for this workflow:"),
        ("defs", [
            ("Manager criterion", "No more than two context bullets, and every explicit decision, action, due date and risk is included."),
            ("Engineering criterion", "Labelled Decisions, Actions, Risks and Context sections. Every explicit decision, owner, date and risk appears in the right one."),
            ("Grounding criterion", "Where an owner, date or decision is not in the notes, the summary says it was not recorded or leaves the field out. It never invents one."),
        ]),
        ("p", "The criteria separate defects from preferences. A missing decision fails completeness. Too much background fails length and structure. Whether the heading should be \"Key updates\" in place of \"Context\" can be looked at later. It is not needed to fix what was reported."),

        ("h", "Use a small regression set"),
        ("p", "A [[regression|regression case]] is a saved input with its expected behaviour, used to detect whether a later change breaks something that used to work. A small set is more practical than every past meeting, provided it covers ordinary input and meaningful variations. Always include the case that failed. You cannot call a change a success if the original failure is no longer tested."),
        ("doc", "Regression set", CASES),
        ("p", "The expected result tests behaviour and does not demand an exact sentence. Claude can word things differently and still keep the required facts and structure. Use the same [[rubric]] before and after, or the comparison can hide a trade-off."),

        ("h", "Change one identifiable component"),
        ("prompt", "Original prompt", OLD),
        ("p", "It asks for \"clearly and thoroughly\" and does not distinguish the audiences, require decisions and actions to be extracted, or forbid filling gaps. The narrowest useful change is the prompt itself. The notes, the source authority, the workflow and the reviewer stay the same, so any difference in results can reasonably be put down to the new instruction."),
        ("prompt", "Revised prompt", NEW),
        ("p", "Replacing the prompt, switching model, adding source documents and changing the review step all at once makes the result impossible to diagnose. A model change may be right when a controlled prompt revision cannot meet the requirement. Test it as a separate change with the same regression set."),

        ("h", "Compare results with the same rubric"),
        ("p", "Before the revision, the 14 May output spent several sentences on share mappings and earlier clean-up. It mentioned migration testing and left out the deferred firewall review, the storage lead, the 21 May date and the conditional risk. It failed both audiences' criteria."),
        ("out", "After the revision: service manager summary", OUT, "good"),
        ("p", "It passes the previously failed case. Then run the same rubric over the normal, edge and incomplete cases. The incomplete case matters most: it has to still mark missing fields as not recorded. That is the proof that a stronger extraction instruction has not made Claude start filling gaps."),

        ("h", "Record the limits"),
        ("p", "A passing test set supports a limited conclusion: the revised prompt did acceptably on the saved cases. It does not prove every future summary will be complete. New meeting formats, ambiguous notes and conflicting statements can produce failures the set does not cover."),
        ("list", [
            "Record the source of the feedback, the audience affected, the defect category and the frequency.",
            "Save the old prompt, the revised prompt, the regression cases, the rubric and the results.",
            "Record unresolved limitations, such as summaries depending on incomplete notes.",
            "Roll back if the change creates a more serious omission, unsupported claim or policy issue.",
            "Escalate ambiguous source material or high-consequence decisions to the responsible reviewer.",
        ]),
        ("note", "Risk boundary", "A tighter format improves readability. It cannot fix missing or unclear notes. Human review is still needed when decisions, owners, dates or risks are unclear."),
    ],
    "takeaways": [
        "Capture the input, output, expected behaviour, defect, impact and frequency before changing anything.",
        "Separate factual and policy defects from stylistic preferences and edge cases.",
        "Turn vague comments into observable acceptance criteria.",
        "Test normal, edge, incomplete and previously failed cases with the same rubric before and after.",
        "Change one component at a time, record the limits, and roll back if it makes things worse.",
    ],
    "practice": "Take one piece of vague feedback you have had on a report or summary, such as \"too long\" or \"not clear\". Rewrite it as two acceptance criteria somebody else could check, and describe the four regression cases you would save.",
    "quiz": [
        {"q": "An engineer says a summary left out a decision that was explicitly written in the meeting notes. What kind of feedback is that?", "options": [
            ("A stylistic preference.", False, "It is about missing content, not tone or layout."),
            ("A completeness defect.", True, "An explicit item in the source is absent from the output."),
            ("An isolated edge case.", False, "The input was ordinary."),
            ("Proof the model must be changed.", False, "The cause has not been diagnosed yet."),
        ]},
        {"q": "Which is a usable acceptance criterion?", "options": [
            ("\"Make it shorter.\"", False, "Two readers can disagree on whether it is short enough."),
            ("\"Make it more useful.\"", False, "Nothing here can be observed or checked."),
            ("\"No more than two context bullets, and every explicit decision, action, due date and risk is included.\"", True, "It describes a result somebody can check."),
            ("\"Sound more senior.\"", False, "That is an impression."),
        ]},
        {"q": "Why must the previously failed case stay in the regression set?", "options": [
            ("To make the set look bigger.", False, "Size is not the point."),
            ("Because you cannot call the change a success if the original failure is no longer tested.", True, "The saved case is how you show the reported defect is fixed, and stays fixed."),
            ("Because it is the easiest case to pass.", False, "It is the one that failed."),
            ("To prove every future summary will be right.", False, "A passing set only supports a conclusion about the saved cases."),
        ]},
        {"q": "After tightening the extraction instruction, which case shows Claude has not started inventing missing details?", "options": [
            ("The normal case.", False, "It has nothing missing to invent."),
            ("The edge case with three decisions.", False, "It tests volume and an empty heading, not missing fields."),
            ("The previously failed case.", False, "It tests that the omitted items now appear."),
            ("The incomplete case, where owner and due date must still be marked \"Not recorded\".", True, "If those fields come back filled in, the stronger instruction introduced a new failure."),
        ]},
        {"q": "Which TWO are good practice when improving a prompt from feedback?", "multi": True, "options": [
            ("Change the prompt, the model and the sources together to save time.", False, "You could not tell which change made the difference."),
            ("Change one identifiable component and keep everything else the same.", True, "Then any difference in results can be attributed to that change."),
            ("Use the same rubric before and after.", True, "Otherwise the comparison can hide a trade-off."),
            ("Delete the old prompt once the new one passes.", False, "Keep it. You may need to roll back."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Feedback and controlled testing", "sub": "Session 30 of 32. Troubleshooting and optimisation.", "notes": "Session 29 was diagnosing one bad output. This is improving a workflow without breaking what already works."},
        {"t": "big", "h": "Feedback is evidence, not a revision request.", "p": "\"Not useful\" tells you something is wrong. It does not tell you what to change.", "notes": "Before touching anything, capture: input, output, expected, defect, impact, frequency."},
        {"t": "cards", "h": "Four kinds of feedback", "cols": 2, "cards": [
            ("Factual defect", "Conflicts with the source."),
            ("Policy defect", "Breaks an explicit rule."),
            ("Stylistic preference", "Tone, length, order, presentation."),
            ("Isolated edge case", "Unusual but legitimate input."),
        ], "notes": "Different priority, different test. A missing decision is not the same as 'I prefer bullets'."},
        {"t": "compare", "h": "From comment to criterion",
         "left_label": "What people said", "left": "\"Too much background.\"\n\"It missed the firewall decision.\"\n\"The action had no owner.\"",
         "right_label": "What you can test", "right": "Two context bullets at most.\nEvery explicit decision, action, date and risk included.\nA missing owner or date is marked \"Not recorded\".",
         "notes": "If two people could disagree about whether it passed, it is not a criterion yet."},
        {"t": "list", "h": "A four-case regression set", "items": [
            ("Normal", "One decision, one action, one risk."),
            ("Edge", "Three decisions, two risks, no actions."),
            ("Incomplete", "An action with no owner or date."),
            ("Previously failed", "The 14 May notes."),
        ], "notes": "Always keep the one that failed. Test behaviour, not exact sentences."},
        {"t": "compare", "h": "Change one thing: the prompt",
         "left_label": "Before", "left": OLD,
         "right_label": "After", "right": "Two summaries, same four headings.\nEvery explicit decision, action, owner, date and risk.\nManagers: two context bullets at most.\n\"None recorded\" for an empty heading.\n\"Not recorded\" for a missing owner or date.\nDo not infer anything.",
         "notes": "Notes, sources, model and reviewer unchanged. So the difference is down to the prompt."},
        {"t": "ask", "h": "Which test case shows the fix did not create a new problem?",
         "answer": "The incomplete one. If the missing owner and date come back filled in, the stronger instruction has made Claude start guessing.",
         "notes": "This is what regression means. Fixing omissions must not cause invention."},
        {"t": "big", "h": "Passing four cases proves four cases.", "p": "Record the limits. Keep the old prompt. Roll back if it gets worse.", "notes": "A tidy format cannot fix unclear notes."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
