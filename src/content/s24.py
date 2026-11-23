SOURCES = """Superseded configuration, effective 15 January
Server Build Catalogue v1: Standard build, 2 vCPU and 8 GB.
Premium build, 4 vCPU and 16 GB.
Build Request Guide v2: an approved build request stays valid
for 30 days.
Build Approval Policy v1: team leads may approve sizing changes
up to 8 vCPU. Platform manager approval is required for 9 to
16 vCPU.

Current authoritative sources, effective 1 July
Server Build Catalogue v2.1: General Purpose build, 4 vCPU and
16 GB. Database build, 8 vCPU and 64 GB.
Build Request Guide v4: an approved build request stays valid
for 14 days.
Build Approval Policy v3: every non-catalogue build requires
Architecture Review. Any build above 16 vCPU also requires
Capacity approval before it is scheduled."""

INSTR = """Prepare internal build request summaries using only the current
Project knowledge. Use the terms General Purpose build and
Database build. State catalogue sizing and the 14-day request
validity when asked.

For any non-catalogue build, state that Architecture Review is
required. If the build is above 16 vCPU, also state that Capacity
approval is required before it is scheduled.

Do not use superseded build names, sizing, validity periods or
approval thresholds. If a requested fact is absent from current
Project knowledge, state that it was not supplied."""

TESTS = """1. Ask for the sizing of both catalogue builds.
   Expected: 4 vCPU and 16 GB, 8 vCPU and 64 GB.

2. Ask how long an approved request stays valid.
   Expected: 14 days.

3. Ask for guidance on a 24 vCPU build with 96 GB.
   Expected: Architecture Review, and Capacity approval before
   scheduling.

4. Ask for a summary of a Premium build.
   Expected: the superseded term is not used and no replacement
   details are invented."""

OUT = """A 24 vCPU build with 96 GB is not a catalogue build, so
Architecture Review is required. Because it is above 16 vCPU,
Capacity approval is also required before the build is scheduled."""

