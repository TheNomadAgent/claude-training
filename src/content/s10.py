RECORD = """Incident: remote desktop logon disruption

02:10  A certificate was renewed on the remote desktop gateway.
02:25  Logon failures rose. Remote logon was unavailable.
02:40  The incident was declared.
03:05  The on-call engineer rebound the previous certificate.
03:20  Logon failure rates returned to normal.

Confirmed impact
- Remote logon was unavailable from 02:25 to 03:20.
- 310 logon attempts failed in that period.
- No data loss was observed.

Cause status
- The failures began after the certificate renewal.
- Investigation has not confirmed the renewal as the root cause.

Open actions
- Server team: preserve the gateway logs.
- Server team: test the renewed certificate in UAT.
- Incident lead: confirm or revise the cause status after
  investigation."""

PROMPT = """Using only the incident record, create:
1. A short executive brief: impact, recovery, cause status, open
   actions.
2. A checklist for the server team with the open actions only.
3. A structured record for the investigating engineer: timeline,
   impact, recovery, cause status, open actions.

Do not infer a root cause. Say when something is unconfirmed.
Make each output fit its reader."""

BRIEF = """Executive brief

Remote desktop logon was unavailable from 02:25 to 03:20, with 310
failed logon attempts. The on-call engineer rebound the previous
certificate at 03:05 and failure rates returned to normal at 03:20.
No data loss was observed.

The failures began after a certificate renewal on the gateway. The
renewal has not been confirmed as the root cause. Open actions are
log preservation, testing the renewed certificate in UAT, and
confirming the cause after investigation."""

CHECKLIST = """Server team checklist

[ ] Preserve the gateway logs.
[ ] Test the renewed certificate in UAT.
[ ] Incident lead: confirm or revise the cause status after
    investigation."""

