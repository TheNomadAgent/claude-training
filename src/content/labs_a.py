# Hands-on labs, sessions 1 to 16. One per session, about ten minutes, all in ONE chat.
# Helios Orbital Ltd and everything in these packs is invented for training.

LABS = {}


def lab(n, title, kind, scenario, pack, tasks, checks, reveal, debrief, start=None, mark="your most recent output in this conversation"):
    LABS[n] = {"title": title, "kind": kind, "minutes": 10, "scenario": [("p", s) for s in scenario], "pack": pack,
               "start": start, "tasks": tasks, "checks": checks, "mark": mark, "reveal": reveal, "debrief": debrief}


def grader(lb):
    lines = ["Stop the exercise there. You are now marking it. Be strict and brief.",
             "",
             "Mark " + lb["mark"] + " against the checklist below.",
             "The files I gave you earlier in this conversation are the only source material.",
             "",
             "CHECKLIST"]
    for i, c in enumerate(lb["checks"], 1):
        lines.append("%d. %s" % (i, c.replace("**", "").replace("`", "")))
    lines += ["",
              "For each numbered check, answer Met, Not met or Cannot tell, and quote the words you based it on.",
              "Then list anything the marked work states that is not in the source material, under \"Not in the source\".",
              "Do not rewrite anything, do not defend your earlier answers and do not give a score."]
    return "\n".join(lines)


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
PROFILE_FILE = ("00-helios-profile.txt", "Customer profile and standing rules", PROFILE)

# ================================================================ 1
lab(1, "Fix the patching update", "Fix it",
    ["Saturday's planned maintenance on Helios's Lyra RDS farm did not finish. Four session hosts were deferred because mission operators were still working through a launch window. The Helios service owner wants an update this morning.",
     "You have the engineer's notes and a one-line prompt somebody used last time. A strong model can sometimes rescue a prompt like that by guessing well. Your job is to write one that leaves nothing to guess."],
    [("01-patch-notes.txt", "Engineer notes from Saturday night", """LYRA RDS PATCHING - ENGINEER NOTES (internal)

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
the 18th. Helios mission planning has been asked."""),
     PROFILE_FILE],
    [("Send the one-line prompt", "Start a chat. Send the starting prompt with **only** `01-patch-notes.txt`. Note what Claude had to guess: the reader, the length, what to leave out."),
     ("Send your own prompt", "In the same chat, add `00-helios-profile.txt` and send a prompt that states the audience, the purpose, the evidence boundary, the constraints from the profile, the format and a word limit."),
     ("Self-check", "Tick the list below against the second update. Count the words."),
     ("Get it marked", "Send the grader prompt as your next message.")],
    ["It says 19 of the 23 session hosts were patched.",
     "It says 4 hosts were deferred, and gives the new maintenance window of Wednesday 18 November, 01:00 to 03:00.",
     "It gives the reason the notes give (operators still had active sessions during a launch window) and no other cause.",
     "It contains no internal ticket number and no engineer name.",
     "It does not promise the four hosts will be done on the 18th. It says they are scheduled or booked.",
     "It is 120 words or fewer, not counting headings.",
     "It says nothing about the state of the four deferred hosts beyond what the notes say: they stay on last month's patch level."],
    ("One prompt that works", """Write a short update for the Helios service owner about
Saturday's planned maintenance on the Lyra RDS session hosts.

Audience: the service owner is an operations manager, not an
engineer. They need to know what was done, what was not, and
what happens next.

Use only the engineer notes and the customer profile. If
something is not in them, do not add it.

Constraints:
- No internal ticket numbers and no engineer names.
- Do not give a reason for anything unless the notes give one.
- Do not promise anything beyond the window that is booked.
- Use the terms "planned maintenance" and "maintenance window".

Format: three short paragraphs headed Done, Outstanding and
Next. No more than 120 words in total."""),
    ["What did the one-line prompt make Claude guess, and would it guess the same way for a colleague tomorrow?",
     "Which single line in your prompt made the biggest difference to the result?"],
    start=("The prompt somebody used last time", "Write an update about the patching."),
    mark="the most recent customer update you wrote in this conversation")

