FOUND = """Uploaded file (fixed)
Change Governance Rules v2.0, dated 10 February 2027
- Only a Programme Office plan marked Approved sets the
  migration schedule.
- The commercial options record is not part of the migration
  coordinator's approved reference set.

Document service (connector)
- "Data Centre Migration Plan": updated 18 February, owned by the
  Programme Office, status Approved. Cutover begins 7 March.
  The service desk stays on the old site until 18 March.
- "Data Centre Migration Plan - Approved": updated 9 January,
  status Superseded. Cutover begins 1 March.
- "Commercial Options": cannot be accessed.

Mail service (connector)
- "Migration: service desk cover", 17 February: confirms service
  desk cover on the old site until 18 March.
- "Migration: asset list", 18 February: the asset list is due
  before the 7 March cutover.
- "Team lunch Friday": available and unrelated."""

PROMPT = """Prepare a short data centre migration brief.

Use the uploaded Change Governance Rules v2.0 only to decide which
source is the authority. Retrieve the current document titled
"Data Centre Migration Plan" and use it only if it is owned by the
Programme Office and marked Approved. Reject any superseded
version.

Summarise only these mail threads:
1. Migration: service desk cover
2. Migration: asset list

Do not use unrelated messages. State that "Commercial Options"
could not be accessed and do not infer what it contains. Do not
send, edit, share or take any other action in a connected system."""

OUT = """Data centre migration brief

Authoritative source: Data Centre Migration Plan, updated
18 February, Programme Office, status Approved.

- Cutover begins 7 March.
- The service desk stays on the old site until 18 March.
- The asset list is due before the 7 March cutover.

Mail reviewed
- "Migration: service desk cover" confirms cover on the old site
  until 18 March.
- "Migration: asset list" says the list is due before cutover.

Not used
- "Data Centre Migration Plan - Approved" is marked Superseded.
- "Team lunch Friday" is unrelated.
- "Commercial Options" could not be accessed and is outside the
  approved reference set. No conclusion is drawn about it."""

