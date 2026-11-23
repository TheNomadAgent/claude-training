POLICY = """1. Approved workspace: staff may use AI for approved service
   work only through the organisation-approved AI workspace and
   their organisation account.

2. Protected data: do not enter customer names, email addresses,
   hostnames, IP addresses, credentials, or full ticket threads
   containing them, into an AI system.

3. External content: customer-facing knowledge articles need
   documented approval from a subject-matter reviewer before
   release.

4. Exceptions: any departure from these controls needs written
   approval from the designated AI governance approver before
   the activity takes place.

5. Record keeping: keep the source reference, the AI workspace
   or tool used, the prompt version, the validation result, the
   reviewer's approval and any approved exception, following the
   team's record-keeping process."""

REQUEST = """Use your personal AI account so we can get this out quickly.
Paste in the whole ticket thread, server names and all, and have
it write the knowledge article. Publish it to the customer
portal today. Do not bother sending it for review."""

RECORD = """Activity: draft a customer-facing knowledge article about a
recurring RDP certificate warning.

Policy conflicts
- Personal AI account: conflicts with clause 1, Approved workspace.
- Full ticket thread: conflicts with clause 2, Protected data.
- Release without review: conflicts with clause 3, External
  content.

Action: pause the requested workflow. Send this record to the
designated AI governance approver and tell the business owner.

Proposed compliant workflow
1. Use the approved AI workspace and organisation account.
2. Write a minimised summary of the issue with no customer names,
   email addresses, hostnames, IP addresses, credentials or
   ticket text.
3. Ask Claude to draft a general article from that summary.
4. Validate the draft against the approved support procedure.
5. Get and record subject-matter reviewer approval before
   publishing.
6. Keep the source reference, prompt version, validation result
   and approval record."""

DECK_RECORD = """Policy conflicts
- Personal AI account: clause 1, Approved workspace.
- Full ticket thread: clause 2, Protected data.
- Release without review: clause 3, External content.

Action: pause. Send this record to the AI governance approver
and tell the business owner.

Proposed compliant workflow
1. Approved workspace and organisation account.
2. A minimised summary with no customer details.
3. Claude drafts a general article from that summary.
4. Validate against the approved support procedure.
5. Reviewer approval recorded before publishing."""