# ================================================================ 2
lab(2, "Three sites, one missing number", "Fix it",
    ["Helios gets a monthly service summary covering Arcturus, Lyra and Vega. You have October's notes for each site. One of them has a gap.",
     "First ask for everything in one go. Then do the same job in steps, checking each step before the next."],
    [("01-arcturus-october.txt", "Arcturus site notes", """ARCTURUS (ARC) - OCTOBER SERVICE NOTES

Servers in scope: 34
Availability: 99.96%
Incidents: 7 (P1: 0, P2: 2, P3: 5)
Changes: 12 implemented, 0 failed
Patch compliance at month end: 31 of 34
Notes: both P2s were the same fault. Disk E: on ARCSQL01 filled
twice. Root cause not confirmed."""),
     ("02-lyra-october.txt", "Lyra site notes", """LYRA (LYR) - OCTOBER SERVICE NOTES

Servers in scope: 36
Availability: 99.82%
Incidents: 4 (P1: 1, P2: 0, P3: 3)
Changes: 9 implemented, 1 failed and rolled back
Patch compliance at month end: 36 of 36
Notes: the P1 was a 43-minute loss of the RDS connection broker
on 9 October during a pass window."""),
     ("03-vega-october.txt", "Vega site notes", """VEGA (VEG) - OCTOBER SERVICE NOTES

Servers in scope: 27
Availability: 99.99%
Incidents: export not supplied. The ground station team's ticket
queue was being migrated and the October export is still to come.
Changes: 5 implemented, 0 failed
Patch compliance at month end: 25 of 27
Notes: none.""")],
    [("Ask for it all at once", "Send the starting prompt with all three files. Find the incident total. What did it do about Vega? Could you check its totals without redoing the sums?"),
     ("Step 1: extract", "In the same chat, ask for only a table of the figures, with \"not supplied\" where a value is missing and no calculations. Check every cell against the files."),
     ("Step 2: total and compare", "Ask for the totals that can be calculated, and which sites each total covers."),
     ("Step 3: draft, then get it marked", "Ask for a summary of under 150 words for the service owner, using only the table and the totals. Then send the grader prompt.")],
    ["The incident total is 11 and it is stated as covering Arcturus and Lyra only.",
     "It says Vega's incident figures were not supplied. It does not say Vega had no incidents.",
     "Changes are 26 implemented and 1 failed, and the failed change is placed at Lyra.",
     "Patch compliance is 92 of 97 across the three sites.",
     "It mentions the Lyra P1 (43 minutes, RDS connection broker, 9 October).",
     "It does not state a root cause for the ARCSQL01 disk fault."],
    ("Three prompts and the right numbers", """STEP 1
From the three site notes, build one table with a row per site
and these columns: servers in scope, availability, incidents
(total, P1, P2, P3), changes implemented, changes failed, patch
compliance. Copy values exactly. Where a value is not in the
notes, write "not supplied". Do not calculate anything yet.

STEP 2
Using only the table, list the totals you can calculate and say
which sites each total covers. If a total cannot include a site,
say so next to the total.

STEP 3
Using only the table and the totals, write the October summary
for the Helios service owner in under 150 words. State plainly
that Vega's incident figures were not supplied.

The right numbers
- Incidents: 11 across Arcturus and Lyra. Vega not supplied.
- Changes: 26 implemented, 1 failed (Lyra).
- Patch compliance: 92 of 97."""),
    ["What did the all-at-once prompt do with Vega's missing incidents? Would you bet on it doing that every time?",
     "At which step would you have caught a wrong number, and what would it cost to catch it at the end?"],
    start=("The all-at-once prompt", "Read these three site notes and write the October service\nsummary for Helios, with totals, a comparison of the sites\nand anything they should worry about."),
    mark="the most recent service summary you wrote in this conversation")

# ================================================================ 3
lab(3, "One change at a time", "Fix it",
    ["From 1 December, Helios's mission operators need MFA to sign in through the RD Gateway. You have the change brief, four acceptance criteria and a first-attempt prompt.",
     "This lab is about method. Improve the prompt by changing **one thing per version**, and score every version against the same four criteria."],
    [("01-change-brief.txt", "Change brief and acceptance criteria", """CHANGE BRIEF - RD GATEWAY SIGN-IN FOR MISSION OPERATORS

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
   no links, no grace period.""")],
    [("Send version 1 unchanged", "Send the starting prompt with the brief. Score the notice against the four criteria: pass or fail for each."),
     ("Version 2: one change", "Pick the worst failure. Send the **whole prompt again** with one thing changed, and start the message with \"Version 2\"."),
     ("Version 3 if you need it", "Score version 2 the same way. If anything still fails, send version 3 with one more change."),
     ("Get it marked", "Send the grader prompt. It will look back over your versions.")],
    ["Each version of the prompt differs from the one before by one change.",
     "Every version was run against the same brief.",
     "The final notice is 100 words or fewer.",
     "The final notice says \"RD Gateway\", \"service desk\" and \"MFA\", and does not say \"VPN\", \"helpdesk\" or \"two-step\".",
     "The final notice states 1 December, who is affected, and that they must register for MFA before then.",
     "The final notice has no phone number, no link and no grace period."],
    ("What a change log looks like", """Version 1 (as given)
  164 words. Says "remote access" and "VPN". Adds a phone number.
  Fails criteria 1, 2 and 4.

Version 2: added "100 words or fewer"
  96 words. Still says "VPN". Phone number gone.
  Fails criterion 2.

Version 3: added "Use the terms RD Gateway, service desk and
MFA. Do not use VPN, helpdesk or two-step."
  94 words. Passes all four.

Your numbers will differ. What matters is one change per
version, the same brief each time and the same four criteria."""),
    ["Did fixing one criterion break another? How did you know?",
     "If you had changed three things at once and it improved, what would you have learned?"],
    start=("Version 1 of the prompt", "Write a notice to the mission operators telling them about the\nnew MFA requirement for remote access. Make sure it is clear and\ncovers everything they need to know."),
    mark="the prompt versions I sent and the final notice you wrote in this conversation")

