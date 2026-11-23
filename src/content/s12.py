PORTFOLIO = """Workload A: 3,000 monitoring alert emails a week
Allowed labels: Disk, Service down, Backup failed, Certificate
Requirement: apply one label. Flag anything that does not fit.

Workload B: 60 weekly customer service summaries
Sources: ticket export and approved engineer notes
Requirement: state completed work, open items and stated next
steps only.

Workload C: 5 problem investigations
Sources: event logs, change records, engineer notes, vendor case
Requirement: compare the records, separate established facts
from conflicts, and list questions for the problem manager.
Authority: the problem manager decides the root cause and any
customer commitment."""

SESSION = {
    "id": 12,
    "slug": "model-families",
    "short": "Haiku, Sonnet and Opus",
    "lead": "Picking a model is an operational decision, like sizing a server. You match it to the workload. Bigger is not automatically right, and smaller is not automatically cheaper.",
    "body": [
        ("h", "A model is a capability choice"),
        ("p", "A [[model]] is the underlying AI that does the work. Its capability affects how well Claude reads instructions, uses supplied information, follows a format, reasons through ambiguity and produces something useful. Choosing one is a practical decision. It is not a matter of always taking the newest or strongest."),
        ("p", "Features and models are related and they are different choices. A feature such as a Project organises the work and holds reference material. The model does the analysis or writing inside it. A well set up Project cannot make an unsuitable model ideal for a hard task. A very capable model does not remove the need for clear instructions and review."),
        ("pull", "Choose the least costly capability that reliably meets the task's quality and consequence requirements."),
        ("p", "Haiku, Sonnet and Opus describe broad positions, not a fixed list of version numbers. The exact models on offer, their limits and their performance change. The lasting skill is choosing by the work, then testing that choice on realistic inputs."),

        ("h", "The three families"),
        ("table", ["Family", "Leans toward", "Fits work that is", "Typical tasks"], [
            ["Haiku", "Speed and economy", "Clear, high-volume, low in ambiguity, with stable instructions and an easily checked format", "Fast classification, extraction, simple transformation, routine routing"],
            ["Sonnet", "Balance of capability, speed and cost", "Varied professional work needing coherent writing, several supplied sources, or practical judgement within stated rules", "Summaries, drafting, everyday analysis"],
            ["Opus", "Capability", "Difficult: conflicting records, real ambiguity, several constraints to reconcile, where a better answer is worth extra cost or waiting", "Nuanced synthesis, hard reasoning, complex comparisons"],
        ]),
        ("p", "[[haiku|Haiku]] is not better at everything. Its advantage is handling suitable work efficiently at scale. [[opus|Opus]] should not become the default for anything that feels important. A clear, repetitive task gains little from extra capability if a faster, cheaper family already meets the standard. [[sonnet|Sonnet]] covers the wide middle."),
        ("note", "More than complexity", "Complexity matters. So do volume, how fast a response is needed ([[latency]]), the quality expected, and what happens if there is an error."),

        ("h", "Worked example: one team, three workloads"),
        ("p", "Your team wants to use Claude on three recurring jobs. Each has approved sources. Claude may classify, summarise, compare and point out gaps. It must not invent an event, a customer commitment or a cause the records do not establish."),
        ("doc", "Workloads", PORTFOLIO),
        ("table", ["Workload", "Family", "Reasoning"], [
            ["3,000 fixed-category alert emails", "Haiku", "Low complexity, very high volume and a need for quick routing favour speed and economy. Quality can be sampled against the label list. A wrong label delays a response. It does not authorise anything."],
            ["60 weekly service summaries", "Sonnet", "Moderate volume and normal turnaround. The task needs professional synthesis across two sources. A service manager reviews each summary before it goes out, which lowers the consequence while quality still matters."],
            ["5 conflicting problem investigations", "Opus", "Low volume leaves room for more cost and waiting. Conflicting records need stronger reasoning. An error could feed a wrong root cause or commitment, though the problem manager still decides."],
        ]),
        ("p", "None of this authorises unattended action. For the investigations, Claude produces an evidence-based comparison and open questions, not a root cause. For the alert routing, someone reviews samples, looks at the unmatched messages and watches whether the label list still fits what is coming in."),

        ("h", "Capability does not replace testing"),
        ("p", "A family label is a starting point, not a guarantee. A stronger model can still misread an instruction, miss a source detail, skip a required field or state something plausible and false. A lighter model can do very well on a narrow task with clear sources and rules. Both need evaluating."),
        ("steps", [
            ("Use realistic samples", "Include incomplete, unusual and conflicting records, not only tidy ones."),
            ("Check the substance", "Factual grounding, required format, omissions and unsupported claims."),
            ("Weigh it against time and cost", "At the volume the task actually runs at."),
            ("Retest on change", "When instructions, source formats or the available models change."),
        ]),

        ("h", "Two common mistakes"),
        ("defs", [
            ("Defaulting to maximum capability", "Putting every task on the strongest family because the work seems important. It raises cost and waiting time without improving a simple result."),
            ("Defaulting to minimum cost", "Using a fast family for work whose ambiguity, conflicting evidence or consequence needs more capable analysis and closer review."),
        ]),
        ("p", "A third: treating a family name as a permanent specification. What is available, and exactly what each model can do, moves faster than the family positions. Confirm which models your environment offers, then evaluate those against the work. Do not rely on an old version name or last year's result."),
    ],
    "takeaways": [
        "A model does the work. A feature organises it. They are separate choices.",
        "Haiku: clear, high-volume work where speed and economy matter.",
        "Sonnet: the balanced choice for most professional work.",
        "Opus: difficult reasoning where a better answer justifies more cost, time and review.",
        "Family names are starting points. Test on realistic samples and retest when anything changes.",
    ],
    "practice": "Pick three recurring jobs your team does. For each, write the volume, how fast it is needed, how ambiguous it is and what happens if it is wrong. Then say which family you would try first and what you would test.",
    "quiz": [
        {"q": "A team must label 3,000 alert emails a week using four fixed categories. A wrong label delays a response slightly. Which family is the best starting point?", "options": [
            ("Opus, because alerts are important.", False, "Importance alone does not justify the most capable family for a clear, repetitive task."),
            ("Sonnet, as the default.", False, "It would work, but the task is narrow and high-volume, which is the case for a faster family."),
            ("Haiku.", True, "Low complexity, high volume and a need for speed favour the fast, economical family, with sampling to check quality."),
            ("Whichever is newest.", False, "Newness is not a selection criterion."),
        ]},
        {"q": "Five investigations each involve logs, change records and notes that contradict one another. An error could support a wrong commitment to a customer. Which family fits, and what else is needed?", "options": [
            ("Haiku, to keep costs down.", False, "Conflicting evidence and real consequence call for more capable analysis."),
            ("Opus, with a person still making the decision.", True, "Low volume leaves room for the cost, the reasoning is hard, and the consequence means human review stays in place."),
            ("Opus, and the output can be sent without review.", False, "Capability does not replace review where the consequence is high."),
            ("Any family, since features matter more than models.", False, "Features organise the work. The model still has to be able to do it."),
        ]},
        {"q": "Which statement about models and features is correct?", "options": [
            ("A well-configured Project makes any model suitable for any task.", False, "A feature cannot supply capability the model lacks."),
            ("The most capable model removes the need for clear instructions.", False, "Every model still needs clear instructions and review."),
            ("Features and models are the same choice under different names.", False, "They are related and separate."),
            ("A feature organises the work and the model performs it.", True, "Both matter and neither substitutes for the other."),
        ]},
        {"q": "Which TWO are sound reasons to retest a model choice?", "multi": True, "options": [
            ("The instructions or source formats have changed.", True, "A change to inputs or rules can change how well any model performs."),
            ("A colleague prefers a different family.", False, "Preference is not evidence."),
            ("The models available in your environment have changed.", True, "Family positions are stable but the actual models move. An old result may not hold."),
            ("The first sample output looked impressive.", False, "One good output is not a reason to retest, or to stop testing."),
        ]},
        {"q": "A team assigns every task to the most capable family because \"all our work is important\". What is the main problem?", "options": [
            ("It breaks a licensing rule.", False, "Nothing here involves licensing."),
            ("It raises cost and response time without improving simple results.", True, "Straightforward tasks gain little from extra capability when a lighter family already meets the standard."),
            ("The most capable family makes more errors.", False, "That is not the issue. Over-provisioning is."),
            ("It removes the need for testing.", False, "No family removes the need for testing."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Haiku, Sonnet and Opus", "sub": "Session 12 of 32. Product and model selection.", "notes": "Frame it as sizing: you would not put a file server on the biggest host in the cluster by default."},
        {"t": "big", "h": "The model does the work. The feature organises it.", "p": "A good Project cannot fix an unsuitable model, and a strong model still needs clear instructions.", "notes": "The exam checks they know these are separate choices."},
        {"t": "cards", "h": "Three families, three positions", "cols": 3, "cards": [
            ("Haiku", "Speed and economy. Clear, high-volume work with a format that is easy to check."),
            ("Sonnet", "Balance. Most professional work: writing, summaries, everyday analysis."),
            ("Opus", "Capability. Conflicting records, real ambiguity, hard reasoning."),
        ], "notes": "These are positions, not version numbers. The actual model names change. There are also tiers the exam does not cover."},
        {"t": "list", "h": "Five things decide the choice", "items": [
            ("Complexity", "How ambiguous or conflicting is the input?"),
            ("Volume", "How many, how often?"),
            ("Speed", "How quickly is the answer needed?"),
            ("Quality", "What does good enough look like?"),
            ("Consequence", "What happens if it is wrong?"),
        ], "notes": "Not just complexity. A simple task at huge volume and a hard task done five times a week are different decisions."},
        {"t": "ask", "h": "Which family for each workload?",
         "pre": "A. 3,000 alert emails a week, four fixed labels\nB. 60 weekly service summaries from tickets and notes,\n   reviewed by a service manager\nC. 5 investigations with conflicting logs and change records",
         "answer": "A Haiku. B Sonnet. C Opus, with the problem manager still deciding.",
         "notes": "Push on C: Opus does not mean no review."},
        {"t": "big", "h": "Choose the least costly capability that reliably meets the need.", "p": "Not the newest. Not the strongest. Not the cheapest.", "notes": "This sentence is close to how the exam phrases it."},
        {"t": "cards", "h": "Two ways to get it wrong", "cols": 2, "cards": [
            ("Always the strongest", "More cost and waiting, no better result on simple work."),
            ("Always the cheapest", "Ambiguous or high-consequence work gets shallow analysis."),
        ], "notes": "Third mistake: treating a family name as a fixed spec. Check what is actually available."},
        {"t": "steps", "h": "Test the choice", "steps": ["Realistic samples", "Check substance", "Weigh time and cost", "Retest on change"], "notes": "Include the messy records in the sample, not only the tidy ones."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
