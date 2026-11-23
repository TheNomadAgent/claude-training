SOURCES = """Patch compliance export (validated by the reporting team)
Production: 118 servers, 112 compliant (94.9%), 3 reboots pending
UAT:         34 servers,  34 compliant (100%),  0 reboots pending
DR:          22 servers,  17 compliant (77.3%), 5 reboots pending

Incident list
Production: Backup job overran into business hours on 12 November.
DR:         Replication paused for 9 hours on 19 November.

Engineer notes
Production: Backup window extended by one hour from 14 November.
UAT:        Refresh from production completed on schedule.
DR:         Replication resumed the same day."""

ONESHOT = """Using the compliance export, incident list and engineer notes, write a
short monthly service report for Production, UAT and DR. Cover patching,
incidents and anything the customer should know."""

ONESHOT_OUT = """Monthly service report

Production is 94.9% patch compliant with 3 reboots pending. A backup job
overran on 12 November and the backup window has since been extended.

UAT is 100% compliant. The refresh from production completed on schedule.

Overall the estate is in good health."""

INVENTORY = """Required environments: Production, UAT, DR
Required sources: compliance export, incident list, engineer notes

Production: export present, incident present, note present
UAT:        export present, no incident entry supplied, note present
DR:         export present, incident present, note present

Result: all three environments and all three sources are represented.
The missing UAT incident entry must not be reported as "no incidents
in UAT". It means none was supplied."""

STAGED = """1. List the required environments and source types.
2. Extract only the supplied figures, incidents and notes, by environment.
3. Check the extraction against the list. Stop for my review.
4. After I approve, identify compliance gaps and anything unusual.
5. Draft the report narrative using only the approved extraction
   and analysis.
6. Stop for the service manager's approval of the narrative.
7. After approval, format the final report with a section for each
   environment."""

