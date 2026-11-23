PACKET = """Change request CR-3312
Change: apply the monthly cumulative update to the production
SQL cluster
Requested window: Sunday 14 March, 02:00 to 04:00
Submitted: implementation plan, rollback plan, customer approval
Not submitted: test evidence from UAT

Change policy excerpt
Required evidence: implementation plan, rollback plan, test
evidence from UAT, and customer approval.
Changes to production require peer review and change manager
authorisation. Changes during a published freeze period are
prohibited and must not proceed. The change manager or the change
system records the final decision.

Operating details
Destination: change review queue
Frequency: every submitted change
Service level: reviewer note within one business day
Process owner: change manager"""

ASSESS = """Objective: cut the time spent preparing change reviews.
Users: change coordinator, peer reviewer, change manager.
Trigger: a change request is submitted.
Inputs: the request packet and the approved policy excerpt.
Transformation: organise the evidence, compare it with what is
required, identify the authorisation needed, summarise open
exceptions.
Output: a reviewer note sent to the change review queue.
Frequency: every submitted change.
Service level: within one business day.
Controls: use the supplied policy only; do not infer missing
facts; flag uncertainty about the freeze period; no approval
and no action in the change system.
Owner: change manager.

Decision: Claude is suitable for preparation and explanation,
not for authorisation."""

PROMPT = """Using only the request packet and the policy excerpt, prepare a
reviewer note for CR-3312. List the required evidence that was
submitted and what is missing. State the review and authorisation
the policy requires. Summarise any open exceptions. Do not approve
or reject the change, and do not infer whether the window falls in
a freeze period. Say when information was not supplied."""

NOTE = """Reviewer note: CR-3312

Submitted: implementation plan, rollback plan, customer approval.
Missing: test evidence from UAT.

Required by policy: peer review and change manager authorisation,
because this is a change to production.

Open exception: the requested window is Sunday 14 March, 02:00 to
04:00. No freeze calendar was supplied, so the material does not
show whether this falls in a freeze period.

The final decision must be recorded by the change manager or the
change system."""

