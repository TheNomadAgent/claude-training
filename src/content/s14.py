SOURCES = """Runbook brief, version 3
Audience: on-call engineers
Approved reboot window: Sunday 02:00 to 04:00
Required title: Monthly patching, production servers

Team style guide
Use plain language and numbered steps.
Spell out an acronym the first time it appears.
One action per step.

Approvals tracker
Rollback procedure: approval not recorded."""

HANDOFF = """Current task: draft the patching runbook for on-call engineers.

Authoritative facts
- Title: "Monthly patching, production servers".
- Reboot window: Sunday 02:00 to 04:00.
- Follow the team style guide: plain language, numbered steps,
  acronyms spelled out on first use, one action per step.

Do not use
- The earlier Saturday 22:00 window.
- The earlier service desk audience.
- The earlier draft structure.

Unresolved
- Approval for the rollback procedure is not recorded. Do not
  include it as approved.

Next task
Draft the runbook using only the facts above. Say so if a fact
you need was not supplied."""

DECK_HANDOFF = """Current task: draft the patching runbook for on-call engineers.

Authoritative facts
- Reboot window: Sunday 02:00 to 04:00.
- Follow the team style guide.

Do not use
- The earlier Saturday 22:00 window or service desk audience.

Unresolved
- Rollback procedure approval is not recorded.
  Do not include it as approved.

Next task: draft using only the facts above."""

INSTR = """Follow the team style guide for runbooks:
- Use plain language.
- Use numbered steps, one action per step.
- Spell out an acronym the first time it appears.
When a fact you need is missing, say it was not supplied."""

