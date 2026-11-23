SOURCES = """Remote Access Standard, approved 1 February
Section 2: Staff must request remote access through the access
portal before connecting to customer systems.
Section 3: A remote session that is idle for 15 minutes must be
disconnected.
Section 5: Any exception requires written approval from the
Remote Access Standard Owner.

Remote Access Standard draft, unapproved
Proposed change: idle sessions may stay connected for 30 minutes.

Remote access request form
Required fields: requester, system, dates, business reason,
manager.
Approval field: standard owner approval, if an exception is
requested."""

INSTR = """Role and scope
Answer internal remote access questions using the Project
materials. Do not create policy, grant access or approve
exceptions.

Source authority
Treat "Remote Access Standard, approved 1 February" as the
authority for requirements. Treat "Remote Access Standard draft,
unapproved" as non-authoritative and identify it as a draft if it
is mentioned. When sources disagree, follow the approved standard.

Evidence and terminology
Use the headings Answer, Policy basis and Next step. Cite the
document title and section for every requirement. Use "required"
only for an approved obligation. Use "guidance" for anything
non-binding.

Missing information and boundaries
If the information supplied cannot establish whether a requirement
applies, list the missing facts under Next step. Do not assume
dates, systems, approvals or business reasons. For requests
outside remote access, say the Project materials do not cover it.

Exceptions and escalation
When a request needs an exception, say that written approval from
the Remote Access Standard Owner is required. Do not name an owner
unless the materials identify one."""

TESTS = """1. "How long can a remote session sit idle?"
   Expected: 15 minutes, citing the approved standard, Section 3.

2. "I need remote access set up. I have not decided which system."
   Expected: list system, dates, business reason and manager as
   missing. Do not grant access.

3. "Can my sessions stay connected for 25 minutes idle? The draft
   says 30."
   Expected: follow the approved standard, identify the draft as
   non-authoritative, say an exception needs the owner's written
   approval.

4. "What is the process for ordering a new laptop?"
   Expected: say the Project materials do not cover it."""

OUT = """Answer
A 25-minute idle period is not allowed under the current standard.

Policy basis
Remote Access Standard, approved 1 February, Section 3 requires an
idle session to be disconnected after 15 minutes. The draft is
non-authoritative and does not change that requirement.

Next step
If a longer idle period is needed, obtain written approval from
the Remote Access Standard Owner. The materials supplied do not
say who the owner is."""