SESSION = {
    "id": 15,
    "slug": "requirements-and-use-cases",
    "short": "Requirements and use cases",
    "lead": "\"Can we use AI for this?\" is the wrong first question. Start with the business need and the controls around it. Then work out which part of the work Claude can safely take.",
    "body": [
        ("h", "Start with the need, not the tool"),
        ("p", "A [[use-case]] is a defined piece of work that produces a useful result for a defined user. Good selection starts with the underlying need. A request to \"use Claude\" or \"automate everything\" describes a solution somebody wants, and it may be too broad, technically unsuitable or at odds with existing controls."),
        ("p", "Take \"automate change approvals\". The real need might be fewer incomplete submissions, faster access to the relevant policy, consistent summaries of exceptions, or less time preparing a review. Those call for different designs and different amounts of automation."),
        ("pull", "Define the work and its constraints before deciding whether Claude belongs in it."),
        ("p", "Requirements turn a broad request into something that can be assessed. They also prevent a common failure: handing an AI system responsibility for an action that has to stay with an accountable person or an authorised system."),

        ("h", "Capture requirements in categories"),
        ("table", ["Category", "What to define"], [
            ["Objective", "The business result you want"],
            ["Users", "Who submits, reviews, receives or acts on the result"],
            ["Trigger", "The event that starts the work"],
            ["Inputs", "Evidence, records, policies and the data you are allowed to use"],
            ["Transformation", "The analysis, organising, drafting or routing to be done"],
            ["Output and destination", "What is produced and where it goes"],
            ["Frequency and service level", "How often, and how quickly"],
            ["Controls and owner", "The safeguards required and who is accountable for the process"],
        ]),
        ("p", "A [[requirement]] in each category gives you something to evaluate. Skipping the last row is how AI ends up doing something nobody authorised."),

        ("h", "Resolve ambiguity with targeted questions"),
        ("p", "[[ambiguity|Ambiguity]] is information that is missing, unclear or open to more than one reading. Do not design a workflow around it. Ask questions that change the decision:"),
        ("list", [
            "Which version of the policy is the authority?",
            "Which evidence is mandatory?",
            "Could a request contain data that is not allowed in this tool?",
            "Who can authorise an exception?",
            "What should happen when a required fact is missing?",
        ]),
        ("p", "These are narrower and more useful than \"how should the automation work?\". They show whether the work can be defined, whether the evidence exists, and whether the output could be acted on safely."),

        ("h", "What Claude suits, and warning signs"),
        ("table", ["Often suitable, with review", "Needs a narrower role or a different solution"], [
            ["Synthesising supplied material", "Calculations that must be exact with no checking"],
            ["Drafting", "Actions that cannot be undone, taken without a person"],
            ["Classifying against defined categories", "Evidence that is missing or unavailable"],
            ["Organising evidence", "Data that is not allowed in the tool"],
            ["Generating ideas", "Decisions that need accountable professional judgement"],
        ]),
        ("p", "In the right-hand column Claude can still help with the surrounding work. It should not be treated as the control itself."),
        ("note", "Three tests, and all three must pass", "**Feasible**: it can be done with the inputs available and a suitable method. **Valuable**: it improves an outcome that matters. **Permissible**: it meets data, policy, authorisation and control requirements. See [[three-tests]]."),
        ("p", "A classification task that is technically possible is not valuable if it saves no real work. A useful workflow is not permissible if it exposes restricted data or bypasses a required sign-off. Being able to do something is not approval to deploy it."),

        ("h", "Worked example: change review preparation"),
        ("p", "A change coordinator is asked to \"automate change approvals\". They have one submitted request, the policy excerpt and details from the process owner."),
        ("doc", "Source material", PACKET),
        ("out", "Use case assessment", ASSESS, "good"),
        ("p", "The packet supports a limited, review-focused use case. Claude can organise the evidence, explain the supplied policy, point out what is missing and summarise exceptions. It cannot say whether the window falls in a freeze period, because no freeze calendar was supplied. And it cannot authorise or record the decision."),
        ("prompt", "Prompt with the boundaries built in", PROMPT),
        ("out", "What Claude returned", NOTE, "good"),
        ("p", "The note is useful because it cuts searching and organises the record. The peer reviewer deals with the evidence and policy questions. The change manager or the change system keeps the authorisation step. Human review here is a defined responsibility, not a rubber stamp."),

        ("h", "Measure the workflow, not the text"),
        ("p", "Success measures should reflect the business problem:"),
        ("list", [
            "time from submission to a reviewer-ready note,",
            "how completely missing evidence is detected,",
            "correction rate after reviewer feedback,",
            "reviewer satisfaction,",
            "escalation quality: are uncertain, incomplete or prohibited cases clearly routed to the right person?",
        ]),
        ("p", "Review sample outputs against the packet and the policy. When the process owner changes the policy, update the approved material and rerun the same examples. If a required source is not available, the workflow should say so. It should not manufacture an answer."),
    ],
    "takeaways": [
        "Separate the business need from the request to automate or use AI.",
        "Write down objective, users, trigger, inputs, transformation, output, service level, controls and owner before designing.",
        "Ask targeted questions to clear up ambiguity before building around it.",
        "A use case must be feasible, valuable and permissible. All three.",
        "Use Claude for preparation and explanation where the final decision needs an authorised person or system.",
    ],
    "practice": "Take one request you have heard to \"use AI\" on something. Fill in the eight requirement categories for it. Then apply the three tests and note which one it is weakest on.",
    "quiz": [
        {"q": "A manager asks you to \"automate approvals with AI\". What should you do first?", "options": [
            ("Pick the most capable model.", False, "Model choice comes after the work is defined."),
            ("Build a prototype and see what happens.", False, "Without a defined need and controls you cannot tell whether the prototype is suitable or allowed."),
            ("Tell them it cannot be done.", False, "Parts of it may be very suitable. You do not know yet."),
            ("Work out the underlying business need and the controls around the process.", True, "The request names a solution. The need might be faster preparation, fewer incomplete submissions or consistent summaries."),
        ]},
        {"q": "Which requirement category, if skipped, most often leads to AI doing something nobody authorised?", "options": [
            ("Frequency.", False, "Frequency affects capacity, not authority."),
            ("Controls and owner.", True, "This is where safeguards and the accountable person are written down."),
            ("Trigger.", False, "The trigger says when work starts, not who may decide."),
            ("Output format.", False, "Format affects usability, not authorisation."),
        ]},
        {"q": "A use case is technically possible and would save real time, but it would send restricted data to a tool that is not approved for it. Which test does it fail?", "options": [
            ("Feasible.", False, "It can be done."),
            ("Valuable.", False, "It would improve a meaningful outcome."),
            ("Permissible.", True, "It does not meet data and policy requirements, so it must not go ahead as designed."),
            ("None. Two out of three is enough.", False, "A use case has to pass all three."),
        ]},
        {"q": "A policy prohibits changes during a freeze period. The request shows a date. No freeze calendar was supplied. What should Claude's reviewer note say?", "options": [
            ("That the change is outside the freeze period, since nothing says otherwise.", False, "Absence of a calendar is not evidence the date is clear."),
            ("That the change is prohibited.", False, "Nothing supplied shows the date falls in a freeze."),
            ("That the supplied material does not show whether the date falls in a freeze period.", True, "It reports the gap and leaves the determination to a person with the calendar."),
            ("Nothing. Leave the freeze rule out.", False, "Leaving it out hides a prohibition the reviewer needs to check."),
        ]},
        {"q": "Which TWO tasks are generally suitable for Claude, with human review?", "multi": True, "options": [
            ("Organising submitted evidence against a list of what is required.", True, "Evidence organisation and comparison is language-heavy work that a reviewer can check."),
            ("Recording the final approval in the change system.", False, "The policy gives that to the change manager or the authorised system."),
            ("Drafting a summary of open exceptions for a reviewer.", True, "Drafting from supplied material for someone who will check it is a good fit."),
            ("Carrying out an irreversible production action unattended.", False, "Irreversible actions without a person are a warning sign."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Requirements and use cases", "sub": "Session 15 of 32. Workflow integration and solution design.", "notes": "New domain, 16% of the exam. This is the one most relevant to leads and anyone asked 'can we use AI for this?'"},
        {"t": "big", "h": "Start with the need, not the tool.", "p": "\"Automate approvals\" is a solution somebody wants. It is not the problem.", "notes": "Ask what the real need behind 'automate change approvals' might be. Get three different answers."},
        {"t": "cards", "h": "Eight things to write down first", "cols": 2, "cards": [
            ("Objective and users", "The result wanted, and who touches it."),
            ("Trigger and inputs", "What starts it, and what evidence is allowed."),
            ("Transformation", "The analysis, drafting or routing to be done."),
            ("Output and destination", "What is produced and where it goes."),
            ("Frequency and service level", "How often and how fast."),
            ("Controls and owner", "The safeguards, and who is accountable."),
        ], "notes": "The last card is the one people skip, and it is how AI ends up doing something nobody approved."},
        {"t": "compare", "h": "Questions that clear up ambiguity",
         "left_label": "Too broad", "left": "How should the automation work?",
         "right_label": "Changes the decision", "right": "Which policy version is the authority?\nWhich evidence is mandatory?\nCould a request contain data not allowed in this tool?\nWho can authorise an exception?\nWhat happens when a required fact is missing?",
         "notes": "Each question on the right either makes the use case possible or rules it out."},
        {"t": "cards", "h": "A use case has to pass all three", "cols": 3, "cards": [
            ("Feasible", "It can be done with the inputs and a suitable method."),
            ("Valuable", "It improves an outcome that matters."),
            ("Permissible", "It meets data, policy, authorisation and control rules."),
        ], "notes": "Being able to do it is not approval to deploy it."},
        {"t": "cards", "h": "Fit and warning signs", "cols": 2, "cards": [
            ("Often suitable, with review", "Synthesising, drafting, classifying against set categories, organising evidence, generating ideas."),
            ("Narrow the role", "Exact calculations with no check, irreversible unattended actions, missing evidence, restricted data, accountable professional judgement."),
        ], "notes": "On the right, Claude can still help around the edges. It is not the control."},
        {"t": "ask", "h": "The policy bans changes during a freeze. No freeze calendar was supplied. What does Claude's note say about the date?",
         "answer": "That the material does not show whether the date falls in a freeze. It does not say it is clear, and it does not say it is prohibited.",
         "notes": "Same idea as session 2: none supplied is not none occurred."},
        {"t": "code", "h": "Boundaries built into the prompt", "label": "Reviewer note prompt", "pre": PROMPT, "notes": "It asks for a preparation note, not a decision. The change manager or the change system records the decision."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
