---
name: ste100
description: Write or rewrite prose in ASD-STE100 Simplified Technical English (Issue 9) and remove AI slop. Applies the countable STE rules (20-word procedure sentences, 25-word descriptive sentences, 6-sentence paragraphs, active voice, allowed verb forms, 3-word noun clusters, one instruction per sentence, condition before command), then a slop check built from Wikipedia's "Signs of AI writing" list, then an optional linter. Use for docs, READMEs, runbooks, instructions, error messages, UI copy, incident reports, release notes, agent prompts and skill files, or when the user says "STE", "STE100", "ASD-STE100", "plain English", "simplify", "too wordy", "cut the fluff", "de-slop", "sounds like AI", or "make it human". Do not use for code, quotes, marketing copy, or text in a named personal voice (LinkedIn, X, Reddit, video scripts) except for the slop check.
---

# ASD-STE100 (non-slop writing)

## What the standard is

ASD-STE100 Simplified Technical English (STE) is a controlled form of English. The European aerospace industry (AECMA, now ASD) started it in 1983 for aircraft maintenance manuals, and the first guide came out in the mid-1980s. The current version is **Issue 9, released January 2025**. It is the first issue published as an international standard. The ASD Simplified Technical English Maintenance Group (STEMG) maintains it, and ASD gives it out free of charge on request through asd-ste100.org (free since Issue 6, 2013).

The standard has two parts:
1. **Writing rules** (53 in recent issues) in nine sections: words, noun clusters, verbs, sentences, procedures, descriptive writing, safety instructions, punctuation and word counts, and writing practices.
2. **A dictionary** of about 900 approved words. Each approved word has **one meaning and one part of speech**. The dictionary also lists common unapproved words with approved alternatives. Technical names and technical verbs for your field (for example "API", "commit", "deploy") are allowed by the writing rules even though they are not in the dictionary.

**Be honest about compliance.** You do not have the official dictionary. This skill gives text that follows the countable rules. It does **not** make text "STE compliant". Never claim compliance. For regulated documents (aviation, defense, medical devices), tell the user to check the output against the official standard with a trained STE writer.

## The core rule: change the words, never the substance

Simplify how the text says something. Do not drop facts, numbers, identifiers, commands, caveats, reasons, or recommendations. Keep the original strength of every claim: "usually" stays "usually", "must" stays "must". If a point needs 6 short sentences, write 6. Add nothing that is not in the source. If a rule makes the text wrong or vague, break the rule.

## Two modes

| Mode | Use for | What changes |
|---|---|---|
| **Practical (default)** | Docs, READMEs, answers, reports, prompts, UI copy | All countable rules below. Vocabulary is looser: use common words, one word per meaning, but technical and common words outside the STE dictionary are fine. Andrej Karpathy calls this asking for text "80% of the way" to STE. |
| **Strict** | Procedures, safety warnings, regulated manuals, when the user asks for strict STE | Countable rules plus dictionary discipline: use each word in one meaning and one part of speech only, prefer the most basic word, and **flag every word you are not sure is approved** so a person can check it in the dictionary. |

## The rules (practical summary)

Full rule notes, with examples and the common cheat-sheet errors, are in `references/rules.md`. Read it for strict mode or when unsure.

**Words**
- One word, one meaning. Use the same word for the same thing every time. Never change words for variety.
- Use the simplest common word: "use" not "utilize", "start" not "commence", "show" not "demonstrate", "help" not "facilitate", "end" not "terminate".
- Use a word only in its usual part of speech. Do not turn nouns into verbs ("action the ticket", "impact the build").
- No idioms, no figures of speech, no vague phrasal verbs ("set up" for install, "carry out" for do, "look into" for examine).
- Technical names and verbs of the field are allowed. Define a term the first time if the reader may not know it.

**Noun clusters**
- No more than 3 nouns in a row. "the handler for password reset requests", not "user password reset request handler". Use prepositions or a short explanation to break long clusters.

**Verbs**
- Allowed forms: infinitive, imperative, simple present, simple past, simple future ("will"), and the past participle used as an adjective ("the installed package").
- No perfect or continuous forms when a simple form works: "The build fails", not "The build has been failing".
- No "-ing" forms, except as part of a technical name ("logging level", "string").
- Active voice. In descriptive text, use the passive only when you do not know who or what does the action.
- Use an action verb, not a noun made from a verb: "Install the package", not "Perform the installation of the package".

**Sentences**
- One topic per sentence.
- Do not leave out words to make text shorter. Keep "the", "a", "an", "that", verbs and subjects. STE is not telegraph style.
- Use vertical lists for complex text and for items in a series.
- Use connecting words ("then", "but", "because", "if") to join thoughts in descriptive text.

**Procedures**
- Sentences of **20 words or fewer**.
- Imperative (command) form: "Open the file." Not "You should open the file" or "The file can be opened".
- One instruction per sentence. Two actions can share a sentence only if they occur at the same time.
- Put a condition before the command: "If the test fails, read the log."
- Numbered steps, in the order the reader does them.
- Put descriptive information in a separate note, not inside the step.