# ================================================================ 4
lab(4, "Same notes, three jobs", "Compare it",
    ["ARCSQL01 has woken the on-call engineer six times in October for the same disk alert. The team wants ideas, an honest analysis and an update for the customer.",
     "Those are three different kinds of task. Write three different prompts from the same notes and see how the instructions have to change."],
    [("01-arcsql01-alert-notes.txt", "Notes on the disk alerts", """ARCSQL01 DISK ALERTS - OCTOBER NOTES

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
Cost: each callout is a minimum two-hour charge.""")],
    [("Brainstorm", "Send the notes with a prompt that gets at least eight varied ideas for reducing the callouts, with no evaluation."),
     ("Analyse", "In the same chat, ask for what the notes state, what can be inferred and what is not known, each line labelled. No fixes."),
     ("Draft", "Ask for a 90-word update for the Helios service owner that stays inside the notes."),
     ("Get it marked", "Send the grader prompt. Then ask yourself which instruction from one prompt would have damaged another.")],
    ["The brainstorm has at least eight ideas and they are not all versions of the same one.",
     "The brainstorm prompt told Claude not to evaluate or rank yet.",
     "The analysis labels the cause of the early space shortage as not known.",
     "The analysis does not recommend a fix.",
     "The customer update is 90 words or fewer, mentions six callouts and the two-hour minimum charge, and states no cause.",
     "The customer update gives no fix date."],
    ("Three prompts that fit the three jobs", """BRAINSTORM
Using the notes, list at least eight different ways we could
reduce after-hours callouts for this alert. Include
unconventional ideas. Do not evaluate or rank them yet.

ANALYSE
Using only the notes, set out what they state, what can
reasonably be inferred, and what is not known. Label each line
Stated, Inferred or Not known. Do not propose a fix.

DRAFT
Using only the notes, write a 90-word update for the Helios
service owner, who is not technical. Say what has been
happening, what it has cost, and that the cause is not yet
confirmed. Do not suggest a cause or promise a fix date."""),
    ["Did ideas from the brainstorm leak into the analysis or the customer update?",
     "Which instruction from your brainstorm prompt would have ruined the customer update?"],
    mark="the brainstorm, the analysis and the customer update in this conversation")

# ================================================================ 5
lab(5, "The summary that left something out", "Catch it",
    ["Helios ran a disaster recovery test at Polaris. Somebody asked an AI tool for a summary for the service owner, and it reads well.",
     "Every number in it is correct. Find what is wrong anyway, first by yourself and then with Claude's help."],
    [("01-brief.txt", "What the summary was asked to cover", """BRIEF FOR THE DR TEST SUMMARY

For: Helios service owner.
Must include:
1. The date of the test.
2. Every system tested.
3. The recovery time target AND the time achieved for each system.
4. Any system that missed its target.
5. Every follow-up action, with its owner and due date.
Use only the DR test record."""),
     ("02-dr-test-record.txt", "The test record", """POLARIS DR TEST RECORD - SATURDAY 17 OCTOBER

System                         Target    Achieved
Lyra RDS farm                  2h 00m    1h 35m
ARCSQL01 imagery catalogue     4h 00m    5h 10m
ARCFS01 file services          8h 00m    6h 20m
VEGTLM01 telemetry ingest      1h 00m    0h 50m

All four systems were recovered.
The imagery catalogue missed its target by 1h 10m. Restore
throughput was lower than expected. Cause not yet determined.

Actions
A1. Review restore throughput for the catalogue.
    Owner: backup lead. Due: 6 November.
A2. Retest the catalogue restore.
    Owner: DR coordinator. Due: 20 November."""),
     ("03-ai-summary.txt", "The AI-written summary to review", """DR TEST SUMMARY

The Polaris disaster recovery test on Saturday 17 October was
successful. All four systems were recovered.

The Lyra RDS farm was recovered in 1h 35m against a 2h target.
File services on ARCFS01 were recovered in 6h 20m against an 8h
target. Telemetry ingest on VEGTLM01 was recovered in 50 minutes
against a 1h target. The imagery catalogue on ARCSQL01 was
restored in just over five hours.

No further action is required.""")],
    [("Read it yourself first", "Two minutes. Compare the summary with the brief. Write down what is missing or wrong before you ask Claude anything."),
     ("Ask for a matrix", "Send all three files. Ask Claude to check the summary against each numbered requirement in the brief and mark it present, absent, accurate or unsupported, quoting the summary."),
     ("Ask for a correction", "In the same chat, ask for a corrected summary using only the test record, changing as little as possible."),
     ("Get it marked", "Send the grader prompt. Did Claude find anything you missed, or the other way round?")],
    ["The review says the catalogue's 4h target is missing from the summary.",
     "The review says the summary does not report that the catalogue missed its target.",
     "The review says both follow-up actions, their owners and due dates are absent, and that \"No further action is required\" contradicts the record.",
     "The corrected summary states 5h 10m against a 4h target for the imagery catalogue.",
     "The corrected summary lists both actions with owner and due date.",
     "The corrected summary gives no cause for the miss beyond \"not yet determined\"."],
    ("What was wrong", """Every figure quoted in the summary is accurate. The problems are
what it leaves out and what it concludes.

- Requirement 3: the catalogue's target (4h) is missing, so the
  reader cannot see it was missed.
- Requirement 4: the miss (5h 10m against 4h) is never stated.
- Requirement 5: both actions, owners and due dates are absent.
- "Successful" and "No further action is required" are not
  supported by the record.

A prompt for the matrix
Check the summary against each numbered requirement in the
brief, using only the DR test record. For each requirement say
Present, Absent, Accurate or Unsupported and quote the words of
the summary you relied on."""),
    ["How many of the problems did you find before asking Claude?",
     "Why is \"restored in just over five hours\" more dangerous than a wrong number?"],
    mark="your requirement-by-requirement review and the corrected summary in this conversation")

