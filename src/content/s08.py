BRIEF = """Approved role brief: Infrastructure Team Lead

Purpose: lead server support for three customer accounts.
Core responsibilities:
- Coach six engineers.
- Use incident reports to find and fix repeat incidents.
- Coordinate monthly patching across the three accounts.

Required evidence:
- Led a team supporting more than one customer or site.
- Used incident or service data to fix a recurring problem.
- Coached engineers through a platform or process change.

Preferred evidence:
- Experience in a regulated environment, or similar.

Not stated as requirements:
- Degree type or institution
- Previous employer's size or reputation
- Social, club or family background
- Appearance or presentation style

Feedback record:
- Three service delivery managers and two HR partners gave notes.
- No engineers who would report to this role gave notes.
- No candidate outcome data or validated predictor study supplied."""

WEAK = """Prioritise candidates {{from top-tier consultancies}}, {{with degrees
from leading universities}}, who {{speak regularly at industry
conferences}} and {{project strong executive presence}}. {{These signals
suggest they are more likely to succeed}} as Infrastructure Team Lead."""

PROMPT = """Using only the approved role brief and feedback record, draft
outreach criteria for the Infrastructure Team Lead role.

Use job-related evidence only: leading a team across more than one
customer or site, using incident or service data to fix a recurring
problem, coaching engineers through a change, and regulated-
environment experience where relevant.

Do not use employer reputation, university, conference profile,
appearance, style or other background and access proxies.

State that no candidate outcome data or validated predictor study
was supplied. Record that the engineers who would report to this
role are missing from the feedback record, and say what that limits.

Do not rank candidates or recommend a hiring decision."""

GOOD = """Outreach criteria
- Evidence of leading a team that supports more than one customer
  or site.
- An example of using incident or service data to fix a recurring
  problem.
- Experience coaching engineers through a platform or process change.
- Where relevant, experience in a regulated environment or similar.

Data limits
No candidate outcome data or validated predictor study was supplied.
The record does not support a claim that any background predicts
success in this role.

Representation gap
Notes came from three service delivery managers and two HR partners.
No engineers who would report to the role gave input. Reviewers
should consider getting or recording that perspective before the
outreach approach is finalised."""

