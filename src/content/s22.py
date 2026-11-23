INVENTORY = """1. Server Patching Standard v4.1, 2026-02-01
   Status: approved and current
   Owner: Platform Standards Team
   Rule: critical security updates must be installed within
   14 days of release.

2. Server Patching Standard v3.2, 2024-05-10
   Status: obsolete
   Owner: Platform Standards Team
   Rule: critical security updates must be installed within
   30 days of release.

3. Server Patching Standard v4.2 draft, 2026-03-12
   Status: unsigned draft
   Owner: not stated
   Rule: critical security updates must be installed within
   7 days of release.

4. Patching Standard v4.1 copy.docx, 2026-02-01
   Status: duplicate of v4.1

5. Patching Standard v4.1 copy.pdf, 2026-02-01
   Status: duplicate of v4.1

6. Patching discussion notes, 2026-03-10
   Status: informal notes
   Owner: not stated
   Content: a 7-day window was suggested for a future revision."""

RECORD = """Server Patching Standard_v4.1_Approved_2026-02-01.pdf
Action: retain and label as the authoritative current standard
Owner: Platform Standards Team
Project review date: 2026-08-01

Server Patching Standard v3.2
Action: exclude. Replaced by approved v4.1

Server Patching Standard v4.2 draft
Action: exclude. Assign to Platform Standards Team for an
approval decision

Patching Standard v4.1 copy.docx
Action: exclude as a duplicate of the retained file

Patching Standard v4.1 copy.pdf
Action: exclude as a duplicate of the retained file

Patching discussion notes
Action: exclude as informal, non-authoritative notes"""

TEST = """According to the approved current patching standard, how soon must
critical security updates be installed? State the version and date
of the standard you used. If the source does not give the answer,
say it was not supplied."""

OUT = """Critical security updates must be installed within 14 days of
release.

Source used: Server Patching Standard v4.1, approved 2026-02-01."""

