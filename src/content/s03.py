PROCEDURE = """Approved procedure: requesting privileged server access

1. Requests for privileged access must be raised through the access portal.
2. Requests sent by email or chat will not be actioned.
3. If the portal is unavailable, an engineer may request emergency
   access by phoning the service desk.
4. The duty manager may review the stated reason when considering an
   emergency request. Approval is discretionary."""

P0 = """Write a short, plain-language notice for application teams, based only
on the approved procedure. Professional, helpful tone."""

D0 = """Raise privileged access requests through the access portal. Requests
sent by email or chat will not be actioned."""

P1 = """Keep the tone and the two accurate statements. Add that if the portal
is unavailable, an engineer may request emergency access by phoning the
service desk. Do not imply that a request will be approved."""

D1 = """Raise privileged access requests through the access portal. Requests
sent by email or chat will not be actioned. If the portal is unavailable,
you may request emergency access by phoning the service desk."""

P2 = """Keep every fact in the current draft. Make it clearer for readers
outside IT: use short sentences and say "will not be processed" in
place of "will not be actioned". Do not add any new facts."""

P3 = """Keep the current wording and all approved facts. Use two headings to
separate the standard rule from emergency requests. State that the duty
manager may review the stated reason and that approval is discretionary.
Do not add eligibility criteria."""

D3 = """How to request privileged access

Raise your request through the access portal. Requests sent by email
or chat will not be processed.

If the portal is unavailable

You may request emergency access by phoning the service desk. The duty
manager may review the reason you give. Approval is discretionary."""

RUBRIC = """Compare the current draft against this rubric:
- States the portal requirement
- States what happens to email and chat requests
- Includes the emergency route when the portal is unavailable
- Does not promise approval
- Separates the standard rule from the discretionary review
List any criterion that is not met and quote the relevant draft text."""

