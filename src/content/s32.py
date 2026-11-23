PLAN = """Two weeks out
- Sit Practice exam 1 with the timer on. Do not look anything up.
- Read the result page. Note your two weakest domains.
- Re-read the sessions listed under "Sessions to revisit".

One week out
- Sit Practice exams 2 and 3 on different days.
- For every miss, read all four reasons, not only the right one.
- Redo the section quizzes for your weakest domain.

Last few days
- Sit Practice exams 4 and 5.
- Redo any exam where you scored under 45.
- Skim the takeaways at the end of each session.

The day before
- No new material. Check your booking, ID and equipment."""

SESSION = {
    "id": 32,
    "slug": "preparing-for-the-exam",
    "short": "Preparing for the exam",
    "lead": "You have done the content. This session covers what the exam looks like, how to pace it, how the questions are built, and how to use the five practice exams.",
    "body": [
        ("h", "What you are sitting"),
        ("p", "The Claude Certified Associate, Foundations exam (code CCAO-F) is Anthropic's entry-level certification for people who use Claude at work. No coding or API knowledge is needed. It tests whether you can prompt well, judge an output, pick the right tool, design a sensible workflow, configure a Project, work within governance and fix things when results are poor."),
        ("table", ["", "Detail"], [
            ["Questions", "60"],
            ["Time", "120 minutes, about two minutes a question"],
            ["Question types", "Multiple choice (one answer) and multiple response (more than one answer)"],
            ["Style", "Short workplace scenarios. Pick the best response"],
            ["Passing score", "720 on a scale of 100 to 1,000"],
            ["Delivery", "Proctored, closed book"],
            ["Fee", "US$99"],
            ["Eligibility", "Staff of organisations in the Claude Partner Network"],
        ]),
        ("note", "Check before you book", "These details were current when this session was written in November 2026. Exam details change. Confirm them in the official exam guide when you register, and go with the guide if anything differs."),
        ("p", "A scaled score is not a percentage. 720 does not mean 72% of questions correct. Scaling adjusts for the difficulty of the particular set of questions you get, so nobody can tell you the exact number of questions you need. Aim well clear of the line."),

        ("h", "Where the marks are"),
        ("p", "The exam has seven domains with published weightings. This is how they map to the sessions, and roughly how many of the 60 questions each one is worth."),
        ("table", ["Domain", "Weight", "About", "Sessions"], [
            ["Prompting and task execution", "14%", "8 questions", "1 to 4"],
            ["Output evaluation and validation", "21%", "13 questions", "5 to 10"],
            ["Product and model selection", "12%", "7 questions", "11 to 14"],
            ["Workflow integration and solution design", "16%", "10 questions", "15 to 19"],
            ["Configuration and knowledge management", "12%", "7 questions", "20 to 24"],
            ["Governance, risk and responsible use", "15%", "9 questions", "25 to 28"],
            ["Troubleshooting and optimisation", "10%", "6 questions", "29 to 31"],
        ]),
        ("p", "Output evaluation is the biggest single block. Add governance and more than a third of the exam is about checking what Claude produced and deciding what is appropriate. Prompt writing, which is what most people think the exam is about, is under a sixth."),

        ("h", "How the questions are built"),
        ("p", "Nearly every question is a short scenario followed by \"what is the best response\" or \"what should happen first\". Usually more than one option sounds reasonable. You are choosing the best one, so read all four before you answer."),
        ("p", "The right answer tends to share a few habits. You have seen them in every session:"),
        ("list", [
            "**It stays inside the evidence.** It uses what was supplied and says \"not stated\" about what was not.",
            "**It keeps a person accountable.** Claude prepares. An authorised person decides, approves and sends.",
            "**It is the narrow fix.** Change one thing, rerun the same test, compare with the same criteria.",
            "**It names an authority.** The current approved source wins over drafts, notes and older versions.",
            "**It matches effort to consequence.** More review where an error would hurt. Less where it would not.",
            "**It checks before it assumes.** Classification before sharing. Status and date before using a record.",
        ]),
        ("p", "The wrong answers have habits too. Learn to spot them and you can often eliminate two options straight away."),
        ("table", ["If an option says...", "It is usually wrong because..."], [
            ["Use the most capable model", "A bigger model does not fix a vague prompt, a bad source or a missing control"],
            ["Remove the review to save time", "Efficiency never comes from removing a necessary control"],
            ["Tell Claude more firmly, or repeat the instruction", "Emphasis is not information"],
            ["Rewrite the whole prompt or start again", "It hides the cause and throws away what works"],
            ["Estimate it, assume it or fill the gap", "Missing information gets reported, not invented"],
            ["The newest file, or the first result, wins", "Authority comes from approval and status, not date or order"],
            ["It is fine because someone senior said so", "Only the authorised exception process changes a control"],
            ["Ask Claude whether its answer is right", "Self-confirmation is not verification"],
            ["Report an outage", "A poor answer is not evidence of a technical fault"],
            ["Add a disclaimer", "A disclaimer controls nothing"],
        ]),
        ("note", "Watch the absolute words", "\"Always\", \"never\", \"guarantees\" and \"all\" are rarely right in this exam. The subject is judgement, and judgement depends on context."),

        ("h", "Multiple response questions"),
        ("p", "Some questions ask you to select more than one answer, and they tell you how many. Read the instruction line first. Treat each option as its own true or false question against the scenario, then check you have selected the number asked for. Every section quiz in this guide has one \"choose two\" question, and each practice exam has ten. In the practice exams a \"choose two\" question scores only if you pick both correct options. That is the strict reading. Check the official guide for how the real exam scores them."),

        ("h", "Pacing"),
        ("p", "Sixty questions in 120 minutes is two minutes each. Most people do not need all of it, and you want time in hand at the end."),
        ("steps", [
            ("First pass: about 75 minutes", "Answer everything you can. If a question takes more than about 90 seconds, pick your best option, flag it and move on."),
            ("Second pass: about 30 minutes", "Go back through the flagged questions only."),
            ("Final check: about 15 minutes", "Make sure nothing is unanswered. Check the multiple response questions have the right number selected."),
        ]),
        ("p", "Never leave a question blank. An unanswered question scores the same as a wrong one, so a guess can only help. Be careful about changing answers on the second pass. Change one only if you can say what you misread the first time."),
        ("p", "A quick checkpoint: you should be at about question 20 after 25 minutes and about question 40 after 50."),

        ("h", "How the practice exams here work"),
        ("p", "There are five practice exams in the menu. Each has 60 questions spread across the seven domains in the same proportions as the real exam: 8, 13, 7, 10, 7, 9 and 6. All 300 questions are different. Fifty of each exam's questions have one correct answer and ten ask you to choose two."),
        ("table", ["Feature", "How it works"], [
            ["Timer", "Optional. \"Start with a 120-minute timer\" gives you the real time limit. The clock pauses if you leave the exam and resumes when you come back"],
            ["Moving around", "Tap any number in the strip, or use Previous and Next. On a keyboard, A to D or 1 to 4 answers and the arrow keys move"],
            ["Flag for review", "Marks a question so you can find it again. Flagged and unanswered questions are counted for you before you finish"],
            ["Answers", "Hidden until you finish, like the real exam"],
            ["Result", "Your score, a bar for each exam domain, and a list of sessions to revisit with links"],
            ["Reasons", "Every option on every question has a reason, right or wrong. \"Show only the ones I missed\" filters the list"],
            ["Saving", "Your progress and result stay in this browser on this device until you start that exam again. Close the page and come back and it is still there"],
            ["Privacy", "Nothing is sent anywhere. Nobody else can see your answers or your score"],
            ["Starting again", "\"Start this exam again\" clears the saved result and puts both the questions and the answer options in a new order"],
        ]),
        ("p", "The section quizzes behave differently on purpose. Those reset every time you visit, because they are for quick practice. The practice exams are kept, because you will want to come back and read the reasons."),
        ("p", "Because the result is saved in the browser, it does not follow you between devices. If you start an exam on your phone, finish it on your phone. Private or incognito windows will not keep it once they are closed."),
        ("note", "What score to aim for", "The target shown on each exam is 45 of 60, which is 75%. That is a study guide and not the pass mark, because the real exam is scaled. If you are consistently at 50 or above across the five, you are in good shape. If one domain's bar is clearly shorter than the rest, that is where your time should go."),

        ("h", "Getting the most out of a practice exam"),
        ("list", [
            "Sit at least one with the timer on, in one sitting, with nothing else open. It is closed book on the day.",
            "Read the reasons for the questions you got **right** as well. A lucky guess is a gap you have not found yet.",
            "For each miss, work out which wrong-answer habit caught you. If it is the same one three times, that is your pattern.",
            "Do not redo an exam the same day. You will be remembering answers, not reasoning. The shuffle helps, and a few days helps more.",
            "Do not burn all five in a weekend. Space them so the result pages can steer your revision in between.",
        ]),

        ("h", "A two-week plan"),
        ("doc", "Suggested run-in", PLAN),

        ("h", "On the day"),
        ("list", [
            "Have your ID ready and sign in early. Proctored exams have check-in steps that take time.",
            "If you are sitting it remotely, clear your desk and close other applications beforehand. The proctoring rules will tell you what is allowed.",
            "Read the last line of each question first. It tells you what you are looking for in the scenario.",
            "When two options both look right, ask which one keeps the evidence boundary and keeps a person accountable.",
            "If you hit a run of hard questions, flag and keep moving. The questions are not in order of difficulty.",
        ]),
        ("p", "You have covered all seven domains and you have 300 practice questions with reasons. The exam is checking whether you use Claude with good judgement, which is the same thing the last 31 sessions have been about."),
    ],
    "takeaways": [
        "60 questions, 120 minutes, about two minutes each. Pass is 720 on a scaled 100 to 1,000, which is not a percentage.",
        "Output evaluation and governance together are more than a third of the exam.",
        "The best answer stays inside the evidence, keeps a person accountable and makes the narrowest fix.",
        "Never leave a blank. Flag, move on and come back.",
        "The five practice exams save on your device until you restart them, and reshuffle when you do.",
    ],
    "practice": "Book a 120-minute slot this week and sit Practice exam 1 with the timer on. Afterwards, write down your two weakest domains and the wrong-answer habit that caught you most often.",
    "quiz": [
        {"q": "The exam has 60 questions and a 120-minute limit. You have spent three minutes on one question and are still unsure. What is the best move?", "options": [
            ("Keep working on it until you are certain.", False, "Time spent here comes off questions you could answer quickly."),
            ("Leave it blank and move on.", False, "A blank scores the same as a wrong answer, so a guess can only help."),
            ("Choose your best option, flag it and move on.", True, "You bank a possible mark and can come back if there is time."),
            ("Pick the longest option.", False, "Length is not a reliable guide."),
        ]},
        {"q": "The passing score is 720 on a scale of 100 to 1,000. What does that mean?", "options": [
            ("You need exactly 72% of the questions correct.", False, "A scaled score is not a percentage of questions."),
            ("It is a scaled score, so it does not convert directly to a number of correct answers.", True, "Scaling adjusts for the difficulty of the question set, so aim well clear of the line."),
            ("You need 720 questions correct.", False, "There are 60 questions."),
            ("Only the first 72 minutes count.", False, "The score is not about time."),
        ]},
        {"q": "Two options both look reasonable. Which test is most likely to separate them?", "options": [
            ("Which one uses the most technical language.", False, "Jargon is not correctness."),
            ("Which one recommends the most capable model.", False, "That is a common wrong-answer habit."),
            ("Which one is listed first.", False, "Position means nothing."),
            ("Which one stays inside the evidence and keeps a person accountable.", True, "Those two habits run through the correct answers in every domain."),
        ]},
        {"q": "Which TWO statements about the practice exams in this guide are correct?", "multi": True, "options": [
            ("Your progress and result are saved on your device until you start that exam again.", True, "They are kept in the browser so you can come back to the reasons."),
            ("Your score is visible to your manager.", False, "Nothing is sent anywhere. Nobody else can see it."),
            ("Starting an exam again puts the questions and the answer options in a new order.", True, "Each attempt is reshuffled."),
            ("They reset every time you open the page, like the section quizzes.", False, "Section quizzes reset. Practice exams are kept."),
        ]},
        {"q": "You scored 52 of 60 on a practice exam. What is the most useful thing to do next?", "options": [
            ("Sit the same exam again straight away to get 60.", False, "You would be remembering answers, not reasoning."),
            ("Read the reasons for the eight you missed, check the domain bars, and skim the reasons on the ones you guessed.", True, "The result page shows where to spend time, and lucky guesses are gaps too."),
            ("Stop revising. You have passed.", False, "A practice score is a guide and the real exam is scaled."),
            ("Skip the result page and start the next exam.", False, "The result page is where the learning is."),
        ]},
    ],
    "deck": [
        {"t": "title", "h": "Preparing for the exam", "sub": "Session 32 of 32. Exam preparation.", "notes": "Last one. No new content today. This is about the exam itself and how to use the practice exams."},
        {"t": "cards", "h": "The exam at a glance", "cols": 4, "cards": [
            ("60", "Questions."),
            ("120 minutes", "About two a question."),
            ("720", "To pass, on a scale of 100 to 1,000."),
            ("Proctored", "Closed book. US$99."),
        ], "notes": "Multiple choice and multiple response. Partner network eligibility. Tell them to confirm details in the official guide when they register."},
        {"t": "list", "h": "Where the 60 questions come from", "items": [
            ("Output evaluation", "21%. About 13 questions."),
            ("Workflow integration", "16%. About 10."),
            ("Governance", "15%. About 9."),
            ("Prompting", "14%. About 8."),
            ("Product and model selection", "12%. About 7."),
            ("Configuration and knowledge", "12%. About 7."),
            ("Troubleshooting", "10%. About 6."),
        ], "notes": "Evaluation plus governance is over a third. Prompt writing is under a sixth. That surprises people."},
        {"t": "cards", "h": "What right answers have in common", "cols": 3, "cards": [
            ("Inside the evidence", "\"Not stated\" beats a good guess."),
            ("A person is accountable", "Claude prepares. People decide."),
            ("The narrow fix", "One change, same test."),
            ("A named authority", "Approved and current wins."),
            ("Effort follows consequence", "More review where it would hurt."),
            ("Check before assuming", "Classify, then share."),
        ], "notes": "When two options both look right, these are the tie-breakers."},
        {"t": "list", "h": "What wrong answers have in common", "items": [
            ("Use the biggest model", "Does not fix a prompt, a source or a control."),
            ("Remove the review", "Never the efficiency answer."),
            ("Say it more firmly", "Emphasis is not information."),
            ("Rewrite everything", "Hides the cause."),
            ("Estimate or assume", "Report the gap."),
            ("Someone senior said so", "Not an exception."),
        ], "notes": "Also: newest file wins, ask Claude if it is right, report an outage, add a disclaimer. Spot two of these and you are down to a coin flip at worst."},
        {"t": "steps", "h": "Pacing", "steps": ["First pass: 75 min", "Flagged ones: 30 min", "Final check: 15 min"], "notes": "Over 90 seconds on one question: best guess, flag, move. Never leave a blank. Question 20 by 25 minutes, 40 by 50."},
        {"t": "cards", "h": "The five practice exams", "cols": 2, "cards": [
            ("Same shape as the real thing", "60 questions each, split 8, 13, 7, 10, 7, 9, 6 across the domains. 300 different questions."),
            ("Saved on your device", "Close it and come back. It stays until you start that exam again. Nobody else sees it."),
            ("Reshuffled on a restart", "Questions and answer options both come back in a new order."),
            ("A reason for every option", "Right and wrong. Read the ones you guessed as well."),
        ], "notes": "Good moment for a live demo: open one, answer three, close the tab, reopen. Then show a result page."},
        {"t": "big", "h": "Aim for 45 of 60. Be happier at 50.", "p": "The target is a study guide. The real exam is scaled, so aim well clear.", "notes": "Space them out. Exam 1 two weeks out, 2 and 3 a week out, 4 and 5 in the last few days. Not all five in a weekend."},
        {"t": "quiz", "h": "Your turn: five questions", "notes": "Ten minutes. Then send them off to book a slot for Practice exam 1."},
    ],
}
