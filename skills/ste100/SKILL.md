---
name: ste100
description: Write or rewrite prose in ASD-STE100 Simplified Technical English and remove AI slop. Short sentences, active voice, one idea per sentence, one word for one meaning, no filler, no hype, no stock AI phrasing, and no loss of facts. Use for docs, instructions, READMEs, reports, emails, UI copy, agent prompts, skill files, and answers, or when the user says "STE", "STE100", "plain English", "simplify", "too wordy", "cut the fluff", "de-slop", "sounds like AI", or "make it human". Not for code, quotes, marketing copy, or text in a named personal voice.
---

# STE100 (non-slop writing)

ASD-STE100 Simplified Technical English is a writing standard from the aerospace industry. It was made so that any reader, in any level of English, gets one meaning from each sentence. This skill uses its main rules, and adds a check for the patterns that make text read as machine-written.

## The core rule: change the words, never the substance

Simplify how you say it. Do not drop facts, numbers, caveats, reasons, or recommendations to make text shorter. If a point needs 6 short sentences, write 6. A correct, complete answer comes first. If a rule below makes the text wrong or vague, break the rule.

## STE rules

**Sentences**
- Instructions: 20 words or fewer. Descriptions: 25 words or fewer. Split long sentences; do not cut content.
- One idea per sentence. One instruction per sentence.
- Active voice: "The script reads the file", not "The file is read". Use passive only when the actor is unknown or does not matter.
- Commands for instructions: "Open the file", not "You may want to open the file".
- Condition before action: "If the test fails, read the log."
- Simple present for facts. "Will" only for real future actions.

**Words**
- Common words: "use" not "utilize", "start" not "commence", "show" not "demonstrate", "help" not "facilitate", "about" not "approximately".
- One word, one meaning. Use the same word for the same thing every time. Do not change words for variety.
- No idioms, metaphors, or vague phrasal verbs. "Install" not "set up" when you mean install. "Do" not "carry out".
- Do not stack more than 3 nouns. "The handler for password reset requests", not "user account password reset request handler".
- Keep articles ("the", "a"). Repeat the noun when "it" or "this" could be unclear.
- Keep technical names (product names, API names, acronyms). Define a term on first use if the reader may not know it.

**Structure**
- Most important information first.
- Steps as a numbered list, one action per step.
- Warnings and cautions before the step they apply to, as short commands.
- One topic per paragraph, 3 to 4 sentences at most.
- Numbers as digits with units: "3 files", "5 min", "$29".

## Slop check

Remove these patterns. They add words and no information, and they tell the reader a machine wrote the text.

| Pattern | Examples | Fix |
|---|---|---|
| Empty openers and closers | "Great question!", "Certainly!", "I hope this helps", "Let me know if you have any other questions" | Delete. Start with the answer. |
| Throat-clearing | "It's important to note that", "It's worth mentioning", "In today's fast-paced world", "When it comes to" | Delete. State the fact. |
| Hype words | "revolutionary", "game-changer", "cutting-edge", "seamless", "robust", "powerful", "unlock", "supercharge", "elevate" | Say what it does, with a number if you have one. |
| Stock AI vocabulary | "delve", "tapestry", "landscape", "realm", "navigate the complexities", "testament to", "underscore", "pivotal", "multifaceted", "embark" | Use the plain word or delete. |
| "Not X, but Y" frames | "It's not just a tool, it's a movement" | State Y directly. |
| Rule of three by habit | "fast, reliable, and scalable" when only one is shown | Keep only what is true and proven. |
| Hedge stacks | "may potentially help to somewhat reduce" | Say how sure you are once, in plain words: "This reduces X in most cases." |
| Restating the question | "You asked about X. X is..." | Answer. |
| Summary of the summary | "In conclusion", "Overall", "To sum up" after a short text | Delete, or end on the one action that matters. |
| Fake enthusiasm and flattery | "What a great idea!", "You're absolutely right!" | Delete. Agree or disagree with a reason. |
| Bold and emoji everywhere | Bold on every other phrase, emoji bullets | Bold only the one thing a skimmer must see. |
| Em dash chains | "The tool — which is new — works — mostly" | Use periods and commas. Split the sentence. |
| Vague claims | "many experts say", "studies show", "significantly faster" | Name the source and the number, or remove the claim. |

## Do not apply to

- Code, commands, config, logs, and quoted or pasted text. Keep them exact. Code comments may follow STE.
- Creative writing, marketing and persuasive copy, and text in a named voice (a personal LinkedIn or X voice, a video script). The slop check still helps there, but the STE sentence rules do not.
- Text in other languages. STE is an English standard.
- Any text where the user asks for a different style. The user wins.

## How to apply

1. Find the one purpose of the text and who reads it.
2. Rewrite with the STE rules. Keep every fact.
3. Run the slop check on the result.
4. Final read: Is any sentence too long? Is any passive voice without a reason? Does one thing have two names? Is any fact missing? Fix, then deliver.
5. Show the new text. List the main changes in 3 bullets only if the user asks.

## Example

Before: "It's worth noting that you'll probably want to leverage a robust caching layer in order to seamlessly mitigate the latency that might be experienced when the database is being queried repeatedly."

After: "Add a cache. The cache stores the results of repeated queries. This reduces the wait time for each request."

The cause (repeated queries), the fix (a cache), and the benefit (less wait time) are all still there. The slop is gone.
