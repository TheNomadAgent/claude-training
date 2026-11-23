SOURCE = """Task: prepare a short comparison memo for the service delivery
manager.
Required: identify the eligible vendors and recommend one
eligible vendor.
Evidence boundary: use only this table.

Mandatory eligibility criteria
1. Annual subscription cost must be $120,000 or less.
2. The vendor must hold ISO 27001 certification.
3. Standard deployment must take 30 calendar days or fewer.

Vendor     Annual cost  ISO 27001  Deployment  Uptime
Kestrel    $108,000     No         21 days     99.95%
Ridgeway   $116,000     Yes        28 days     99.90%
Tarn       $122,000     Yes        20 days     99.99%"""

MEMO = """To: Service Delivery Manager
Subject: Patch management tool comparison

Kestrel offers the lowest annual subscription cost at $108,000
and a 21-day deployment. Ridgeway costs $116,000 with a 28-day
deployment. Tarn has the highest uptime at 99.99%, but costs
$122,000 a year.

Kestrel is the strongest option because it has the lowest cost
and a faster deployment than Ridgeway. I recommend selecting
Kestrel."""

FIXED = """To: Service Delivery Manager
Subject: Patch management tool comparison

The mandatory criteria are an annual cost of $120,000 or less,
ISO 27001 certification, and deployment within 30 calendar days.

Kestrel costs $108,000 and deploys in 21 days, but does not hold
ISO 27001 certification. Tarn holds ISO 27001 certification and
deploys in 20 days, but its annual cost is $122,000. Neither
vendor is eligible.

Ridgeway costs $116,000, holds ISO 27001 certification and
deploys in 28 days. Ridgeway is the only eligible vendor and is
recommended."""

DECK_SOURCE = """Mandatory: cost $120,000 or less, ISO 27001, deploy in 30 days
or fewer. Recommend one eligible vendor. Use only this table.

Vendor     Annual cost  ISO 27001  Deployment  Uptime
Kestrel    $108,000     No         21 days     99.95%
Ridgeway   $116,000     Yes        28 days     99.90%
Tarn       $122,000     Yes        20 days     99.99%"""

