INSTR = """Answer onboarding questions using only the approved knowledge
materials.
Name the source document when giving a process instruction.
Do not confirm that monitoring, backup, access or any checklist
item is complete or approved.
If the material does not answer the question, say it was not
supplied and direct the person to the onboarding coordinator.
For anything that needs a team's approval, name the responsible
team and tell the person to use the established approval route."""

BRIEF = """Purpose
Pilot a Claude Project for routine server onboarding questions,
using Onboarding Checklist v4, Access Matrix v2 and Monitoring
Standard v1.

Current baseline
15 completed onboardings: median checklist completion was 6
business days. Coordinators handled five clarification exchanges
per onboarding.

Pilot design
Engineers may use the Project for guidance. It must name its
source, must not confirm completion or approval, and must send
unanswered or approval-dependent questions to the coordinator.

Expected value
Test whether clarification exchanges fall by 20% with no increase
in missed team approvals. Faster completion is not assumed.

Ownership and controls
The coordinator reviews unresolved cases weekly.
Each team keeps its approval authority.
Document owners review the approved materials before the pilot
and whenever a source changes.
The coordinator records escalations and any incorrect or
unsupported answers.

Implementation cost
About 20 hours for source review, instructions, setup and user
guidance, plus two hours a week reviewing issues during the pilot.

Residual risks
The Project may give incomplete guidance, use an out-of-date
source, misroute an exception, or be asked something outside
the supplied material.

Evaluation and expansion
Review after 15 pilot onboardings. Compare clarification
exchanges, missed approvals, escalations and user feedback with
the baseline. Expand only if owners confirm source maintenance,
controls and results are acceptable."""

