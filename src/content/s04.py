FACTS = """Callout fact pack: low disk space alerts

Scope
- 61 Windows servers under after-hours monitoring
- An alert fires at 10% free space on any volume

Last quarter (1 August to 31 October)
- 41 after-hours callouts came from disk alerts:
  log file growth: 23; temp and cache files: 11; real data growth: 7
- No automated cleanup was in place.

Constraints
- No new tooling spend above $500.
- Alert thresholds cannot change without change board approval.
- Recommendation due to the service manager by 5 December."""

P_AN = """Using only the fact pack, analyse which callout cause to tackle first:
log file growth, temp and cache files, or real data growth.

Compare them by callout count, what evidence is missing, fit with the
$500 cap, and whether a fix would need a threshold change. Do not infer
why any of them happens. List assumptions separately. End with a ranked
recommendation and a short reason."""

O_AN = """1. Log file growth: 23 of 41 callouts. Largest share. No cost stated.
2. Temp and cache files: 11 of 41. Second. No cost stated.
3. Real data growth: 7 of 41. Smallest. Cleanup would not address it.

Assumptions: last quarter is a reasonable guide for planning. It is
not a forecast.
Recommendation: start with log file growth. Hold any spend until
research shows what a fix costs."""

P_RE = """Research what the fact pack can establish about disk alert callouts
for the December recommendation.

Use only the fact pack, and treat last quarter as the most recent
evidence available. Cite each finding by fact pack heading. List
unresolved questions separately from findings. Do not use outside
sources and do not estimate future callouts."""

O_RE = """Findings
- 41 after-hours callouts came from disk alerts. [Last quarter]
- Log growth caused 23, temp and cache 11, data growth 7. [Last quarter]
- No automated cleanup was in place. [Last quarter]

Unresolved
- No source says which servers the callouts came from.
- No source says why logs grew or which applications wrote them.
- No source gives the cost of any fix beyond the $500 cap."""

P_BR = """Brainstorm 12 ways to reduce after-hours disk alert callouts, using
the fact pack.

Spread them across cleanup automation, alert handling, capacity, and
process. Respect the $500 cap and the threshold rule. Aim for clearly
different approaches, including some that need research first. Do not
rank, reject or recommend anything yet."""

O_BR = """- Scheduled log cleanup on the affected servers
- Log rotation settings reviewed per application
- Scheduled temp and cache cleanup
- Alert routed to a morning queue when free space is stable
- A business-hours weekly free-space review
- Runbook step so the first responder can clear logs safely
- Capacity request for volumes with real data growth
- Trend report to spot volumes that will alert next month
- Propose a threshold change to the change board
- Compress old logs before deleting them
- Move application logs to a separate volume
- Monthly check that cleanup jobs are still running"""

P_DR = """Draft an email to the service manager recommending a first step on
disk alert callouts.

Purpose: get agreement to pilot scheduled log cleanup. State the 41
callouts last quarter and the three-way split. Do not promise a
reduction figure and do not propose a threshold change. Format: subject
line, then a body under 150 words in plain language, ending with one
clear request."""

O_DR = """Subject: Proposal to pilot scheduled log cleanup

Last quarter we had 41 after-hours callouts from low disk space alerts.
Log file growth accounted for 23, temp and cache files for 11, and real
data growth for 7. No automated cleanup was in place.

I recommend we pilot scheduled log cleanup first, as it addresses the
largest group. This needs no change to alert thresholds. I do not yet
have evidence for how many callouts it would remove, so the pilot would
measure that.

Could you approve a pilot so we can report results in the new year?"""

