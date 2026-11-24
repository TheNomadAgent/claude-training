# Hands-on labs. One per session, about ten minutes, built around one fictional customer.
# Helios Orbital Ltd and everything in these packs is invented for training.
#
# LABS[n] = {
#   "title", "kind", "minutes",
#   "scenario": [body blocks],
#   "pack": [(file name, caption, text)],
#   "start": (caption, text) or None,
#   "tasks": [(title, text)],
#   "checks": [text],              self-check list, also used to build the grader prompt
#   "reveal": (caption, text),
#   "debrief": [text],
# }

PROFILE = """HELIOS ORBITAL LTD - CUSTOMER PROFILE (fictional, for training)

What they do
Helios Orbital operates a small fleet of earth-observation
satellites and sells the imagery. Mission operators work shifts
around launch and pass windows, so "after hours" is often their
busiest time.

Sites and server name prefixes
ARC  Arcturus    primary data centre
LYR  Lyra        mission operations, including the RDS farm
VEG  Vega        ground station
CAS  Castor      head office
POL  Polaris     disaster recovery
OLD  legacy      servers inherited from Kepler Dynamics (acquired)

Domains
helios.corp      main domain
kepler.local     legacy domain from the acquisition

Server names
Site prefix, role, number. LYRRDS07 is RDS session host 07 at
Lyra. ARCSQL01 is SQL Server 01 at Arcturus.

People and roles (roles only, no names)
Service owner            Helios's operations manager. Not technical.
Mission operators        Shift staff who use the Lyra RDS farm.
Helios IT lead           Technical contact.
Service delivery manager Our side. Owns the customer relationship.

Standing rules for anything sent to Helios
- Say "planned maintenance", "service desk" and "maintenance window".
- Never give internal ticket numbers or engineer names.
- Never promise a completion time that has not been scheduled.
- Times are New Zealand time."""

# ---------------------------------------------------------------- Lab 1
L1_NOTES = """LYRA RDS PATCHING - ENGINEER NOTES (internal)

Window: Saturday 14 November, 22:00 to 02:00.
Scope: 23 RDS session hosts, LYRRDS01 to LYRRDS23.
Result: 19 patched and rebooted. 4 deferred.
Deferred: LYRRDS07, LYRRDS12, LYRRDS18, LYRRDS21.
Why deferred: mission operators still had active sessions on those
four hosts at 01:30. A launch window was in progress. We did not
force logoffs.
New window for the four: Wednesday 18 November, 01:00 to 03:00.
Booked and agreed with the Helios IT lead.
Impact so far: none reported. The 19 patched hosts are in service.
Until the 18th the four deferred hosts stay on last month's
patch level.
Internal ref: INC0048812. Engineer: R. Tane.
Not known yet: whether the launch schedule will clash again on
the 18th. Helios mission planning has been asked."""

L1_START = """Write an update about the patching."""

L1_REVEAL = """Write a short update for the Helios service owner about
Saturday's planned maintenance on the Lyra RDS session hosts.

Audience: the service owner is an operations manager, not an
engineer. They need to know what was done, what was not, and
what happens next.

Use only the engineer notes below. If something is not in the
notes, do not add it.

Constraints:
- No internal ticket numbers and no engineer names.
- Do not give a reason for anything unless the notes give one.
- Do not promise anything beyond the window that is booked.
- Use the terms "planned maintenance" and "maintenance window".

Format: three short paragraphs headed Done, Outstanding and
Next. No more than 120 words in total.

[paste 01-patch-notes.txt here]"""

# ---------------------------------------------------------------- Lab 2
L2_ARC = """ARCTURUS (ARC) - OCTOBER SERVICE NOTES

Servers in scope: 34
Availability: 99.96%
Incidents: 7 (P1: 0, P2: 2, P3: 5)
Changes: 12 implemented, 0 failed
Patch compliance at month end: 31 of 34
Notes: both P2s were the same fault. Disk E: on ARCSQL01 filled
twice. Root cause not confirmed."""

L2_LYR = """LYRA (LYR) - OCTOBER SERVICE NOTES

Servers in scope: 36
Availability: 99.82%
Incidents: 4 (P1: 1, P2: 0, P3: 3)
Changes: 9 implemented, 1 failed and rolled back
Patch compliance at month end: 36 of 36
Notes: the P1 was a 43-minute loss of the RDS connection broker
on 9 October during a pass window."""

L2_VEG = """VEGA (VEG) - OCTOBER SERVICE NOTES

Servers in scope: 27
Availability: 99.99%
Incidents: export not supplied. The ground station team's ticket
queue was being migrated and the October export is still to come.
Changes: 5 implemented, 0 failed
Patch compliance at month end: 25 of 27
Notes: none."""