# ================================================================ 6
lab(6, "Seven sentences, four of them invented", "Catch it",
    ["An AI tool summarised the Helios Backup Standard for the team wiki. Some of what it says is in the standard. Some of it is not.",
     "Sort every sentence into supported, inferred or unsupported."],
    [("01-backup-standard.txt", "The standard", """HELIOS BACKUP STANDARD v2.1 (approved)
Owner: Platform Standards team

1. Production servers are backed up nightly.
2. Backups are retained for 35 days.
3. A restore test is performed for each tier-1 system.
4. Restore test results are recorded in the backup register.
5. A failed backup is re-run on the next business day."""),
     ("02-ai-summary.txt", "The AI-written summary", """BACKUP STANDARD - SUMMARY

S1. Production servers are backed up every night.
S2. Backups are kept for 35 days.
S3. Tier-1 systems are restore tested every 90 days.
S4. This is required by section 7.3 of the standard.
S5. Results go in the backup register, so an auditor could
    review them.
S6. A failed backup is re-run within four hours.
S7. The standard is owned by Mere Aroha in Platform Standards.""")],
    [("Mark it up yourself", "Two minutes. Label S1 to S7 as supported, inferred or unsupported."),
     ("Ask Claude to classify", "Send both files. Ask for each sentence to be labelled Supported, Inferred or Unsupported, with the clause of the standard quoted, or \"nothing in the standard\"."),
     ("Ask for a clean version", "In the same chat, ask for the summary rewritten using only the standard, with \"not stated\" where the standard is silent."),
     ("Get it marked", "Send the grader prompt.")],
    ["S3 is marked unsupported: the standard gives no frequency for restore tests.",
     "S4 is marked unsupported: the standard has no section 7.3.",
     "S6 is marked as contradicting the standard, which says the next business day.",
     "S7 is marked unsupported for the named person: the standard names a team only.",
     "S5 is marked as an inference: the register is stated, the auditor is not.",
     "The clean version says the restore test frequency is not stated."],
    ("The answers", """S1 Supported    clause 1
S2 Supported    clause 2
S3 Unsupported  clause 3 gives no frequency
S4 Unsupported  there is no section 7.3
S5 Inferred     clause 4 says results are recorded. The auditor
                is an inference
S6 Contradicts  clause 5 says the next business day
S7 Unsupported  the owner is a team. No person is named

The pattern to remember: specific, confident details (a number
of days, a section number, a person's name) are where invented
content hides."""),
    ["Which invented detail looked most believable, and why?",
     "S6 is not just unsupported. It is wrong. Which is worse in a wiki?"],
    mark="your sentence-by-sentence classification and the clean summary in this conversation")

# ================================================================ 7
lab(7, "The business case that does not add up", "Catch it",
    ["Helios needs a monitoring licence for 164 servers. A draft business case recommends Option B. It contains an arithmetic contradiction, a term that changes meaning, an unstated assumption and an ambiguous instruction.",
     "Find all four."],
    [("01-draft-business-case.txt", "The draft", """MONITORING LICENCE - DRAFT BUSINESS CASE

Helios has 164 servers to monitor.

Option A: $4,500 a month. Covers up to 200 servers.
Option B: $3,600 a month. Covers up to 120 servers, then $30 a
month for each additional server.

In this paper "availability" means uptime during business hours,
08:00 to 18:00 on weekdays.

Option A offers 99.5% availability. Option B offers 99.2%
availability measured around the clock.

Recommendation: Option B is the lowest-cost choice at $3,600 a
month and is recommended. The saving funds the Vega upgrade.

Next step: notify the team by end of week.""")],
    [("Read it yourself first", "Two minutes. Work out what Option B really costs for 164 servers."),
     ("Ask Claude to review it", "Send the draft. Ask for every internal inconsistency, ambiguity, unstated assumption and reasoning gap, each with the line quoted."),
     ("Ask for the sums", "In the same chat, ask for the monthly cost of each option at 164 servers with the working shown. Check it by hand."),
     ("Get it marked", "Send the grader prompt.")],
    ["Option B at 164 servers is worked out as $4,920 a month (3,600 plus 44 times 30).",
     "The review says Option A is cheaper than Option B at 164 servers, so the recommendation contradicts the figures.",
     "The review says \"availability\" is defined as business hours and then used for a round-the-clock figure, so the two percentages cannot be compared.",
     "The review says \"notify the team by end of week\" does not say which team or which day.",
     "The review says the paper assumes the server count stays at 164 without saying so.",
     "The review does not invent facts about either product."],
    ("The four defects", """1. Arithmetic. Option B for 164 servers is 3,600 + (44 x 30) =
   $4,920 a month. Option A is $4,500. B is not the lowest cost.
   There is no saving to fund the Vega upgrade.

2. Term shift. "Availability" is defined as business hours, then
   B's figure is quoted around the clock. The two numbers measure
   different things.

3. Unstated assumption. The comparison assumes 164 servers. If
   the estate shrinks to 150 or fewer, B becomes cheaper or
   equal. If it grows, B gets worse.

4. Ambiguity. "Notify the team by end of week" names no team and
   no day."""),
    ["Did you get $4,920 before Claude did?",
     "At what server count do the two options cost the same?"],
    mark="your review of the draft business case and your cost working in this conversation")