SESSION = {
    "id": 19,
    "slug": "integrating-and-communicating-value",
    "short": "Integration and stakeholder value",
    "lead": "Claude can help with a process as it stands, or it can make a different process possible. Those are different changes, and each needs an honest case built on a baseline, costs and what could still go wrong.",
    "body": [
        ("h", "Augmentation and redesign are different changes"),
        ("defs", [
            ("Augmentation", "Claude sits inside the existing workflow. The steps, owners, approval points and final decisions stay where they are. Claude might summarise a request, draft a response or find the relevant material. A person still takes the action and approves the result. See [[augmentation]]."),
            ("Redesign", "The process itself changes because Claude makes a different approach practical. Where work starts, who sees a request first, how information reaches people, or which cases need a person may all move. A self-service helper that answers routine questions from approved material and passes on only the unresolved ones is redesign. See [[redesign]]."),
        ]),
        ("p", "Neither is automatically better. Start with augmentation when source quality is uncertain, people may resist a new process, or governance favours a trial that is easy to reverse. Consider redesign once evidence shows the supported work is repeatable, sources are maintained, controls work and the changed process gives acceptable results."),
        ("pull", "Claude can assist a process without becoming the owner of the process."),

        ("h", "Worked example: server onboarding"),
        ("p", "A coordinator runs server onboarding for new customers across the server, network, security, backup and service desk teams. There is a 32-item checklist. Over the last 15 onboardings, completion took a median of 6 business days, and the coordinator handled five clarification exchanges each time. The approved sources are the Onboarding Checklist v4, Access Matrix v2 and Monitoring Standard v1. Each team stays responsible for approvals in its area."),
        ("p", "That log is a baseline, not a promise. It does not say why each clarification happened, whether the approved documents could have answered them, or whether self-service would shorten completion. Those unknowns belong in the plan and in the conversation with stakeholders."),
        ("p", "The documents are authoritative for their stated instructions and nothing more. A heading called \"monitoring\" does not let Claude confirm monitoring has been set up. Confirmation is an action the accountable team performs through the existing route."),

        ("h", "Where Claude sits in the workflow"),
        ("p", "Design starts with the path the work takes, not with a feature list. Where does a request begin? How does the relevant context reach Claude? Where does the output go? Who reviews it? How does an exception become a visible record?"),
        ("table", ["", "Augmented", "Redesigned"], [
            ["Entry point", "The coordinator receives the question as usual", "The engineer asks a Claude Project first"],
            ["Claude's part", "Drafts a reply from approved material the coordinator supplies", "Answers routine questions from approved material in the Project"],
            ["Review", "The coordinator checks and sends it", "Unanswered or approval-dependent questions go to the coordinator"],
            ["Approvals", "Each team approves exactly as before", "Each team approves exactly as before"],
            ["Easy to reverse?", "Yes", "Less so"],
        ]),
        ("prompt", "Project instructions for the redesigned option", INSTR),

        ("h", "Choose the smallest justified change"),
        ("p", "Augmentation is easier to undo. It tests whether Claude can help coordinators find and word approved guidance without changing anyone else's experience or moving accountability. It also reveals source gaps, because coordinators see which questions the documents cannot answer. Its limit is that the coordinator is still the way in for nearly every question."),
        ("p", "Redesign may cut routine clarification traffic. It also creates new duties: someone has to maintain the approved materials, watch the unresolved cases and check the routing instructions are still right. And engineers need to understand when self-service guidance is enough and when an approval route applies."),
        ("note", "Operational limit", "An answer that sounds complete can still miss a condition, use an old source or misread the question. Set review by the consequence of the action, not by how confident the wording sounds."),

        ("h", "Answer each stakeholder's concern"),
        ("table", ["Stakeholder", "What they need to hear"], [
            ["Users", "Is it understandable, quick, and clear about when to escalate?"],
            ["Managers", "What operational benefit is expected, and what does it cost to get?"],
            ["Risk teams", "Data boundaries, source authority, review controls, and how exceptions are investigated"],
            ["Process owners", "Who is accountable for documents, routing, decisions and upkeep"],
        ]),
        ("p", "A usable [[value-case]] has five parts:"),
        ("steps", [
            ("Baseline", "Current performance, measured."),
            ("Expected improvement", "A target you can test. It is not a fact yet."),
            ("Implementation cost", "Setup, source review, training, monitoring and owners' time."),
            ("Residual risk", "What can still go wrong after controls. See [[residual-risk]]."),
            ("Evaluation schedule", "When the evidence is reviewed and who can authorise expansion."),
        ]),
        ("p", "Here a reasonable pilot target is 20% fewer clarification exchanges, from five to four per onboarding, with no increase in missed approvals. That is a planning target drawn from the baseline. It is not a forecast of time saved everywhere, and it is not grounds for removing anyone's role."),

        ("h", "A balanced sponsor briefing"),
        ("out", "Sponsor briefing", BRIEF, "good"),
        ("p", "The briefing keeps observed facts apart from estimates and test criteria, and gives every group something concrete to approve or challenge. If the pilot shows unsupported answers or failed routing, the narrow response is to fix the source, the instruction or the escalation path and run the same evaluation again. It is not to claim success from a few happy comments."),

        ("h", "Keep claims in proportion to the evidence"),
        ("defs", [
            ("Overclaiming", "Saying Claude \"automates onboarding\" when it drafts or retrieves guidance. That hides where review is still needed and lets people assume approvals and accountability have gone. Describe the step that changed, the control that stayed and the owner who acts on the output."),
            ("Counting only the good news", "Count incorrect, unsupported and escalated answers alongside time saved. Check whether anyone bypassed an established route, whether sources stayed current and whether owners could act on the recorded exceptions."),
        ]),
    ],
    "takeaways": [
        "Augmentation keeps the process and its owners. Redesign changes the path the work takes.",
        "Start with the smallest justified change, usually augmentation, and move to redesign on evidence.",
        "Users, managers, risk teams and process owners each need a different question answered.",
        "A value case has a baseline, a testable target, implementation cost, residual risk and an evaluation schedule.",
        "Say exactly what changed. \"Claude drafts replies\" is not \"Claude automates onboarding\".",
    ],
    "practice": "Take an AI idea you would like your manager to back. Write the five parts of its value case in one line each. If you cannot write the baseline, that is the first thing to go and measure.",
    "quiz": [
        {"q": "A coordinator uses Claude to draft replies to questions, checks each one and sends it through the usual channel. Every team approves as before. What kind of change is this?", "options": [
            ("Redesign.", False, "The path, owners and approvals are unchanged."),
            ("Full automation.", False, "A person still checks and sends every reply."),
            ("Augmentation.", True, "Claude assists inside the existing workflow and people keep the actions and approvals."),
            ("Elimination.", False, "No step has been removed."),
        ]},
        {"q": "When is it sensible to start with augmentation instead of redesign?", "options": [
            ("When source quality, adoption or governance controls still need testing.", True, "Augmentation is easier to reverse and exposes source gaps before the process itself changes."),
            ("When the team wants the biggest possible change.", False, "The size of the ambition is not a reason. Evidence is."),
            ("When there is no baseline.", False, "A missing baseline is a reason to measure first, under either approach."),
            ("Never. Redesign is always better.", False, "Neither is automatically better."),
        ]},
        {"q": "Which TWO belong in a value case for a Claude pilot?", "multi": True, "options": [
            ("A baseline of current performance.", True, "Without one there is nothing to compare the pilot against."),
            ("A promise that time savings are guaranteed.", False, "Expected improvement is a target to test."),
            ("Residual risks that remain after controls.", True, "Stakeholders need to know what can still go wrong."),
            ("A statement that roles will be removed.", False, "A planning target is not grounds for removing roles."),
        ]},
        {"q": "A risk team is reviewing a proposed Claude pilot. What do they most need to see?", "options": [
            ("That users find it quick.", False, "That matters to users. It is not the risk team's question."),
            ("Data boundaries, source authority, review controls and how exceptions are investigated.", True, "These are what let a risk team judge whether the pilot is controlled."),
            ("That the model is the most capable available.", False, "Capability does not answer a control question."),
            ("A list of features.", False, "Features do not describe controls or accountability."),
        ]},
        {"q": "A pilot report says \"Claude now automates onboarding\". In practice it drafts guidance that a coordinator reviews, and every team still approves its own items. What is wrong with the statement?", "options": [
            ("Nothing. It is a fair summary.", False, "It describes something that did not happen."),
            ("It is too short.", False, "Length is not the problem."),
            ("It should name the model family.", False, "That would not fix the overclaim."),
            ("It overclaims, and hides where human review and approval are still required.", True, "State the step that changed, the control that stayed and who acts on the output."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Integration and stakeholder value", "sub": "Session 19 of 32. Workflow integration and solution design.", "notes": "Last one in this domain. It is the one for anyone who has to pitch an AI idea upward."},
        {"t": "cards", "h": "Two different changes", "cols": 2, "cards": [
            ("Augmentation", "Claude helps inside the existing process. Same steps, same owners, same approvals."),
            ("Redesign", "The process itself changes. Where work starts and who sees it first may move."),
        ], "notes": "Neither is better by default. The exam asks you to tell which one a scenario describes."},
        {"t": "big", "h": "Claude can assist a process without owning it.", "p": "Start with the smallest justified change. Move to redesign on evidence.", "notes": "Augmentation is easier to reverse, and it shows you where the source documents have gaps."},
        {"t": "compare", "h": "Same onboarding, two designs",
         "left_label": "Augmented", "left": "Coordinator receives the question.\nClaude drafts a reply from approved material.\nCoordinator checks and sends it.\nEach team approves as before.",
         "right_label": "Redesigned", "right": "Engineer asks a Claude Project first.\nIt answers routine questions from approved material.\nUnanswered or approval-dependent questions go to\nthe coordinator.\nEach team approves as before.",
         "notes": "Point out the last line is identical. Approvals do not move in either design."},
        {"t": "cards", "h": "Four audiences, four questions", "cols": 2, "cards": [
            ("Users", "Is it clear, quick, and obvious when to escalate?"),
            ("Managers", "What benefit, and at what cost?"),
            ("Risk teams", "Data boundaries, source authority, controls, exception handling."),
            ("Process owners", "Who is accountable for documents, routing and upkeep?"),
        ], "notes": "One pitch does not fit all four. The briefing has to answer each."},
        {"t": "steps", "h": "Five parts of a value case", "steps": ["Baseline", "Target", "Cost", "Residual risk", "Evaluation"], "notes": "The target is something you will test. It is not a fact yet."},
        {"t": "ask", "h": "\"Claude now automates onboarding.\" It drafts guidance that a coordinator reviews. What is wrong with that sentence?",
         "answer": "It overclaims. Say what changed, which control stayed, and who acts on the output: \"Claude drafts replies. The coordinator reviews and sends them.\"",
         "notes": "Overclaiming makes people assume the approvals have gone."},
        {"t": "list", "h": "Count the bad news too", "items": [
            ("Incorrect answers", "How many, and on what?"),
            ("Unsupported answers", "Where did it go beyond the sources?"),
            ("Escalations", "Were they routed correctly?"),
            ("Bypassed routes", "Did anyone skip an approval?"),
            ("Stale sources", "Did the documents stay current?"),
        ], "notes": "A pilot judged only on time saved and nice comments has not been evaluated."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. This closes the workflow integration domain."},
    ],
}
