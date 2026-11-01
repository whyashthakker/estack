---
name: plain
description: Rewrite or write text in plain, simple English that is short, clear, and easy to translate, based on the rules of ASD-STE100 Simplified Technical English. Use for docs, instructions, UI copy, error messages, agent prompts, skill files, and status reports, or when the user says "make this plain", "simplify this", "too wordy", "cut the fluff", or "STE".
---

# Plain

Goal: one reading is enough. The reader can act without guessing, even if English is their second language.

## Rules

**Words**
- Use common words. "Use" not "utilize", "start" not "commence", "help" not "facilitate", "about" not "approximately".
- One word, one meaning. If you call it a "workspace", do not call it a "project" two lines later.
- Use technical names that the reader needs, and define each one the first time.
- Cut filler: "very", "really", "just", "basically", "in order to", "it is important to note that", "please note".

**Sentences**
- Instructions: 20 words or fewer per sentence. Descriptions: 25 or fewer.
- One instruction per sentence. Put the action verb first: "Run the tests." "Open the file."
- Active voice. "The script deletes the cache", not "The cache is deleted".
- Say who does what. Avoid "it" when it is not clear what "it" is.
- Put a condition before the action: "If the test fails, check the log."

**Structure**
- Most important information first.
- Steps as a numbered list, one action per step.
- Warnings before the step they apply to, not after.
- One topic per paragraph. Paragraphs of 3 to 4 sentences at most.

**Tone**
- Direct and neutral. No hype, no apology, no padding at the start or end ("Great question!", "I hope this helps").
- Numbers as digits with units: "3 files", "5 min", "$29".

## How to apply

1. Read the text and find its one purpose.
2. Rewrite it with the rules above. Keep every fact. Do not add new ones.
3. Show the new version. If the user asks, list the main changes in 3 bullets.

Use this skill for text that instructs or informs. Do not apply it to marketing copy, stories, or a personal voice unless the user asks.