# ================================================================ 8
lab(8, "Who is missing from the shortlist?", "Catch it",
    ["Helios wants five mission operators as \"RDS champions\" to help test changes. An AI tool produced a shortlist from the operator list.",
     "The approved criteria are shift coverage, site coverage and completed training. Check what the shortlist was really built on, and who it left out."],
    [("01-operators.txt", "Operator list (invented, roles only)", """MISSION OPERATORS - CHAMPION CANDIDATES

ID  Site  Shift  Years  Tickets logged  RDS training done
A   LYR   Day    6      41              Yes
B   LYR   Day    4      38              Yes
C   LYR   Day    2      35              Yes
D   LYR   Day    5      33              No
E   LYR   Day    1      30              Yes
F   LYR   Night  7       9              Yes
G   LYR   Night  3       7              Yes
H   LYR   Night  2       4              No
I   VEG   Day    5      12              Yes
J   VEG   Night  4       5              Yes
K   VEG   Night  1       3              Yes
L   CAS   Day    3      14              Yes

APPROVED CRITERIA
1. Both shifts are represented.
2. More than one site is represented.
3. Every champion has completed RDS training.
The operations manager makes the final choice."""),
     ("02-ai-shortlist.txt", "The AI-produced shortlist", """RECOMMENDED RDS CHAMPIONS

A, B, C, D and E.

These are the five most engaged operators, based on the number
of tickets they have logged.""")],
    [("Look for yourself", "Two minutes. Who is on the shortlist, by site and shift? Who is not?"),
     ("Ask Claude to test it", "Send both files. Ask Claude to check the shortlist against the three approved criteria and say what the shortlist was really based on."),
     ("Ask for options, not a decision", "In the same chat, ask for two alternative groups of five that meet all three criteria, showing the evidence for each person, for the operations manager to choose from."),
     ("Get it marked", "Send the grader prompt.")],
    ["The review says the shortlist has no night-shift operators.",
     "The review says the shortlist is all Lyra, so only one site is represented.",
     "The review says D has not completed RDS training and so fails criterion 3.",
     "The review says \"tickets logged\" is not an approved criterion.",
     "Each alternative group has both shifts, more than one site, and only trained operators (no D, no H).",
     "The alternatives are offered as options. Claude does not make the final choice."],
    ("What the shortlist got wrong", """- Shift: all five are day shift. Criterion 1 fails.
- Site: all five are Lyra. Criterion 2 fails.
- Training: D has not done the training. Criterion 3 fails.
- Basis: "tickets logged" is not one of the approved criteria.
  It is a proxy. Night-shift operators log fewer tickets, which
  may say more about when the service desk is staffed than
  about how engaged they are.

One group that meets all three criteria: A, F, I, J, L.
The operations manager decides."""),
    ["Why might night-shift operators log fewer tickets?",
     "The shortlist looked objective because it used a number. What was the number really measuring?"],
    mark="your review of the shortlist and the alternative groups in this conversation")

# ================================================================ 9
lab(9, "Three sources, one runtime", "Catch it",
    ["A draft recommendation for the Vega ground station says the proposed UPS gives 18 minutes of runtime at full load \"per the manufacturer\". You have three sources that mention a runtime.",
     "Work out which source is the authority, and what the draft is allowed to say."],
    [("01-sources.txt", "Three sources", """SOURCE 1 - Manufacturer specification sheet
Voltara HX-3000, revision C, dated March 2026. Marked "current".
Runtime: 11 minutes at full load. 24 minutes at half load.

SOURCE 2 - Manufacturer brochure
Voltara HX-3000, revision A, dated 2023.
Runtime: 18 minutes at full load.
Footer: "Superseded by revision C."

SOURCE 3 - Forum post, undated
"We run an HX-3000 and get 20+ minutes easily."
No load figure given."""),
     ("02-draft-claim.txt", "The claim in the draft", """The Voltara HX-3000 provides 18 minutes of runtime at full load
per the manufacturer, which is enough to cover the Vega
generator start-up.""")],
    [("Decide for yourself", "One minute. Which source wins, and why?"),
     ("Ask Claude to rank the sources", "Send both files. Ask for the three sources ranked by authority and currency, with the reason for each."),
     ("Ask for the claim to be corrected", "In the same chat, ask for the claim rewritten using only what the authoritative source supports, and a list of what is still unknown."),
     ("Get it marked", "Send the grader prompt.")],
    ["Revision C of the specification sheet is identified as the authoritative, current source.",
     "The 18-minute figure is traced to the superseded revision A brochure.",
     "The forum post is treated as non-authoritative, with no load figure.",
     "The corrected claim says 11 minutes at full load (and may add 24 minutes at half load).",
     "The corrected claim does not say the runtime is enough to cover generator start-up, because the start-up time and the Vega load were not supplied.",
     "The unknowns listed include the actual load at Vega."],
    ("The answer", """Authority and currency
1. Specification sheet, revision C, March 2026, marked current.
   Primary and current. This one governs.
2. Brochure, revision A, 2023. Same manufacturer, superseded.
3. Forum post. Anecdote, no date, no load figure.

Corrected claim
"The Voltara HX-3000 provides 11 minutes of runtime at full load
and 24 minutes at half load (manufacturer specification,
revision C, March 2026)."

Still unknown
- The load the UPS would carry at Vega.
- How long the Vega generator takes to start.
So the draft cannot say the runtime is "enough"."""),
    ["The draft said \"per the manufacturer\" and that was true. Why was it still wrong?",
     "What would you need before you could write \"enough to cover generator start-up\"?"],
    mark="your source ranking and the corrected claim in this conversation")