**Descriptive writing**
- Sentences of **25 words or fewer**.
- **6 sentences or fewer** per paragraph, one topic per paragraph.
- Start with the most important information: the topic sentence comes first.
- Give only the information the reader needs.

**Safety instructions (warnings and cautions)**
- Start with a simple, clear command or condition: "Do not delete the main branch." "Stop the service before you edit the config."
- Give the risk in a short explanation after the command: what can happen.
- Put the warning **before** the step it applies to, not after.

**Punctuation and word counts**
- No semicolons. Use two sentences.
- No contractions in strict mode ("do not", not "don't"). Practical mode may keep them if the user's style uses them.
- Use parentheses only for references, labels and short clarifications. Do not hide instructions in them.
- A hyphenated word, a number with its unit, and a code identifier each count as one word.

**Writing practices**
- Say exactly what you mean. Use numbers and units: "3 files", "5 min", "$29", not "a few" or "quickly".
- Keep the same structure for the same type of information (every error message: what happened, then what to do).

## Slop check

STE fixes sentence shape. It does not catch every pattern that makes text read as machine-written. After the rewrite, remove the patterns in `references/slop-patterns.md`. The short list:

1. **Empty openers and closers:** "Great question!", "Certainly!", "I hope this helps", "Let me know if...". Start with the answer.
2. **Inflated significance:** "stands as a testament", "pivotal", "underscores its importance", "evolving landscape", "indelible mark", "setting the stage for".
3. **AI vocabulary clusters:** "delve", "tapestry", "intricate", "meticulous", "crucial", "vibrant", "showcase", "realm", "navigate", "foster", "Additionally" at the start of every paragraph.
4. **Copula avoidance:** "serves as", "stands as", "functions as", "boasts", "features" where "is" or "has" works.
5. **Negative parallelisms:** "It's not just X, it's Y", "not X, but Y", "no X, no Y, just Z". State Y.
6. **Trailing "-ing" analysis clauses:** "..., highlighting the need for...", "..., ensuring that...". These also break the STE "-ing" rule. Write a second sentence or delete.
7. **Promotional tone:** "groundbreaking", "seamless", "robust", "powerful", "game-changer", "unlock", "supercharge", "renowned", "nestled in the heart of".
8. **Vague attribution:** "experts say", "industry reports", "studies show", "observers note". Name the source or remove the claim.
9. **Rule of three by habit:** "fast, reliable, and scalable" when only one is shown.
10. **Formulaic sections:** "Challenges and Future Outlook", "Despite these challenges...", a conclusion that repeats the summary.
11. **Hedge stacks:** "may potentially help to somewhat reduce". Say how sure you are once.
12. **Formatting slop:** bold on every phrase, emoji bullets, headings over two-line sections, em dash chains.
13. **Chatbot artifacts:** "As an AI...", "Here is a revised version:", placeholder text, "as of my last update".

Wikipedia's editors warn that no single pattern proves text is AI-written, and that accuracy and sourcing matter more than surface patterns. Fix the pattern because it wastes the reader's time, not to hide anything.

## Do not apply to

- Code, commands, config, logs, file paths, and quoted or pasted text. Keep them exact. Code comments may follow STE.
- Persuasive and marketing copy, stories, and text in a named voice (a personal LinkedIn or X voice, video scripts). Run only the slop check there; the STE sentence rules do not apply.
- Text in other languages. STE is an English standard.
- Any text where the user asks for a different style. The user wins.

## Workflow

1. Find the text type: **procedure** (steps), **description** (explanation), or **safety instruction**. Many documents mix them. Use the rule set for each part.
2. Choose the mode: practical unless the user asks for strict or the text is a procedure or warning in a regulated field.
3. Rewrite with the rules. Keep every fact, number, identifier and hedge strength.
4. Run the slop check.
5. Optional: run the linter on the result and fix real hits. It gives false positives (for example "string" ends in "-ing"):
   ```bash
   python3 ~/.claude/skills/ste100/scripts/ste_check.py FILE.md
   python3 ~/.claude/skills/ste100/scripts/ste_check.py --procedure FILE.md   # 20-word limit for all sentences
   ```
6. Final read: Is any sentence too long? Is there a passive with a known actor? Does one thing have two names? Is any fact missing? Is any hedge stronger or weaker than the source?
7. Deliver the text. In strict mode, list the words to check in the dictionary. Do not mention STE unless the user asked for it.

## Example

Before (descriptive, 33 words, passive, hedges, slop):
"It's worth noting that a robust caching layer should be leveraged in order to seamlessly mitigate the latency that might potentially be experienced when the database is being queried repeatedly by the application."

After (3 sentences, 8 to 10 words each):
"Add a cache between the application and the database. The cache keeps the results of repeated queries. This decreases the wait time for each request."

Before (procedure, two instructions, condition last, no warning):
"Run the migration and then restart the server, but make sure you've taken a backup first if you're on production."

After:
"**Caution:** On production, make a backup before you continue. A failed migration can delete data.
1. Run the migration.
2. Restart the server."