L2_START = """Read these three site notes and write the October service
summary for Helios, with totals, a comparison of the sites
and anything they should worry about."""

L2_REVEAL = """STEP 1 - extraction prompt
From the three site notes below, build one table with a row per
site and these columns: servers in scope, availability, incidents
(total, P1, P2, P3), changes implemented, changes failed, patch
compliance. Copy values exactly. Where a value is not in the
notes, write "not supplied". Do not calculate anything yet.

[check the table against the three files before going on]

STEP 2 - comparison prompt
Using only the table above, list the totals you can calculate and
say which sites each total covers. If a total cannot include a
site, say so next to the total. Then list the two or three
differences between sites that stand out.

STEP 3 - drafting prompt
Using only the table and the comparison, write the October
summary for the Helios service owner in under 150 words. State
plainly that Vega's incident figures were not supplied.

What a good result says
- Incidents: 11 across Arcturus and Lyra. Vega not supplied.
- Changes: 26 implemented, 1 failed (Lyra).
- Patch compliance: 92 of 97.
- It never says Vega had no incidents."""

# ---------------------------------------------------------------- Lab 3
L3_BRIEF = """CHANGE BRIEF - RD GATEWAY SIGN-IN FOR MISSION OPERATORS

What is changing: from Tuesday 1 December, signing in to the Lyra
RDS farm through the RD Gateway will need multi-factor
authentication (MFA).
Who is affected: members of GRP-Mission-Operators. About 60 people.
What they need to do: register for MFA before 1 December using
the self-service portal. Registration takes about five minutes.
What happens if they do not: they will not be able to sign in
from 1 December until they register.
Help: the service desk can assist with registration.
Not decided yet: whether there will be a grace period. Do not
mention one.
Approved terms: "RD Gateway", "service desk", "MFA".
Not approved: "VPN", "helpdesk", "two-step".

ACCEPTANCE CRITERIA FOR THE NOTICE
1. 100 words or fewer.
2. Uses the approved terms and none of the unapproved ones.
3. States the date, who is affected and the one action needed.
4. Contains nothing that is not in this brief. No phone numbers,
   no links, no grace period."""

L3_START = """Write a notice to the mission operators telling them about the
new MFA requirement for remote access. Make sure it is clear and
covers everything they need to know.

[paste 01-change-brief.txt here, without the acceptance criteria]"""

L3_REVEAL = """A change log that shows the method

Version 1 (baseline, unchanged)
  Result: 164 words. Says "VPN" twice. Adds a helpdesk phone
  number. Fails criteria 1, 2 and 4.

Version 2: added "100 words or fewer"
  Result: 96 words. Still says "VPN". Phone number gone.
  Fails criterion 2. Passes 1, 3 and 4.

Version 3: added "Use the terms RD Gateway, service desk and
MFA. Do not use VPN, helpdesk or two-step."
  Result: 94 words. Passes all four.

Your numbers will differ. What matters is one change per version,
the same brief every time, and the same four criteria."""

# ---------------------------------------------------------------- Lab 4
L4_NOTES = """ARCSQL01 DISK ALERTS - OCTOBER NOTES

Server: ARCSQL01, SQL Server, Arcturus. Hosts the imagery
catalogue database.
Alert: disk E: above 90% used.
After-hours callouts in October: 6 (3rd, 9th, 14th, 20th, 26th,
30th). All between 01:00 and 04:00.
Each time: the on-call engineer cleared old backup files from
E:\\Backup and the alert closed.
E: is 500 GB. The database files are on a different drive.
Backups to E: run nightly at 00:30.
Backup retention on E: is set to 14 days.
Catalogue database size: 31 GB on 1 October, 38 GB on 31 October.
Not known: why space runs out before the 14-day clean-up, and
whether anything else writes to E:.
Cost: each callout is a minimum two-hour charge."""

L4_START = """Look at these notes about the ARCSQL01 disk alerts and help."""

L4_REVEAL = """BRAINSTORM
Using the notes below, list at least eight different ways we
could reduce after-hours callouts for this alert. Include
unconventional ideas. Do not evaluate or rank them yet.

ANALYSE
Using only the notes below, set out what the notes state, what
can reasonably be inferred, and what is not known. Label each
line Stated, Inferred or Not known. Do not propose a fix.

DRAFT
Using only the notes below, write a 90-word update for the
Helios service owner, who is not technical. Say what has been
happening, what it has cost, and that the cause is not yet
confirmed. Do not suggest a cause or promise a fix date.

What to notice
The analysis should list "why space runs out early" under Not
known. If your draft or your analysis states a cause, it has
gone beyond the notes."""