# ================================================================ 10
lab(10, "One incident, three readers", "Fix it",
    ["On 9 October the Lyra RDS connection broker was down for 43 minutes during a pass window. Three groups need to hear about it: our engineers, the Helios service owner and the mission operators.",
     "Write three versions from one incident record. The facts must not change between them."],
    [("01-incident-record.txt", "Incident record (internal)", """INCIDENT RECORD - LYRA RDS CONNECTION BROKER

Date: Friday 9 October.
Start: 02:14. Service restored: 02:57. Duration: 43 minutes.
What failed: the RD Connection Broker service on LYRRDB01 stopped.
Effect: mission operators could not start new sessions. Existing
sessions kept working.
Fix: the service was restarted by the on-call engineer.
Cause: under investigation. A scheduled certificate task ran on
LYRRDB01 at 02:10. A link to the outage is NOT confirmed.
There is a single connection broker. No standby.
Next: root cause review due 23 October.
Internal ref: INC0047730. Engineer: P. Nikora.
Customer communications must be approved by the service delivery
manager before they are sent."""),
     PROFILE_FILE],
    [("Engineers", "Send both files. Ask for a technical summary for the engineering team with server names and times."),
     ("Service owner", "In the same chat, ask for a version for the Helios service owner: impact first, plain language, under 100 words, following the standing rules."),
     ("Mission operators", "Ask for a three-sentence version for the operators: what happened to them and what to do if it happens again."),
     ("Get it marked", "Send the grader prompt.")],
    ["All three versions give the date (9 October) and the duration (43 minutes).",
     "All three say the cause is under investigation. None states the certificate task as the cause.",
     "The two customer versions contain no internal reference and no engineer name.",
     "The service owner version leads with the effect on operators, not with the technical failure.",
     "The engineer version includes LYRRDB01, the times and the single-broker point.",
     "Somewhere, Claude notes that the customer versions need service delivery manager approval before they are sent."],
    ("What good looks like", """Same facts in all three: 9 October, 43 minutes, new sessions
could not start, existing sessions kept working, cause under
investigation, review due 23 October.

What changes
- Engineers: LYRRDB01, 02:14 to 02:57, service restarted, single
  broker with no standby, certificate task at 02:10 with link
  not confirmed.
- Service owner: impact first, plain words, what happens next.
- Operators: what they saw, and to contact the service desk if
  they cannot start a session.

What must never change: the cause. "A certificate task ran four
minutes earlier" is a fact. "The certificate task caused it" is
not in the record."""),
    ["Did any version turn \"a task ran at 02:10\" into \"a task caused it\"?",
     "Who has to approve the customer versions, and did Claude remember?"],
    mark="the three versions of the incident summary in this conversation")

# ================================================================ 11
lab(11, "Pick the right tool for five jobs", "Decide it",
    ["Helios work comes in different shapes. Some of it is a quick question, some recurs every week, some needs current sources and some needs a standalone document.",
     "Match five jobs to chat, a Project, Research or an Artifact. Then check what the tool you are using can do."],
    [("01-five-jobs.txt", "Five jobs", """FIVE JOBS FOR THE HELIOS ACCOUNT

J1. Reword one sentence in an email to the Helios IT lead.
J2. Draft the weekly planned maintenance notice, every week,
    using the same style rules and approved terms.
J3. Produce an overview of current vendor guidance on support
    options for Windows Server 2012 R2, with references.
J4. Create a one-page RDS patching checklist the team can look
    at beside the chat and refine.
J5. Answer engineers' recurring questions from the approved
    Helios standards documents.""")],
    [("Decide first", "One minute. Write your own answer for J1 to J5."),
     ("Ask Claude", "Send the file. Ask which of chat, a Project, Research or an Artifact fits each job, with one line of reasoning each."),
     ("Challenge one", "In the same chat, pick the answer you agree with least and ask Claude to argue the alternative."),
     ("Ask what this tool can do, then get it marked", "Ask: \"Which of those four can you do in the tool I am using right now, and what can you not confirm?\" Then send the grader prompt.")],
    ["J1 is matched to an ordinary chat.",
     "J2 and J5 are matched to a Project, because the same instructions or references are reused.",
     "J3 is matched to Research, because it needs current sources with references.",
     "J4 is matched to an Artifact, because it is a standalone document to view and refine.",
     "Each match has a reason tied to the job, not just a label.",
     "When asked about the current tool, Claude said what it could not confirm instead of asserting features."],
    ("The matches", """J1 Chat       one-off, no lasting context
J2 Project    recurring, same rules and terms each time
J3 Research   current information from many sources, cited
J4 Artifact   standalone content to view and iterate on
J5 Project    recurring questions from a maintained set of
              reference documents

Not every tool has all four. CONVER and Copilot may not offer
Projects, Research or Artifacts the way claude.ai does. Check
what you have before you design a workflow around it."""),
    ["Which of the four do you have in the tool you used today?",
     "J2 and J5 are both Projects. What is different about what you would put in each?"],
    mark="your matching of the five jobs and your answer about the current tool in this conversation")

# ================================================================ 12
lab(12, "Which model for which job?", "Decide it",
    ["Three Helios workloads are candidates for Claude. They need very different amounts of reasoning.",
     "Assign each to a model tier and say how you would prove the choice."],
    [("01-workloads.txt", "Three workloads", """THREE HELIOS WORKLOADS

W1. Sort about 4,000 monitoring alert emails a day into five
    fixed categories. Each alert is two or three lines. Speed
    matters.

W2. Draft the weekly planned maintenance notice from approved
    facts and a style guide. One a week. A person reviews it.

W3. Reconcile conflicting support clauses across three long
    contracts inherited from the Kepler Dynamics acquisition,
    and explain the implications for the service owner.""")],
    [("Decide first", "One minute. Fastest tier, balanced tier or most capable tier for each?"),
     ("Ask Claude", "Send the file. Ask for a tier for each workload with the reason, in terms of complexity, volume, speed and cost."),
     ("Ask for the test", "In the same chat, ask how you would confirm each choice: what inputs, what quality bar, what you would measure."),
     ("Get it marked", "Send the grader prompt.")],
    ["W1 is assigned to the fastest, lowest-cost tier.",
     "W3 is assigned to the most capable tier.",
     "W2 is assigned to a balanced or fast tier, with human review noted.",
     "Each choice has a test on representative inputs with a stated quality bar.",
     "The answer says that specific model names, prices and limits should be checked in current documentation.",
     "The answer does not claim a bigger model removes the need for review on W3."],
    ("A reasonable answer", """W1 Fastest tier. Simple, high volume, speed matters.
   Test: 200 real alerts already labelled by an engineer.
   Bar: agreed accuracy, such as 97%, and no missed critical.

W2 Balanced tier, or fast if it passes. Low volume, reviewed.
   Test: four past weeks' facts. Bar: zero unsupported claims,
   approved terms used.

W3 Most capable tier. Long documents, ambiguity, nuance.
   Test: clauses a contracts person has already reconciled.
   Bar: finds every known conflict, invents none.
   Still needs review by someone with authority.

Tiers trade capability against speed and cost. Test on your own
task before you commit."""),
    ["Would you have put W1 on the biggest model \"to be safe\"? What would that have cost?",
     "What is the quality bar for W3, and who is qualified to judge it?"],
    mark="your tier choices and test plans in this conversation")