SESSION = {
    "id": 4,
    "slug": "adapting-prompts",
    "short": "Adapting prompts to the job",
    "lead": "The same facts can feed four different jobs. Each job needs different instructions, and each is judged by a different standard.",
    "body": [
        ("h", "Say what kind of work it is"),
        ("p", "A prompt should describe the kind of work Claude has to do, not only the topic. There are four kinds the exam cares about."),
        ("defs", [
            ("Analysis", "Narrows evidence you already have into a decision. [[analysis|Definition.]]"),
            ("Research", "Finds evidence and shows where each piece came from. [[research|Definition.]]"),
            ("Drafting", "Turns approved facts into communication for a defined reader. [[drafting|Definition.]]"),
            ("Brainstorming", "Produces a wide spread of options before anyone chooses. [[brainstorming|Definition.]]"),
        ]),
        ("p", "They can all use the same source material and still pull in different directions. \"State only conclusions the evidence supports\" protects an analysis from overclaiming. The same instruction strangles a brainstorm, where the whole point is variety and an untested idea may be worth a look later."),
        ("pull", "Name the work product first. Then set instructions and a standard that fit it."),

        ("h", "One fact pack, four prompts"),
        ("p", "Your team keeps getting called out after hours for low disk space alerts. You have to recommend an approach to the service manager."),
        ("doc", "Fact pack", FACTS),
        ("p", "The fact pack supports statements about scope, last quarter's counts and the constraints. It does not say why logs grew, what any fix costs, or what next quarter will look like. Those are open questions or jobs for later research."),

        ("h", "Analysis: start from the decision"),
        ("p", "An analysis prompt names the decision, the things being compared, the dimensions to compare them on, the limits of the source, and how to lay out the reasoning. You are not asking Claude to discover facts. You are asking it to make the supplied facts useful for a bounded choice."),
        ("prompt", "Analysis prompt", P_AN),
        ("out", "What Claude returned", O_AN, ""),

        ("h", "Research: make evidence traceable"),
        ("p", "A research prompt defines a question and a boundary for gathering evidence: the scope, how recent a source has to be ([[recency]]), which sources count, how to cite them ([[citation]]), and how to report what could not be found."),
        ("prompt", "Research prompt", P_RE),
        ("out", "What Claude returned", O_RE, ""),
        ("p", "The \"Unresolved\" list is a result in its own right. It tells you what evidence you would need before making a stronger claim."),

        ("h", "Brainstorming: go wide, judge later"),
        ("p", "A brainstorming prompt asks for possibilities, not one justified conclusion. Categories stop the list clustering around the obvious tactic. Hard constraints keep the ideas usable. Holding back evaluation stops early criticism from shrinking the set."),
        ("prompt", "Brainstorming prompt", P_BR),
        ("out", "What Claude returned", O_BR, ""),
        ("p", "Note that \"propose a threshold change to the change board\" is on the list. The constraint says thresholds cannot change *without* approval, so asking for approval is a legitimate option. A brainstorm respects constraints. It does not have to avoid everything near them."),

        ("h", "Drafting: write for the reader"),
        ("p", "Drafting comes after the facts and the direction are agreed. The prompt defines the reader, the purpose, the voice, what may and may not be claimed, the format, and what to revise for."),
        ("prompt", "Drafting prompt", P_DR),
        ("out", "What Claude returned", O_DR, "good"),

        ("h", "Judge each one by the right standard"),
        ("table", ["Kind of work", "The prompt defines", "It is good when"], [
            ["Analysis", "Decision, options, comparison dimensions, assumptions, reasoning structure", "The comparison fits the decision, the reasoning is visible, and conclusions stay inside the evidence"],
            ["Research", "Question, scope, recency, acceptable sources, citations, how to report unknowns", "Every finding traces to an acceptable source and the unknowns are listed"],
            ["Drafting", "Reader, purpose, voice, factual limits, format, revision criteria", "It fits the audience, purpose, voice, facts and format"],
            ["Brainstorming", "Quantity, categories, hard constraints, no ranking yet", "The ideas are varied, respect the constraints and have not been filtered early"],
        ]),
        ("p", "Do not mark all four as if they were final recommendations. The analysis ranks, because ranking was asked for. The research refuses to turn last quarter into a forecast. The email gives numbers and one request without adding anything the fact pack cannot support. The brainstorm is a good brainstorm because it is varied, not because each idea is proven."),
        ("note", "Common mismatch", "\"Give only verified conclusions\" belongs in research and analysis. In a brainstorm, apply it to the hard constraints only, never as a filter on untested ideas."),

        ("h", "Chain them in a sensible order"),
        ("steps", [
            ("Brainstorm", "Get a broad set of options while enforcing the constraints that cannot move."),
            ("Research", "Look into the promising ones, with stated source and recency rules."),
            ("Analyse", "Compare the evidence against the real decision criteria."),
            ("Draft", "Write for the reader, using approved facts and the chosen direction."),
        ]),
        ("p", "This is [[chaining]], and a person reviews at each handover. Someone decides which ideas are worth researching, whether the sources are good enough, whether each [[assumption]] is acceptable, and whether the draft can go out."),
    ],
    "takeaways": [
        "Analysis makes a decision: define the options, the comparison and the assumptions.",
        "Research makes evidence traceable: set scope, sources, recency, citations and how to report unknowns.",
        "Drafting serves a reader: set purpose, voice, factual limits and format.",
        "Brainstorming widens the options: ask for variety first, evaluate later.",
        "Chain them brainstorm, research, analyse, draft, with a person checking each handover.",
    ],
    "practice": "Take one problem your team is working on. Write four one-line prompts for it: one each for brainstorming, research, analysis and drafting. Check that each asks for a different kind of result.",
    "quiz": [
        {
            "q": "Which instruction belongs in a brainstorming prompt?",
            "options": [
                ("\"State only conclusions supported by the supplied evidence.\"", False, "That protects analysis from overclaiming. In a brainstorm it removes the untested ideas you are looking for."),
                ("\"Cite each finding by source heading.\"", False, "Citations make research traceable. Brainstormed ideas are not findings."),
                ("\"Give 12 clearly different approaches across four categories. Do not rank or reject any yet.\"", True, "Quantity, spread across categories and delayed evaluation are what keep a brainstorm wide."),
                ("\"Keep the body under 150 words with a subject line.\"", False, "That is a format requirement for a draft, not for generating options."),
            ],
        },
        {
            "q": "A research output is good when:",
            "options": [
                ("it ends with a single confident recommendation.", False, "Recommending is the job of analysis. Research supplies and traces the evidence."),
                ("each finding can be traced to an acceptable source, and what remains unknown is listed.", True, "Traceability and an honest list of gaps are the standard for research."),
                ("it contains as many ideas as possible.", False, "Breadth of ideas is the standard for brainstorming."),
                ("it reads well for a non-technical audience.", False, "Fit to a reader is the standard for drafting."),
            ],
        },
        {
            "q": "You ask for an analysis using only the fact pack. Claude writes: \"Log growth is caused by verbose debug logging left on after a release.\" What is the problem?",
            "options": [
                ("The analysis is too short.", False, "Length is not the issue. One sentence can overstep the evidence."),
                ("It should have included more ideas.", False, "Generating ideas is brainstorming. The request was for analysis."),
                ("It states a cause the fact pack does not support.", True, "The fact pack gives counts, not causes. This is a conclusion outside the evidence boundary, which is the main failure for analysis."),
                ("It should have been written as an email.", False, "Format belongs to drafting and is unrelated to the unsupported claim."),
            ],
        },
        {
            "q": "A team needs options, evidence, a decision and then a message to the customer. What order should the four kinds of prompt run in?",
            "options": [
                ("Draft, analyse, research, brainstorm.", False, "Drafting first means writing a message before any decision or evidence exists."),
                ("Research, brainstorm, draft, analyse.", False, "Research needs options to investigate, and a draft should follow the decision."),
                ("Analyse, brainstorm, research, draft.", False, "There is nothing to analyse until options exist and evidence has been gathered."),
                ("Brainstorm, research, analyse, draft.", True, "Widen the options, gather evidence on the promising ones, decide, then communicate."),
            ],
        },
        {
            "q": "Which TWO items belong in a drafting prompt?",
            "multi": True,
            "options": [
                ("The intended reader and the purpose of the message.", True, "A draft is judged by whether it helps a particular reader understand and act."),
                ("How recent a source must be to count.", False, "Recency rules belong in a research prompt."),
                ("The required format and length.", True, "Layout and length are part of what makes a draft fit for its use."),
                ("An instruction not to rank the ideas.", False, "Holding back evaluation is a brainstorming instruction."),
            ],
        },
    ],
    "deck": [
        {"t": "title", "h": "Adapting prompts to the job", "sub": "Session 4 of 31. Prompting and task execution.",
         "notes": "Last one in the prompting domain. After today they have the whole 14% of the exam that covers prompting."},
        {"t": "big", "h": "Same facts. Four different jobs.", "p": "Analysis, research, drafting and brainstorming need different instructions, and each is judged differently.",
         "notes": "Most poor prompts name a topic and never say which of these four they want."},
        {"t": "code", "h": "Today's fact pack", "label": "Low disk space alerts", "pre": FACTS,
         "notes": "Ask what it does not tell us: why logs grew, what a fix costs, what next quarter looks like."},
        {"t": "cards", "h": "What each one is for", "cols": 2, "cards": [
            ("Analysis", "Narrows evidence you already have into a decision."),
            ("Research", "Finds evidence and shows where each piece came from."),
            ("Drafting", "Turns approved facts into a message for a defined reader."),
            ("Brainstorming", "Produces a wide spread of options before anyone chooses."),
        ], "notes": "One press per card."},
        {"t": "cards", "h": "What good looks like", "cols": 2, "cards": [
            ("Analysis", "The comparison fits the decision. Reasoning is visible. Conclusions stay inside the evidence."),
            ("Research", "Every finding traces to an acceptable source. Unknowns are listed."),
            ("Drafting", "Fits the reader, purpose, voice, facts and format."),
            ("Brainstorming", "Varied, within the hard constraints, and not filtered early."),
        ], "notes": "The exam often shows an output and asks whether it is good. The answer depends on which of these it was meant to be."},
        {"t": "ask", "h": "\"Only give verified conclusions.\" Where does that help, and where does it hurt?",
         "answer": "It helps analysis and research. In a brainstorm it kills the untested ideas you wanted. Apply it there to hard constraints only.",
         "notes": "Good discussion point. Ask who has had a brainstorm come back with three safe, obvious ideas."},
        {"t": "compare", "h": "Same facts, opposite instructions",
         "left_label": "Brainstorming", "left": "Give 12 clearly different ways to reduce callouts.\nSpread them across cleanup, alert handling,\ncapacity and process.\nRespect the $500 cap and the threshold rule.\nDo not rank, reject or recommend yet.",
         "right_label": "Analysis", "right": "Using only the fact pack, decide which cause\nto tackle first.\nCompare by callout count, missing evidence,\ncost fit and threshold impact.\nDo not infer causes. List assumptions.\nEnd with a ranked recommendation.",
         "notes": "One says do not rank. The other says end with a ranking. Both are right for their job."},
        {"t": "steps", "h": "Chain them in this order", "steps": ["Brainstorm", "Research", "Analyse", "Draft"],
         "notes": "A person reviews at every arrow: which ideas to research, whether sources are good enough, whether assumptions hold, whether the draft can go out."},
        {"t": "ask", "h": "The analysis says: \"Log growth is caused by verbose debug logging.\" What went wrong?",
         "answer": "The fact pack gives counts, not causes. Claude stepped outside the evidence. For analysis, that is the main failure.",
         "notes": "Ties back to session 1: evidence boundary. And to their day job: do not state a root cause without evidence."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. This closes the prompting domain."},
    ],
}