SESSION = {
    "id": 22,
    "slug": "managing-uploaded-knowledge",
    "short": "Managing uploaded knowledge",
    "lead": "A Project's knowledge is only as good as what you chose to leave out. Five documents that agree beat fifty that argue with each other.",
    "body": [
        ("h", "Quality matters more than volume"),
        ("p", "Uploaded knowledge is material deliberately made available to support work in a Project: policies, reference documents, procedures, templates. More files do not automatically mean better answers. A big collection with outdated or conflicting documents can make a simple factual question harder to answer reliably."),
        ("p", "[[curation|Curating]] knowledge means deciding what belongs, what does not, and who keeps that decision up to date. The aim is a set of sources that is relevant to the Project's purpose, authoritative, current, complete enough for likely questions and free of avoidable duplication. It is upkeep, not a one-time upload."),
        ("pull", "When sources disagree, resolve the conflict before you ask Claude to use them."),
        ("p", "Claude may retrieve the relevant parts of a larger knowledge set when it answers. [[retrieval|Retrieval]] does not make an obsolete document authoritative just because it was uploaded. Clear titles, meaningful wording, version details and a focused collection all improve the odds that the right material is found and read correctly. Retrieval does not replace governing your sources, or human review."),

        ("h", "Worked example: an inherited patching Project"),
        ("p", "You inherit a Project that answers engineers' questions about the patching standard. Its job is limited to explaining the approved standard. You have no authority to approve a draft or to turn discussion notes into policy."),
        ("doc", "Source inventory", INVENTORY),
        ("p", "The install window differs across versions: 14, 30 and 7 days. That makes it a good fact to test with."),

        ("h", "Selection criteria"),
        ("p", "A [[source-inventory]] lists what is available and the decision made about each item. It exposes conflicts that file names hide. Check every source against the same criteria. Do not keep a file because it might be useful one day."),
        ("table", ["Criterion", "Question"], [
            ["Purpose", "Does it support the Project's defined work?"],
            ["Authority", "Was it approved by whoever can set the rule?"],
            ["Currency", "Is it the current version, or has it been replaced?"],
            ["Completeness", "Does it hold enough context to support the answer?"],
            ["Sensitivity", "Is it appropriate to make available to the Project and the people who can use it?"],
            ["Ownership", "Is a person or team named to maintain it?"],
            ["Update frequency", "How often should it be reviewed?"],
        ]),
        ("p", "The criteria lead to one of five actions:"),
        ("defs", [
            ("Retain", "An authoritative source the Project needs."),
            ("Label", "Mark a retained source with its purpose, status, date and version."),
            ("Replace", "Swap an older source for its approved successor."),
            ("Exclude", "Remove anything irrelevant, obsolete, duplicated or unapproved."),
            ("Assign for review", "When ownership or authority is unclear."),
        ]),
        ("note", "Sensitivity is a separate decision", "A document can be current and authoritative and still need access controls or a different workflow because of what it contains. Do not upload sensitive material just because Claude could help summarise it."),

        ("h", "Make sources findable"),
        ("p", "File names are working metadata. `standard-final-new.pdf` tells the next maintainer nothing about whether the file is approved, current or replaced. A good name gives the document's purpose, version, status and date: `Server Patching Standard_v4.1_Approved_2026-02-01.pdf`. The title and opening lines inside the document should say the same."),
        ("p", "Duplicates deserve attention. Two files with identical content are not two pieces of evidence. They give retrieval competing targets and double the upkeep. Keep one [[canonical|canonical file]] in the Project."),
        ("note", "Conflict warning", "An unsigned draft and informal notes can be useful while a policy is being developed. Neither should sit beside an approved standard as a source of answers, unless the Project's purpose is explicitly to compare versions."),

        ("h", "Curate the collection"),
        ("out", "Completed curation record", RECORD, "good"),
        ("p", "Version 4.1 stays as the single source. Its named owner establishes authority and its status establishes currency. A review date six months out is recorded because the source is durable and may still change."),
        ("p", "Version 3.2 is not kept \"for history\". It gives a different operational answer and is explicitly obsolete. The draft goes back to the standards team for a decision. The notes record a proposal, not a rule. One PDF is kept and both spare copies go."),

        ("h", "Test that the right source controls"),
        ("p", "After curating, ask a question whose answer differs between versions. Use a [[fresh-chat|fresh chat]] in the Project, and ask for the source as well as the answer. That makes unsupported certainty easier to spot."),
        ("prompt", "Test question", TEST),
        ("out", "What Claude returned", OUT, "good"),
        ("p", "If the answer cites an excluded or obsolete document, look first for a duplicate or old file you missed. Make the narrowest correction and rerun the same test. Do not add more documents."),
        ("p", "Supported file types, knowledge capacity, how retrieval behaves and plan limits all change. Check Anthropic's current documentation for your plan before designing a large collection or depending on a file format. Those details affect how you implement this. They do not change the need for source authority and upkeep."),
    ],
    "takeaways": [
        "Curate, do not accumulate. Relevant, authoritative, current sources beat a large unreviewed pile.",
        "Check each source for purpose, authority, currency, completeness, sensitivity, ownership and update frequency.",
        "Remove obsolete versions, drafts, informal notes and duplicates that should not guide answers.",
        "Give each retained source a clear name, an owner and a review date.",
        "Test with a fact that differs between versions and confirm the approved source wins.",
    ],
    "practice": "Open a shared folder your team treats as reference material. List six files and give each one of the five actions: retain, label, replace, exclude or assign for review. Note any with no clear owner.",
    "quiz": [
        {"q": "A Project's knowledge contains an approved standard, an obsolete version and an unsigned draft, each giving a different deadline. What should the knowledge owner do before anyone uses it?", "options": [
            ("Leave all three so Claude has more to work with.", False, "More conflicting material makes a simple question harder to answer reliably."),
            ("Resolve the conflict: keep the approved standard and exclude the others.", True, "Sources that should not guide answers are removed before Claude is asked to use them."),
            ("Tell Claude to use the newest file.", False, "Newest is not approved. The newest here is an unsigned draft."),
            ("Add a fourth document explaining the differences.", False, "That adds to the pile without removing the conflict."),
        ]},
        {"q": "Two files in a Project contain identical content in different formats. What is the best action?", "options": [
            ("Keep both, as two sources are stronger than one.", False, "Identical copies are not independent evidence."),
            ("Keep both and label one as a backup.", False, "The spare copy still competes in retrieval and doubles the upkeep."),
            ("Keep one canonical file and exclude the other.", True, "One reference copy avoids competing targets and drift."),
            ("Delete both and rely on memory.", False, "The Project still needs its authoritative source."),
        ]},
        {"q": "Which file name is most useful to a future maintainer?", "options": [
            ("policy-final-new.pdf", False, "It says nothing about status, version or date."),
            ("Patching (2).docx", False, "It gives no version, status or date."),
            ("READ THIS ONE.pdf", False, "It asserts importance and explains nothing."),
            ("Server Patching Standard_v4.1_Approved_2026-02-01.pdf", True, "It states the purpose, version, status and date."),
        ]},
        {"q": "A document is current and authoritative, and it contains restricted personal information. Which criterion needs its own decision before uploading?", "options": [
            ("Sensitivity.", True, "Being useful and authoritative does not settle whether it is appropriate to make available in the Project."),
            ("Currency.", False, "It is already current."),
            ("Purpose.", False, "It may well serve the purpose. That is not the open question."),
            ("File format.", False, "Format is an implementation detail."),
        ]},
        {"q": "After curating a knowledge set, which TWO steps make a good grounding test?", "multi": True, "options": [
            ("Ask a question whose answer differs between the versions.", True, "It will expose whether the wrong version is still influencing answers."),
            ("Ask an easy question every version agrees on.", False, "Agreement tells you nothing about which source controlled."),
            ("Ask Claude to state the version and date of the source it used.", True, "Seeing the source makes unsupported certainty easy to spot."),
            ("Upload more documents first, to be safe.", False, "That reintroduces the risk curation removed."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Managing uploaded knowledge", "sub": "Session 22 of 31. Configuration and knowledge management.", "notes": "Think SharePoint: everyone has seen a folder with final, final2 and FINAL-use-this."},
        {"t": "big", "h": "Curate, do not accumulate.", "p": "Five documents that agree beat fifty that argue with each other.", "notes": "Retrieval finds relevant text. It does not decide which document is the authority."},
        {"t": "ask", "h": "How many of these six should stay?",
         "pre": "1. Patching Standard v4.1, approved and current: 14 days\n2. Patching Standard v3.2, obsolete: 30 days\n3. Patching Standard v4.2, unsigned draft: 7 days\n4. v4.1 copy.docx\n5. v4.1 copy.pdf\n6. Discussion notes: 7 days was suggested",
         "answer": "One. The approved v4.1, as a single canonical file with an owner and a review date.",
         "notes": "Ask why not keep v3.2 for history. Because it gives a different operational answer and it is in the answer pool."},
        {"t": "cards", "h": "Seven checks before a file goes in", "cols": 2, "cards": [
            ("Purpose and authority", "Does it serve the Project, and was it approved by whoever sets the rule?"),
            ("Currency and completeness", "Is it the current version, with enough context?"),
            ("Sensitivity", "Is it appropriate for this Project and its users?"),
            ("Ownership and review", "Who maintains it, and how often is it checked?"),
        ], "notes": "Sensitivity is separate from usefulness. Current and authoritative can still be wrong to upload."},
        {"t": "cards", "h": "Five possible actions", "cols": 3, "cards": [
            ("Retain", "Authoritative and needed."),
            ("Label", "Purpose, status, date, version."),
            ("Replace", "Old version for its approved successor."),
            ("Exclude", "Irrelevant, obsolete, duplicate, unapproved."),
            ("Assign for review", "Ownership or authority unclear."),
        ], "notes": "The draft gets excluded and assigned back to its owners for a decision."},
        {"t": "compare", "h": "File names are metadata",
         "left_label": "Tells you nothing", "left": "policy-final-new.pdf",
         "right_label": "Purpose, version, status, date", "right": "Server Patching Standard_v4.1_Approved_2026-02-01.pdf",
         "notes": "The title and first lines inside the document should say the same thing."},
        {"t": "big", "h": "Two identical copies are not two pieces of evidence.", "p": "They are two things to find and two things to keep current.", "notes": "Keep one canonical file."},
        {"t": "code", "h": "Test the fact that differs", "label": "Grounding test", "pre": TEST, "notes": "If the answer cites the wrong version, look for a leftover file first. Do not add more documents."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