# ================================================================ 13
lab(13, "The cheaper model that costs more", "Compare it",
    ["Two model options have been trialled for Helios service desk ticket triage. One is cheaper per ticket. Somebody wants to pick it on price.",
     "Work out the real monthly cost of each."],
    [("01-triage-trial.txt", "Trial results", """TICKET TRIAGE TRIAL

Volume: 4,000 tickets a month.
Requirement: a triage result within 5 seconds.

Option X: $0.004 per ticket. Typical response 1.2 seconds.
          12% of results needed correcting by an analyst.
Option Y: $0.011 per ticket. Typical response 3.5 seconds.
          3% of results needed correcting by an analyst.

Each correction takes an analyst about five minutes, costed at
$2.50.

These rates come from a trial of 200 tickets.""")],
    [("Estimate first", "One minute. Which is cheaper overall? Write your guess."),
     ("Ask for the sums", "Send the file. Ask for the total monthly cost of each option, model cost plus correction cost, with the working shown."),
     ("Check and question", "Check the arithmetic by hand. In the same chat, ask which option meets the requirement and what the trial does not tell you."),
     ("Get it marked", "Send the grader prompt.")],
    ["Option X is costed at $1,216 a month ($16 model cost plus 480 corrections at $2.50).",
     "Option Y is costed at $344 a month ($44 model cost plus 120 corrections at $2.50).",
     "The answer says Y is cheaper overall even though it costs more per ticket.",
     "The answer says both options meet the 5-second requirement.",
     "The answer flags that the correction rates come from a 200-ticket trial and may not hold at volume.",
     "The working is shown, so each number can be checked."],
    ("The sums", """Option X
  Model:       4,000 x 0.004 =    $16
  Corrections: 4,000 x 12%   =    480 x 2.50 = $1,200
  Total                           $1,216

Option Y
  Model:       4,000 x 0.011 =    $44
  Corrections: 4,000 x 3%    =    120 x 2.50 =   $300
  Total                             $344

Y is $872 a month cheaper. The model price was never the big
number. People's time was.

Both meet the 5-second requirement. The rates come from 200
tickets, so confirm them on a bigger sample."""),
    ["Was your first guess right?",
     "What would the answer be if the requirement were 2 seconds?"],
    mark="your cost comparison of Option X and Option Y in this conversation")

# ================================================================ 14
lab(14, "Write the handoff", "Fix it",
    ["A long chat about migrating the Arcturus file server has wandered. It holds real decisions, a couple of abandoned ideas and some open questions, all mixed together.",
     "Get Claude to write a handoff summary good enough to start a clean chat from."],
    [("01-chat-so-far.txt", "Notes from the long chat", """ARCFS01 MIGRATION - WHAT THE CHAT COVERED (in the order it came up)

- Goal: move file shares from ARCFS01 to ARCFS02 with no change
  to share paths for users.
- Talked about DFS Replication to seed the data. Dropped it:
  too slow to set up for this timeline.
- Decision: use Robocopy with security and timestamps copied.
- Talked about doing it mid-week. Dropped it.
- Decision: cutover on the weekend of 28 and 29 November.
- Constraint: no changes at all from 21 to 24 November. Launch
  window.
- Constraint: shares must stay readable during the pre-copy.
- Long tangent about printer drivers. Not relevant.
- Open: some folders have permissions for kepler.local accounts
  that no longer resolve. Not decided what to do with them.
- Open: who signs off the cutover on the day. Not decided.
- First draft of the comms was written and rejected as too long.""")],
    [("Ask for a handoff", "Send the file. Ask for a handoff summary for a new chat under four headings: Goal, Decisions, Constraints, Open items. 120 words or fewer."),
     ("Test it", "In the same chat, ask: \"Using only that summary, what date is the cutover and what must not happen on 22 November?\""),
     ("Tighten it", "If anything abandoned or irrelevant got in, ask for it to be removed."),
     ("Get it marked", "Send the grader prompt.")],
    ["The goal says ARCFS01 to ARCFS02 with no change to share paths.",
     "Decisions list Robocopy and the cutover on 28 and 29 November.",
     "Constraints list the 21 to 24 November freeze and shares staying readable during pre-copy.",
     "Open items list the unresolved kepler.local permissions and who signs off the cutover.",
     "DFS Replication, the mid-week idea, the printer drivers and the rejected comms draft are left out.",
     "The summary is 120 words or fewer."],
    ("A good handoff", """GOAL
Move file shares from ARCFS01 to ARCFS02 with no change to
share paths for users.

DECISIONS
- Copy with Robocopy, keeping security and timestamps.
- Cutover on the weekend of 28 and 29 November.

CONSTRAINTS
- No changes from 21 to 24 November (launch window).
- Shares stay readable during the pre-copy.

OPEN ITEMS
- What to do with permissions for kepler.local accounts that
  no longer resolve.
- Who signs off the cutover on the day.

Left out on purpose: DFS Replication, the mid-week option, the
printer drivers and the rejected comms draft."""),
    ["Did anything abandoned sneak into the summary?",
     "Why paste a summary into a new chat and not the whole transcript?"],
    mark="the most recent handoff summary you wrote in this conversation")

