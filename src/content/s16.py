SOURCES = """Backup charter
- Go-live target: 1 March
- First-year hardware or service cost plus setup: no more
  than $120,000
- Usable capacity: at least 40 TB
- Tested full restore of the file server: 4 hours or less
- Retention: 90 days

Capacity report
- Current protected data: 31 TB
- Growth over the last 12 months: 6 TB

Restore test report
- Option North (on-site appliance): 3.5 hours
- Option Cloud (cloud backup service): 5 hours
- Option Colo (appliance in a co-location site): 3 hours

Platform assessment
- North: 48 TB usable, setup estimate $28,000
- Cloud: 60 TB tier, setup estimate $9,000
- Colo: 40 TB usable, setup estimate $35,000

Vendor quotes, unverified
- North: $70,000 first year, delivery in 6 weeks
- Cloud: $66,000 first year, available immediately
- Colo: $58,000 first year, delivery in 8 weeks"""

DECK_SOURCES = """                  North      Cloud      Colo
Capacity          48 TB      60 TB      40 TB      need 40
Tested restore    3.5 h      5 h        3 h        need 4 or less
Setup estimate    $28,000    $9,000     $35,000
Vendor quote      $70,000    $66,000    $58,000    unverified
Delivery          6 weeks    now        8 weeks    unverified

Charter: go-live 1 March, $120,000 first-year cap,
90-day retention."""

PLAN = """Create a research plan for comparing the North, Cloud and Colo
backup options.

Use only the supplied source material. Do not select an option
and do not invent vendor, licence, network or staffing facts.

For each research question, give:
1. the decision criterion,
2. the evidence required,
3. whether the source is authoritative or an interested party,
4. the current finding,
5. the uncertainty or what still needs validating.

Cover budget, capacity, restore time, retention and go-live
timing. End with a coverage check listing missing evidence."""

LEDGER = """Claim: North meets the capacity and restore-time requirements.
Evidence: 48 TB usable; 3.5-hour tested restore.
Source: platform assessment and restore test report.
Uncertainty: 90-day retention at that capacity is not stated.
Implication: confirm retention sizing before treating North as
compliant.

Claim: Cloud does not currently meet the restore-time requirement.
Evidence: 5-hour tested restore against a 4-hour limit.
Source: restore test report.
Uncertainty: no documented change that would shorten it.
Implication: keep Cloud as a conditional option only if a
documented change closes the gap.

Claim: Colo is the lowest quoted first-year price.
Evidence: $58,000, against $66,000 and $70,000.
Source: vendor quotes, unverified.
Uncertainty: quotes are interested-party claims. Colo's 40 TB
leaves no headroom above the 40 TB minimum.
Implication: verify the quote and review capacity against growth."""

BRIEF = """Options
- North: meets reported capacity and restore time. Confirm
  retention sizing, quote and delivery date.
- Colo: meets reported capacity and restore time. No capacity
  headroom. Confirm quote and delivery date.
- Cloud: does not meet the reported restore time. Do not advance
  without a documented change.

Phased sequence
1. Evidence validation (backup team and finance): confirm
   retention sizing, full cost components and vendor terms.
2. Operational review (server team): assess North and Colo
   against growth and restore procedures.
3. Scenario review (service owner): compare outcomes if a quote
   changes, delivery slips or growth is higher.
4. Decision gate (authorised decision-maker): approve, defer or
   reject before any order.
5. Order and implementation: begins only after written
   authorisation."""

