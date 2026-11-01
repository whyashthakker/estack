---
name: ship
description: Finish and ship a change safely. Checks what changed, runs the project's own typecheck, lint, and tests, stages only the files this task touched, writes a short commit message, updates the changelog only for real product changes, and pushes after the user agrees. Use when the user says "ship it", "push", "commit and push", "deploy", "we're done", or asks to update release notes.
---

# Ship

Goal: the change lands clean, small, and easy to undo. Nothing extra goes with it.

## 1. Look at what changed

Run `git status`, `git diff --stat`, and `git log origin/<branch>..HEAD`. Sort the files into:
- **This task:** files you or the user changed for this work.
- **Not this task:** other edits in the tree (another agent, another session, the user's work in progress). Do not stage these. List them for the user.

Never stage `.env*`, secrets, large binaries, or build output.

## 2. Check

Find the project's own commands (`package.json` scripts, `Makefile`, `justfile`, CI config) and run the fast ones: typecheck, lint, unit tests for the touched area. Ask before a slow full build.

Confirm that each check really ran: read the output, not only the exit code. A command that was not found, or a test runner that found zero tests, is not a pass. If a check fails, fix it or stop and report. Do not ship red.

## 3. Changelog (only for product changes)

Update the changelog or release notes only when a user of the product would notice the change: a new feature, a pricing or account change, a redesign, a fixed bug they reported. Content (blog posts, docs copy), refactors, and internal tools do not go in a public changelog. When in doubt, leave it out.

## 4. Commit

- Stage paths by name: `git add path/a path/b`. Not `git add -A`.
- Message: one short line in the imperative mood, under about 60 characters ("Add retry to payment webhook"). Add a body only if the reason is not obvious.
- Follow the repo's own conventions if it has them (look at `git log`).

## 5. Push

Ask before you push unless the user already said to. Before you push to the default branch, check whether the push starts a deploy or kills a running job (CI config, deploy hooks). If the push is rejected, pull with rebase, run the checks again, then push. Never force-push a shared branch.

## 6. Report

Commit hash, what shipped, what you did not stage and why, and the checks that ran.