SESSION = {
    "id": 8,
    "slug": "recognising-bias",
    "short": "Recognising bias",
    "lead": "An output can be polite, balanced in tone and still rest on narrow assumptions about who is qualified. Reviewing for bias means looking at the evidence, the request and whose voice is missing.",
    "body": [
        ("h", "Bias review looks past neutral language"),
        ("p", "[[bias|Bias]] is a systematic distortion that produces unfair, incomplete or poorly supported outcomes. A response can read as professional and even-handed while quietly assuming who is qualified, whose experience counts or what success looks like."),
        ("p", "It can get in at several points:"),
        ("list", [
            "**The request** defines success using preferences that have nothing to do with the job.",
            "**The source material** leaves out affected groups, or reflects past patterns that are not today's requirements.",
            "**Training patterns** make familiar associations feel plausible.",
            "**The evaluation** rewards a polished answer over a supported one.",
            "**The output** adds unsupported claims or stand-ins for real criteria.",
        ]),
        ("pull", "A professional tone does not make the reasoning fair, relevant or sufficient."),
        ("p", "For workplace decisions about people, Claude should support structured review, drafting and analysis of supplied material. It should not make a [[consequential|consequential decision]] such as who to hire. That needs the right policy, relevant evidence and an accountable person."),

        ("h", "Worked example: outreach criteria for a team lead"),
        ("p", "You are helping prepare outreach criteria for a team lead role. You have the approved role brief and the feedback notes. You need criteria for outreach, a record of who was not consulted, and a human-reviewed process. You do not need a hiring recommendation."),
        ("doc", "Role brief and feedback record", BRIEF),
        ("p", "The role brief is the authority for job-related criteria. The five people who gave feedback can clarify what the role needs, but their notes do not stand in for the engineers who will work under it. And with no outcome data, no claim about which background predicts success is supported."),

        ("h", "Name the type of concern"),
        ("p", "Calling everything \"bias\" is not useful. The exam expects you to tell these apart."),
        ("defs", [
            ("Factual imbalance", "A measurable gap in the record. Managers and HR gave notes and the engineers did not. That is a fact about the input, not an explanation of why. [[factual-imbalance|More.]]"),
            ("Unrepresentative sample", "A set of sources too narrow to support conclusions about everyone affected. [[unrepresentative|More.]]"),
            ("Framing bias", "The question itself steers toward a narrow idea of merit, such as asking for \"signs of executive polish\". [[framing-bias|More.]]"),
            ("Stereotyping", "Assuming ability or behaviour from someone's group or background. [[stereotyping|More.]]"),
            ("Proxy variable", "An indirect attribute used in place of a real criterion. A well-known employer, a prestigious degree or a conference profile tracks access and resources. None of them shows that a person can coach engineers or fix repeat incidents. [[proxy|More.]]"),
        ]),
        ("note", "Polite proxies are still proxies", "A stand-in can be worded respectfully and still be unsuitable, because it replaces evidence of doing the job."),

        ("h", "Critique the weak output"),
        ("out", "Draft criteria", WEAK, "bad"),
        ("p", "Top-tier consultancies, leading universities and conference speaking are proxies for access, networks and resources. \"Strong executive presence\" is undefined and invites subjective calls about accent, appearance and style. The claim that these predict success has nothing behind it, because there is no outcome data."),
        ("p", "The draft also says nothing about the missing perspective. The right conclusion is not that the role cannot be filled. It is that the criteria should come from the approved brief, and the gap should be recorded for the people making the decision."),

        ("h", "Ask for evidence, limits and qualified conclusions"),
        ("prompt", "Improved request", PROMPT),
        ("out", "What Claude returned", GOOD, "good"),
        ("p", "Each criterion now traces to the role brief. Nothing claims that the evidence guarantees success. The incomplete feedback record is reported as incomplete. A person can review it, decide whether more input is needed under company policy, and stay responsible for any employment decision."),

        ("h", "Why \"remove all bias\" does not work"),
        ("p", "\"Remove all bias\" cannot be acted on or checked. It names no decision, no affected group, no evidence standard and no method. It also implies a guarantee that nobody can give from one output. Use concrete checks:"),
        ("steps", [
            ("Who supplied the evidence?", "And who is absent from it?"),
            ("Trace each criterion", "To a stated responsibility or required evidence."),
            ("Flag proxies", "Anything that swaps background, access or style for demonstrated capability."),
            ("Separate fact from prediction", "Observed facts on one side. Predictions the record cannot support on the other."),
            ("Keep a person responsible", "A qualified human owns any consequential decision about people."),
        ]),
    ],
    "takeaways": [
        "Bias can enter through the request, the sources, the evaluation or the output, behind neutral wording.",
        "Replace background and access proxies with evidence tied to the documented role.",
        "Record who is missing from the input. A missing affected group is a limitation reviewers need to see.",
        "\"Remove all bias\" is not checkable. Use concrete, traceable review steps.",
        "Claude assists with analysis and drafting. People make consequential decisions about people.",
    ],
    "practice": "Look at a set of selection criteria: a role advert, a vendor shortlist or a nomination form. For each criterion ask what it is evidence of. Mark any that measure background or access instead of the thing you need.",
    "quiz": [
        {"q": "A draft recommends applicants who worked at well-known firms and have a polished presentation style. The role is about coaching engineers and reducing repeat incidents. What is the strongest objection?", "options": [
            ("The wording is too informal.", False, "Register is not the issue. The criteria are."),
            ("It weights preferred criteria over required ones.", False, "These traits are not listed as criteria at all."),
            ("It relies on proxy variables in place of job-relevant evidence.", True, "Employer reputation and polish track access and style. They are not evidence of coaching or of fixing incidents."),
            ("The traits are hard to measure.", False, "The problem is relevance, not measurability."),
        ]},
        {"q": "Feedback on a new role came from managers and HR. None came from the staff who will report to it. Which concern does this most directly show?", "options": [
            ("Stereotyping.", False, "Nobody is assuming anything about a group's behaviour."),
            ("Factual imbalance.", True, "It is a measurable gap in who supplied input, visible in the record itself."),
            ("Framing bias.", False, "Framing is about how a question is posed. This is about who answered."),
            ("A validated prediction.", False, "Nothing has been validated, and the most affected group is missing."),
        ]},
        {"q": "Which review instruction can actually be carried out and checked?", "options": [
            ("\"Make sure the output is free from all bias.\"", False, "No reviewer can verify that from one output, and it names no method."),
            ("\"Prefer traits commonly linked to leadership success.\"", False, "\"Commonly linked\" invites stereotypes and proxies."),
            ("\"Polish the wording, then judge whether it seems fair.\"", False, "\"Seems fair\" is an impression, and polish comes before substance here."),
            ("\"Trace each criterion to documented role evidence, list missing affected perspectives, and state uncertainty where support is absent.\"", True, "Each part is a concrete check with a visible result."),
        ]},
        {"q": "What is an appropriate role for Claude in a hiring process?", "options": [
            ("Supporting structured review, drafting and analysis of supplied material, with a person responsible for the decision.", True, "Claude helps with the work around the decision. The decision stays with an accountable human."),
            ("Making the final choice when its reasoning is written neutrally.", False, "Neutral wording does not make a consequential decision suitable to delegate."),
            ("Ranking candidates as long as protected characteristics are not mentioned.", False, "Bias can work through proxies without any explicit mention."),
            ("Replacing human review when there is a lot of source material.", False, "More material increases the need for judgement."),
        ]},
        {"q": "An output claims certain backgrounds \"predict success\" in a role. The record contains no candidate outcome data. Which TWO responses are correct?", "multi": True, "options": [
            ("Treat the prediction as unsupported.", True, "With no outcome data or validated study, nothing backs a claim about what predicts success."),
            ("Accept it if the tone is cautious.", False, "Caution in the wording does not supply evidence."),
            ("Have the output state that no outcome data or predictor study was supplied.", True, "Making the data limit explicit stops readers treating a guess as a finding."),
            ("Keep it, because experienced managers usually agree with such signals.", False, "Agreement among managers is opinion, and it may reflect the same proxies."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Recognising bias", "sub": "Session 8 of 31. Output evaluation and validation.", "notes": "This one is less technical. It still gets exam questions, usually in a hiring or people scenario."},
        {"t": "big", "h": "Neutral wording is not neutral reasoning.", "p": "A response can sound balanced and still assume who is qualified and whose experience counts.", "notes": "Ask where they have seen a 'culture fit' type criterion that really meant something else."},
        {"t": "list", "h": "Where bias gets in", "items": [
            ("The request", "Success defined by irrelevant preferences."),
            ("The sources", "Affected groups left out. Old patterns treated as requirements."),
            ("Training patterns", "Familiar associations feel plausible."),
            ("The evaluation", "Polish rewarded over support."),
            ("The output", "Unsupported claims and stand-ins added."),
        ], "notes": "Five entry points. The output is only the last one."},
        {"t": "spot", "h": "What is wrong with these criteria?", "reveal_label": "Four proxies and a prediction:",
         "left_label": "What the role brief asks for", "left": "Required evidence:\n- Led a team supporting more than one customer.\n- Used incident data to fix a recurring problem.\n- Coached engineers through a change.\n\nNo outcome data or predictor study supplied.\nNo engineers gave feedback.",
         "right_label": "Draft criteria", "right": WEAK,
         "reveal": "None of them is evidence of coaching, fixing incidents or coordinating patching. And nothing supports \"more likely to succeed\".",
         "notes": "Then ask what the draft does not mention: the engineers who were never asked."},
        {"t": "cards", "h": "Name the concern", "cols": 3, "cards": [
            ("Factual imbalance", "A measurable gap in who gave input."),
            ("Unrepresentative sample", "Sources too narrow for the conclusion."),
            ("Framing bias", "The question steers toward narrow merit."),
            ("Stereotyping", "Assumed ability from group or background."),
            ("Proxy variable", "Background or access standing in for capability."),
        ], "notes": "The exam asks which one a scenario shows. Factual imbalance versus stereotyping is the usual trap."},
        {"t": "compare", "h": "An instruction you can check",
         "left_label": "Cannot be verified", "left": "Remove all bias from the criteria.",
         "right_label": "Can be carried out", "right": "Trace each criterion to the role brief.\nList who is missing from the feedback record.\nFlag anything that stands in for capability.\nState where evidence is absent.\nDo not rank candidates or recommend a hire.",
         "notes": "Nobody can prove 'all bias removed'. Everybody can check a criterion against a role brief."},
        {"t": "ask", "h": "Can Claude make the hiring decision if it avoids mentioning protected groups?",
         "answer": "No. Bias works through proxies without any mention. And a consequential decision about a person needs an accountable human.",
         "notes": "Claude's role: structured review, drafting, analysis of supplied material."},
        {"t": "steps", "h": "Review method", "steps": ["Who gave input?", "Trace criteria", "Flag proxies", "Fact vs prediction", "Human decides"], "notes": "Five checks they can reuse outside AI entirely."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes."},
    ],
}