SESSION = {
    "id": 3,
    "slug": "iterating-prompts",
    "short": "Iterating prompts",
    "lead": "The first response is a draft to inspect. Work out what is actually wrong with it before you change a word of the prompt.",
    "body": [
        ("h", "Prompting is a feedback loop"),
        ("p", "A useful piece of work with Claude often takes more than one request. The first response gives you something concrete to assess. It is not a reason to bin the task and start again."),
        ("steps", [
            ("Request", "Ask for a draft."),
            ("Inspect", "Read it against the task and the source."),
            ("Diagnose", "Name the main weakness."),
            ("Revise", "Change the instruction to address that weakness."),
            ("Compare", "Check the new version against the old one and your criteria."),
        ]),
        ("p", "[[iteration|Iteration]] does not mean piling on instructions until the answer looks longer or shinier. Each revision should address a gap you observed. That protects the parts that already work, makes changes easy to review, and lowers the chance that a sweeping new request brings in unsupported content or drops a requirement."),
        ("pull", "Diagnose the output before you decide how to revise the prompt."),
        ("p", "It also leaves a trail. You can say why each change was asked for and whether it worked. That matters most when the result is going to a customer."),

        ("h", "Worked example: the access notice"),
        ("p", "You need to turn an approved internal procedure into a short notice for a customer's application teams. The notice must not change approved facts, must not suggest an exception is automatic, and must not present a discretionary review as a guaranteed service."),
        ("doc", "Approved procedure", PROCEDURE),
        ("p", "A request for plain language is fine. Plain language still has to keep four different things apart: a mandatory rule, a consequence, a route that is available, and a decision somebody may or may not make in your favour."),
        ("prompt", "First prompt", P0),
        ("out", "First draft", D0, ""),

        ("h", "Diagnose the actual defect"),
        ("p", "The draft is short, professional and fully supported by the procedure. Its [[defect]] is completeness. It leaves out the emergency route, so an engineer facing a portal outage gets no hint that there is another way."),
        ("p", "Before editing, classify the problem. The type tells you the fix."),
        ("table", ["Defect type", "How you recognise it", "What fixes it"], [
            ["Missing context", "Claude lacked background it needed", "Supply the background"],
            ["Unclear success criteria", "The draft is reasonable but not what you wanted", "State checkable requirements"],
            ["Wrong format", "Right content, wrong shape", "Specify the layout"],
            ["Wrong tone", "Right content, wrong voice for the reader", "Name the audience and tone"],
            ["Unsupported claims", "Statements with no basis in the source", "Restate the evidence boundary"],
            ["Knowledge gap", "The source does not contain the answer", "Get the fact from whoever owns it"],
        ]),
        ("p", "A [[knowledge-gap]] is the one people misdiagnose. If the material you supplied does not contain the answer, asking Claude to be more detailed or more creative cannot produce it. It can only produce a guess."),
        ("p", "Here the source does contain the missing fact. So this is not a knowledge gap, and it is not tone or format either. The first prompt simply never required every material point to be covered."),
        ("note", "Diagnosis first", "Do not fix a completeness problem by adding unrelated requests about style, length or creativity."),
        ("p", "Good feedback names the weak area and the change you want: \"Separate the mandatory rule from the discretionary review.\" Feedback like \"Make it better\" gives no standard. Claude may change wording, length or tone and leave the real problem untouched."),

        ("h", "Revise one thing at a time"),
        ("p", "The conversation already holds the procedure and a sound first draft, so a [[follow-up|follow-up prompt]] is the efficient move. Say what to keep, then state the one change."),
        ("prompt", "Revision 1: fix completeness", P1),
        ("out", "Second draft", D1, ""),
        ("p", "The exception is in, and the rule and consequence are unchanged. The next weakness is clarity for the audience: \"actioned\" is service-desk language."),
        ("prompt", "Revision 2: fix clarity", P2),
        ("p", "One problem remains. The procedure says the duty manager *may* review the reason and that approval is discretionary. The notice must not turn that into a promise."),
        ("prompt", "Revision 3: separate the rule from the discretion", P3),
        ("out", "Final draft", D3, "good"),
        ("p", "Three rounds, three named defects, and nothing that was correct got disturbed along the way. Whether the notice is fit to send is still your decision, not Claude's."),

        ("h", "Use a rubric to compare"),
        ("p", "A [[rubric]] turns \"is this good?\" into a list of visible checks. Ask Claude to compare the draft against it and quote the text it relied on. Then look yourself. Claude can point out apparent omissions and unclear wording. It does not replace the judgement needed to approve a customer communication."),
        ("prompt", "Rubric check", RUBRIC),

        ("h", "Follow up, or start again?"),
        ("table", ["Follow up when", "Start a new conversation when"], [
            ["The conversation holds reliable source material", "Old drafts keep leaking into new answers"],
            ["Your instructions have stayed consistent", "Replaced or conflicting instructions are piling up"],
            ["You are changing one thing in a sound draft", "Corrections stop sticking"],
        ]),
        ("p", "That second column describes [[context-drift]]. When you restart, give the new conversation the authoritative source, the current draft if it is worth keeping, and the exact goal. A restart clears clutter. It does not supply facts the source never had."),
    ],
    "takeaways": [
        "Inspect and classify the problem before you revise. The defect type tells you the fix.",
        "Change one thing per round, and say explicitly what to keep.",
        "A knowledge gap is fixed by supplying the fact, never by asking for more detail.",
        "Use a rubric to compare drafts, then check it yourself. Approval stays with a person.",
        "Follow up while the context is sound. Start fresh when it has drifted.",
    ],
    "practice": "Take a draft an AI tool gave you that was not quite right. Write down the single main defect and its type from the table. Then write a follow-up that names what to keep and the one change to make.",
    "quiz": [
        {
            "q": "A draft notice is accurate and concise, but it leaves out an exception that is clearly stated in the source you supplied. What kind of defect is this?",
            "options": [
                ("A knowledge gap.", False, "A knowledge gap means the source does not contain the answer. Here it does."),
                ("A completeness defect: the prompt did not require every material point to be covered.", True, "The fact was available and simply was not asked for. A targeted follow-up fixes it."),
                ("A tone defect.", False, "The tone was described as professional and suitable. Nothing about voice is wrong."),
                ("An unsupported claim.", False, "Everything in the draft is supported. The problem is what is absent, not what is asserted."),
            ],
        },
        {
            "q": "Which follow-up is most likely to fix that draft without damaging the parts that work?",
            "options": [
                ("\"Make it better.\"", False, "This names no defect and no standard. Claude may change tone or length and still omit the exception."),
                ("\"Rewrite it from scratch with more detail.\"", False, "A full rewrite puts the correct sentences at risk and invites extra content the source does not support."),
                ("\"Keep the tone and the two accurate statements. Add the emergency route. Do not imply approval.\"", True, "It preserves what is sound, names the one change and guards against the obvious overclaim."),
                ("\"Be more creative.\"", False, "Creativity is not what a policy notice is missing, and it encourages invention."),
            ],
        },
        {
            "q": "The notice needs to state how quickly emergency requests are answered. The approved procedure does not say. What should you do?",
            "options": [
                ("Ask Claude for a more detailed draft.", False, "Detail cannot come from nowhere. Claude would have to make a figure up."),
                ("Start a new conversation and try again.", False, "A restart clears clutter. It does not add a fact the source never contained."),
                ("Ask Claude what response time is typical for this kind of request.", False, "A typical figure is not your organisation's commitment, and publishing it would create one."),
                ("Get the figure from whoever owns the procedure, or have the notice say it is not specified.", True, "This is a knowledge gap. The only real fix is to supply the fact or report its absence."),
            ],
        },
        {
            "q": "Which TWO situations are good reasons to start a new conversation instead of sending another follow-up?",
            "multi": True,
            "options": [
                ("Several instructions have been replaced and now conflict with each other.", True, "Conflicting directions in the history make focused revision unreliable. A clean start with the current instructions fixes that."),
                ("One sentence is missing from an otherwise sound draft.", False, "That is exactly what a narrow follow-up is for. The context is fine."),
                ("Claude keeps bringing back wording from old drafts after being corrected.", True, "That is context drift. The accumulated drafts are steering the output."),
                ("The source document lacks a fact you need.", False, "A new conversation will have the same gap. The fact has to be supplied."),
            ],
        },
        {
            "q": "You ask Claude to compare a draft against a five-point rubric. It reports that all five criteria are met. What is the right next step?",
            "options": [
                ("Send the draft. It passed.", False, "Claude's assessment is an aid. Approval of a customer communication stays with a person."),
                ("Check the text Claude quoted against each criterion yourself, then decide.", True, "The rubric makes the checks visible so that you can verify them. The judgement is still yours."),
                ("Drop the rubric next time, since Claude handles it.", False, "The rubric is what makes the comparison reviewable. Removing it removes your standard."),
                ("Ask Claude to assess it again until it finds a problem.", False, "Repeating the request without a reason invites invented faults. Verify the evidence instead."),
            ],
        },
    ],
    "deck": [
        {"t": "title", "h": "Iterating prompts", "sub": "Session 3 of 32. Prompting and task execution.",
         "notes": "Recap: session 1 was building the prompt, session 2 was splitting the job. Today is what you do when the first answer is nearly right."},
        {"t": "big", "h": "Diagnose the output before you touch the prompt.", "p": "The first response is a draft to inspect. It is not a verdict on the task.",
         "notes": "Same instinct as troubleshooting: do not change three things at once and hope."},
        {"t": "steps", "h": "The loop", "steps": ["Request", "Inspect", "Diagnose", "Revise", "Compare"],
         "notes": "Most people skip straight from Request to Revise. The two in the middle are the skill."},
        {"t": "ask", "h": "This draft is accurate and concise. So what is wrong with it?",
         "pre": "Procedure\n1. Requests must be raised through the access portal.\n2. Requests by email or chat will not be actioned.\n3. If the portal is unavailable, an engineer may request\n   emergency access by phoning the service desk.\n4. The duty manager may review the reason. Approval is\n   discretionary.\n\nFirst draft\nRaise privileged access requests through the access portal.\nRequests sent by email or chat will not be actioned.",
         "answer": "Completeness. The emergency route is missing. The source had it, the prompt never required it.",
         "notes": "Push them to name the type, not just the missing sentence."},
        {"t": "cards", "h": "Name the defect, and the fix follows", "cols": 3, "cards": [
            ("Missing context", "Supply the background."),
            ("Unclear criteria", "State checkable requirements."),
            ("Wrong format", "Specify the layout."),
            ("Wrong tone", "Name the reader and the voice."),
            ("Unsupported claims", "Restate the evidence boundary."),
            ("Knowledge gap", "Get the fact from its owner. Rewording will not help."),
        ], "notes": "Linger on knowledge gap. Asking for more detail when the source lacks the answer just produces a guess."},
        {"t": "compare", "h": "Feedback Claude can act on",
         "left_label": "No standard", "left": "Make it better.",
         "right_label": "Names what to keep and what to change", "right": "Keep the tone and the two accurate statements.\nAdd that if the portal is unavailable, an engineer may\nrequest emergency access by phoning the service desk.\nDo not imply that a request will be approved.",
         "notes": "Three parts: preserve, change, guard."},
        {"t": "list", "h": "Three rounds, one defect each", "items": [
            ("Completeness", "Add the emergency route."),
            ("Clarity", "\"Will not be processed\" for readers outside IT."),
            ("Rule versus discretion", "Headings that keep \"must\" apart from \"may\"."),
        ], "notes": "Nothing that was already right got disturbed. That is the benefit of narrow revisions."},
        {"t": "code", "h": "Turn \"is it good?\" into checks", "label": "Rubric check", "pre": RUBRIC,
         "notes": "Claude quotes its evidence so you can verify it. A pass from Claude is not approval."},
        {"t": "cards", "h": "Follow up, or start again?", "cols": 2, "cards": [
            ("Follow up", "The source is in the conversation, your instructions are consistent, and you are changing one thing."),
            ("Start again", "Old drafts keep leaking back in, or instructions conflict. Bring the source, the current draft and the exact goal."),
        ], "notes": "A restart clears clutter. It does not create facts the source never had."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. Question 3 is the knowledge gap one. Worth a discussion."},
    ],
}