SESSION = {
    "id": 14,
    "slug": "context-and-memory",
    "short": "Context, memory and boundaries",
    "lead": "A long conversation is not a better conversation. As work grows, you decide what carries forward: into this chat, into a Project, into a handoff note, or nowhere.",
    "body": [
        ("h", "Context is the working information"),
        ("p", "[[context|Context]] is the information available to Claude for the current interaction: your request, material supplied in the chat, earlier turns, and any Project setup that applies. It lets Claude connect a new task to decisions already made. More history is not automatically better context."),
        ("p", "Long conversations collect old drafts, changed assumptions, abandoned ideas and instructions that contradict each other. When those sit alongside the current source material, Claude may give weight to something that is no longer the authority."),
        ("pull", "Relevant, authoritative context beats a complete record of everything said before."),
        ("p", "Signs of a context problem:"),
        ("list", [
            "a constraint you set earlier gets dropped,",
            "Claude asks something the conversation already answered,",
            "older and newer instructions pull against each other,",
            "attention wanders back to earlier, irrelevant work,",
            "terminology becomes inconsistent.",
        ]),
        ("p", "These do not prove Claude ignored a particular item. They tell you to inspect the conversation and probably simplify what it is working from."),

        ("h", "Worked example: a runbook conversation that needs repair"),
        ("p", "You have a long-running chat about rewriting a patching runbook. Early on it assumed a Saturday 22:00 window and a service desk audience, and it settled on a draft structure. Since then the approved brief has changed. The rollback procedure has still not been approved."),
        ("doc", "Current sources", SOURCES),
        ("p", "The chat has useful material, and it is not a reliable source by itself. The brief is the authority for audience, window and title. The style guide is the authority for stable writing rules. The tracker is the authority for the rollback approval, which is still open. Where earlier turns conflict with these, the earlier turns are background."),

        ("h", "Continue, summarise or restart"),
        ("table", ["Choice", "When", "What it does"], [
            ["Continue", "Earlier turns are still relevant, consistent and useful for the next step", "Avoids restating things that are accurate and needed"],
            ["Summarise", "The history has valuable decisions but has grown long, repetitive or mixed with exploration", "Keeps the facts, decisions, constraints, open questions and next task. Drops superseded options and working-out"],
            ["Restart", "Old assumptions conflict with the new task, or the chat is too tangled to repair", "Creates a fresh working boundary"],
        ]),
        ("p", "A good summary is not a transcript. And a restart does not remove the need to supply the right sources, nor does it make an unsupported conclusion valid. The new chat needs the [[handoff-summary]] and any relevant authoritative documents."),
        ("note", "Boundary rule", "Do not tell a new chat to \"use the earlier conversation\" unless the facts it needs have been supplied again or are available through a suitable Project setup."),

        ("h", "Create a clean handoff"),
        ("p", "Here you should not continue. The old window, audience and structure conflict with the current brief, and the rollback question could be mistaken for permission. The narrowest fix is a handoff summary and a focused new chat."),
        ("out", "Handoff summary", HANDOFF, "good"),
        ("p", "The new chat now has a usable boundary. The handoff also keeps the open approval visible, which stops Claude turning a missing approval into an assumed one."),

        ("h", "Persist stable information on purpose"),
        ("defs", [
            ("Project instructions", "Standing guidance for every chat in a Project. Put durable operating rules here. See [[project-instructions]]."),
            ("Project knowledge", "Reference documents needed across related chats and kept up to date there. See [[project-knowledge]]."),
            ("Memory", "A personalisation feature. It is separate from Project instructions, Project knowledge and the source documents you supply for a task. See [[memory]]."),
        ]),
        ("prompt", "Project instructions", INSTR),
        ("p", "These instructions hold only stable style rules and one grounding rule. The style guide can live in Project knowledge. The approved brief can too, while it is current, as long as someone checks its version when the facts change. A reboot window that may move next quarter should not be written into permanent instructions. It belongs in the current brief."),
        ("p", "Do not treat memory as an authoritative record, an approval register, or a replacement for supplying current evidence. How memory behaves, what controls exist, the defaults and which plans have it all change, so check the current settings before relying on it or managing it."),
        ("note", "Data minimisation", "Do not keep sensitive information just because it might be handy later. Persist only what has a clear work purpose, proper authorisation and a suitable place to live. See [[data-minimisation]]."),

        ("h", "Keeping the boundary over time"),
        ("p", "Do not fix a context problem by loading every document and chat excerpt into a new request. More material brings more conflicts. Supply the smallest set of authoritative material the task needs, and say which source wins when two differ."),
        ("steps", [
            ("Check for conflicts", "Do current instructions clash with earlier ones in the chat?"),
            ("Separate decisions from ideas", "Final decisions on one side. Abandoned options and brainstorming on the other."),
            ("Keep open approvals open", "Record them as unresolved, never as implied permission."),
            ("Review standing instructions", "Stable rules only. No temporary facts."),
            ("Drop what has no purpose", "Especially anything sensitive."),
        ]),
    ],
    "takeaways": [
        "Context is what Claude can see now. A long history is not better context.",
        "Continue when the history is sound, summarise when it is long but valuable, restart when assumptions conflict.",
        "A restart needs a handoff summary and the current sources. It does not create facts.",
        "Durable rules go in Project instructions. Maintained references go in Project knowledge. Temporary facts go in neither.",
        "Memory is for personalisation. It is not an authority for facts or approvals.",
    ],
    "practice": "Open the longest AI conversation you have going. Write a five-line handoff summary for it: current task, authoritative facts, what not to use, what is unresolved, and the next task. Notice what you left out.",
    "quiz": [
        {"q": "A long conversation contains an old audience, an outdated figure and an abandoned concept. The approved brief has since changed all three. What is the best way to continue?", "options": [
            ("Carry on in the same chat and hope the newest instruction wins.", False, "Conflicting material in the history can still steer the output."),
            ("Start a new chat and tell it to use the earlier conversation.", False, "A new chat cannot rely on an old one unless the facts are supplied again."),
            ("Write a handoff summary, start a focused chat, and supply the current sources.", True, "It keeps what is authoritative, names what must not be used, and gives the new chat a clean boundary."),
            ("Paste every earlier draft into a new chat so nothing is lost.", False, "More material brings the same conflicts along."),
        ]},
        {"q": "What belongs in Project instructions?", "options": [
            ("This month's campaign figure.", False, "A figure that will change is a temporary fact. It belongs in the current brief."),
            ("An unapproved photograph, noted as approved.", False, "An open approval must stay recorded as open."),
            ("A sensitive detail that might be useful one day.", False, "Data minimisation says not to keep things without a clear purpose."),
            ("Stable writing rules that apply to every chat in the Project.", True, "Durable operating rules are what instructions are for."),
        ]},
        {"q": "Which statement about Claude's memory feature is correct?", "options": [
            ("It is the authoritative record of approvals.", False, "Approvals belong in their proper source record."),
            ("It is a personalisation feature, separate from Project knowledge and supplied sources.", True, "It helps tailor responses. It does not replace current evidence."),
            ("It replaces the need to supply source documents.", False, "A task still needs its authoritative sources."),
            ("Its behaviour and controls never change.", False, "They do change, so check the current settings."),
        ]},
        {"q": "Which TWO are signs that a conversation's context needs attention?", "multi": True, "options": [
            ("Claude asks a question the conversation already answered.", True, "Repeated questions suggest the working state has become cluttered."),
            ("The conversation is only three turns long.", False, "Short, coherent conversations are fine to continue."),
            ("A constraint set earlier has stopped being applied.", True, "A dropped constraint is a classic sign that older material is crowding it out."),
            ("Claude followed the requested format.", False, "That is the conversation working as intended."),
        ]},
        {"q": "A rights tracker shows no approval recorded for an image. How should a handoff summary treat it?", "options": [
            ("Leave it out, to keep the summary short.", False, "Leaving it out risks the new chat assuming it is fine to use."),
            ("List it as approved, since nobody objected.", False, "No objection is not an approval."),
            ("List it as unresolved and say not to use it as approved.", True, "Keeping the open approval visible stops a missing approval being treated as permission."),
            ("Store it in memory for later.", False, "Memory is not an approval register."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Context, memory and boundaries", "sub": "Session 14 of 32. Product and model selection.", "notes": "Everyone has had a chat go strange after forty turns. Today explains why and what to do."},
        {"t": "big", "h": "A long conversation is not a better conversation.", "p": "Old drafts and replaced instructions stay in view and keep pulling on the answer.", "notes": "Links back to session 3: context drift."},
        {"t": "list", "h": "Signs the context needs attention", "items": [
            ("Dropped constraints", "A rule you set earlier stops being applied."),
            ("Repeated questions", "It asks what the chat already answered."),
            ("Conflicting instructions", "Old and new pull against each other."),
            ("Wandering attention", "It drifts back to earlier work."),
            ("Shifting terms", "The same thing gets different names."),
        ], "notes": "These are symptoms to inspect, not proof of a specific failure."},
        {"t": "cards", "h": "Continue, summarise or restart", "cols": 3, "cards": [
            ("Continue", "History is relevant, consistent and useful for the next step."),
            ("Summarise", "Valuable decisions buried in a long, repetitive thread."),
            ("Restart", "Old assumptions conflict with the new task."),
        ], "notes": "A restart still needs the right sources. It does not create facts."},
        {"t": "code", "h": "A clean handoff", "label": "Handoff summary", "pre": DECK_HANDOFF, "notes": "Five parts: task, authoritative facts, do not use, unresolved, next task. The 'unresolved' part is what stops a missing approval becoming an assumed one."},
        {"t": "cards", "h": "Where things should live", "cols": 3, "cards": [
            ("Project instructions", "Durable rules for every chat in the Project."),
            ("Project knowledge", "Maintained reference documents."),
            ("The current brief", "Facts that will change, like this quarter's window."),
        ], "notes": "A reboot window that may move does not belong in permanent instructions."},
        {"t": "big", "h": "Memory is personalisation, not authority.", "p": "It is not an approval register and it does not replace supplying current sources.", "notes": "Memory behaviour and settings change. Tell them to check their own settings. Good moment to show Settings on your account if you want."},
        {"t": "ask", "h": "Should you paste every earlier draft into the new chat so nothing is lost?",
         "answer": "No. More material brings the same conflicts with it. Supply the smallest authoritative set and say which source wins.",
         "notes": "Also mention data minimisation: do not keep sensitive detail without a purpose."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. This closes the product and model selection domain."},
    ],
}
