INSTR = """Purpose: draft planned maintenance notices for customers.

Voice: clear, calm and practical. Short paragraphs. Active voice.

Approved terms: use "planned maintenance", "service desk" and
"maintenance window". Do not use "outage", "helpdesk" or "downtime".

Audience: address the customer's staff directly in notices. Address
the customer's IT contacts in technical summaries.

Claims: use only facts found in approved Project knowledge or in
the current request. Do not claim improved performance, no impact
or guaranteed completion times unless they are supplied.

Output: give a draft, then list any missing facts as
"Not supplied"."""

TEST = """Draft a notice for the customer's staff. Planned maintenance on
the file service takes place on Saturday 14 March from 22:00 to
02:00. Shared drives will be unavailable during the maintenance
window. Keep it under 90 words. Do not add benefits or details
that are not supplied."""

OUT = """Planned maintenance on the file service, Saturday 14 March

We are carrying out planned maintenance on the file service on
Saturday 14 March from 22:00 to 02:00.

Shared drives will be unavailable during the maintenance window.

If you have questions, contact the service desk.

Not supplied: reason for the maintenance and any actions staff
need to take beforehand."""

SESSION = {
    "id": 20,
    "slug": "configuring-a-project",
    "short": "Configuring a Project",
    "lead": "A Project holds the rules and references that stay the same, so each chat only has to carry what is new. Getting that split right is most of the work.",
    "body": [
        ("h", "Use a Project for stable, repeated work"),
        ("p", "A Claude [[project]] is a focused workspace for a continuing kind of work. It can hold [[project-instructions]], knowledge sources and related chats. Depending on your plan and workspace setup it may also offer sharing or permission controls. Together these give recurring tasks a maintained context, so nobody has to restate the same rules in every chat."),
        ("defs", [
            ("Use a Project when", "The work recurs, needs stable context, relies on shared reference material or follows a repeatable team workflow."),
            ("An ordinary chat is fine when", "It is a one-off question or a short draft, with no durable rules or references."),
        ]),
        ("p", "Creating a Project for every task adds setup and makes upkeep harder."),
        ("p", "Before adding anything, define the [[project-boundary]]: the purpose, who uses it, what inputs it accepts, what outputs it produces, and what it does not do. A narrow boundary tells people what belongs there and stops unrelated instructions diluting it."),
        ("pull", "Put lasting guidance in the Project. Put the immediate job in the chat."),

        ("h", "Worked example: maintenance notices"),
        ("p", "You are setting up a Project for the planned maintenance notices your team sends to customers. Its stable sources are the customer communications style guide and the service catalogue. This week's job is a file service migration on Saturday 14 March."),
        ("p", "The Project accepts approved maintenance details, a requested format, an audience and anything specific to the job. It produces a draft for a person to review. It does not approve changes, commit to completion times, estimate impact or replace the service manager's review. Those exclusions matter as much as the output, because they keep a drafting workspace from turning into a decision-making one."),

        ("h", "Separate permanent context from task context"),
        ("defs", [
            ("Project instructions", "Stable directions that shape how Claude responds in the Project: voice, approved terms, how to address each audience, format, and limits on claims. Instructions are not evidence. \"Use the term planned maintenance\" establishes no fact about any maintenance."),
            ("Knowledge sources", "Maintained reference material that supplies facts or approved guidance. Each should be relevant, authoritative for its subject and reviewed when it changes. See [[project-knowledge]]."),
            ("Task context", "The date, the service affected, the window and the type of notice. These apply to one job, so they go in the chat."),
        ]),
        ("prompt", "Project instructions", INSTR),
        ("p", "If the 14 March window were written into the instructions, it could be reused in a later notice. Uploading this week's migration plan as knowledge has the same problem: old details stay available for future drafts. Keeping task context out of permanent setup reduces stale context and makes the setup easier to inspect."),

        ("h", "What carries between chats"),
        ("p", "Related chats help a team organise work inside one Project. A new chat should not be taken as proof that details from an earlier one will be available. What is in a conversation belongs to that conversation. How search, memory, sharing, permissions and limits behave across chats varies with product version and workspace settings."),
        ("p", "For dependable recurring work, put durable information where it is explicitly supported: in the instructions or the knowledge. Do not rely on an earlier chat holding a decision or a correction. If several people use the Project, check the current sharing and permission settings in your workspace and the official documentation before granting access or assuming who can see or change what."),
        ("note", "Context boundary", "A Project organises work. Only explicit, supported Project context should be treated as dependable across separate chats."),

        ("h", "Test it in a fresh chat"),
        ("p", "Open a new chat in the Project and run a known test. A [[fresh-chat|fresh chat]] has no conversation history, so it checks whether the saved instructions and knowledge are enough. The test task includes this week's facts, because those are not permanent rules."),
        ("prompt", "Test task", TEST),
        ("out", "What Claude returned", OUT, "good"),
        ("p", "The draft uses the approved terms, addresses staff directly, stays inside the format, uses the supplied date and window, and lists what is missing instead of inventing it. It makes no claim about performance or impact. You still review it against the source before it goes out. Following instructions does not guarantee the content is complete or suitable."),
        ("p", "Then open the saved instructions and the knowledge list. Neither should contain \"14 March\", the file service window or this notice request. Looking directly is a better check of the boundary than seeing what a later chat appears to remember."),

        ("h", "Keep it maintained"),
        ("steps", [
            ("Keep the purpose narrow", "Recurring maintenance notices and nothing else."),
            ("Rules in instructions", "Voice, terms, audience and claim limits."),
            ("Facts in maintained knowledge", "Authoritative sources for anything that recurs."),
            ("Job details in the chat", "Dates, windows and requests for this notice."),
            ("Test after changes", "A fresh chat, checking both rule-following and factual grounding."),
            ("Verify the product behaviour", "Creation, sharing, permissions and context features change. Check before relying on them."),
        ]),
        ("p", "When terms, audiences or source documents change, update the source that is responsible. Do not add an instruction that contradicts an old one, and do not leave two versions of a reference side by side."),
    ],
    "takeaways": [
        "Projects suit bounded, recurring work. One-off tasks belong in a chat.",
        "Define the boundary first: purpose, users, inputs, outputs and exclusions.",
        "Durable rules go in instructions, maintained facts in knowledge, and this job's details in the chat.",
        "Instructions are not evidence. They shape behaviour and establish no facts.",
        "Test in a fresh chat, then inspect the saved setup directly.",
    ],
    "practice": "Think of something your team writes repeatedly. Write its Project boundary in five lines: purpose, users, inputs, outputs, exclusions. Then list three things that would go in instructions and three that must stay in the chat.",
    "quiz": [
        {"q": "Which piece of work is the best candidate for a Claude Project?", "options": [
            ("A one-off question about a pasted error message.", False, "A single question with no lasting rules belongs in a chat."),
            ("Weekly customer notices that follow the same style guide and approved terms.", True, "It recurs, needs stable context and relies on shared reference material."),
            ("A quick rewording of one sentence.", False, "A short one-time draft does not need maintained setup."),
            ("Any task at all, to keep things tidy.", False, "A Project per task creates setup and upkeep for no benefit."),
        ]},
        {"q": "A maintenance notice Project is being set up. Where should \"Saturday 14 March, 22:00 to 02:00\" go?", "options": [
            ("In the Project instructions.", False, "It applies to one job. In permanent instructions it could be reused wrongly later."),
            ("In Project knowledge, as an uploaded plan.", False, "That keeps this week's details available to future drafts."),
            ("In the chat for this notice.", True, "One-time task context belongs in the current request."),
            ("Nowhere. Claude should work it out.", False, "Claude cannot know the window unless it is supplied."),
        ]},
        {"q": "What does the instruction \"Use the term planned maintenance\" establish?", "options": [
            ("That maintenance is planned for this weekend.", False, "A wording rule states no fact about any event."),
            ("That the customer has approved the window.", False, "Approval is a fact that would need a source."),
            ("How Claude should word things. It is not evidence of any fact.", True, "Instructions shape behaviour. Facts come from knowledge sources or the current request."),
            ("That no impact is expected.", False, "That would be an unsupported claim."),
        ]},
        {"q": "Why test a Project's setup in a fresh chat?", "options": [
            ("Fresh chats respond faster.", False, "Speed is not the reason."),
            ("It proves earlier chats are shared automatically.", False, "It shows the opposite: you should not depend on earlier chats."),
            ("It removes the need to review the output.", False, "The output is still reviewed against the source."),
            ("With no conversation history, it shows whether the saved instructions and knowledge are enough.", True, "Anything the test gets right has to come from the explicit setup or the test request."),
        ]},
        {"q": "Which TWO belong in a Project boundary?", "multi": True, "options": [
            ("What the Project does not do, such as approving changes.", True, "Exclusions stop a drafting workspace becoming a decision-making one."),
            ("This week's deadline.", False, "That is task context for the chat."),
            ("Who uses it and what inputs it accepts.", True, "Users and inputs define what belongs in the Project."),
            ("The model's version number.", False, "That is not part of the boundary."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Configuring a Project", "sub": "Session 20 of 31. Configuration and knowledge management.", "notes": "New domain, 12% of the exam. Session 11 covered when to use a Project. This is how to set one up properly."},
        {"t": "big", "h": "Lasting guidance in the Project. The immediate job in the chat.", "p": "Getting that split right is most of the work.", "notes": "Everything else today is detail on this one sentence."},
        {"t": "cards", "h": "Define the boundary first", "cols": 3, "cards": [
            ("Purpose", "Draft planned maintenance notices."),
            ("Users", "The team that sends them."),
            ("Inputs", "Approved details, format, audience."),
            ("Outputs", "A draft for a person to review."),
            ("Exclusions", "No approving changes, no commitments, no impact estimates."),
        ], "notes": "The exclusions card is what keeps a drafting tool from becoming a decision tool."},
        {"t": "cards", "h": "Three places, three kinds of content", "cols": 3, "cards": [
            ("Project instructions", "Voice, approved terms, audience, claim limits, output shape."),
            ("Knowledge sources", "Maintained, authoritative references."),
            ("The chat", "This job: the date, the service, the window."),
        ], "notes": "Instructions are not evidence. 'Use the term planned maintenance' tells you nothing about any maintenance."},
        {"t": "ask", "h": "Where does \"Saturday 14 March, 22:00 to 02:00\" go?",
         "answer": "In the chat. In the instructions or knowledge it would still be there for next month's notice.",
         "notes": "Stale context is the classic Project failure."},
        {"t": "code", "h": "Instructions for the notices Project", "label": "Project instructions", "pre": INSTR, "notes": "Walk through: purpose, voice, terms, audience, claims, output. Nothing here is about a specific job."},
        {"t": "big", "h": "Do not rely on what an earlier chat said.", "p": "Only explicit Project context is dependable across separate chats.", "notes": "Cross-chat behaviour, memory and sharing vary by version and settings. If it matters, put it in instructions or knowledge."},
        {"t": "list", "h": "Test, then look", "items": [
            ("Open a fresh chat", "No history to lean on."),
            ("Run a known test", "Include this job's facts in the request."),
            ("Check the draft", "Right terms, right audience, nothing invented."),
            ("Inspect the saved setup", "No dates or job details in instructions or knowledge."),
        ], "notes": "Good live demo: do this in the Project you built in session 11."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
