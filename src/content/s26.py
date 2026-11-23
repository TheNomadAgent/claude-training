INPUT = """Month | Ticket category | Contact channel | Tickets
April | Password reset  | Phone           | 1,240
April | Password reset  | Portal          |   860
April | VPN access      | Portal          |   980
May   | Password reset  | Phone           | 1,410
May   | Password reset  | Portal          |   830
May   | VPN access      | Portal          | 1,020"""

PROMPT = """Using only the aggregated data provided, summarise the
month-to-month changes by ticket category and contact channel.
State the changes you can see. Do not infer user motives, who the
users are, or causes that are not in the data."""

SESSION = {
    "id": 26,
    "slug": "data-sensitivity-and-privacy",
    "short": "Data sensitivity and privacy",
    "lead": "An export is not one harmless object because most of its columns look routine. Go through it field by field before any of it gets near a chat.",
    "body": [
        ("h", "Classify before sharing"),
        ("p", "Data handling starts before anything is uploaded, pasted, connected or saved in a Project. First identify the category of information, its [[classification]] under your organisation's policy, and the purpose it is permitted for. Being asked for an analysis does not authorise access or disclosure."),
        ("p", "Common sensitive categories:"),
        ("list", [
            "personal information,",
            "financial and account data,",
            "health information,",
            "credentials,",
            "confidential business material,",
            "legally privileged material,",
            "records covered by a specific industry or government rule.",
        ]),
        ("p", "Personal information can be a direct identifier such as an email address. It can also be a combination of details that identifies someone in context."),
        ("p", "A data classification is an organisational label that sets handling expectations: who may access the material, where it may be stored, and whether it may be used with an AI tool. Classifications and rules differ between organisations and countries. When a policy, contract, regulation or customer commitment is unclear, do not read permission into convenience."),
        ("pull", "Use the least data necessary, in a workspace approved for that data and that purpose."),

        ("h", "Worked example: a ticket trend request"),
        ("p", "You are asked to show how ticket volumes changed month to month by category and contact channel. The data handling standard allows Service Internal data in the approved analytics workspace. Restricted data needs approval. Credentials, payment details, health details and legal case material are prohibited there. You have a raw export from the service desk tool."),
        ("p", "Build a field inventory first. It separates what each field is worth to this job from the risk it carries."),
        ("table", ["Field", "Category", "Needed?", "Decision"], [
            ["Requester name and email address", "Direct identifiers, personal information", "No", "Remove"],
            ["Office location, job title, start month", "Quasi-identifiers", "No", "Remove"],
            ["Month opened, ticket category, contact channel", "Activity fields", "Yes", "Keep, for aggregation only"],
            ["Charge-back account and amount", "Financial and account data", "No", "Remove"],
            ["Accessibility accommodation note", "Health information", "No", "Remove"],
            ["Temporary password in the work notes", "Credential", "No", "Remove immediately"],
            ["HR investigation notes", "Confidential, possibly privileged", "No", "Remove. Seek review if it ever has to be handled"],
        ]),

        ("h", "Minimise, and think about combinations"),
        ("p", "[[data-minimisation|Data minimisation]] means supplying only the fields and records the stated purpose needs. The purpose here is not to contact users, investigate an account or diagnose one person's experience. It is to describe overall changes in category and channel. Identifiers, financial fields, health details, credentials and investigation notes contribute nothing to that."),
        ("p", "Removing direct identifiers is necessary and may not be enough. Office location, job title and start month are [[quasi-identifier|quasi-identifiers]]. Each looks broad alone. Together they can narrow a record down to one person, especially when matched with information available elsewhere. That is [[re-identification]] risk."),
        ("p", "A dataset with no names can still be personal information under policy or law if people can be re-identified. You do not need those three fields for a category and channel trend, so removing them is safer than arguing for keeping them."),
        ("note", "Practical distinction", "A field that would be useful for some other question later is not necessary for this one."),

        ("h", "Choose the right control"),
        ("p", "Several controls reduce exposure. They do not give the same protection."),
        ("defs", [
            ("Redaction", "Removes or masks specific content such as an email address. It can leave other identifying combinations in place. See [[redaction]]."),
            ("Anonymisation", "Aims to make identification no longer reasonably possible. Deleting a name is not reliable [[anonymisation]] when quasi-identifiers or outside data can reconnect records to people."),
            ("Aggregation", "Combines individual records into group values, such as ticket count by month, category and channel. Very small groups can still disclose something, so follow any rule for suppressing or combining them. See [[aggregation]]."),
            ("Synthetic data", "Artificially generated data that resembles the patterns in the source. Useful for testing and demos. It may not preserve the real results, and it must be assessed for privacy and usefulness first. See [[synthetic-data]]."),
        ]),
        ("p", "For this request, aggregation is the right control, because the output is about group trends and not individuals. Synthetic data would not answer the real question reliably. Redaction alone would leave ticket-level rows nobody needs, and the linkage risk that comes with them."),

        ("h", "Prepare the approved input"),
        ("p", "Before using Claude, confirm the purpose (monthly ticket trend analysis) and that the workspace is authorised for Service Internal aggregate data. Also confirm who has access to the workspace, the retention period that applies, and whether source material or generated analysis may be kept there. Those checks cover purpose limitation, authorisation, retention, data residency, and who can see it later."),
        ("doc", "Aggregated input", INPUT),
        ("prompt", "Request", PROMPT),
        ("p", "The prepared input has no ticket-level rows, no direct identifiers and no quasi-identifiers. The prompt keeps Claude to the evidence supplied."),
        ("note", "A prompt is not a data control", "\"Do not retain this information\" is an instruction to Claude. It does not override organisational policy, workspace configuration, contractual obligations or the product's data controls. Retention and privacy are decided through approved settings and governance, not prompt wording."),

        ("h", "Know when to escalate"),
        ("p", "Some requests cannot be safely settled by one engineer. Escalate when the classification is uncertain, the permitted purpose is unclear, a regulated record may be involved, or the data would have to be used somewhere not explicitly approved for it."),
        ("table", ["Ask", "When"], [
            ["Privacy", "Personal information, re-identification risk, consent, purpose limitation or residency are uncertain"],
            ["Legal", "Contracts, legal holds, privilege, regulated disclosures or country-specific obligations may apply"],
            ["Security", "Credentials, account data, access controls, a new connection or a new workspace is involved"],
            ["Compliance", "An industry, customer or internal control sets handling or record-keeping requirements"],
        ]),
        ("p", "Product privacy, retention, plan and enterprise-control details change. Before relying on a particular Claude workspace or configuration for sensitive material, check the current official documentation and your organisation's approved-use guidance. If the two do not clearly support what you intend, use a more minimised dataset or pause for review."),
    ],
    "takeaways": [
        "Classify first: category, classification and permitted purpose, before anything is shared.",
        "Inventory an export field by field. Keep only what this purpose needs.",
        "Removing names is not anonymisation. Combinations of quasi-identifiers can re-identify people.",
        "Redaction, anonymisation, aggregation and synthetic data address different risks. Match the control to the output.",
        "A prompt is not a retention control. Escalate uncertainty to privacy, legal, security or compliance.",
    ],
    "practice": "Take the column headings from a report or export you handle (headings only, no data). Mark each as direct identifier, quasi-identifier, sensitive, or needed for the purpose. Count how many you would actually keep.",
    "quiz": [
        {"q": "An export has had names and email addresses removed. It still has office location, job title and start month on every row. What risk remains?", "options": [
            ("None. Without names it is anonymous.", False, "A dataset without names can still identify people."),
            ("Re-identification, because the combination can narrow a record to one person.", True, "Quasi-identifiers look broad alone and can single someone out together."),
            ("Only a formatting risk.", False, "The risk is to privacy, not layout."),
            ("A risk that Claude will reject the file.", False, "Whether a tool accepts data says nothing about whether it should be shared."),
        ]},
        {"q": "The goal is a month-to-month trend in ticket volume by category and channel. Which control fits best?", "options": [
            ("Redaction of email addresses only.", False, "It leaves ticket-level rows and linkage risk that the task does not need."),
            ("Synthetic data.", False, "It may not preserve the real results, so it cannot answer the real question reliably."),
            ("No control. Upload the full export.", False, "That exposes identifiers, credentials and sensitive notes for no benefit."),
            ("Aggregation into counts by month, category and channel.", True, "The output is about groups, so group-level values are all that is needed."),
        ]},
        {"q": "A prompt ends with \"do not retain this information\". What does that achieve?", "options": [
            ("It guarantees nothing is stored.", False, "Prompt wording does not control retention."),
            ("It overrides the workspace's configuration.", False, "Settings and governance decide that, not the prompt."),
            ("It is an instruction to Claude and does not override policy, configuration, contracts or product data controls.", True, "Retention and privacy are decided through approved settings and governance."),
            ("It makes any data safe to paste.", False, "The data decision comes before the prompt."),
        ]},
        {"q": "Which TWO fields should be kept for the ticket trend analysis?", "multi": True, "options": [
            ("Month the ticket was opened.", True, "It is needed to show change over time."),
            ("Requester email address.", False, "A direct identifier the trend does not need."),
            ("Ticket category.", True, "It is one of the two dimensions being analysed."),
            ("Temporary password in the work notes.", False, "A credential. Remove it immediately."),
        ]},
        {"q": "You are not sure whether a dataset's classification allows it to be used in a particular workspace. What should you do?", "options": [
            ("Go ahead, because the analysis is useful.", False, "Convenience is not permission."),
            ("Pause and escalate to the right function, or use a more minimised dataset.", True, "Uncertain classification or permitted purpose is a reason to escalate."),
            ("Ask Claude whether it is allowed.", False, "Claude does not know your organisation's policy or contracts."),
            ("Rename the file so it looks less sensitive.", False, "That changes nothing about the content."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Data sensitivity and privacy", "sub": "Session 26 of 31. Governance and responsible use.", "notes": "Practical one. Everyone here has pasted a log or an export somewhere they should not have."},
        {"t": "big", "h": "Least data necessary, in a workspace approved for it.", "p": "Classify before you share. Being asked for an analysis is not permission.", "notes": "Three checks: category, classification, permitted purpose."},
        {"t": "list", "h": "The ticket export, field by field", "items": [
            ("Requester name and email", "Direct identifiers. Remove."),
            ("Office, job title, start month", "Quasi-identifiers. Remove."),
            ("Month, category, channel", "Needed. Keep for aggregation."),
            ("Charge-back account, accessibility note", "Financial and health. Remove."),
            ("Temporary password in the notes", "Credential. Remove immediately."),
            ("HR investigation notes", "Confidential. Remove and seek review."),
        ], "notes": "Three fields survive. That ratio is normal."},
        {"t": "ask", "h": "No name, no email. Is this row anonymous?",
         "pre": "Office: Hamilton\nJob title: Payroll Manager\nStart month: March 2019",
         "answer": "No. There is probably one of those. Quasi-identifiers combine to single a person out.",
         "notes": "Re-identification. Removing direct identifiers is necessary and often not enough."},
        {"t": "cards", "h": "Four controls, four different jobs", "cols": 2, "cards": [
            ("Redaction", "Masks specific content. Other identifying combinations can remain."),
            ("Anonymisation", "Identification no longer reasonably possible. Deleting a name does not get you there."),
            ("Aggregation", "Group values in place of individual rows. Watch very small groups."),
            ("Synthetic data", "Made-up data with similar patterns. Good for tests and demos, not for real answers."),
        ], "notes": "For a trend question, aggregate."},
        {"t": "code", "h": "What actually goes to Claude", "label": "Aggregated input", "pre": INPUT, "notes": "No ticket rows, no identifiers, no quasi-identifiers. And it fully answers the question."},
        {"t": "big", "h": "A prompt is not a data control.", "p": "\"Do not retain this\" does not override policy, configuration, contracts or product settings.", "notes": "Retention is decided in settings and governance."},
        {"t": "cards", "h": "Who to ask", "cols": 2, "cards": [
            ("Privacy", "Personal information, re-identification, consent, residency."),
            ("Legal", "Contracts, legal holds, privilege, regulated disclosure."),
            ("Security", "Credentials, access controls, new connections or workspaces."),
            ("Compliance", "Industry, customer or internal control requirements."),
        ], "notes": "If you are unsure, minimise further or pause."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
