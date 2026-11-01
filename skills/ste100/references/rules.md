# ASD-STE100 rule notes

Our own summary of the ideas in ASD-STE100 Issue 9 (January 2025), grouped by the standard's nine rule sections. It is not the official text. Rule numbers differ between issues and between secondary sources, so this file does not cite them. For formal work, get the official standard free from asd-ste100.org.

## Section 1: Words

| Idea | Do | Do not |
|---|---|---|
| Approved words only (strict mode) | Use words from the dictionary, in their approved meaning and part of speech | Use a word in a second meaning, even if it is approved in its first meaning |
| One word, one meaning | "Remove the cover." ... "Install the cover." | "Take off the cover." ... "Put back the lid." |
| Technical names | Names of things in your field: "API key", "pull request", "webhook", "Postgres" | Invent a new name for a thing that already has one |
| Technical verbs | Verbs specific to the field: "commit", "deploy", "compile", "merge" | Use a technical verb for a general action ("deploy your attention") |
| Simple words | "use", "start", "show", "help", "end", "about" (concerned with), "get" | "utilize", "commence", "demonstrate", "facilitate", "terminate" |
| Same part of speech | "Do a test of the endpoint." / "Make sure that the test passes." | "Test the endpoint." in strict mode, because TEST is approved as a noun only |

**Common cheat-sheet errors** (from a fact-check of a widely shared STE cheat sheet, Max Nardit, 2026):
- **APPROXIMATELY is approved** as an adverb. ABOUT is approved as a preposition that means "concerned with". So "approximately 5 min" is correct STE. Practical mode may still prefer "about 5 min".
- **TEST is approved as a noun only.** "Do a test", not "Test it", in strict mode.
- **"in order to" → "to"** is good advice, but it is a writing choice, not a dictionary entry.

When you are not sure a word is approved, keep it in practical mode and **flag it** in strict mode. Do not guess.

## Section 2: Noun clusters

- Do not use more than **3 nouns** in a row.
- Break long clusters with prepositions: "the configuration file for the deployment pipeline", not "deployment pipeline configuration file".
- If a long cluster is the official name of a thing (a product or a field label), keep it, and use a short form or explanation after the first use.

## Section 3: Verbs

- Allowed: infinitive ("to install"), imperative ("Install"), simple present ("installs"), simple past ("installed"), simple future ("will install"), past participle as an adjective ("the installed package").
- Not allowed: perfect tenses ("has installed", "had installed"), continuous forms ("is installing"), past participle with a helper to build complex tenses.
- "-ing" forms only as part of a technical name ("logging level", "load balancing"), never as a verb.
- Active voice. In descriptive writing, the passive is allowed only when the actor is unknown.
- Use the verb for the action, not a noun built from it: "Configure the server", not "Do the configuration of the server". "Examine the logs", not "Perform an examination of the logs".

## Section 4: Sentences

- One topic per sentence.
- Do not leave out words to shorten text: keep articles, the subject, the verb and "that".
- Use vertical lists to make complex text clear.
- Use connecting words and phrases to link sentences that hold related topics ("then", "but", "if", "because", "after").

## Section 5: Procedures

- **20 words or fewer** per sentence.
- Write one instruction per sentence. Two actions may share a sentence only when the reader does them at the same time.
- Use the imperative. Put a condition at the start: "If the build fails, ...", "When the job stops, ...".
- Write steps in the order of the task. Number them.
- Put descriptive information (why, what happens next) in a note, separate from the step.

## Section 6: Descriptive writing

- **25 words or fewer** per sentence.
- **6 sentences or fewer** per paragraph. One topic per paragraph.
- Start with the topic sentence. Give the most important information first.
- Use paragraphs to show the logic of the text. Give only the information the reader needs.

## Section 7: Safety instructions

- Start the warning or caution with a simple, clear command or condition.
- Give a short explanation of the risk: what can happen if the reader does not obey.
- Put the safety instruction before the step it applies to.
- Do not put two different risks in one warning.

Example: "**Warning:** Do not run this command on the production database. It deletes all rows in the users table."

## Section 8: Punctuation and word counts

- No semicolons.
- Use colons to introduce a list.
- Use parentheses only for references, labels and short explanations.
- No contractions in strict mode.
- Word counts: a hyphenated word, a number with its unit, a date, and an identifier such as a file path each count as one word. Items in a vertical list are counted as separate sentences.

## Section 9: Writing practices

- Use the same structure for the same type of content (every error message, every step, every release note).
- Be specific: numbers and units, not "a few" or "soon".
- Write for the reader who knows the least English and the least about the task.

## Sources

- ASD-STE100 Issue 9, ASD Simplified Technical English Maintenance Group (STEMG), January 2025. Free on request from asd-ste100.org.
- Wikipedia, "Simplified Technical English" (history, issue dates, rule and dictionary sizes).
- Max Nardit, "ASD-STE100 for LLMs: rules, example and prompt, plus Karpathy's tips and a cheat sheet fact-check" (dictionary errors, practical vs strict modes).
- explainx.ai, "How to use ASD-STE100 Simplified Technical English with AI" (rule block and linter idea).