SESSION = {
    "id": 2,
    "slug": "decomposing-complex-tasks",
    "short": "Decomposing complex tasks",
    "lead": "Some jobs are one prompt. Others are a pipeline. The skill is knowing which one you are holding, and where a person needs to look before the next stage runs.",
    "body": [
        ("h", "One step, or several?"),
        ("p", "A one-step task has a clear input, one transformation and a limited output: rewrite this paragraph, pull the action items out of this transcript, summarise this one approved report. Claude can do these in a single request because there is little to depend on and you can check the result directly."),
        ("p", "A complex task combines several sources, decisions, audiences or deliverables. Asking for the finished thing in one large [[one-shot|one-shot prompt]] causes three problems. Missing inputs stay hidden. The output is long and hard to inspect. And an early mistake gets built on, so the final document sounds complete while resting on something nobody checked."),
        ("pull", "Later work should build on checked results, not on guesses."),
        ("p", "[[decomposition|Decomposition]] splits the job into stages, each with a defined result. It makes every [[dependency]] visible: facts are extracted before they are analysed, analysis is checked before it supports a recommendation, and a draft is approved before it is formatted and sent."),

        ("h", "Worked example: the monthly service report"),
        ("p", "You need a monthly report for a customer covering three environments: Production, UAT and DR. You have a compliance export, an incident list and engineer notes. The export is the authority for numbers. The incident list is the authority for what was logged. The notes are context, and only as written. None of them lets Claude infer a cause, an owner or a commitment that is not on the page."),
        ("doc", "Source material", SOURCES),

        ("h", "What the one-shot version does"),
        ("prompt", "One-shot prompt", ONESHOT),
        ("out", "What Claude returned", ONESHOT_OUT, "bad"),
        ("p", "DR is missing. It was the weakest environment, at 77.3% compliance with a nine-hour replication pause. Nothing in the report is false, so a quick read passes it. The closing line, \"in good health\", rests on two environments out of three."),
        ("p", "The prompt named DR. That was not enough, because the prompt gave Claude no separate moment to show that every environment and every source had been covered."),

        ("h", "A pattern that works"),
        ("steps", [
            ("Clarify the objective", "Who reads it, what it must cover, how long, what decision it supports."),
            ("Inventory the inputs", "List every environment, source type and missing item. This is the [[inventory]]."),
            ("Extract the facts", "A structured record of figures and events. No interpretation yet."),
            ("Check completeness", "Compare the record with the inventory before any analysis. The [[completeness-check]]."),
            ("Analyse", "Find the gaps and oddities, working from the approved record."),
            ("Draft and validate", "Write the narrative, then get its wording and emphasis approved."),
            ("Format", "Apply the final layout only once the content is approved."),
        ]),
        ("p", "The stages can vary. What matters is that each one answers a single question and produces an [[intermediate|intermediate deliverable]] somebody can check. The next stage receives that checked result. It does not go back and re-read the raw material mixed with earlier guesses."),

        ("h", "The check that catches the omission"),
        ("p", "The fix for the missing environment is not a longer drafting prompt. It is a separate first step: have Claude build the inventory and check against it, and review that before anything else runs."),
        ("out", "Inventory and completeness check", INVENTORY, "good"),
        ("p", "DR is now flagged as required before a word of the report is written. The check also handles a quieter trap. No UAT incident was supplied, but that does not prove UAT had no incidents. \"None supplied\" and \"none occurred\" are different claims, and only the first is supported."),
        ("note", "Watch for this one", "The exam likes the difference between missing evidence and evidence of nothing. If a source has no entry for something, the safe statement is that no entry was supplied."),

        ("h", "Human gates"),
        ("p", "A [[human-gate]] is not just another prompt. It is a point where a person decides whether Claude should carry on. Put one where:"),
        ("list", [
            "validated figures are about to feed the next stage,",
            "a business decision changes what the message should say,",
            "approval decides whether the content may go out at all.",
        ]),
        ("p", "Claude can organise and compare what you give it. It cannot grant your organisation's approval. And when Claude proposes a plan, that plan is a proposal. It is worth asking for when the route is unclear, but check that it covers every environment, every source, a completeness check and an approval stop before you let it run."),
        ("prompt", "Staged workflow", STAGED),
        ("p", "The first gate comes after extraction and the completeness check. The reporting team validated the export, but you still confirm the extracted values match it before they drive the analysis. The second gate comes after drafting, when the service manager decides whether the emphasis is right for the customer."),
        ("p", "Once both gates are passed, formatting is low risk. Claude can put the approved text into headings or a template. Formatting is not a chance to add new analysis, commitments or explanations."),
    ],
    "takeaways": [
        "Use one prompt for a clear, limited transformation you can check directly.",
        "For anything with several sources or sign-offs, start with an inventory and a completeness check.",
        "Analysis and drafting should run on approved intermediate results.",
        "Stop for a person wherever validation, a business decision or approval changes what happens next.",
    ],
    "practice": "Pick a report or handover you produce regularly. Write its inventory: every item it must cover and every source it draws on. Then mark where a person has to approve something before the next step.",
    "quiz": [
        {
            "q": "Which task is the best fit for a single prompt?",
            "options": [
                ("A quarterly report drawn from five sources that needs finance sign-off.", False, "Several sources and an approval step mean dependencies and a gate. That calls for stages."),
                ("Rewriting one supplied paragraph in plain language.", True, "One input, one transformation, a short output you can check directly."),
                ("A migration recommendation comparing three options for two audiences.", False, "Multiple options and audiences mean separate analysis and drafting work, each worth checking."),
                ("A root cause report built from logs, a timeline and three engineers' notes.", False, "The facts need extracting and checking before anyone reasons about cause."),
            ],
        },
        {
            "q": "An analyst sends every source in one prompt and gets a well-written report covering two of three regions. Nothing in it is false. What would have exposed the problem earliest?",
            "options": [
                ("Asking for a more polished draft.", False, "Polish improves wording. It does not show whether everything was covered."),
                ("Raising the word limit.", False, "A longer report can leave out the same region."),
                ("An input inventory and completeness check before any analysis.", True, "Listing the required regions and sources first, then checking against that list, flags the missing region before a narrative exists to hide it."),
                ("Proofreading the report for tone.", False, "Tone review looks at how it reads, not at what is absent."),
            ],
        },
        {
            "q": "The incident list has no entry for the UAT environment. Which statement can the report safely make?",
            "options": [
                ("\"UAT had no incidents this month.\"", False, "The source does not say that. A missing entry is not proof that nothing happened."),
                ("\"UAT incidents were minor and resolved.\"", False, "This invents incidents and an outcome. Neither is in the material."),
                ("\"No incident entry was supplied for UAT.\"", True, "It reports exactly what the evidence shows and leaves the open question visible."),
                ("\"UAT is the most stable environment.\"", False, "That is a conclusion drawn from an absence of data, not from data."),
            ],
        },
        {
            "q": "In a staged reporting workflow, which TWO points most need a human gate?",
            "multi": True,
            "options": [
                ("After extraction and the completeness check, before the figures feed the analysis.", True, "Everything after this depends on those figures. An error here is carried into every later stage."),
                ("After the narrative is drafted, before it is formatted and sent.", True, "Wording and emphasis for a customer are a business decision. Someone accountable has to approve them."),
                ("Only at the very end, once the report is formatted.", False, "By then any early mistake is built into the whole document and expensive to unpick."),
                ("None. Claude proposed the plan, so it can run through.", False, "A plan is a proposal for work. It is not evidence the work was done correctly, and Claude cannot grant approval."),
            ],
        },
        {
            "q": "You ask Claude how to approach a large task and it returns a tidy seven-step plan. What should you do next?",
            "options": [
                ("Run it. A detailed plan shows the result will be correct.", False, "A plan describes intended work. It says nothing yet about whether the work is right."),
                ("Check the plan covers every required item and source, includes a completeness check and stops for approval, then authorise it.", True, "Reviewing stages, inputs and gates before execution is how you catch a gap while it is still cheap to fix."),
                ("Remove the review stops so it finishes faster.", False, "The stops are where errors get caught. Removing them brings back the one-shot failure."),
                ("Ask for a longer plan with more steps.", False, "More steps do not make a plan more complete. Coverage and gates do."),
            ],
        },
    ],
    "deck": [
        {"t": "title", "h": "Decomposing complex tasks", "sub": "Session 2 of 31. Prompting and task execution.",
         "notes": "Last session was about one prompt done well. Today is about knowing when one prompt is the wrong tool."},
        {"t": "big", "h": "Later work should build on checked results, not guesses.", "p": "An early mistake does not stay small. Every stage after it treats it as fact.",
         "notes": "Relate it to a change plan: nobody runs step 6 before confirming step 2 worked."},
        {"t": "cards", "h": "One step, or several?", "cols": 2, "cards": [
            ("One prompt is fine", "One input, one transformation, a short result you can check. Rewrite a paragraph. Pull actions from one transcript. Summarise one report."),
            ("Break it up", "Several sources, decisions, audiences or deliverables. A monthly report. A migration recommendation. A root cause write-up."),
        ], "notes": "Ask for an example of each from their own week."},
        {"t": "ask", "h": "The prompt asked for Production, UAT and DR. What is wrong with this report?",
         "pre": ONESHOT_OUT,
         "answer": "DR is missing: 77.3% compliant with a nine-hour replication pause. Nothing stated is false, so it passes a quick read.",
         "notes": "Let them find it. Most people check what is there. Few check what is absent."},
        {"t": "steps", "h": "A pattern that works", "steps": ["Clarify", "Inventory", "Extract", "Check", "Analyse", "Draft", "Format"],
         "notes": "Each stage answers one question and hands a checked result to the next. Stages can vary. That rule does not."},
        {"t": "code", "h": "The check that catches it", "label": "Inventory and completeness check", "pre": INVENTORY,
         "notes": "This runs before any writing. DR is flagged as required while fixing it is still cheap."},
        {"t": "big", "h": "\"None supplied\" is not \"none occurred\".", "p": "A missing UAT incident entry tells you about the list. It does not tell you about UAT.",
         "notes": "This distinction turns up in exam scenarios. Wintel version: no alert fired does not mean the server was healthy."},
        {"t": "cards", "h": "Where a person has to stop the line", "cols": 3, "cards": [
            ("Figures feed the next stage", "Confirm extracted values match the validated source before analysis uses them."),
            ("A decision changes the message", "What to emphasise for a customer is a business call."),
            ("Approval decides release", "Claude can organise and compare. It cannot sign off."),
        ], "notes": "A gate is a decision point, not just another prompt."},
        {"t": "ask", "h": "Claude hands you a tidy seven-step plan. Is the job safe to run?",
         "answer": "Not yet. A plan is a proposal. Check it covers every item and source, has a completeness check, and stops for approval before formatting.",
         "notes": "Good moment to mention plan mode in tools they already use."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes, then discuss the select-two question."},
    ],
}
