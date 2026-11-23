CHATPROMPT = """Using only the change calendar excerpt below, list the maintenance
windows approved for the file server migration. Do not add windows
that are not listed.

Change calendar excerpt
Approved windows:
- Saturday 6 March, 22:00 to 02:00
- Saturday 13 March, 22:00 to 02:00
Freeze: no changes from 20 to 28 March."""

INSTR = """For migration communications, treat the approved message guide
and the migration runbook as the authoritative sources.

Use only dates and commitments found in those sources. If a
requested detail is not in the knowledge provided, say it was
not supplied.

For every draft, include:
1. The proposed message
2. Which approved statements it uses
3. Anything that needs a person to review

Do not approve changes, confirm outage windows or make
commitments on the customer's behalf."""

MAP = """Chat
- Answer: which maintenance windows are approved?

Project
- Hold: message guide, migration runbook, sign-off rules
- Apply: standing drafting and review instructions

Research
- Investigate: current vendor end-of-support dates and
  known issues
- Produce: cited findings for a person to review

Artifact
- Deliver: migration tracker with servers, owners and status
- Include: the reviewed vendor summary"""

SESSION = {
    "id": 11,
    "slug": "chat-projects-research-artifacts",
    "short": "Chat, Projects, Research, Artifacts",
    "lead": "Claude offers several ways to work. They are not a ladder from basic to advanced. Each one solves a different problem, and the skill is picking the smallest one that does the job.",
    "body": [
        ("h", "Choose the container first"),
        ("p", "Chat, Projects, Research and Artifacts can all support the same piece of business work, and they do different things for it. Reaching for the most elaborate one by default adds setup, can bury the authoritative source, and can leave you with an output that is awkward to maintain."),
        ("p", "Start from the task. Ask:"),
        ("list", [
            "Does it need context that persists beyond this conversation?",
            "Does it need investigation across outside sources that change?",
            "Does it repeat under the same rules?",
            "Are other people involved?",
            "Should the result be a substantial deliverable that gets refined on its own?",
        ]),
        ("pull", "Use the smallest experience that keeps the context, evidence and deliverable the task needs."),

        ("h", "What each one is"),
        ("defs", [
            ("Chat", "An ordinary conversation. Right for direct work where everything needed can be supplied in that conversation: a pasted excerpt, a short instruction, a focused question. A later task should not depend on an old chat unless the material is supplied again or kept somewhere persistent. [[chat|Definition.]]"),
            ("Project", "A self-contained workspace for related work. It holds [[project-instructions]], knowledge files and related chats, so recurring work runs on the same guidance and the same source material. [[project|Definition.]]"),
            ("Research", "For investigation that benefits from repeated searching, comparing several sources, pulling them together and citing them. It is for gathering evidence, not for making an answer longer. [[research-feature|Definition.]]"),
            ("Artifact", "Substantial standalone content, a tool, a visual or something interactive that is refined separately from the conversation around it. [[artifact|Definition.]]"),
        ]),

        ("h", "Worked example: one migration, four kinds of work"),
        ("p", "You are coordinating a file server migration for a customer. Four needs come up in the same week."),
        ("table", ["Need", "Evidence and pattern", "Best fit", "Why"], [
            ["Which maintenance windows are approved?", "One supplied excerpt, a one-off question", "Chat", "Everything needed fits in one conversation"],
            ["Draft and check weekly customer updates", "Stable rules, approved references, related work", "Project", "Standing instructions and knowledge keep it consistent"],
            ["What are the vendor's current end-of-support dates and known issues?", "Changing information from several outside sources", "Research", "Repeated searching and citations are the point"],
            ["A migration tracker the customer can look at", "An interactive, standalone deliverable", "Artifact", "It needs its own refinement and use"],
        ]),
        ("prompt", "The Chat task", CHATPROMPT),
        ("p", "This is not a Research task, because the answer is in a supplied source. It is not a Project, because it is a one-off question. Claude should list the two windows and should not infer a third."),

        ("h", "Projects for stable, governed work"),
        ("p", "The Project is the operating context for the recurring updates. The message guide, runbook and sign-off rules go into [[project-knowledge]]. The instructions say how Claude must use them. That cuts down repeated pasting and keeps separate chats working from the same reference set."),
        ("prompt", "Project instructions", INSTR),
        ("p", "Governed work means work done inside defined rules, approved sources and review responsibilities. The instructions do not make an output approved. They tell Claude to separate supported from unsupported content and to flag what a person has to review. You still check each draft against the real approval process."),
        ("p", "A Project earns its keep when several related chats are needed: one for the customer update, one for the runbook review, one for internal status. It is not just a longer chat. Its value is the maintained setup and the related body of work."),

        ("h", "Combining them without blurring them"),
        ("out", "Completed work map", MAP, "good"),
        ("p", "Each piece keeps one job. The Project holds the persistent context. Research does the multi-source investigation. The Artifact is the standalone deliverable. Combining them does not turn a Project into a source of outside evidence, Research into a policy store, or an Artifact into an approval system."),
        ("note", "A citation is not a verdict", "A citation shows where a statement came from. It does not show the source is authoritative, current enough, or appropriate to share. Review Research findings before they go into something the customer will see."),

        ("h", "Mistakes to avoid"),
        ("table", ["Mistake", "Why it fails"], [
            ["Using an ordinary chat for recurring work and expecting old instructions to hold", "A chat is not a maintained shared workspace"],
            ["Putting outside claims into a Project and treating them as verified", "Authority comes from the source and the review, not from where the text is stored"],
            ["Asking for Research when the answer is in an internal document", "No investigation is needed"],
            ["Building an Artifact for a short answer", "It can stay in the conversation"],
            ["Keeping a long interactive tracker as chat text", "Its layout and behaviour need their own iteration"],
        ]),
        ("p", "Which features you have, how sharing works, which plans include what, and the labels in the interface all change over time. Check Anthropic's current documentation and your own workspace settings before you design a process that depends on one of them."),
    ],
    "takeaways": [
        "Chat: direct work where the context fits in the conversation.",
        "Project: recurring work that needs standing instructions, knowledge and related chats.",
        "Research: changing, multi-source questions that need investigation and citations.",
        "Artifact: a substantial standalone deliverable, tool, visual or interactive piece.",
        "Storing something in a Project does not verify it, and a citation does not make a source authoritative.",
    ],
    "practice": "List four things you asked an AI tool to help with last week. For each, decide which of the four experiences fits and write one line saying why. Note whether the tool you actually use at work has an equivalent.",
    "quiz": [
        {"q": "A coordinator pastes a one-page change calendar and asks which windows are approved. Which experience fits?", "options": [
            ("Research, to be thorough.", False, "The answer is in the supplied page. Nothing needs investigating."),
            ("A Project, so the calendar is kept.", False, "It is a one-off question. No recurring rules or related chats are involved."),
            ("Chat.", True, "The full context fits in one conversation and the answer does not need to persist."),
            ("An Artifact.", False, "A short list of dates does not need a standalone deliverable."),
        ]},
        {"q": "A team drafts a customer update every week using the same approved message guide and sign-off rules. Which experience fits best?", "options": [
            ("A new chat each week, pasting the guide in.", False, "It works, but it invites drift and repeated effort, with no shared standing rules."),
            ("A Project, with the guide as knowledge and the rules as instructions.", True, "Recurring work under stable rules is what a Project is for."),
            ("Research.", False, "The sources are internal and already approved."),
            ("An Artifact.", False, "An Artifact is a deliverable. It is not the place to hold standing rules."),
        ]},
        {"q": "Someone needs to know what three vendors currently say about end-of-support dates, with sources they can check. Which experience fits?", "options": [
            ("Chat, from memory.", False, "The information changes and needs sources. An answer from memory may be out of date and cannot be traced."),
            ("A Project.", False, "A Project holds your reference material. It does not go and gather outside evidence."),
            ("An Artifact.", False, "That is a format for a deliverable, not a way to investigate."),
            ("Research.", True, "Changing information across several outside sources, with citations, is the case for Research."),
        ]},
        {"q": "Which TWO statements are correct?", "multi": True, "options": [
            ("Text stored in a Project is verified by being there.", False, "Authority comes from the source and the review process, not the storage location."),
            ("A citation shows where a statement came from, not that the source is authoritative.", True, "You still have to judge whether the source is reliable, current and appropriate to share."),
            ("A Project is just a longer chat.", False, "Its value is the maintained instructions, knowledge and related chats."),
            ("One piece of work can use several experiences, each with a distinct role.", True, "A Project for context, Research for evidence and an Artifact for the deliverable can sit together."),
        ]},
        {"q": "Sales leaders need an interactive tracker showing milestones, owners and review status that they can open and come back to. Which experience fits?", "options": [
            ("An Artifact.", True, "A substantial, standalone, interactive deliverable that is refined separately from the chat."),
            ("An inline chat reply.", False, "A long interactive tracker is hard to use and maintain as chat text."),
            ("Research.", False, "Nothing is being investigated."),
            ("Project instructions.", False, "Instructions tell Claude how to work. They are not a deliverable."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Chat, Projects, Research, Artifacts", "sub": "Session 11 of 31. Product and model selection.", "notes": "New domain: 12% of the exam. Say up front that Copilot and other tools have equivalents, and the exam uses Claude's names."},
        {"t": "big", "h": "Use the smallest experience that does the job.", "p": "These are not a ladder from basic to advanced. Each solves a different problem.", "notes": "Default mistake is reaching for the biggest feature."},
        {"t": "cards", "h": "What each one is for", "cols": 2, "cards": [
            ("Chat", "Direct work. Everything needed fits in the conversation."),
            ("Project", "Recurring work. Standing instructions, knowledge files and related chats."),
            ("Research", "Changing, multi-source questions. Investigation with citations."),
            ("Artifact", "A substantial standalone piece: document, tracker, tool or visual."),
        ], "notes": "One press each. Ask what the nearest Copilot equivalent is for each."},
        {"t": "list", "h": "Five questions that pick the container", "items": [
            ("Persist?", "Does the context need to outlive this conversation?"),
            ("Investigate?", "Does it need outside sources that change?"),
            ("Repeat?", "Does it recur under the same rules?"),
            ("Others?", "Are other people involved?"),
            ("Deliverable?", "Is the result something refined on its own?"),
        ], "notes": "No to all five means chat."},
        {"t": "ask", "h": "Which experience for each?",
         "pre": "1. Which maintenance windows are approved? (one page supplied)\n2. Weekly customer updates from an approved message guide\n3. Current vendor end-of-support dates, with sources\n4. A migration tracker the customer can open",
         "answer": "1 Chat. 2 Project. 3 Research. 4 Artifact.",
         "notes": "Take answers from the room before revealing. Ask why 1 is not Research."},
        {"t": "code", "h": "Project instructions set the rules", "label": "Project instructions", "pre": INSTR, "notes": "Instructions do not make output approved. They make Claude separate supported from unsupported and flag what needs review."},
        {"t": "list", "h": "Live demo: a Project in two minutes", "items": [
            ("Open Projects", "Left navigation, then Projects."),
            ("Create one", "New Project. Give it a name."),
            ("Set instructions", "Paste the instructions from the last slide."),
            ("Add knowledge", "Upload one short reference file."),
            ("Start a chat in it", "Ask a question the file answers, then one it does not."),
        ], "notes": "Rehearse this on your own account first and use a clean demo project. Anthropic is rolling out a new version of Projects, so button labels may differ slightly from these."},
        {"t": "cards", "h": "Substitution mistakes", "cols": 2, "cards": [
            ("Chat for recurring work", "Old instructions are not a maintained workspace."),
            ("Project as proof", "Storing a claim does not verify it."),
            ("Research for an internal answer", "Nothing to investigate."),
            ("Artifact for a short answer", "It can stay in the conversation."),
        ], "notes": "And: a citation tells you where it came from, not whether the source is any good."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