SESSION = {
    "id": 10,
    "slug": "human-review-and-format",
    "short": "Human review, audience and format",
    "lead": "How much review an output needs depends on what happens if it is wrong. And the same checked facts can be reshaped for different readers without changing a single one of them.",
    "body": [
        ("h", "Review follows consequence"),
        ("p", "Human review is not one final check applied the same way to everything. How much is needed depends on:"),
        ("list", [
            "the likely impact if the material is wrong,",
            "how sensitive the information is,",
            "whether the resulting action can be reversed,",
            "any regulation that applies,",
            "how new the subject is,",
            "whether it will be published or acted on.",
        ]),
        ("p", "A low-stakes internal draft may only need its author to check the facts. Something that directs recovery work, informs senior decisions or goes outside the company needs more. And the reviewer needs authority over the subject or the decision. Being a good writer is not enough."),
        ("note", "When to step review up", "Increase review when an output can affect people, commitments, safety, compliance, public understanding or a consequential action."),
        ("p", "Some categories need a subject-matter expert before use: legal or regulatory interpretation, health or safety guidance, financial commitments, employment decisions, and factual claims made to people outside the organisation. Claude can help organise the material. It does not replace the responsible authority."),

        ("h", "One validated record, three readers"),
        ("p", "After an overnight incident you have one validated record. Executives, the server team and the investigating engineer all need something from it. Only confirmed facts go in, and nobody states a root cause before the investigation does."),
        ("doc", "Validated incident record", RECORD),
        ("p", "The record keeps evidence apart from interpretation. The timing shows the failures came after the renewal. That is not proof the renewal caused them. You may say the renewal is under investigation. You may not say it caused the outage."),

        ("h", "Editing is not validation"),
        ("p", "Editing improves how something reads: shorter, plainer, decision first, actions as a checklist. [[validation|Validation]] tests whether each claim is supported by an authoritative source that is good enough for the use."),
        ("p", "People mix these up because a polished sentence sounds more credible than its evidence. Changing \"the renewal caused the outage\" to \"the renewal triggered the outage\" is editing. Both are still unsupported. The valid statement is that the failures began after the renewal and the cause is unconfirmed."),
        ("pull", "Clearer wording cannot make an unsupported conclusion valid."),

        ("h", "Adapt four things. Keep the facts."),
        ("table", ["Reader", "What they need"], [
            ["Executives", "Business impact, current status, what is uncertain, decisions or risks needing attention"],
            ["Specialists", "Exact timestamps, observations and status fields"],
            ["Operators", "Ordered actions and a way to mark them done"],
            ["Customers", "Plain language, the impact on them and a next step, without internal detail or unconfirmed causes"],
        ]),
        ("p", "Four things change with the reader: **depth**, **vocabulary**, **tone** and **call to action**. The facts do not. An executive brief can leave out investigation steps because they do not affect the decision in front of that reader. A specialist record keeps them. Neither is allowed to add a claim that is not in the record."),

        ("h", "Pick the format from how it will be used"),
        ("defs", [
            ("Inline answer", "A short, self-contained reply the reader takes in at once. Good for an executive brief or a status message."),
            ("Structured data", "Fixed fields that can be reused, filtered, compared or passed to another system. Good for a specialist record. See [[structured-data]]."),
            ("Artifact", "A more substantial, reusable piece that people work through, revise, share or collaborate on. Good for a maintained checklist. See [[artifact]]."),
        ]),
        ("p", "Format does not reduce the need for review. A tidy table can hold an unsupported statement just as well as a paragraph can. Whatever the format, put the most consequential current information first and label uncertainty where it applies."),
        ("prompt", "Transformation prompt", PROMPT),
        ("out", "Executive brief (inline)", BRIEF, "good"),
        ("out", "Server team checklist (artifact)", CHECKLIST, "good"),
        ("p", "The prompt gives no word count. Useful length depends on the task and the reader, and an arbitrary limit invites padding or cuts."),

        ("h", "Review against one shared rubric"),
        ("p", "Do not pick the version that sounds most confident. Score each output against the same [[rubric]]."),
        ("table", ["Criterion", "Question"], [
            ["Faithfulness", "Does every claim trace to the validated record?"],
            ["Uncertainty", "Is the unconfirmed cause still clearly labelled?"],
            ["Audience fit", "Do depth, language, tone and actions suit the reader?"],
            ["Findability", "Can the reader locate impact, evidence, risk and next actions quickly?"],
            ["Format fit", "Can it be used, reused or worked on as intended?"],
        ]),
        ("p", "Match the reviewer to the output. The incident lead reviews the executive brief. The server team lead reviews the checklist, because that person can confirm the actions are safe and complete. The investigating engineer reviews the specialist record. If the brief were going to customers, review would step up again: someone authorised to speak for the company and the relevant technical authority would both need to approve it."),
        ("note", "Authority check", "A reviewer has to be able to validate the claims and approve their use. A general editor can improve clarity. They cannot confirm technical evidence or authorise an external statement."),
    ],
    "takeaways": [
        "Scale review to impact, sensitivity, reversibility, regulation, novelty and whether it will be published or acted on.",
        "Legal, safety, financial, employment and external factual content needs a subject-matter reviewer.",
        "Editing changes how it reads. Validation checks whether it is supported. One does not replace the other.",
        "For a different reader, change depth, vocabulary, tone and call to action. Never the facts.",
        "Choose inline, structured data or an Artifact from how the output will be used, and review it either way.",
    ],
    "practice": "Take one incident or change you worked on. Write two sentences about it for a manager and two for another engineer. Check that both versions contain the same facts and that neither states a cause you could not prove.",
    "quiz": [
        {"q": "Which factor most strongly signals that a response needs more human review before use?", "options": [
            ("It is well written and neatly formatted.", False, "Presentation is not a risk signal."),
            ("It was generated quickly.", False, "Speed says nothing about what is at stake."),
            ("It could influence safety, commitments or a consequential action.", True, "Review effort should scale with what happens if the output is wrong."),
            ("It uses plain language.", False, "Readability does not raise the stakes."),
        ]},
        {"q": "An incident record says failures began after a certificate renewal and that the cause is unconfirmed. A draft says \"the renewal caused the outage\". An editor changes it to \"the renewal triggered the outage\". What has the edit achieved?", "options": [
            ("It has validated the claim.", False, "No evidence was added. Only a word changed."),
            ("Nothing useful. Both versions state a cause the record does not support.", True, "This is editing, not validation. The supported statement is that failures followed the renewal and the cause is unconfirmed."),
            ("It has made the claim acceptable for executives.", False, "A different audience does not make an unsupported claim acceptable."),
            ("It has turned the claim into an inference.", False, "It is still stated as fact and is not labelled as an interpretation."),
        ]},
        {"q": "When adapting one validated set of facts for executives, specialists and operators, which four things should change?", "options": [
            ("Root cause, chronology, ownership and technical detail.", False, "Root cause and chronology are facts. They stay the same for every reader."),
            ("Evidence standard, source authority, confidence and scope.", False, "These concern what is true and how well supported it is. They do not vary by audience."),
            ("Validation method, review authority, status and impact.", False, "These describe process and consequences, not how a message is tailored."),
            ("Depth, vocabulary, tone and call to action.", True, "These fit a message to its reader without touching the facts."),
        ]},
        {"q": "A server team needs a step-by-step checklist that several people will work through, revise and share over a few days. Which format fits best?", "options": [
            ("An inline answer.", False, "An inline reply is read once. It is a poor home for something revised over days."),
            ("An Artifact.", True, "A substantial, reusable piece of work that people return to, edit and share is what an Artifact is for."),
            ("A one-line status message.", False, "A line of text cannot hold a checklist."),
            ("Structured data, because all shared work belongs in fields.", False, "A procedural checklist is steps to work through, not records to filter."),
        ]},
        {"q": "Which TWO reviewers are appropriate for an operator checklist that tells engineers what to do after an incident?", "multi": True, "options": [
            ("A general editor, to confirm the actions are technically safe.", False, "An editor can improve clarity. They cannot validate technical actions."),
            ("The team lead with authority over that operational work.", True, "They can confirm the actions are safe, complete and theirs to assign."),
            ("Whoever wrote the fastest draft.", False, "Speed of drafting gives no authority to approve."),
            ("A technical specialist for the system involved.", True, "They can check the steps against how the system actually behaves."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Human review, audience and format", "sub": "Session 10 of 32. Output evaluation and validation.", "notes": "Last session in the output evaluation domain. Three ideas today: how much review, who it is for, and what shape it takes."},
        {"t": "big", "h": "Review follows consequence.", "p": "How much checking an output needs depends on what happens if it is wrong.", "notes": "Same logic as change risk: a standard change and a major change do not get the same scrutiny."},
        {"t": "list", "h": "What raises the level of review", "items": [
            ("Impact", "Who or what is affected if it is wrong?"),
            ("Sensitivity", "How sensitive is the information?"),
            ("Reversibility", "Can the resulting action be undone?"),
            ("Regulation", "Does a rule apply?"),
            ("Novelty", "Is the subject new to the team?"),
            ("Publication", "Will it be published or acted on?"),
        ], "notes": "And the reviewer needs authority over the subject. A good writer is not automatically a valid reviewer."},
        {"t": "compare", "h": "Editing is not validation",
         "left_label": "Unsupported", "left": "The certificate renewal caused the outage.\n\nEdited:\nThe certificate renewal triggered the outage.",
         "right_label": "Supported by the record", "right": "Logon failures began after the certificate renewal\non the gateway.\n\nThe renewal has not been confirmed as the root cause.",
         "notes": "Swapping 'caused' for 'triggered' changes a word. It adds no evidence."},
        {"t": "cards", "h": "Change four things. Keep the facts.", "cols": 2, "cards": [
            ("Depth", "How much detail the reader needs for their decision."),
            ("Vocabulary", "Their terms, not yours."),
            ("Tone", "Briefing, instruction or reassurance."),
            ("Call to action", "What you need this reader to do next."),
        ], "notes": "Exam question: which four elements change. Root cause and timeline never do."},
        {"t": "cards", "h": "Pick the format from the use", "cols": 3, "cards": [
            ("Inline answer", "Short and self-contained. Read once. An executive brief."),
            ("Structured data", "Fixed fields to filter, compare or reuse. A specialist record."),
            ("Artifact", "Worked through, revised and shared. A maintained checklist."),
        ], "notes": "A neat table can still hold an unsupported statement. Format does not replace review."},
        {"t": "list", "h": "One rubric for every version", "items": [
            ("Faithfulness", "Every claim traces to the record."),
            ("Uncertainty", "The unconfirmed cause is still labelled."),
            ("Audience fit", "Depth, language, tone and actions suit the reader."),
            ("Findability", "Impact, risk and next actions are easy to find."),
            ("Format fit", "It can be used the way it is meant to be."),
        ], "notes": "Do not pick the version that sounds most confident."},
        {"t": "ask", "h": "Who should review the server team's checklist?",
         "answer": "The team lead with authority over that work, and a specialist for the system. An editor can fix wording. They cannot confirm the steps are safe.",
         "notes": "Then ask: what changes if the executive brief is going to the customer?"},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. This closes the output evaluation domain apart from session 5."},
    ],
}