# ================================================================ 15
lab(15, "Five ideas for change review", "Decide it",
    ["Somebody wants to \"use AI in change review\" for Helios. That is not a requirement yet. There are five concrete ideas on the table.",
     "Sort them, then turn the best one into a requirement two people could check."],
    [("01-change-review.txt", "The process and five ideas", """HELIOS CHANGE REVIEW

How it works today
An engineer fills in a change request form. The change advisory
board (CAB) meets on Tuesdays and approves or rejects each
change. Only the CAB can approve. A missed rollback plan is the
most common reason for rejection.

Five ideas for using Claude
I1. Draft a plain-language summary of each change request for
    the CAB pack, from the form.
I2. Check each form for missing fields, such as no rollback
    plan, before it goes to the CAB.
I3. Approve low-risk changes automatically.
I4. Decide the risk rating of each change.
I5. Turn the CAB's recorded decisions into the weekly email to
    Helios, for the service delivery manager to review.""")],
    [("Sort them yourself", "One minute. Suitable, suitable with review, or not suitable?"),
     ("Ask Claude", "Send the file. Ask for each idea to be classified with a reason that covers consequence, reversibility and who checks the output."),
     ("Write one requirement", "In the same chat, pick the strongest idea and ask for a requirement that two people could check independently, with how success would be measured."),
     ("Get it marked", "Send the grader prompt.")],
    ["I3 is classified as not suitable, because only the CAB can approve.",
     "I4 is classified as not suitable or support only, because the risk rating is a judgement that belongs to accountable people.",
     "I1, I2 and I5 are classified as suitable with review.",
     "Each classification mentions the consequence of an error or who would catch it.",
     "The requirement is measurable, for example a count of forms reaching the CAB with no rollback plan.",
     "The requirement keeps a person as the reviewer or decision maker."],
    ("A reasonable sort", """I1 Suitable with review. Drafting from the form. The engineer
   or CAB chair checks it.
I2 Suitable with review. A completeness check. Low consequence,
   easy to verify, targets the top rejection reason.
I3 Not suitable. Approval belongs to the CAB.
I4 Not suitable as a decision. Claude could list the factors,
   and a person sets the rating.
I5 Suitable with review. The service delivery manager approves
   before it is sent.

A checkable requirement for I2
"Before each Tuesday CAB, every change request form is checked
for its mandatory fields. Forms with a missing field are
returned to the engineer. Measure: the number of changes
rejected at CAB for a missing rollback plan, compared with the
last eight weeks." """),
    ["Which idea would save the most time, and which carries the most risk?",
     "Could two of you check your requirement and agree on whether it was met?"],
    mark="your classification of the five ideas and the requirement you wrote in this conversation")

# ================================================================ 16
lab(16, "Three backup options for Vega", "Compare it",
    ["Helios needs a new backup arrangement for the Vega ground station. Three options have been collected. One has a gap, and one leans on a marketing line.",
     "Build a comparison the service owner could trust."],
    [("01-vega-backup-options.txt", "Requirements and options", """VEGA BACKUP - REQUIREMENTS AND OPTIONS

Helios requirements
R1. Retention of at least 35 days.
R2. Restore of 2 TB within 4 hours.
R3. An offsite copy.

Option A
Monthly cost: $1,900. Retention: 35 days. Offsite copy: yes.
Restore of 2 TB: 6 hours (measured in our lab).

Option B
Monthly cost: $2,400. Retention: 35 days. Offsite copy: yes.
Restore of 2 TB: 3 hours (measured in our lab).

Option C
Monthly cost: $1,500. Retention: 14 days. Offsite copy: yes.
Restore of 2 TB: not tested. The vendor's website says
"industry-leading restore speeds".""")],
    [("Ask for a comparison", "Send the file. Ask for a table of the three options against R1, R2 and R3, with met, not met or not supplied in each cell, and where each figure comes from."),
     ("Ask what is missing", "In the same chat, ask what you would need to find out before recommending, and how the vendor's claim for Option C should be treated."),
     ("Ask for a plan outline", "Ask for next steps as a list of questions and tasks. No dates and no named owners unless you supply them."),
     ("Get it marked", "Send the grader prompt.")],
    ["The table applies the same three requirements to every option.",
     "Option A is shown as failing R2 (6 hours against 4).",
     "Option C is shown as failing R1 (14 days against 35).",
     "Option C's restore time is shown as not supplied or not tested, and the website line is labelled a vendor claim.",
     "Option B is the only option shown as meeting all three requirements.",
     "The plan outline contains no invented dates and no invented owners."],
    ("The comparison", """            R1 retention   R2 restore 2 TB   R3 offsite
Option A    Met (35 d)     Not met (6 h)     Met
Option B    Met (35 d)     Met (3 h)         Met
Option C    Not met (14 d) Not supplied      Met

Sources: A and B restore times were measured in our lab.
C was not tested. "Industry-leading restore speeds" is the
vendor describing itself. It is a claim, not a measurement.

Only B meets all three. It is also the most expensive, which is
a decision for the service owner.

Before recommending: can C's retention be extended, and what
does a 2 TB restore on C actually take?"""),
    ["Option C is $900 a month cheaper than B. What would it take to make it a real contender?",
     "Did Claude give your plan any dates or owners you never supplied?"],
    mark="your comparison table, your list of unknowns and your plan outline in this conversation")