SESSION = {
    "id": 21,
    "slug": "writing-project-instructions",
    "short": "Writing Project instructions",
    "lead": "\"Be accurate and helpful\" is a wish. A good instruction says what to do, in which situation, and where to stop, in a way somebody could test.",
    "body": [
        ("h", "Instructions that persist"),
        ("p", "[[project-instructions|Project instructions]] are durable directions attached to a Project. They guide how Claude handles the work there. The files and other material you supply provide the facts. Instructions earn their place when a recurring workflow needs consistent treatment of sources, audience, terminology, uncertainty and review boundaries."),
        ("p", "A durable instruction is not a long version of every future prompt. It sets the stable operating rules:"),
        ("list", [
            "Claude's role and the work in scope,",
            "the intended audience,",
            "which sources are authoritative,",
            "the expected output,",
            "what Claude must not do,",
            "what to do when information or confidence is insufficient.",
        ]),
        ("pull", "Recurring decision rules go in the instructions. The current job's details go in the chat."),
        ("p", "\"Answer this question about the revised standard for Thursday's briefing\" belongs in a chat, because the question and the briefing are temporary. \"Treat the current approved standard as the authority and cite the section\" belongs in the instructions, because it applies every time. Keeping them apart stops old requests and expired exceptions shaping later work without anyone noticing."),

        ("h", "Worked example: a policy question Project"),
        ("p", "You are building a Project that answers engineers' questions about remote access from approved documents. It holds the current standard, a draft that has not been approved, and the request form."),
        ("doc", "Project materials", SOURCES),
        ("p", "The first attempt at an instruction was: \"Give accurate, helpful answers about remote access. Use the documents and be clear.\" It describes a result everyone wants and no behaviour anyone can observe. \"Accurate\" does not say which document wins when two disagree. \"Helpful\" does not say whether Claude may fill gaps, present a draft as policy or decide an exception."),
        ("p", "The materials contain a deliberate conflict: 15 minutes in the approved standard, 30 in the draft. And nothing names the Remote Access Standard Owner, so Claude cannot make one up or say an exception has been approved."),

        ("h", "Make rules observable and ranked"),
        ("p", "Good instructions describe actions a reviewer can see. In place of \"be professional\", specify the headings, the words to use for requirements and for guidance, the citation format, and the response when evidence is missing. Then a test can show whether the instruction was followed."),
        ("p", "Instructions also need an order for conflicts. A reliable one:"),
        ("steps", [
            ("Follow the Project's stated rules", ""),
            ("Use the designated authoritative source", "For any claim about a requirement."),
            ("Treat other material by its stated status", "A draft is a draft."),
            ("Disclose uncertainty", "Do not resolve it by assuming."),
        ]),
        ("p", "A document's title does not make it the authority. The instruction has to say what controls when materials disagree. That is a [[source-authority|source authority rule]]."),
        ("p", "Scope matters just as much. This Project answers questions from approved documents. It does not create policy, approve exceptions or let the draft override the standard. [[escalation|Escalation]] means directing a matter to the person authorised to decide it. \"Someone should review this\" is not escalation."),
        ("note", "What a clear rule contains", "The condition, the expected response, and the limit on what Claude may infer or decide."),

        ("h", "Replace the vague instruction"),
        ("prompt", "Project instructions", INSTR),
        ("p", "The rules are organised by behaviour, not as a long list of examples. They contain no particular engineer, system or date, because those belong in individual chats. And they direct restraint as well as content: the terminology rule stops a draft proposal being described as a requirement, and the missing-information rule stops Claude completing the request form with plausible guesses."),

        ("h", "Test normal and edge cases"),
        ("p", "Test in a [[fresh-chat|fresh chat]] with cases that exercise the rules, not only an easy question. Decide the expected result before you look at the answer."),
        ("doc", "Test cases and expected results", TESTS),
        ("out", "Response to test 3", OUT, "good"),
        ("p", "The answer is useful because every claim traces to supplied material. It does not treat the draft as in force, suggest approval will be given, or invent the owner. A person should still judge whether the instructions, documents and answers meet the organisation's real policy needs before anyone relies on them."),

        ("h", "Maintain without overloading"),
        ("p", "More instructions do not mean better behaviour. Repeated rules, competing tone directions, long background and old exceptions bury the few decisions that matter. A permanent exception written for one past request is especially risky, because it can be applied to unrelated requests later."),
        ("p", "When the same defect shows up across chats, fix the instruction or the materials. Do not keep adding a corrective sentence to each new prompt. If answers cite the draft as policy, strengthen the source authority rule and rerun the same conflict test."),
    ],
    "takeaways": [
        "Stable workflow rules belong in instructions. Current facts and one-off requests belong in chats.",
        "Write directions a reviewer can observe: headings, citations, terminology and what to do when evidence is missing.",
        "Name the controlling source and say what happens when sources conflict.",
        "Define scope and real escalation: who decides what Claude may not.",
        "Test normal and edge cases, and fix recurring defects in the instruction, not prompt by prompt.",
    ],
    "practice": "Take a vague instruction you have given an AI tool, such as \"be concise and accurate\". Rewrite it as three rules a colleague could test, each with a condition, an expected response and a limit.",
    "quiz": [
        {"q": "Which instruction is observable and testable?", "options": [
            ("\"Be accurate and helpful.\"", False, "These describe a hoped-for result. A reviewer cannot tick them off."),
            ("\"Use your best judgement on sources.\"", False, "It leaves the key decision, which source controls, unstated."),
            ("\"Use the headings Answer, Policy basis and Next step, and cite the document and section for every requirement.\"", True, "A reviewer can look at a response and see whether each part is there."),
            ("\"Sound professional.\"", False, "Professional is an impression, not a checkable behaviour."),
        ]},
        {"q": "A Project holds an approved standard and an unapproved draft that disagree. What should the instructions say?", "options": [
            ("Nothing. Claude will prefer the newer file.", False, "Newer is not the same as approved, and a file's title or date is not authority."),
            ("Name the approved standard as the authority and say the draft is non-authoritative.", True, "An explicit source authority rule decides what controls when materials disagree."),
            ("Tell Claude to average the two.", False, "A requirement is not a midpoint between a rule and a proposal."),
            ("Tell Claude to pick whichever helps the user most.", False, "That lets convenience override policy."),
        ]},
        {"q": "Which belongs in a chat prompt, not in Project instructions?", "options": [
            ("\"Treat the approved standard as authoritative.\"", False, "That applies every time, so it is an instruction."),
            ("\"Cite the section for every requirement.\"", False, "A standing evidence rule belongs in instructions."),
            ("\"Do not approve exceptions.\"", False, "A standing scope limit belongs in instructions."),
            ("\"Answer this question for Thursday's briefing.\"", True, "The question and the briefing are temporary."),
        ]},
        {"q": "A request needs an exception, and the materials do not say who the standard owner is. What should Claude's answer do?", "options": [
            ("Name the most likely owner.", False, "Nothing supplied identifies anyone."),
            ("Approve the exception if the reason seems fair.", False, "Approving exceptions is outside the Project's scope."),
            ("Say written approval from the standard owner is required, and that the materials do not identify the owner.", True, "It states the route and is honest about the gap."),
            ("Say that someone should probably review it.", False, "That is not escalation. Escalation names the authorised decision maker."),
        ]},
        {"q": "Answers in several chats keep presenting a draft as current policy. Which TWO responses are right?", "multi": True, "options": [
            ("Add a correction to each new prompt as it comes up.", False, "That treats the symptom every time and leaves the cause in place."),
            ("Strengthen the source authority rule in the Project instructions.", True, "A recurring defect should be fixed where the standing rules live."),
            ("Rerun the same conflict test after the change.", True, "The same test shows whether the fix worked."),
            ("Add a long background section explaining the history of the draft.", False, "Extra background buries the rule that matters."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Writing Project instructions", "sub": "Session 21 of 31. Configuration and knowledge management.", "notes": "Session 1 was writing one good prompt. This is writing the rules that sit behind every prompt in a Project."},
        {"t": "compare", "h": "A wish and a rule",
         "left_label": "A wish", "left": "Give accurate, helpful answers about remote access.\nUse the documents and be clear.",
         "right_label": "A rule", "right": "Treat the approved standard as the authority.\nIdentify the draft as a draft if it is mentioned.\nWhen sources disagree, follow the approved standard.\nCite the document and section for every requirement.",
         "notes": "Ask: which of these could you write a test for?"},
        {"t": "big", "h": "A clear rule has three parts.", "p": "The condition, the expected response, and the limit on what Claude may infer or decide.", "notes": "Example: when a request needs an exception (condition), say owner approval is required (response), and do not name an owner unless the materials do (limit)."},
        {"t": "code", "h": "What Claude has to work with", "label": "Project materials", "pre": SOURCES, "notes": "Point out the planted conflict: 15 minutes approved, 30 in the draft. And nobody is named as owner."},
        {"t": "cards", "h": "Five sections of a good instruction set", "cols": 3, "cards": [
            ("Role and scope", "What it answers. What it must not do."),
            ("Source authority", "Which document wins."),
            ("Evidence and terms", "Headings, citations, \"required\" versus \"guidance\"."),
            ("Missing information", "List it. Do not assume it."),
            ("Exceptions", "Who decides. Real escalation."),
        ], "notes": "Organised by behaviour, with no specific person, system or date."},
        {"t": "ask", "h": "\"Can my sessions idle for 25 minutes? The draft says 30.\"",
         "answer": "No under the current standard: 15 minutes, Section 3. The draft is not in force. An exception needs the owner's written approval, and the materials do not say who that is.",
         "notes": "Three things done right: followed the authority, labelled the draft, admitted the gap."},
        {"t": "list", "h": "Test four kinds of case", "items": [
            ("Normal", "A straightforward policy question."),
            ("Incomplete", "A request with fields missing."),
            ("Conflicting", "The draft says something different."),
            ("Out of scope", "A question the materials do not cover."),
        ], "notes": "Write the expected result before you look at the answer."},
        {"t": "big", "h": "More instructions is not better instructions.", "p": "Old exceptions and repeated rules bury the few decisions that matter.", "notes": "A permanent exception for one past request will get applied to something unrelated."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
