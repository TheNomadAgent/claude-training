STANDARD = """Privileged Access Review Standard
- An authorised reviewer decides whether privileged access is
  kept or removed, and approves the final notice.
- Decisions may rely only on the access record and the approved
  policy library.
- Exceptions must be escalated to an authorised reviewer.
- Communications to account holders need reviewer approval before
  they are sent."""

PROMPT = """Using only the supplied access record and approved policy
excerpts:

1. List the record fields that are present and name any required
   field that was not supplied.
2. Quote the policy passages relevant to the stated review
   criteria.
3. Write a neutral reviewer summary that keeps access-record facts
   separate from policy text.
4. Do not decide whether access is kept or removed, recommend an
   outcome, infer missing facts or draft a final notice.
5. Flag any apparent exception or missing information for the
   authorised reviewer."""

OUT = """Required record fields
- Current group memberships: present
- Manager attestation: not supplied

Relevant approved policy
- "Decisions may rely only on the access record and the approved
  policy library."
- "Exceptions must be escalated to an authorised reviewer."

Neutral reviewer summary
The access record lists the account's current group memberships.
A manager attestation was not supplied. The policy requires an
authorised reviewer's judgement and escalation of exceptions. No
access decision is given."""

SESSION = {
    "id": 25,
    "slug": "appropriate-and-inappropriate-uses",
    "short": "Appropriate and inappropriate uses",
    "lead": "Whether Claude can do a task quickly is the wrong question. The right one is what role Claude should have in it, and who is still accountable afterwards.",
    "body": [
        ("h", "Decide the role before using Claude"),
        ("p", "An appropriate use depends on more than speed. A sound decision weighs seven things:"),
        ("list", [
            "the task's purpose,",
            "the people affected,",
            "the data involved,",
            "the consequence of an error,",
            "whether the result can be reversed,",
            "the expertise required,",
            "the oversight available.",
        ]),
        ("p", "Those decide whether Claude can assist, whether extra controls are needed, or whether the use should not go ahead."),
        ("p", "Low-risk assistance supports work a person can review easily and correct without real harm: drafting from approved facts, summarising non-sensitive material, brainstorming options, organising information, preparing a decision for human review. Claude contributes wording, structure or retrieval. It does not become the accountable decision maker."),
        ("p", "Risk goes up when an output affects somebody's access to a service, their employment, money, legal position or safety, or a commitment made to a customer. Regulated advice, employment decisions, customer commitments, safety instructions and actions with financial or legal consequences all need particular care. A fluent answer is not evidence that its conclusions are correct, permitted or right for the case."),
        ("pull", "Use Claude to support accountable work, not to transfer accountability."),

        ("h", "Worked example: a privileged access review"),
        ("p", "Your team runs the quarterly review of privileged accounts for a regulated customer. Access records hold sensitive information about named staff, and removing access can stop someone doing their job. Several uses of Claude have been proposed, from drafting a note to letting Claude decide and send the removal notice itself. You need to classify each one, and redesign the autonomous proposal without losing the useful parts."),
        ("doc", "The governing standard", STANDARD),
        ("p", "The standard sets the authority boundary. It does not let a tool infer missing evidence, replace a reviewer or communicate a final decision. It also names the authoritative sources. Asking for an answer, a heading or a recommendation does not create evidence that those sources do not contain."),

        ("h", "Classify the purpose and the consequence"),
        ("p", "Start with the actual role proposed for Claude, not a broad label like \"review support\". The same tool can be appropriate in one step and inappropriate in the next. This is [[classification]] of the use."),
        ("table", ["Proposed role for Claude", "Classification", "Reason"], [
            ["Draft an internal review note from facts the reviewer approved", "Appropriate with review", "The reviewer controls the facts and checks the draft before use"],
            ["Summarise non-sensitive public vendor guidance for the team", "Appropriate", "The material is not sensitive and the summary is not a case decision"],
            ["Organise access-record facts and relevant policy passages for a reviewer", "Higher risk, support role only", "Sensitive data and real consequences need validation and human judgement"],
            ["Decide who loses access and send the notice without reviewer approval", "Inappropriate", "It hands over regulated judgement, communication authority and accountability"],
        ]),
        ("p", "Higher risk does not automatically mean prohibited. It means a narrower scope and stronger [[safeguard|safeguards]]. Ask whether Claude is preparing information for an authorised person, or making the consequential decision itself. If the output can cause harm before a qualified person checks it, the design is too autonomous."),
        ("note", "When is human review meaningful?", "Only when the reviewer has the authority, the source material, the time and the expertise to challenge or reject the output."),

        ("h", "Uses that must not proceed"),
        ("list", [
            "**It conflicts with policy.** Claude cannot make the final access decision because the standard gives that to an authorised reviewer.",
            "**It exceeds the evidence.** Claude cannot fill gaps in the record by assuming facts, searching unapproved sources or presenting an inference as verified.",
            "**It disguises AI output as professional judgement.** A reviewer must not paste an unvalidated recommendation into a decision record as their own analysis. They examine the evidence, apply the policy and make the call themselves.",
            "**The data is not approved for the purpose.** Sensitive records go only through an organisation-approved Claude environment under the internal data rules. If that route is not available, the records do not go into an unapproved tool because the task looks useful.",
        ]),

        ("h", "Redesign the autonomous proposal"),
        ("p", "The choice is not between unrestricted automation and dropping Claude. Separate preparing the evidence from making the judgement. In the redesign, Claude checks whether the required record fields appear to be present, pulls the relevant passages from the approved policy library, and writes a neutral summary for the reviewer. It does not decide, treat an exception as approved, send a notice or commit to anything."),
        ("prompt", "Bounded prompt", PROMPT),
        ("out", "What Claude returned", OUT, "good"),
        ("p", "The reviewer gets a preparation document, not an unreviewed conclusion. Where a required fact is missing, the output says it was not supplied. It does not invent a likely answer."),

        ("h", "Apply safeguards"),
        ("p", "Safeguards are operational controls on what Claude receives, what it can produce and what happens next. They should match the consequence of the task."),
        ("defs", [
            ("Approved data", "Only information permitted in the approved environment, and approved policy excerpts."),
            ("Bounded scope", "Completeness checks, retrieval, organisation and neutral summary. Nothing more."),
            ("Validation", "Compare every quoted passage and record fact with the source."),
            ("Human approval", "An authorised reviewer makes the decision and approves any communication."),
            ("Logging", "Keep the sources used, the summary, the reviewer's corrections and the final decision record."),
            ("Escalation", "Missing evidence, possible exceptions and uncertain policy go to an authorised reviewer."),
        ]),
        ("p", "Logging makes the work reviewable. It does not make an unsupported output correct. Validation is still needed, because Claude can leave things out, misread context, or sound more certain than the sources justify."),
        ("note", "Oversight limit", "A later audit is not a substitute for approval before a consequential action is taken."),
    ],
    "takeaways": [
        "Weigh purpose, people, data, consequence, reversibility, expertise and oversight.",
        "Classify the specific role proposed for Claude, not a broad label.",
        "Claude can organise approved evidence. Authorised people make consequential decisions.",
        "A request cannot override policy, supply missing evidence or move accountability.",
        "Redesign risky uses with approved data, bounded scope, validation, approval, logging and escalation.",
    ],
    "practice": "List four ways your team could use an AI assistant on one process, such as change approval. Classify each as appropriate, appropriate with review, higher risk in a support role, or inappropriate, and give the reason in one line.",
    "quiz": [
        {"q": "Which proposed use of Claude is inappropriate?", "options": [
            ("Drafting an internal note from facts the reviewer has approved.", False, "The reviewer controls the facts and checks the draft."),
            ("Summarising non-sensitive public guidance for the team.", False, "Non-sensitive material, and not a decision."),
            ("Organising record facts and policy passages for a reviewer to assess.", False, "Higher risk, but acceptable as a bounded support role with safeguards."),
            ("Deciding who loses privileged access and sending the notice without reviewer approval.", True, "It hands regulated judgement, communication authority and accountability to a tool."),
        ]},
        {"q": "A task is classified as higher risk. What does that mean in practice?", "options": [
            ("Claude must not be used for any part of it.", False, "Higher risk does not automatically mean prohibited."),
            ("It needs a narrower scope and stronger safeguards.", True, "Claude can prepare information for an authorised person while the judgement stays with them."),
            ("It needs a more capable model and nothing else.", False, "Model choice does not replace safeguards or authority."),
            ("It only needs a disclaimer on the output.", False, "A disclaimer controls nothing."),
        ]},
        {"q": "When is a human review step meaningful?", "options": [
            ("Whenever someone glances at the output before it goes out.", False, "A glance cannot challenge anything."),
            ("When an audit happens later.", False, "A later audit does not replace approval before a consequential action."),
            ("When the reviewer has the authority, source material, time and expertise to challenge or reject the output.", True, "Without those, the review is a formality."),
            ("When the output looks confident and well written.", False, "Fluency is not evidence."),
        ]},
        {"q": "A required document is missing from a case record. What should a bounded preparation prompt make Claude do?", "options": [
            ("State that the field was not supplied and flag it for the reviewer.", True, "A request cannot create evidence the sources do not contain."),
            ("Infer the most likely content.", False, "That presents an inference as evidence."),
            ("Search other sources until something turns up.", False, "Decisions may rely only on the approved sources."),
            ("Recommend an outcome anyway.", False, "Recommending is outside the bounded role."),
        ]},
        {"q": "Which TWO are safeguards for the redesigned process?", "multi": True, "options": [
            ("Limiting Claude to completeness checks, retrieval and neutral summary.", True, "Bounded scope keeps Claude in a preparation role."),
            ("Letting Claude send the notice so nothing is delayed.", False, "That removes the human approval the standard requires."),
            ("Comparing each quoted passage and fact with the source.", True, "Validation catches omissions, misreadings and overstated certainty."),
            ("Skipping logging to save time.", False, "Logging is what makes the work reviewable."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Appropriate and inappropriate uses", "sub": "Session 25 of 31. Governance and responsible use.", "notes": "New domain: governance, 15% of the exam. Four sessions."},
        {"t": "big", "h": "Support accountable work. Do not transfer accountability.", "p": "The question is what role Claude has, not whether it can do the task quickly.", "notes": "This sentence answers most governance questions on the exam."},
        {"t": "list", "h": "Seven things to weigh", "items": [
            ("Purpose", "What is the output for?"),
            ("People", "Who is affected?"),
            ("Data", "What goes in?"),
            ("Consequence", "What does an error cost?"),
            ("Reversibility", "Can it be undone?"),
            ("Expertise and oversight", "Whose judgement is needed, and who can check it?"),
        ], "notes": "Drafting a comms note and deciding someone's access are different on nearly all seven."},
        {"t": "list", "h": "Four proposals for the access review", "items": [
            ("Draft a note from approved facts", "Appropriate with review."),
            ("Summarise public vendor guidance", "Appropriate."),
            ("Organise record facts and policy for a reviewer", "Higher risk. Support role only."),
            ("Decide and send the removal notice", "Inappropriate."),
        ], "notes": "Reveal one at a time and ask the room to classify before showing the answer."},
        {"t": "ask", "h": "When does \"a human reviews it\" actually count?",
         "answer": "When the reviewer has the authority, the source material, the time and the expertise to challenge or reject it.",
         "notes": "A rubber stamp is not a control."},
        {"t": "compare", "h": "Redesign, do not abandon",
         "left_label": "Too autonomous", "left": "Review this account, decide whether privileged access should be removed, and send the notice.",
         "right_label": "Bounded", "right": "List which record fields are present and which are missing.\nQuote the relevant policy passages.\nWrite a neutral summary for the reviewer.\nDo not decide, recommend, infer or draft a notice.",
         "notes": "Split evidence preparation from judgement."},
        {"t": "cards", "h": "Six safeguards", "cols": 3, "cards": [
            ("Approved data", "Approved environment, approved excerpts."),
            ("Bounded scope", "Prepare. Do not decide."),
            ("Validation", "Check every quote and fact."),
            ("Human approval", "The authorised reviewer decides."),
            ("Logging", "Sources, summary, corrections, decision."),
            ("Escalation", "Gaps and exceptions go up."),
        ], "notes": "Logging makes it reviewable. It does not make it correct."},
        {"t": "big", "h": "A later audit is not approval.", "p": "Consequential actions get checked before they happen.", "notes": "Finding out in next quarter's audit that the wrong admin lost access is too late."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
