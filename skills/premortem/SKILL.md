---
name: premortem
description: Run a premortem on a plan, launch, migration, or change before it ships. Assume it already failed, list the most likely reasons, rank them by likelihood and cost, and turn the top risks into checks, guards, or a rollback plan. Use when the user says "premortem", "what could go wrong", "stress test this plan", "is this safe to ship", or before a launch, a data migration, a pricing change, a big refactor, or anything costly to undo.
---

# Premortem

Goal: find the failure before your users do. People are better at explaining a failure than predicting one, so start from the failure.

## 1. State the plan

In three lines: what will change, who it affects, and how you will know it worked (one measurable signal). If you cannot write the signal, that is the first risk.

## 2. Assume it failed

"It is 30 days later. This failed badly. Why?" Write 8 to 12 causes. Cover each area:

- **Data:** loss, corruption, wrong migration order, no backup, bad defaults for old rows.
- **Users:** confusing change, broken links or bookmarks, emails that go to the wrong people, a step they did not expect.
- **Money:** wrong price or currency, double charge, free access by mistake, a cost spike (API, compute, email).
- **Scale and timing:** a cron job and a deploy at the same time, rate limits, a cold cache, time zones.
- **Dependencies:** a third-party API changes or fails, an expired key, a quota.
- **People:** the one person who knows it is away, no one watching after launch.
- **Security:** a new endpoint with no auth, secrets in logs, user input passed to an agent or a shell.

Read the real code and config for each one you suspect. A risk you checked beats a risk you imagined.

## 3. Rank

For each cause: likelihood (low, med, high), cost if it happens (low, med, high), and whether it is easy to undo. Keep the top 3 to 5: high on two of the three.

## 4. Turn risks into actions

For each top risk, one of:
- **Prevent:** a test, a validation, a guard, a feature flag, a dry run.
- **Detect:** an alert, a log line, a dashboard check at a set time after launch.
- **Recover:** a written rollback step that someone has tried once.

## 5. Report

A short table (risk, likelihood, cost, action, owner), then a go / go-with-fixes / stop call with one line of reason. Do not make the fixes in this skill unless the user asks. Ship after with `ship`.