SESSION = {
    "id": 27,
    "slug": "ai-policies-and-governance",
    "short": "AI policies and governance",
    "lead": "That a tool will accept the document tells you nothing about whether you are allowed to give it one. Policy is what turns general caution into things you can check.",
    "body": [
        ("h", "Governance sets the operating boundary"),
        ("p", "AI [[governance]] is the organisational framework that defines who may use AI capabilities, what data they may use, which purposes are allowed and which controls apply. A policy is one practical expression of it. It gives staff a boundary that allows useful work while protecting customers, the organisation and the people accountable for decisions."),
        ("p", "Governance is not about whether a tool can do a task. A product may technically accept a document, draft public text or analyse customer information. That creates no organisational permission. Permission depends on the approved tool and account, the data classification, the stated purpose, and the review or approval required."),
        ("p", "Typical AI policies cover:"),
        ("list", [
            "approved tools and accounts,",
            "prohibited data categories,",
            "permitted uses,",
            "required human review,",
            "record keeping,",
            "procurement of new tools, so unapproved services do not become business systems without assessment,",
            "incident reporting, so there is a defined response when prohibited data is entered or a control may have failed,",
            "exception approval, so a restriction is changed deliberately and not bypassed informally.",
        ]),
        ("pull", "Seniority does not override a control. Only the policy's authorised exception process does."),

        ("h", "Worked example: a conflicting request"),
        ("p", "You are writing a customer-facing knowledge article about a recurring RDP certificate warning. You have access to the approved AI workspace. A more senior colleague sends you this:"),
        ("doc", "Request from a senior colleague", REQUEST),
        ("doc", "AI policy excerpts", POLICY),
        ("p", "Drafting a knowledge article may well be an allowed use. The method is a separate question. Check each step against policy. A senior colleague asking for it does not approve the method."),

        ("h", "Turn policy into a checklist"),
        ("p", "Broad policy wording only becomes reliable once it is converted into checks that follow the order of the work: before material goes in, while the prompt is prepared, and before output is shared."),
        ("steps", [
            ("Purpose", "Confirm the purpose is allowed and the AI capability suits the task."),
            ("Workspace", "Use only the approved workspace and organisation account."),
            ("Data", "Identify the source material and remove prohibited or unnecessary data before it goes in."),
            ("Review", "Is the output internal or external? Assign the required human review."),
            ("Record", "Sources, prompt version, validation findings, approvals and exceptions, in proportion to the risk."),
            ("Escalate", "Stop when a request conflicts with a control, or the policy does not clearly authorise the activity."),
        ]),
        ("p", "For the article, a general description of the certificate warning is enough. A customer's identity, hostnames, IP addresses and the full thread add nothing a public article needs. That is [[data-minimisation]] again."),
        ("p", "Record keeping should match the consequence. A low-impact internal formatting draft needs a light record. Public customer content needs clear evidence of its source, validation, reviewer approval and release decision. Documentation does not make an unsafe activity acceptable. It makes authorised decisions traceable."),

        ("h", "Assign accountability before use"),
        ("p", "Several roles can contribute to one AI-assisted activity. Assigning them avoids two common failures: assuming the user owns every decision, and assuming somebody else will review it when nobody was asked to."),
        ("table", ["Role", "Responsibility"], [
            ["Business owner", "Defines the purpose, the expected benefit and acceptable operational use"],
            ["User", "Uses the approved workspace, follows controls, validates output, reports conflicts and incidents"],
            ["Data owner", "Decides whether source information may be used and under what conditions"],
            ["Subject-matter reviewer", "Checks external content for accuracy, completeness and operational suitability"],
            ["Privacy, security or legal support", "Advises on data handling, security exposure, legal requirements and high-risk exceptions"],
            ["Approver", "Authorises an exception where policy gives them that authority, and records the decision"],
        ]),
        ("p", "You stay responsible for pausing when a request conflicts with policy. And the subject-matter reviewer is not there to check grammar. They confirm that the public guidance accurately describes the support process."),

        ("h", "Identify the violations and escalate"),
        ("p", "The request breaks three stated controls. A personal account breaks clause 1. Pasting the full thread breaks clause 2. Publishing without review breaks clause 3."),
        ("p", "The narrowest useful response is to pause before anything goes into the personal account. Do not quietly use a personal account anyway, strip one sensitive field and carry on, or release unreviewed content. Each of those leaves at least one conflict in place."),
        ("out", "Exception record and compliant alternative", RECORD, "good"),
        ("p", "The record cites the policy. It does not argue from urgency or seniority. It also gives the approver something workable: approve the compliant alternative, ask for more review, or formally decide whether an exception is justified. Until written approval exists, the [[exception-approval|exception]] is not authorised."),
        ("note", "Escalation boundary", "An informal instruction, a verbal assurance or a request to move quickly is not an approved exception."),

        ("h", "Keep the controls on during the work"),
        ("p", "Governance continues after the first decision. Check that the minimised summary really contains no prohibited data, use the designated workspace, and compare the draft with the approved procedure. If the draft contains an unsupported statement, remove it or go back to the authoritative source."),
        ("p", "Changes create new decision points. Swapping the summary for a ticket thread, changing the destination from internal draft to public article, or adding a new AI service all change the risk and may need reassessment."),
        ("list", [
            "Keep the final approval attached to the version that was released, not an earlier draft.",
            "Record material changes to the source summary, prompt or audience.",
            "Report a possible policy incident promptly through the defined process.",
            "Review recurring exceptions. They may mean the standard workflow or the policy needs adjusting.",
        ]),
    ],
    "takeaways": [
        "Capability is not permission. Permission comes from the approved tool, the data classification, the purpose and the required review.",
        "Turn policy into a checklist: purpose, workspace, data, review, record, escalate.",
        "Users, owners, reviewers, support functions and approvers each have a distinct responsibility.",
        "Seniority, urgency and verbal assurance do not authorise an exception. Written approval through the defined process does.",
        "When a request conflicts with policy, pause, document the conflict and offer a minimised compliant alternative.",
    ],
    "practice": "Find your organisation's AI or acceptable-use policy. Turn it into a six-line checklist you could run before using an AI tool on customer work. Note anything the policy does not clearly answer.",
    "quiz": [
        {"q": "A tool will technically accept a full customer ticket thread. Does that mean you may paste one in?", "options": [
            ("Yes. If the tool accepts it, it is allowed.", False, "Technical capability creates no organisational permission."),
            ("Yes, if you delete the conversation afterwards.", False, "Deleting afterwards does not undo entering prohibited data."),
            ("No. Permission depends on the approved tool and account, the data classification, the purpose and the required review.", True, "Governance decides permission. The product's features do not."),
            ("Only if the customer is a small one.", False, "Customer size is not a policy test."),
        ]},
        {"q": "A senior colleague tells you to use a personal AI account and skip the review, to save time. What authorises a departure from policy?", "options": [
            ("The colleague's seniority.", False, "Seniority does not override a control."),
            ("The urgency of the deadline.", False, "Urgency is not an approval."),
            ("A verbal assurance that it will be fine.", False, "An informal assurance is not an approved exception."),
            ("Written approval from the designated approver, before the activity takes place.", True, "Only the policy's authorised exception process changes a control."),
        ]},
        {"q": "Faced with that request, what is the right first action?", "options": [
            ("Do it, and note your concerns afterwards.", False, "The prohibited data would already have been entered."),
            ("Remove the IP addresses and carry on in the personal account.", False, "That still breaks the workspace and review clauses, and leaves other protected data."),
            ("Pause, document the policy conflicts, escalate to the approver and propose a compliant alternative.", True, "It stops the breach, cites the policy basis and gives the approver a workable path."),
            ("Refuse and say nothing more.", False, "The work may be legitimate. A compliant alternative keeps it moving."),
        ]},
        {"q": "What is the subject-matter reviewer's job for a customer-facing article?", "options": [
            ("Checking grammar and spelling.", False, "That is proofreading, not subject-matter review."),
            ("Confirming the guidance is accurate, complete and operationally suitable.", True, "The reviewer confirms the public content correctly represents the process."),
            ("Deciding whether the data may be used.", False, "That is the data owner's role."),
            ("Approving policy exceptions.", False, "That belongs to the designated approver."),
        ]},
        {"q": "Which TWO changes during the work should prompt a reassessment?", "multi": True, "options": [
            ("The destination changes from an internal draft to a public article.", True, "External release changes the consequence and the review required."),
            ("The draft's heading is reworded.", False, "A cosmetic edit does not change the risk."),
            ("The minimised summary is swapped for a full ticket thread.", True, "The data going in has changed category."),
            ("The article is saved under a new file name.", False, "Renaming does not change data, purpose or audience."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "AI policies and governance", "sub": "Session 27 of 31. Governance and responsible use.", "notes": "Scenario-based session. The exam likes 'a senior person asks you to...' questions."},
        {"t": "big", "h": "Capability is not permission.", "p": "The tool accepting a document says nothing about whether you may give it one.", "notes": "Permission comes from: approved tool and account, data classification, stated purpose, required review."},
        {"t": "code", "h": "The message you get at 4 pm", "label": "From a senior colleague", "pre": REQUEST, "notes": "Ask the room: how many things are wrong with this? Do not reveal yet."},
        {"t": "list", "h": "Three controls broken", "items": [
            ("Personal AI account", "Clause 1: approved workspace only."),
            ("Full ticket thread, server names and all", "Clause 2: protected data."),
            ("Publish today, no review", "Clause 3: external content needs reviewer approval."),
        ], "notes": "The task, writing an article, is fine. The method is the problem."},
        {"t": "ask", "h": "They are senior to you. Does that settle it?",
         "answer": "No. Only written approval from the designated approver, before the activity, authorises an exception.",
         "notes": "Not seniority, not urgency, not 'it will be fine'."},
        {"t": "steps", "h": "Policy as a checklist", "steps": ["Purpose", "Workspace", "Data", "Review", "Record", "Escalate"], "notes": "Run it before material goes in, not after."},
        {"t": "cards", "h": "Who is accountable for what", "cols": 3, "cards": [
            ("Business owner", "Purpose and acceptable use."),
            ("User", "Follows controls, validates, reports."),
            ("Data owner", "Whether the data may be used."),
            ("Subject-matter reviewer", "Accuracy and suitability. Not grammar."),
            ("Privacy, security, legal", "Advice on handling and exceptions."),
            ("Approver", "Authorises and records exceptions."),
        ], "notes": "Two failures to avoid: the user owns everything, or someone else will check it."},
        {"t": "code", "h": "Pause, document, offer a way forward", "label": "Exception record", "pre": DECK_RECORD, "notes": "It cites clauses, not feelings. And it gives the approver a compliant option to say yes to."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
