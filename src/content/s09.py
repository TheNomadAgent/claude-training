SOURCES = """Manufacturer specification sheet, New Zealand model
Published 3 March 2026
Product: 3 kVA rack UPS, 2U, with one internal battery pack.
Runtime: "Up to 18 minutes at half load, at 25 C, with new
batteries."
Time to shut down connected equipment: not stated.

Supplier trade-in guide, New Zealand
Published 20 January 2027
Offer period: 1 February to 30 April 2027.
Eligible items: new rack UPS units, 1 kVA and above.
Rebate: 15% of the purchase price, maximum $300.
Conditions: trade in a working UPS and buy from an authorised
New Zealand reseller.

Independent test report
Published 12 August 2026
Tested product: the same 3 kVA New Zealand model, new batteries.
Result: 11 minutes at 80% load, at 30 C.
The report did not test half load or a staged shutdown."""

DRAFT = """We should buy this UPS for the comms room. It is a 3 kVA, 2U unit
with an internal battery pack. It will run for 18 minutes in an
outage, which is enough to shut down all 12 servers cleanly. We
will also get a $300 rebate, so it is excellent value."""

FIXED = """The New Zealand model is a 3 kVA, 2U rack UPS with one internal
battery pack. The manufacturer states up to 18 minutes of runtime
at half load, at 25 C, with new batteries. An independent test of
the same model measured 11 minutes at 80% load, at 30 C.

The supplier's trade-in offer runs from 1 February to 30 April 2027.
It gives 15% of the purchase price, up to $300, and requires trading
in a working UPS and buying from an authorised New Zealand reseller.

Do not treat this unit as sufficient to shut down all 12 servers
until we know the comms room load and how long a staged shutdown
takes."""