SESSION = {
    "id": 24,
    "slug": "maintaining-configurations",
    "short": "Maintaining configurations",
    "lead": "A Project that worked in January can be confidently wrong by July. Nobody broke it. The standards moved and the Project did not.",
    "body": [
        ("h", "Configuration quality changes over time"),
        ("p", "A configured Claude workflow is its instructions, its knowledge sources, any connected systems, its access permissions and its test results. It can work well on the day it is built and become unreliable when standards, policies, teams, terminology or source systems change. Stale configuration produces confident output based on information that used to be correct."),
        ("p", "Maintenance is not editing a prompt when an answer looks off. It is a controlled process:"),
        ("steps", [
            ("Identify the authoritative change", "What changed, and which source says so."),
            ("Assess what depends on it", "Instructions, knowledge, permissions, tests."),
            ("Update those elements", "Replace, do not stack."),
            ("Document the reason", "So the next reviewer knows why a rule exists."),
            ("Test the changed configuration", "Before colleagues go back to using it."),
        ]),
        ("pull", "Configuration should reflect current authoritative sources, not a pile of historical exceptions."),

        ("h", "Worked example: an inherited build-request Project"),
        ("p", "You inherit a Project the team uses to prepare internal build request summaries. It still carries the old build names, sizing, request validity and approval thresholds. Current documents have replaced all three sources. You need to update it, record each change and its owner, remove the obsolete rules and run [[regression|regression tests]] before anyone uses it again."),
        ("doc", "Source material", SOURCES),
        ("p", "Old facts are not kept just because they were in the previous instructions or uploads."),

        ("h", "Assign owners and define change triggers"),
        ("p", "One role should own the overall configuration and coordinate its upkeep. That does not mean writing every source document. It means knowing which sources are authoritative, keeping the register, requesting access changes, and deciding when the Project is ready for release."),
        ("defs", [
            ("Source owner", "Confirms the factual content of a knowledge source."),
            ("Permission owner", "Confirms who may access a connected system or the Project's material."),
            ("Evaluation owner", "Confirms the test set is still useful after the workflow changes."),
        ]),
        ("p", "Define your [[change-trigger|change triggers]] before an error shows up. Useful ones: a scheduled review, a policy revision, a product release, a recurring error, a source being replaced, a team change, and a connector permission change. Scheduled reviews catch quiet decay. Event triggers respond when a known dependency moves."),
        ("note", "Maintenance principle", "A new version of a source is a review trigger, even if nobody has reported a wrong answer yet."),

        ("h", "Use a configuration register"),
        ("p", "A [[config-register|configuration register]] is a maintained record of what the Project relies on and who is accountable for each part. It makes dependencies visible, which matters most when one policy feeds several workflows. Keep it with the workflow documentation, not in somebody's chat history."),
        ("table", ["Item", "Owner", "Version and date", "Next review", "Used for"], [
            ["Project instructions", "Wintel technical lead", "Configuration v2, 1 July", "1 October", "Build request summaries"],
            ["Build catalogue knowledge", "Platform engineering", "v2.1, 1 July", "1 October", "Build names and sizing"],
            ["Guide and approval knowledge", "Platform policy owner", "Guide v4, Policy v3, 1 July", "1 October", "Validity and approval guidance"],
            ["Connector permissions and test set", "Access administrator and technical lead", "Permissions v2, Test set v1, 1 July", "1 October", "Source access and release checks"],
        ]),

        ("h", "Repair, simplify and test before release"),
        ("p", "First replace the three old knowledge documents with the current catalogue, guide and policy. Then revise the instructions. The right repair is **not** to add a note such as \"ignore the previous approval rule\". Both rules would still be there, and that is ambiguity waiting to happen. Obsolete names, facts and approval guidance are removed."),
        ("p", "The change record says the catalogue, guide and policy were replaced on 1 July. You own the instruction update. The source owners stay responsible for the accuracy of their documents. That keeps accountability for the configuration separate from authority over the facts."),
        ("prompt", "Updated Project instructions", INSTR),
        ("p", "A small regression set checks the behaviour most likely to break. It does not prove every request will be right. It does give you a repeatable release gate, and you rerun the same prompts after every material change."),
        ("doc", "Regression set", TESTS),
        ("out", "Response to test 3", OUT, "good"),

        ("h", "Maintenance, troubleshooting or outage?"),
        ("table", ["Situation", "What it is", "Narrow response"], [
            ["The authoritative facts or governing wording changed", "Content maintenance", "Update the dependent configuration and rerun the regression set"],
            ["Sources are current, and the request's wording, structure or constraints give a poor result", "Prompt troubleshooting", "Fix the prompt or instruction and rerun the same test. Leave current knowledge alone"],
            ["Claude or a connected source is unavailable, or access fails", "Product or service outage", "Follow the support and continuity process and record the symptom. Do not rewrite policy instructions"],
        ]),
        ("p", "An availability problem is not evidence that your content is stale."),
    ],
    "takeaways": [
        "Instructions, knowledge, permissions and tests can all go stale.",
        "Give the configuration an owner, and give each source, permission and test set its own.",
        "Define change triggers up front. A new source version is one, with or without complaints.",
        "Replace obsolete content. Do not stack \"ignore the previous rule\" on top of it.",
        "Run a small regression set before colleagues use the changed Project.",
    ],
    "practice": "Pick a runbook, template or Project your team reuses. Write a four-row register for it: item, owner, version and date, next review. Then list three events that should trigger a review.",
    "quiz": [
        {"q": "A Project's approval rule has been replaced by a new policy. What is the correct repair?", "options": [
            ("Add \"ignore the previous approval rule\" to the instructions.", False, "Both rules stay in place, which creates ambiguity."),
            ("Leave it until someone reports a wrong answer.", False, "A new source version is already a review trigger."),
            ("Add the new policy alongside the old one in knowledge.", False, "Conflicting sources would sit side by side."),
            ("Remove the old rule and its source, add the current ones, and rerun the regression set.", True, "Obsolete content is replaced, and the change is tested before release."),
        ]},
        {"q": "What is a configuration register for?", "options": [
            ("Storing every chat held in the Project.", False, "It records dependencies and ownership, not conversations."),
            ("Recording what the Project relies on, who owns each part, versions and review dates.", True, "It makes dependencies and accountability visible to the next maintainer."),
            ("Replacing the need to test.", False, "The register documents. Testing is still required."),
            ("Listing users' favourite prompts.", False, "That is not what it tracks."),
        ]},
        {"q": "Claude cannot reach an approved connected source and reports an access failure. What kind of problem is this?", "options": [
            ("Content maintenance. Rewrite the policy instructions.", False, "Changing instructions will not fix an availability problem."),
            ("Prompt troubleshooting. Reword the request.", False, "The wording is not the cause."),
            ("An outage or access problem. Follow the support and continuity process.", True, "Record the symptom and do not treat it as evidence that content is stale."),
            ("Proof the knowledge is out of date.", False, "Availability says nothing about whether content is current."),
        ]},
        {"q": "Which TWO are sensible change triggers for reviewing a Project's configuration?", "multi": True, "options": [
            ("A source document is replaced by a new version.", True, "A known dependency has changed."),
            ("Someone on the team prefers a different font.", False, "That has no bearing on the configuration's accuracy."),
            ("A scheduled quarterly review falls due.", True, "Scheduled reviews catch quiet decay."),
            ("The Project was used ten times this week.", False, "Usage alone is not a change in a dependency."),
        ]},
        {"q": "After a material change, what does a small regression set give you?", "options": [
            ("Proof that every possible request will be answered correctly.", False, "It samples critical behaviour. It is not proof of everything."),
            ("A repeatable release gate for the behaviour most likely to break.", True, "The same prompts, rerun after each material change, show whether critical behaviour held."),
            ("A replacement for source owners.", False, "Owners still confirm the facts."),
            ("A way to avoid documenting the change.", False, "The reason for the change is still recorded."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Maintaining configurations", "sub": "Session 24 of 32. Configuration and knowledge management.", "notes": "Last session in this domain. Treat a Project like any other config item: it has an owner, a version and a review date."},
        {"t": "big", "h": "Nobody broke it. The standards moved and the Project did not.", "p": "Stale configuration gives confident answers that used to be right.", "notes": "Same as an out-of-date runbook, except this one answers back fluently."},
        {"t": "compare", "h": "What the Project still says, and what is true now",
         "left_label": "In the Project, from 15 January", "left": "Standard build: 2 vCPU, 8 GB\nPremium build: 4 vCPU, 16 GB\nRequests valid for 30 days\nTeam leads approve up to 8 vCPU",
         "right_label": "Current, from 1 July", "right": "General Purpose build: 4 vCPU, 16 GB\nDatabase build: 8 vCPU, 64 GB\nRequests valid for 14 days\nNon-catalogue builds need Architecture Review\nAbove 16 vCPU also needs Capacity approval",
         "notes": "Every single fact changed, including the names."},
        {"t": "steps", "h": "Maintenance is a process", "steps": ["Identify the change", "Find what depends on it", "Update", "Document why", "Test"], "notes": "Not 'edit the prompt when an answer looks off'."},
        {"t": "ask", "h": "Why not just add \"ignore the previous approval rule\"?",
         "answer": "Because both rules are still there. Remove the old one. Replace, do not stack.",
         "notes": "Exam favourite. Accumulated exceptions are the opposite of maintenance."},
        {"t": "cards", "h": "Owners and triggers", "cols": 2, "cards": [
            ("Owners", "One for the configuration. One each for sources, permissions and the test set."),
            ("Scheduled trigger", "A review date. Catches quiet decay."),
            ("Event triggers", "Policy revision, product release, source replaced, team change, permission change, recurring error."),
            ("The register", "Item, owner, version and date, next review, what it is used for."),
        ], "notes": "A new source version is a trigger even with zero complaints."},
        {"t": "code", "h": "A regression set is a release gate", "label": "Regression set", "pre": TESTS, "notes": "Four prompts. Test 4 checks the old name does not creep back and nothing is invented to replace it."},
        {"t": "cards", "h": "Three different problems", "cols": 3, "cards": [
            ("Maintenance", "The facts changed. Update the configuration."),
            ("Prompt troubleshooting", "Sources are fine, the request is not. Fix the wording."),
            ("Outage", "Claude or a source is unavailable. Follow the support process."),
        ], "notes": "Do not rewrite policy instructions because a connector is down."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