SESSION = {
    "id": 5,
    "slug": "accuracy-and-completeness",
    "short": "Accuracy and completeness",
    "lead": "A memo can be well written, confident and correct in every number it quotes, and still recommend the wrong vendor. What it leaves out matters as much as what it says.",
    "body": [
        ("h", "Fluency is not evidence"),
        ("p", "A clear memo looks reliable because it uses professional language, logical headings and confident conclusions. Those describe the presentation. They say nothing about whether a claim is true, whether required information is missing, or whether the memo does the job it was asked to do. So review starts with the source material and the requested result, not with an impression of the writing."),
        ("p", "Check an output on six separate dimensions:"),
        ("defs", [
            ("Factual accuracy", "Does each claim match the supplied evidence or an authoritative outside source?"),
            ("Completeness", "Are all the required facts, criteria and requested parts there?"),
            ("Relevance", "Does the content help answer the stated task?"),
            ("Internal consistency", "Do the claims, numbers and conclusions agree with each other?"),
            ("Instruction compliance", "Did it follow the constraints: format, scope, recommendation rules, evidence boundary?"),
            ("Audience fitness", "Does the reader get enough context, the right terminology and a level of detail they can act on?"),
        ]),
        ("p", "An output can be accurate and incomplete, complete and badly targeted, or pleasant in tone and non-compliant with its instructions."),
        ("pull", "Accept an output only after checking what it says, what it leaves out, and whether it serves the decision it was requested for."),

        ("h", "Worked example: three patching tool vendors"),
        ("p", "You have to write a short memo for the service delivery manager comparing three patch management tools. A vendor is eligible only if it meets every mandatory criterion. The memo must identify the eligible vendors and recommend one of them, using only the supplied information."),
        ("doc", "Requirement set", SOURCE),
        ("p", "This record is the authority for the review. It holds both the vendor facts and the instructions Claude has to follow. No capability, deployment risk or business preference may be inferred if it is not in the record."),
        ("p", "The table supports one precise conclusion. Kestrel meets the cost and deployment limits and lacks the required certification. Tarn has the certification and the fastest deployment and is over the cost limit. **Ridgeway is the only vendor that meets all three.** That follows from the facts supplied, not from writing quality or general assumptions about vendors."),

        ("h", "Build the review rubric first"),
        ("p", "Before accepting an output, or comparing several, turn the task into a review [[rubric]]: a short, task-specific set of checks used to make acceptance decisions consistently. It stops a reviewer praising a well-written answer while missing the requirement that decides whether it can be used."),
        ("list", [
            "Every cost, certification, deployment and uptime claim matches the source table.",
            "Each vendor is assessed against all three mandatory criteria.",
            "The memo says explicitly which vendors are eligible.",
            "The recommendation names an eligible vendor and gives reasons the source supports.",
            "The memo is concise and understandable for the service delivery manager.",
        ]),
        ("p", "Every recommendation needs traceable support. If a task uses outside information, trace important claims to a named authoritative source such as an approved policy, a signed contract or current vendor documentation. If the task is limited to supplied material, general knowledge does not count as evidence."),
        ("note", "Defect or preference?", "Writing \"annual cost\" for \"annual subscription cost\" keeps the meaning, because the source has only one annual cost. Leaving out the certification requirement changes the eligibility decision. Defects affect meaning, compliance or usefulness. Harmless preferences do not."),

        ("h", "Test the memo against the record"),
        ("out", "What Claude returned", MEMO, "bad"),
        ("p", "None of the numbers contradicts the source. Kestrel is the cheapest and deploys in 21 days. Ridgeway costs $116,000 and takes 28 days. Tarn has the highest uptime and costs $122,000. That makes the omission easy to miss on a quick read."),
        ("p", "So do not start by asking whether any sentence looks wrong. Map each source requirement and important source fact to a place in the output."),
        ("table", ["Source requirement or fact", "Present?", "Finding"], [
            ["Kestrel cost: $108,000", "Yes", "Accurate"],
            ["Kestrel deployment: 21 days", "Yes", "Accurate"],
            ["Ridgeway cost: $116,000", "Yes", "Accurate"],
            ["Ridgeway deployment: 28 days", "Yes", "Accurate"],
            ["Tarn cost: $122,000", "Yes", "Accurate"],
            ["Tarn uptime: 99.99%", "Yes", "Accurate"],
            ["ISO 27001 status for all vendors", "No", "Mandatory criterion omitted"],
            ["Eligibility against all three criteria", "No", "Required assessment omitted"],
            ["Identify eligible vendors", "No", "Instruction not followed"],
            ["Recommend an eligible vendor", "No", "Kestrel is not eligible"],
            ["Ready for the audience", "Partly", "Concise, but the decision is unusable"],
        ]),
        ("p", "The matrix separates \"nothing is obviously wrong\" from \"everything required is present\". The included claims are accurate. The certification criterion and the eligibility assessment are missing, and that makes the recommendation non-compliant. Kestrel cannot be recommended, because the source says outright that it does not hold ISO 27001."),
        ("note", "Review finding", "An omission can produce a materially wrong business decision even when every statement that was included is correct."),

        ("h", "Correct the result without changing the evidence"),
        ("p", "The narrow correction is to put back the omitted criteria and revise only the conclusion the full record does not support. Do not add claims about security risk, product quality or vendor suitability beyond the mandatory screen. None of that was supplied."),
        ("out", "Corrected memo", FIXED, "good"),
        ("p", "This version is more useful because it answers the decision that was asked for, not because it is longer. It traces eligibility to every mandatory criterion, rules vendors out without inventing reasons, and recommends the one vendor the source supports. A person is still responsible for deciding whether the requirement set itself is adequate before any purchase goes ahead."),

        ("h", "A repeatable acceptance process"),
        ("p", "The same method works for summaries, policy drafts, analyses and comparisons."),
        ("steps", [
            ("Identify the frame", "Purpose, audience, instructions and evidence boundary. Keep source facts apart from prompt instructions."),
            ("List what is required", "The required facts and the required parts of the output."),
            ("Check the claims", "Mark each required fact and criterion as present, absent, accurate or unsupported."),
            ("Look for what is missing", "Investigate omissions even when the prose is polished."),
            ("Correct from evidence", "Only with what the source, or an authorised outside record, supports."),
            ("Accept against the rubric", "Only when it meets the task-specific checks."),
        ]),
        ("p", "Spend review effort in proportion to consequence. A typo in a low-stakes internal draft is a presentation issue. A missing mandatory criterion in a vendor recommendation can change what gets bought. When an output influences an approval, compliance, a financial commitment or an operational action, use a documented rubric and require human review before it is used."),
    ],
    "takeaways": [
        "Professional wording does not prove accuracy or complete coverage.",
        "Check accuracy, completeness, relevance, consistency, instruction compliance and audience fitness separately.",
        "Write the rubric from the task before you read the output.",
        "Map every requirement to the output. A matrix exposes what a quick read misses.",
        "Correct from the evidence supplied, and do not invent the missing context.",
    ],
    "practice": "Take a recent AI-drafted summary or recommendation and the request behind it. List every requirement in the request, then mark each as present, absent, accurate or unsupported in the output. Note anything you only spotted because you made the list.",
    "quiz": [
        {"q": "A memo quotes six figures and all six match the source. What has that established?", "options": [
            ("The memo is ready to send.", False, "Accurate included claims say nothing about what was left out."),
            ("The recommendation is sound.", False, "A recommendation can rest on accurate figures and still ignore a mandatory criterion."),
            ("Partial accuracy. Completeness and instruction compliance still have to be checked.", True, "The dimensions are separate. Accuracy of what is present does not cover what is absent."),
            ("The memo is complete.", False, "Completeness is about required items being present, which has not been checked."),
        ]},
        {"q": "A vendor must meet three mandatory criteria. The memo recommends the cheapest vendor and never mentions certification, which that vendor lacks. What is the defect?", "options": [
            ("A stylistic preference.", False, "It changes the decision, so it is a defect and not a preference."),
            ("An omission that makes the recommendation non-compliant.", True, "A mandatory criterion was left out, so an ineligible vendor was recommended."),
            ("A factual error in the cost figures.", False, "The figures quoted are correct."),
            ("A formatting problem.", False, "The layout is not the issue."),
        ]},
        {"q": "When should the review rubric be written?", "options": [
            ("After reading the output, so it fits what was produced.", False, "That lets the output set the standard it is judged by."),
            ("Only if the output looks wrong.", False, "The dangerous outputs are the ones that look right."),
            ("It is not needed for short memos.", False, "Length does not decide consequence."),
            ("Before accepting or comparing outputs, from the task and its requirements.", True, "A rubric built from the task keeps acceptance decisions consistent and catches missing requirements."),
        ]},
        {"q": "Which change to an output is a harmless preference and not a defect?", "options": [
            ("Writing \"annual cost\" where the source says \"annual subscription cost\", when there is only one annual cost.", True, "The meaning is preserved, so nothing about the decision changes."),
            ("Dropping one of the mandatory criteria.", False, "That changes the eligibility decision."),
            ("Recommending a vendor that fails a criterion.", False, "That breaks the instruction to recommend an eligible vendor."),
            ("Adding a claim about product quality that the source does not contain.", False, "That is an unsupported claim outside the evidence boundary."),
        ]},
        {"q": "The memo wrongly recommends an ineligible vendor. Which TWO belong in a narrow correction?", "multi": True, "options": [
            ("Put back the omitted criterion and assess every vendor against all three.", True, "It restores what the record requires."),
            ("Add a paragraph on each vendor's general security reputation.", False, "Nothing about reputation was supplied."),
            ("Change the recommendation to the vendor the full record supports.", True, "Only the unsupported conclusion is revised."),
            ("Rewrite the whole memo in a more formal tone.", False, "Tone was not the defect."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Accuracy and completeness", "sub": "Session 5 of 32. Evaluating outputs.", "notes": "New domain: output evaluation, 21% of the exam, the biggest one. Six sessions."},
        {"t": "big", "h": "Fluency is not evidence.", "p": "Good headings and a confident tone describe the presentation. They do not tell you it is right or complete.", "notes": "Start from the source and the request, not from how the writing feels."},
        {"t": "cards", "h": "Six separate checks", "cols": 3, "cards": [
            ("Accuracy", "Does each claim match the evidence?"),
            ("Completeness", "Is everything required there?"),
            ("Relevance", "Does it help answer the task?"),
            ("Consistency", "Do the numbers and conclusions agree?"),
            ("Compliance", "Did it follow the instructions?"),
            ("Audience fit", "Can the reader act on it?"),
        ], "notes": "An output can pass one and fail another. That is the whole session."},
        {"t": "code", "h": "The requirement set", "label": "Source", "pre": DECK_SOURCE, "notes": "Give the room 30 seconds: which vendor is eligible? Only Ridgeway."},
        {"t": "spot", "h": "Every number here is correct. What is wrong?",
         "left_label": "The source says", "left": "Mandatory: $120,000 or less, ISO 27001, 30 days or fewer.\n\nKestrel: $108,000, no ISO 27001, 21 days\nRidgeway: $116,000, ISO 27001, 28 days\nTarn: $122,000, ISO 27001, 20 days",
         "right_label": "Claude's memo", "right": "Kestrel offers the lowest cost at $108,000 and a 21-day deployment. Ridgeway costs $116,000 with a 28-day deployment. Tarn has the highest uptime but costs $122,000.\n\nKestrel is the strongest option. I recommend selecting Kestrel.",
         "reveal": "ISO 27001 is never mentioned. Kestrel does not hold it, so Kestrel is not eligible.",
         "reveal_label": "Missing:",
         "notes": "Let them hunt for a wrong number. There is not one. The fault is what is absent."},
        {"t": "big", "h": "An omission can be a wrong decision.", "p": "Even when every statement that was included is true.", "notes": "'Nothing looks wrong' is not the same as 'everything required is present'."},
        {"t": "list", "h": "Map requirements to the output", "items": [
            ("Six vendor figures", "Present. Accurate."),
            ("ISO 27001 status", "Absent. Mandatory criterion."),
            ("Eligibility for each vendor", "Absent. Required."),
            ("Recommend an eligible vendor", "Failed. Kestrel is not eligible."),
        ], "notes": "Write the rubric from the task first, then walk the output against it."},
        {"t": "compare", "h": "Defect or preference?",
         "left_label": "Preference: leave it", "left": "\"Annual cost\" for \"annual subscription cost\".\nA different sentence order.\nBullets where you would use a paragraph.",
         "right_label": "Defect: fix it", "right": "A mandatory criterion left out.\nAn ineligible vendor recommended.\nA claim the source does not support.",
         "notes": "Defects change meaning, compliance or usefulness. Fix narrowly: restore the criterion, change the conclusion, add nothing new."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