SESSION = {
    "id": 9,
    "slug": "fact-checking",
    "short": "Fact-checking and sources",
    "lead": "You check claims, not documents. A source only helps when it supports the exact claim being made, including the conditions attached to it.",
    "body": [
        ("h", "Pull out the claims that can be checked"),
        ("p", "Fact-checking starts by separating what can be tested from everything else in a draft."),
        ("table", ["Kind of statement", "Example", "How to treat it"], [
            ["Factual claim", "\"The unit is 3 kVA\"", "Test it against evidence"],
            ["Opinion", "\"This is a sensible choice\"", "Not directly checkable. It may rest on facts that are"],
            ["Recommendation", "\"Buy this model\"", "Ask what it assumes"],
            ["Promotional language", "\"Excellent value\"", "Needs stated criteria and evidence, or it goes"],
        ]),
        ("p", "Claude can pull candidate claims out of a draft, group them and lay out an [[evidence-log]]. A person still has to open the sources that decide the matter and judge what they actually establish."),
        ("pull", "A source is useful only when it supports the exact claim being made."),

        ("h", "Check the risky claims first"),
        ("p", "Not every claim deserves the same effort. Start with the ones that are:"),
        ("list", [
            "**high consequence** if wrong,",
            "**new** to the audience,",
            "**precise**, with exact numbers or conditions,",
            "**likely to change**, such as prices, eligibility rules and specifications.",
        ]),
        ("p", "A loose descriptive phrase can wait until the claims carrying the decision are settled."),

        ("h", "Worked example: a UPS recommendation"),
        ("p", "A colleague has drafted a recommendation to buy a UPS for a customer's comms room. You have three documents. Nothing has been supplied about the room's actual load or how long the servers take to shut down."),
        ("out", "Draft recommendation", DRAFT, ""),
        ("doc", "Available sources", SOURCES),

        ("h", "Choose sources by authority and fit"),
        ("p", "A hierarchy helps. The manufacturer's sheet is the [[primary-source]] for the product's stated specification and test conditions. The supplier's guide is the authority for the trade-in offer. The independent report is a credible secondary source for what was observed in its own test, and for nothing wider."),
        ("p", "Authority is not enough. Check fit as well:"),
        ("defs", [
            ("Jurisdiction and variant", "Is it the New Zealand model and a New Zealand offer?"),
            ("Version and date", "Is this the current document?"),
            ("Publication date versus effective date", "The guide was published on 20 January. The offer applies from 1 February. See [[effective-date]]."),
            ("Qualifiers", "\"Up to 18 minutes\" comes with half load, 25 C and new batteries. Drop those and the meaning changes. See [[qualifier]]."),
        ]),
        ("p", "\"Eligible items\" names a product category. It does not remove the trade-in, reseller, date and calculation conditions written next to it."),

        ("h", "Record the evidence and a status"),
        ("table", ["Claim in the draft", "Evidence", "Status"], [
            ["3 kVA, 2U, internal battery pack", "The manufacturer's sheet states all three for this model", "Verified"],
            ["It will run for 18 minutes in an outage", "The maker says up to 18 minutes at half load, 25 C, new batteries. The independent test measured 11 minutes at 80% load", "Contradicted"],
            ["We will get a $300 rebate", "The category qualifies, but the rebate is 15% up to $300 and needs a trade-in and an authorised reseller. Price and trade-in were not supplied", "Partially supported"],
            ["Enough to shut down all 12 servers", "No source states the room's load or the shutdown time", "Unresolved"],
        ]),
        ("p", "A status describes how the available evidence relates to one claim. It is not a grade for the source."),
        ("note", "Unresolved does not mean false", "It means the record does not have enough relevant evidence. It must not be rewritten as a favourable conclusion, and it must not be recorded as contradicted either. Note what fact or source would settle it."),

        ("h", "Revise without hiding the uncertainty"),
        ("out", "Revised recommendation", FIXED, "good"),
        ("p", "The revision does not force the manufacturer and the tester to agree. They measured different conditions, so both stay in, each with its limits. The rebate becomes conditional. The shutdown claim is removed until someone supplies the evidence."),

        ("h", "Keep a record someone else could repeat"),
        ("p", "For each claim, keep: the claim, source title, source date, the date it applies from, the exact supporting passage, your interpretation, and the status. When a spec sheet is revised or an offer changes, you update one row."),
        ("steps", [
            ("Match the basics", "Variant, jurisdiction, units and dates all line up with the claim."),
            ("Read around the quote", "Check the surrounding text before using a figure or quotation."),
            ("Separate conditions", "The source's test conditions on one side, the recommendation's assumed conditions on the other."),
            ("Mark the gaps", "Unresolved, with what would settle it."),
            ("Get review", "Before anyone relies on a high-consequence eligibility or purchase conclusion."),
        ]),
    ],
    "takeaways": [
        "Separate checkable facts from opinions, recommendations and promotional language.",
        "Check consequential, precise, new and changeable claims first.",
        "Match each source to the exact claim: authority, variant, jurisdiction, version, dates and qualifiers.",
        "Use a status for each claim: verified, contradicted, partially supported or unresolved.",
        "Unresolved means not enough evidence. Record what would settle it.",
    ],
    "practice": "Take a vendor datasheet you have used recently. Find one \"up to\" or \"as low as\" figure and write down every condition attached to it. Then ask whether your environment meets those conditions.",
    "quiz": [
        {"q": "What should a reviewer do first when fact-checking a recommendation?", "options": [
            ("Confirm the overall conclusion.", False, "The conclusion depends on the individual claims. Those come first."),
            ("Separate checkable factual claims from opinions and recommendations.", True, "Only factual claims can be tested, so identifying them tells you what to check and how."),
            ("Check every sentence with the same effort.", False, "Opinions and promotional phrases cannot be verified the way facts can."),
            ("Improve the wording.", False, "Editing is not validation."),
        ]},
        {"q": "A draft says a device \"will run for 18 minutes\". The only source says \"up to 18 minutes at half load, at 25 C, with new batteries\". How should the claim be judged?", "options": [
            ("Verified, because the number matches.", False, "The number matches but the claim dropped every condition attached to it."),
            ("Verified, because the manufacturer is the primary source.", False, "Being the primary source does not change what the source actually says."),
            ("Not supported as written, because removing the conditions changes the meaning.", True, "\"Up to\" under stated conditions is a ceiling in one setup. Without the qualifiers it becomes a different, stronger claim."),
            ("Unresolved, because test conditions rarely matter.", False, "The conditions are exactly what define the figure."),
        ]},
        {"q": "A team cannot find enough relevant evidence to confirm a claim. How should it be recorded?", "options": [
            ("Contradicted, since missing evidence suggests it is false.", False, "Missing evidence is not evidence against. Contradicted needs a source that says otherwise."),
            ("Verified, if it seems reasonable.", False, "Seeming reasonable is not verification."),
            ("Partially supported.", False, "That needs some supporting evidence. Here there is not enough to say so."),
            ("Unresolved, with a note of what fact or source would settle it.", True, "It is neither confirmed nor refuted, and the note makes the gap actionable."),
        ]},
        {"q": "A rebate guide was published on 20 January and says the offer runs from 1 February to 30 April. Which TWO statements are correct?", "multi": True, "options": [
            ("A purchase on 25 January qualifies, because the guide was already published.", False, "Publication only tells you when the document became available."),
            ("The effective period, not the publication date, decides which purchases qualify.", True, "Rules apply from their effective date."),
            ("A reviewer should check the dates as well as the source's authority.", True, "An authoritative source for the wrong period does not support the claim."),
            ("Dates do not matter if the source is official.", False, "Authority without fit is not enough."),
        ]},
        {"q": "A manufacturer's figure and an independent test disagree because they measured different conditions. What should the revised brief do?", "options": [
            ("Use the manufacturer's figure, as the primary source.", False, "That hides a relevant independent result."),
            ("Use the independent figure and delete the other.", False, "The manufacturer's figure is still true for its stated conditions."),
            ("Average the two.", False, "An average of two different test conditions describes neither."),
            ("Keep both, each with its conditions stated.", True, "They are not in conflict once the conditions are shown. The reader can see what each one does and does not tell them."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Fact-checking and sources", "sub": "Session 9 of 32. Output evaluation and validation.", "notes": "Sessions 6 and 7 were about one supplied source. Today there are several sources, and they do not all carry the same weight."},
        {"t": "big", "h": "You check claims, not documents.", "p": "A source only helps when it supports the exact claim, conditions included.", "notes": "Everyone has been burned by an 'up to' figure on a datasheet."},
        {"t": "cards", "h": "Four kinds of statement", "cols": 2, "cards": [
            ("Factual claim", "\"The unit is 3 kVA.\" Test it."),
            ("Opinion", "\"A sensible choice.\" Not directly checkable."),
            ("Recommendation", "\"Buy this model.\" Ask what it assumes."),
            ("Promotional language", "\"Excellent value.\" Needs criteria, or it goes."),
        ], "notes": "Only the first one can be verified. The exam asks you to separate them before checking."},
        {"t": "list", "h": "Check these first", "items": [
            ("High consequence", "What happens if it is wrong?"),
            ("Precise", "Exact numbers and conditions."),
            ("New", "The audience has not seen it before."),
            ("Likely to change", "Prices, eligibility, specifications."),
        ], "notes": "Risk-based. Do not spend equal effort on every sentence."},
        {"t": "ask", "h": "\"It will run for 18 minutes in an outage.\" Verified?",
         "pre": "Manufacturer: \"Up to 18 minutes at half load, at 25 C,\nwith new batteries.\"\n\nIndependent test: 11 minutes at 80% load, at 30 C.",
         "answer": "No. The draft dropped every condition, and an independent test under heavier load measured 11 minutes.",
         "notes": "Qualifiers are part of the claim."},
        {"t": "cards", "h": "Authority is not enough. Check fit.", "cols": 2, "cards": [
            ("Jurisdiction and variant", "Right country, right model?"),
            ("Version and date", "Is this the current document?"),
            ("Published versus effective", "Out on 20 January. Applies from 1 February."),
            ("Qualifiers", "\"Up to\", \"eligible items\", \"under test conditions\"."),
        ], "notes": "Published date versus effective date is a favourite exam trap."},
        {"t": "cards", "h": "Give every claim a status", "cols": 2, "cards": [
            ("Verified", "The source states exactly this."),
            ("Contradicted", "A relevant source says otherwise."),
            ("Partially supported", "Some of it holds. Conditions or facts are missing."),
            ("Unresolved", "Not enough evidence. Note what would settle it."),
        ], "notes": "Unresolved is not false and it is not a pass."},
        {"t": "big", "h": "Two sources can disagree and both be right.", "p": "Different test conditions give different numbers. Keep both, with their conditions.", "notes": "Do not average them and do not pick the nicer one."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