SESSION = {
    "id": 16,
    "slug": "research-and-planning",
    "short": "Research and planning",
    "lead": "Claude is good at turning a vague question into a structured investigation and a staged plan. It should organise evidence and uncertainty. It should not turn uncertainty into certainty.",
    "body": [
        ("h", "From a broad question to a research design"),
        ("p", "\"Which backup platform should we move to?\" is too broad to research reliably. It bundles several things: what is feasible, what evidence is needed, which constraints are fixed, what is still uncertain and who can approve a commitment. Claude is useful for breaking that apart before it is asked to recommend anything."),
        ("p", "A [[research-design]] has four parts:"),
        ("defs", [
            ("Research questions", "What has to be learned."),
            ("Boundaries", "What Claude must not assume, or look into beyond the task."),
            ("Source needs", "Which records can support each claim."),
            ("Decision criteria", "How the options will be compared later."),
        ]),
        ("p", "Exploratory research is for generating possibilities, unknowns and questions. It can use preliminary material, including what vendors say, as long as that is labelled. Evidence for a consequential decision has a higher bar. A choice that commits money or a contract should rest on validated records, not on attractive descriptions."),
        ("pull", "Use Claude to organise evidence and uncertainty, not to turn uncertainty into certainty."),

        ("h", "Worked example: three backup options"),
        ("p", "You are preparing a decision brief on three backup options for a customer. Nothing has been chosen, nothing may be ordered, and the vendor quotes have not been verified."),
        ("doc", "Source material", SOURCES),
        ("p", "The charter, capacity report, restore test and platform assessment support defined facts in their own area. The vendor quotes are [[interested-party|interested-party claims]] about price and delivery. They guide follow-up. They do not prove final commercial terms."),

        ("h", "Ask for the plan before the brief"),
        ("p", "Request a research plan first. It gives you a review point before any conclusions appear. The plan maps each question to a source, says what would count as enough evidence, and lists what is unresolved."),
        ("prompt", "Research plan prompt", PLAN),
        ("p", "Review the plan for coverage, not for polish. It should test every charter constraint. Here it has to notice that Cloud misses the restore-time limit on current evidence, and that price and delivery are unverified for all three, so neither budget nor go-live timing is fully validated."),
        ("note", "Evidence standard", "A source can be useful without being authoritative. Label how much authority it has and keep the conclusion within what it can support."),

        ("h", "Keep claims traceable"),
        ("p", "A decision brief should not blend facts, calculations and assumptions into one sentence. Ask for an [[evidence-ledger]] first. Each row keeps the claim, the evidence, the source, the uncertainty and what it means for the plan. A reviewer can then challenge one conclusion without rereading every document."),
        ("out", "Evidence ledger (extract)", LEDGER, "good"),
        ("p", "This matters when Claude adds things up. Quote plus setup gives North $98,000, Cloud $75,000 and Colo $93,000. All are under the $120,000 cap. They are planning figures, not confirmed budget results, because the quotes are unverified and nothing says whether other costs apply."),

        ("h", "Turn validated findings into a phased plan"),
        ("p", "Once the ledger has been reviewed, Claude can lay out options and a sequence. The plan assigns responsibilities by role, shows what depends on what, and keeps a milestone separate from a decision that has been made. A proposed owner is a planning assignment. It is not evidence that anyone has accepted the work."),
        ("out", "Decision brief", BRIEF, "good"),

        ("h", "Scenario planning"),
        ("p", "[[scenario-planning|Scenario planning]] prepares for assumptions that may change. If Colo's delivery slips from eight weeks, does it still make 1 March? If growth runs above 6 TB a year, how soon does Colo's 40 TB run out? Claude can lay out the branches. The organisation has to define the trigger and accept the trade-off."),
        ("steps", [
            ("Tie each claim to a source", "Cost, timing, capacity and restore time."),
            ("Record gaps", "Missing evidence becomes an assumption or a validation task."),
            ("Separate the options", "Compliant options on one side, conditional ones on the other."),
            ("Hold the gate", "An authorised person approves before money is committed. That is the [[decision-gate]]."),
        ]),
    ],
    "takeaways": [
        "Design the research first: questions, boundaries, source needs and decision criteria.",
        "Keep validated records apart from interested-party claims such as vendor quotes.",
        "Use an evidence ledger so every claim stays tied to its source and its uncertainty.",
        "Totals built on unverified figures are planning figures, not confirmed results.",
        "Put an authorised decision gate before any commitment of money.",
    ],
    "practice": "Take a decision your team is weighing. Write three research questions for it, the source that could answer each, and whether that source is authoritative or has an interest in the outcome.",
    "quiz": [
        {"q": "What are the four parts of a research design?", "options": [
            ("Budget, timeline, owner and vendor.", False, "Those are plan details, not what defines the research."),
            ("Research questions, boundaries, source needs and decision criteria.", True, "They say what must be learned, what must not be assumed, what can support each claim and how options will be compared."),
            ("Draft, edit, review and publish.", False, "That is a writing workflow."),
            ("Haiku, Sonnet, Opus and Research.", False, "Those are model families and a product feature."),
        ]},
        {"q": "A vendor's quote says a platform will be delivered in six weeks. How should that be treated in a decision brief?", "options": [
            ("As a confirmed fact, because it is in writing.", False, "It is written by a party that benefits from the sale."),
            ("As false, because vendors exaggerate.", False, "Nothing shows it is false. It is unverified."),
            ("As an interested-party claim that guides follow-up and needs verifying.", True, "Useful for planning questions, not proof of final terms."),
            ("It should be left out entirely.", False, "It is relevant. It just needs the right label."),
        ]},
        {"q": "Why ask Claude for a research plan before asking for the decision brief?", "options": [
            ("It makes the final brief longer.", False, "Length is not the purpose."),
            ("It proves the conclusions in advance.", False, "A plan proves nothing. It organises what must be checked."),
            ("It removes the need for a person to approve.", False, "Approval stays with an authorised person."),
            ("It gives a review point where coverage and source authority can be checked before conclusions appear.", True, "You can see whether every constraint is tested and what is still unverified."),
        ]},
        {"q": "Claude adds an unverified vendor quote to a validated setup estimate and reports a first-year total under the budget cap. Which TWO statements are right?", "multi": True, "options": [
            ("The total is a planning figure, not a confirmed budget result.", True, "One of its inputs is unverified and other costs may apply."),
            ("The total confirms the option is within budget.", False, "A sum is only as reliable as its weakest input."),
            ("The brief should say the quote needs verifying.", True, "Keeping the uncertainty next to the figure stops it being read as settled."),
            ("The arithmetic makes the quote authoritative.", False, "Adding a number to another does not change where it came from."),
        ]},
        {"q": "An option fails one fixed requirement on current evidence, and nobody has documented a way to fix that. How should the brief present it?", "options": [
            ("As a conditional option that should not advance without a documented change.", True, "It is kept visible and clearly separated from options that meet the requirements."),
            ("As equal to the others, to stay neutral.", False, "Treating a non-compliant option as equal hides a material fact."),
            ("As the recommended option if it is cheapest.", False, "Price does not offset a failed fixed requirement."),
            ("It should be deleted with no mention.", False, "Readers should see it was considered and why it is not advancing."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Research and planning", "sub": "Session 16 of 32. Workflow integration and solution design.", "notes": "Useful for anyone who writes options papers or gets asked 'which one should we go with?'"},
        {"t": "big", "h": "Organise the uncertainty. Do not hide it.", "p": "Claude is good at structuring an investigation. It should not turn open questions into settled ones.", "notes": "Ask who has seen an options paper where the cheapest vendor quote was treated as the budget."},
        {"t": "cards", "h": "Design the research first", "cols": 2, "cards": [
            ("Research questions", "What has to be learned."),
            ("Boundaries", "What must not be assumed."),
            ("Source needs", "Which records can support each claim."),
            ("Decision criteria", "How the options will be compared."),
        ], "notes": "'Which backup platform?' hides five separate questions."},
        {"t": "code", "h": "Three options, five sources", "label": "What the sources say", "pre": DECK_SOURCES, "notes": "Ask: which of these would you not trust at face value? The quotes."},
        {"t": "ask", "h": "The vendor says six weeks delivery. Fact?",
         "answer": "An interested-party claim. Useful for follow-up, not proof of final terms. Label it and verify it.",
         "notes": "A source can be useful without being authoritative."},
        {"t": "code", "h": "Ask for the plan before the brief", "label": "Research plan prompt", "pre": PLAN, "notes": "Review the plan for coverage, not polish. Does it test every charter constraint?"},
        {"t": "cards", "h": "An evidence ledger keeps claims honest", "cols": 3, "cards": [
            ("Claim", "One statement."),
            ("Evidence", "The figure or fact behind it."),
            ("Source", "Where it came from, and how much authority that has."),
            ("Uncertainty", "What is not known."),
            ("Implication", "What it means for the plan."),
        ], "notes": "Quote plus setup is a planning figure, not a confirmed budget result."},
        {"t": "steps", "h": "Phased plan", "steps": ["Validate evidence", "Operational review", "Scenario review", "Decision gate", "Order"], "notes": "Nothing is ordered before the gate. A proposed owner is an assignment, not acceptance."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
