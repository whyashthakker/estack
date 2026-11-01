---
name: explain
description: Explain code, a concept, a diff, or what the agent just did, in layers that match the user's level. Starts with one plain sentence, then goes deeper only as far as needed, with a small diagram or example. Use when the user says "explain", "what does this do", "I don't get this", "walk me through", "ELI5", "how does X work", or asks about a file, function, error, or term.
---

# Explain

Goal: the user understands the thing well enough to change it or decide about it. Not a lecture. Not a tour of everything.

## 1. Find the level

Use what you already know about the user (their questions, their code, their role). If you do not know, assume a smart person who is new to this exact topic. Do not ask about level unless the answer would change a lot.

## 2. Write in layers

Stop at the layer that answers the question. The user can ask for more.

1. **One sentence.** What it is or does, in plain words, with no jargon. "This function retries a failed payment up to three times, then gives up."
2. **Why it exists.** The problem it solves. One to three sentences.
3. **How it works.** The main steps in order. Use a short numbered list or a small ASCII diagram for flows:
   ```
   request -> check cache -> hit? -> return
                           \-> miss -> call API -> save -> return
   ```
4. **The tricky part.** The one thing that surprises people or causes bugs here. Point to the exact line (`file:line`).
5. **Go deeper.** Only if asked: edge cases, history (`git log -L` or `git blame` when "why" matters), alternatives.

## 3. Rules

- Define each new term the first time, in six words or fewer. "Idempotent (safe to run twice)".
- Use the user's real code and names in examples, not foo/bar.
- One idea per paragraph. Short sentences.
- If you are not sure how something works, read the code or run it. Say "I checked" or "I did not check". Never guess and present it as fact.
- For "what did you just do": list each change, why you made it, and what the user should check.

## 4. Close the loop

End with one line: the single most useful thing to remember. If the topic is worth keeping, offer `quiz-me`.