SESSION = {
    "id": 23,
    "slug": "connectors-and-permissions",
    "short": "Connectors and permissions",
    "lead": "A connector lets Claude work with live records in another system. It does not hand over a master key. What Claude can reach is whatever every layer of permission allows, and no more.",
    "body": [
        ("h", "Current information has a boundary"),
        ("p", "A [[connector]] links Claude to an outside service that you or your organisation have authorised. Depending on the connector, the permissions available, organisational controls and what the product currently supports, Claude may be able to retrieve information, search records or carry out supported actions there. It is not general permission to read every record or change every item."),
        ("p", "An upload is different. It gives Claude a [[snapshot]]: the file as it was when you supplied it."),
        ("table", ["", "Upload", "Connector"], [
            ["What Claude gets", "A fixed copy", "The current record in its home system"],
            ["Best when", "An approved reference set must stay unchanged for the task", "Information changes often, or the live record is the authority"],
            ["Main risk", "The original changes and the copy does not", "Pulling in more than the task needs, or the wrong record"],
        ]),
        ("pull", "Use the source that matches the decision: a fixed approved snapshot, or the current governed record."),

        ("h", "Worked example: a migration brief from mixed sources"),
        ("p", "You are preparing an internal brief on a data centre migration. You have connectors to the document service and the mail service, and one uploaded PDF of governance rules. The brief must use the current approved plan and two named mail threads only. No action in any connected system is wanted."),
        ("doc", "What is available", FOUND),

        ("h", "Choose deliberately"),
        ("p", "The governance PDF should stay an upload. It is a defined, approved reference whose job is to settle which source is the authority. It is not there to supply changing operational detail."),
        ("p", "The plan and the mail threads should come through connectors, because their current versions matter. If you uploaded a copy of the plan, a later update in the document service would not reach your analysis."),
        ("p", "That does not make every connected record relevant. Limit retrieval to the named document, the two named threads and the fields the brief needs. That is [[data-minimisation]] applied to connectors."),
        ("note", "Identity before content", "Check a record's title, update date, status, owner and scope before using what it says. A similar name does not make a record current. Here the document with \"Approved\" in its title is the superseded one."),

        ("h", "Permissions limit what Claude can do"),
        ("p", "What a connector can actually reach is the narrowest limit set by four things. These are the [[effective-permissions]]."),
        ("steps", [
            ("Source system permissions", "What your account is allowed to see and do there."),
            ("Connector authorisation", "What you granted when you connected it."),
            ("Organisational controls", "What your administrators allow."),
            ("Product capability", "What this connector supports right now."),
        ]),
        ("p", "If any one of those blocks access, Claude should not retrieve the material or look for a way round."),
        ("p", "So the inaccessible \"Commercial Options\" record is a known gap. It is not evidence about its contents. A sound brief says it could not be accessed and is outside the approved reference set. It does not guess at likely options, borrow from an obsolete file, or ask Claude to get past access controls."),
        ("p", "[[least-privilege|Least privilege]] means granting only the access a legitimate task needs. A connector used to read plans does not need permission to edit them."),
        ("note", "Reading and acting are different", "Before a consequential action in another system, such as sending an email, updating a record or sharing a document, a person should review the proposed action and confirm it explicitly: the exact recipient, record, change and scope. A connector supporting the action does not remove that step."),

        ("h", "A bounded request"),
        ("prompt", "Brief request", PROMPT),
        ("out", "What Claude returned", OUT, "good"),
        ("p", "The brief keeps source facts apart from the access limitation. It also does not let a confirmation in an email stand in for the approved plan's authority over the schedule. The mail threads add operational detail. The approved plan sets the dates."),

        ("h", "Diagnose connector problems narrowly"),
        ("p", "Connector problems are usually about the source or the authorisation, not about reasoning."),
        ("table", ["Symptom", "Likely cause", "Response"], [
            ["Nothing can be retrieved", "The account is disconnected", "Reconnect it"],
            ["A specific record is refused", "Insufficient permission", "Ask the source owner or administrator, if the access is justified"],
            ["Several similar results", "The search is too loose", "Tighten by title, date, owner, status or location"],
            ["The content looks out of date", "The source data is stale", "Verify with the record owner. Do not assume the newest visible date is right"],
            ["An action will not run", "The connector does not support it as configured", "Do not improvise a workaround or claim it was done"],
        ]),
        ("p", "Connector capabilities, consent prompts and administrator controls change. Check the current state before relying on read or action access."),
    ],
    "takeaways": [
        "Uploads are fixed snapshots. Connectors reach current records in their home system.",
        "Check a record's identity, date, status and owner before using its content.",
        "Effective access is the narrowest of source permissions, connector authorisation, organisational controls and product capability.",
        "Record inaccessible material as unavailable. Do not infer its contents or work around the restriction.",
        "Apply least privilege, and get explicit human confirmation before any consequential action.",
    ],
    "practice": "Think of a report you build from live systems. For each input, decide whether it should be a fixed upload or a live connection, and write one line on why. Then list the minimum access each would need.",
    "quiz": [
        {"q": "A fixed, approved rules document must stay unchanged for the length of a task. A status record is updated daily in its home system. How should each reach Claude?", "options": [
            ("Upload both, so nothing changes.", False, "An uploaded copy of the status record would miss later updates."),
            ("Connect to both, so both are live.", False, "The rules document is meant to be a fixed reference."),
            ("Upload the rules document and use a connector for the status record.", True, "A snapshot suits the fixed reference. Live access suits the record that changes."),
            ("Paste both from memory.", False, "Neither would be reliable or traceable."),
        ]},
        {"q": "A connector returns two documents with nearly the same title. One is marked Approved and updated last week. The other has \"Approved\" in its title and is marked Superseded. What should happen?", "options": [
            ("Use the one with Approved in the title.", False, "A title is not status. That record is marked Superseded."),
            ("Use both and merge them.", False, "Merging pulls superseded content into the result."),
            ("Check status, date and owner, then use the current approved one and reject the other.", True, "Record identity comes before content. Similar names do not establish which is current."),
            ("Use whichever appears first.", False, "Result order means nothing about authority."),
        ]},
        {"q": "A connector reports that one record cannot be accessed. How should the brief handle it?", "options": [
            ("Estimate what it probably contains.", False, "Being unable to read something is not evidence about what it says."),
            ("Say it could not be accessed and draw no conclusion about its contents.", True, "It is a known gap. Reporting it plainly keeps the brief accurate."),
            ("Ask Claude to find another way in.", False, "An access limit is not something to work around."),
            ("Leave it out with no mention.", False, "Readers should know a named source was unavailable."),
        ]},
        {"q": "Which TWO of these limit what Claude can reach through a connector?", "multi": True, "options": [
            ("Your permissions in the source system.", True, "The connector cannot see more than the account behind it."),
            ("How confidently the request is worded.", False, "Wording does not change permissions."),
            ("Your organisation's administrator controls.", True, "Administrators can restrict what connectors may do."),
            ("How long the conversation has been running.", False, "Conversation length is unrelated to access."),
        ]},
        {"q": "A connector supports sending email. Claude has drafted a message to a customer. What should happen before it is sent?", "options": [
            ("Nothing. The connector supports it, so it can go.", False, "Support for an action does not remove the need for review."),
            ("Claude should send it and report afterwards.", False, "A consequential action should be confirmed before it happens."),
            ("Grant the connector broader permissions first.", False, "That goes against least privilege and does not address the review."),
            ("A person reviews it and explicitly confirms the recipient, content and scope.", True, "Retrieval and external action are treated differently. Consequential actions need explicit human confirmation."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Connectors and permissions", "sub": "Session 23 of 32. Configuration and knowledge management.", "notes": "Copilot's equivalent is its access to SharePoint, mail and Teams. Same principles apply."},
        {"t": "cards", "h": "Two ways to give Claude a source", "cols": 2, "cards": [
            ("Upload", "A fixed snapshot. Right when an approved reference must not change during the task."),
            ("Connector", "The current record in its home system. Right when it changes often or the live record is the authority."),
        ], "notes": "The risk with an upload is the original moving on. The risk with a connector is pulling in too much, or the wrong record."},
        {"t": "ask", "h": "Which migration plan do you use?",
         "pre": "\"Data Centre Migration Plan\"\n  updated 18 February, Programme Office, status Approved\n  cutover begins 7 March\n\n\"Data Centre Migration Plan - Approved\"\n  updated 9 January, status Superseded\n  cutover begins 1 March",
         "answer": "The first. The one with \"Approved\" in its title is the superseded one. Check status, date and owner, not the name.",
         "notes": "Identity before content."},
        {"t": "steps", "h": "Four layers decide what Claude can reach", "steps": ["Source permissions", "Connector authorisation", "Organisation controls", "Product capability"], "notes": "The narrowest one wins. If any layer blocks it, Claude does not get it and does not look for a way round."},
        {"t": "big", "h": "\"Could not access\" tells you nothing about what is inside.", "p": "Record the gap. Do not guess, borrow from an old file, or work around the restriction.", "notes": "Same family as 'none supplied is not none occurred' from session 2."},
        {"t": "code", "h": "A bounded request", "label": "Brief request", "pre": PROMPT, "notes": "It names the sources, the authority test, what to do about the inaccessible record, and it forbids actions."},
        {"t": "cards", "h": "Reading and acting are different", "cols": 2, "cards": [
            ("Least privilege", "Grant only what the task needs. Reading plans does not need edit rights."),
            ("Confirm before acting", "Sending, editing or sharing needs a person to confirm the exact recipient, record and change."),
        ], "notes": "A connector supporting an action does not remove the review."},
        {"t": "list", "h": "When a connector misbehaves", "items": [
            ("Nothing retrieved", "Reconnect the account."),
            ("One record refused", "Ask the owner, if access is justified."),
            ("Several similar results", "Tighten title, date, owner or status."),
            ("Looks out of date", "Verify with the record owner."),
            ("Action will not run", "Not supported. Do not improvise."),
        ], "notes": "Usually a source or authorisation problem, not a reasoning problem."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
