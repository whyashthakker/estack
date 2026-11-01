---
name: quiz-me
description: Turn the work the agent just did (or a topic, file, or doc) into a short quiz so the user learns while they ship. Asks 3 to 5 questions one at a time, grades each answer, and explains the gaps. Use when the user says "quiz me", "test me", "did I get this", "check my understanding", or after a large change they must own and maintain.
---

# Quiz me

Goal: the user can maintain what the agent built. Agents write code faster than people read it. A short quiz finds the gaps before they become bugs.

## 1. Pick the material

- Default: the changes in this session (`git diff` against the start point, or the files you edited).
- Or: the topic, file, or doc the user names.
- Find the 3 to 5 ideas the user **must** know to own this. Ignore trivia (exact names, line numbers, syntax).

Good targets:
- Why this approach and not the obvious other one.
- What breaks if a key line is removed or changed.
- Where the data comes from and where it goes.
- Which case is not handled.
- How to check that it works.

## 2. Ask one question at a time

Mix the types:
- **Predict:** "If the API returns 429, what does `fetchUser` do?"
- **Spot the bug:** show a 3 to 8 line variant with one change. "What is wrong here?"
- **Choose:** multiple choice with plausible wrong answers. Use the AskUserQuestion tool when you have it.
- **Explain back:** "In one sentence, why do we cache before we check auth?"

Wait for the answer before the next question. Do not give hints in the question.

## 3. Grade honestly

- Right: say so in a few words, then add one fact they did not mention.
- Partly right: say which part is right, then fill the gap.
- Wrong: say it is wrong, give the right answer, and point to the exact code (`file:line`).
- Do not praise a wrong answer to be kind.

## 4. Score and next step

End with: score (for example 3/5), the one weak area, and one action ("read `lib/cache.ts:40-70`" or "ask me to `explain` the retry logic"). Offer a second round on the weak area only.
