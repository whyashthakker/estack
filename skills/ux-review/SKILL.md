---
name: ux-review
description: Review a flow, screen, or piece of product copy from the user's point of view. Checks orientation, next steps, friction, error recovery, and leaked internal details, then rewrites the copy in plain words. Use when the user asks to improve UX, review a flow, simplify onboarding, write button or error copy, reduce friction, or asks "is this confusing".
---

# UX review

Core idea: users care about outcomes, not how the system works. Before each label, message, or step, ask: "Is this for the user, or for the engineer?"

## 1. Frame it

Write four short lines before you judge anything:
- **Who:** the user and what they already know.
- **Job:** the one thing they came to do now.
- **Where:** entry, decision, waiting, success, error, or exit.
- **Fear:** what could worry them (losing data, cost, a mistake they cannot undo, looking foolish).

## 2. Walk the flow

Read the real code or open the real page (use `verify-ui` if you can run it). For each step check:

1. Can they tell where they are?
2. Can they tell what to do next? Is there one clear main action?
3. Does each piece of text help the job?
4. Do internal details leak? (model names, vendor names, error codes, "Initializing...", "Calling API...")
5. On error, do they know what happened and what to do?
6. Is the app asking for effort too early? (account or card before any value, a choice they cannot judge yet)

## 3. Fix the copy

- Buttons: verb + object. "Save draft", "Send invite". Not "Submit", "Proceed", "OK".
- Status: "Saving..." then "Saved". Name the outcome, not the process: "Getting your results", not "Fetching data".
- Errors: what happened in plain words, then what to do. "We could not save your file. Check your connection and try again."
- Empty states: what will appear here, and one action to start.
- Remove confirmation dialogs for small actions that are easy to undo.

## 4. Report

List problems by how much they hurt the job (worst first): the step, the problem, the fix, and the new copy. Keep each fix small enough to ship on its own. Do not redesign the whole flow unless the user asks.