LABS = {
1: {
    "title": "Fix the patching update",
    "kind": "Fix it",
    "minutes": 10,
    "scenario": [
        ("p", "Saturday's planned maintenance on Helios's Lyra RDS farm did not finish. Four session hosts were deferred because mission operators were still working through a launch window. The Helios service owner wants an update this morning."),
        ("p", "You have the engineer's notes and a one-line prompt somebody used last time. A strong model can sometimes rescue a prompt like that by guessing well. Your job is to write one that leaves nothing to guess."),
    ],
    "pack": [
        ("00-helios-profile.txt", "Customer profile. Skim it once. You will reuse it in later labs.", PROFILE),
        ("01-patch-notes.txt", "Engineer notes from Saturday night", L1_NOTES),
    ],
    "start": ("The prompt somebody used last time", L1_START),
    "tasks": [
        ("Run the one-line prompt", "In a new chat, paste the starting prompt and **only** `01-patch-notes.txt`. Leave the customer profile out. Write down what Claude had to guess: the reader, the length, what to leave out. Did the ticket number or the engineer's name get through?"),
        ("Rewrite the prompt", "In a **new** chat, write a prompt that states the audience, the purpose, the evidence boundary, the constraints from the customer profile, the format and a word limit. Read the profile for the rules. Paste both files this time."),
        ("Run it and self-check", "Tick off the self-check list below against the output. Count the words. Do not trust a feeling that it is short enough."),
        ("Get a second opinion", "Copy the grader prompt, paste your output where it says to, and run it. Did the grader agree with your own ticks?"),
    ],
    "checks": [
        "It says 19 of the 23 session hosts were patched.",
        "It says 4 hosts were deferred, and gives the new maintenance window of Wednesday 18 November, 01:00 to 03:00.",
        "It gives the reason the notes give (operators still had active sessions during a launch window) and no other cause.",
        "It contains no internal ticket number and no engineer name.",
        "It does not promise the four hosts will be done on the 18th. It says they are scheduled.",
        "It is 120 words or fewer, not counting headings.",
        "It says nothing about the state of the four deferred hosts beyond what the notes say: they stay on last month's patch level.",
    ],
    "reveal": ("One prompt that works", L1_REVEAL),
    "debrief": [
        "What did the one-line prompt make Claude guess, and would it guess the same way for a colleague tomorrow?",
        "Which single line in your prompt made the biggest difference to the result?",
    ],
},
2: {
    "title": "Three sites, one missing number",
    "kind": "Fix it",
    "minutes": 10,
    "scenario": [
        ("p", "Helios gets a monthly service summary covering Arcturus, Lyra and Vega. You have October's notes for each site. One of them has a gap."),
        ("p", "The prompt below asks for everything in one go. Run it, see what it does with the gap, then do the job in steps with a check between each."),
    ],
    "pack": [
        ("01-arcturus-october.txt", "Arcturus site notes", L2_ARC),
        ("02-lyra-october.txt", "Lyra site notes", L2_LYR),
        ("03-vega-october.txt", "Vega site notes", L2_VEG),
    ],
    "start": ("The one-shot prompt", L2_START),
    "tasks": [
        ("Run the one-shot prompt", "Paste the starting prompt and all three files into a new chat. Find the incident total it reports. What did it do about Vega? Could you check any of its totals without redoing the sums yourself?"),
        ("Step 1: extract", "In a new chat, ask only for a table of the figures, with \"not supplied\" where a value is missing. Check every cell against the files before you go on."),
        ("Step 2: compare", "Ask for the totals that can be calculated, and which sites each total covers."),
        ("Step 3: draft and self-check", "Ask for the summary, using only the table and the comparison. Tick off the self-check list."),
    ],
    "checks": [
        "The incident total is 11 and it is stated as covering Arcturus and Lyra only.",
        "It says Vega's incident figures were not supplied. It does not say Vega had no incidents.",
        "Changes are 26 implemented and 1 failed, and the failed change is placed at Lyra.",
        "Patch compliance is 92 of 97 across the three sites.",
        "It mentions the Lyra P1 (43 minutes, RDS connection broker, 9 October).",
        "It does not state a root cause for the ARCSQL01 disk fault.",
    ],
    "reveal": ("Three prompts and what a good result says", L2_REVEAL),
    "debrief": [
        "What did the one-shot prompt do with Vega's missing incidents? Would you bet on it doing that every time?",
        "At which step would you have caught a wrong number, and what would it have cost to catch it at the end?",
    ],
},
3: {
    "title": "One change at a time",
    "kind": "Fix it",
    "minutes": 10,
    "scenario": [
        ("p", "From 1 December, Helios's mission operators need MFA to sign in through the RD Gateway. You have the change brief, four acceptance criteria and a first-attempt prompt."),
        ("p", "This lab is about method. You will improve the prompt by changing **one thing per version** and scoring every version against the same four criteria."),
    ],
    "pack": [
        ("01-change-brief.txt", "Change brief and acceptance criteria", L3_BRIEF),
    ],
    "start": ("Version 1 of the prompt. Do not edit it yet.", L3_START),
    "tasks": [
        ("Run version 1 as it is", "Score the output against the four acceptance criteria. Write down pass or fail for each. Keep the prompt."),
        ("Make one change", "Pick the worst failure. Change one thing in the prompt to fix it. Save it as version 2 and run it in a new chat with the same brief."),
        ("Score and repeat", "Score version 2 against the same four criteria. If something still fails, make one more change as version 3."),
        ("Write your change log", "Three lines: the version, the one thing you changed, and which criteria passed."),
    ],
    "checks": [
        "You still have version 1 exactly as it was given.",
        "Each version differs from the one before by one change.",
        "Every version was run with the same brief and scored against the same four criteria.",
        "Your final notice is 100 words or fewer.",
        "Your final notice says \"RD Gateway\", \"service desk\" and \"MFA\", and does not say \"VPN\", \"helpdesk\" or \"two-step\".",
        "Your final notice has no phone number, no link and no grace period.",
    ],
    "reveal": ("What a change log looks like", L3_REVEAL),
    "debrief": [
        "Did fixing one criterion break another? How did you know?",
        "If you had changed three things at once and it improved, what would you have learned?",
    ],
},
4: {
    "title": "Same notes, three jobs",
    "kind": "Compare it",
    "minutes": 10,
    "scenario": [
        ("p", "ARCSQL01 has woken the on-call engineer six times in October for the same disk alert. The team wants ideas, an honest analysis and an update for the customer."),
        ("p", "Those are three different kinds of task. You will write three different prompts from the same notes and see how the instructions have to change."),
    ],
    "pack": [
        ("01-arcsql01-alert-notes.txt", "Notes on the disk alerts", L4_NOTES),
    ],
    "start": ("The do-everything prompt", L4_START),
    "tasks": [
        ("Brainstorm", "Write a prompt that gets at least eight varied ideas for reducing the callouts, with no evaluation. Run it."),
        ("Analyse", "In a new chat, write a prompt that separates what the notes state, what can be inferred and what is not known. Run it."),
        ("Draft", "In a new chat, write a prompt for a 90-word update to the Helios service owner that stays inside the notes. Run it."),
        ("Compare", "Put the three prompts side by side. Which instructions appear in one and would damage another?"),
    ],
    "checks": [
        "Your brainstorm prompt asked for many options and told Claude not to evaluate yet.",
        "The brainstorm output has at least eight ideas and they are not all versions of the same one.",
        "Your analysis output labels the cause of the early space shortage as not known.",
        "Your analysis output does not recommend a fix.",
        "Your draft is 90 words or fewer, mentions six callouts and the two-hour minimum charge, and states no cause.",
        "Your draft has no fix date and no internal detail the service owner does not need.",
    ],
    "reveal": ("Three prompts that fit the three jobs", L4_REVEAL),
    "debrief": [
        "What happened when the starting prompt just said \"help\"?",
        "Which instruction from your brainstorm prompt would have ruined the customer update?",
    ],
},
}


def grader(lab):
    lines = ["You are marking a short training exercise. Be strict and brief.", "",
             "SOURCE MATERIAL"]
    for name, _cap, text in lab["pack"]:
        lines += ["--- " + name + " ---", text, ""]
    lines += ["CHECKLIST"]
    for i, c in enumerate(lab["checks"], 1):
        lines.append("%d. %s" % (i, c))
    lines += ["",
              "MY WORK",
              "[paste your final output here. If a check is about your prompts or your method, paste those too]",
              "",
              "For each numbered check, answer Met, Not met or Cannot tell, and quote the words from my work that",
              "you based it on. If my work states anything that is not in the source material, list it at the end",
              "under \"Not in the source\". Anything in any of the files above counts as source material.",
              "Do not rewrite my work and do not give a score."]
    return "\n".join(lines)
