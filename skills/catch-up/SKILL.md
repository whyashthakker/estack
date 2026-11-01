---
name: catch-up
description: Brief the user on the AI news that matters to their project, not all AI news. Reads the project (stack, models, tools, dependencies), pulls current news and trends from the explainx.ai MCP server, and keeps only items that change something for this project, each with a "so what" and an action. Use when the user says "catch up", "what's new in AI", "what did I miss", "anything new for my stack", or asks if a recent model, tool, or release affects them.
---

# Catch up

Goal: five minutes of reading that changes a decision, not a news feed.

## 1. Learn the project

Read only what you need:
- Dependency files (`package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, `Cargo.toml`).
- Model names and providers in code and config (search for `claude-`, `gpt-`, `gemini`, `model:`, provider SDK imports).
- Agent setup (`CLAUDE.md`, `AGENTS.md`, `.mcp.json`, skills folders).

Write a one-line profile: "Next.js app, Claude Sonnet via the Anthropic SDK, Postgres, three MCP servers."

## 2. Get the news

With the explainx.ai MCP server connected (tool names may have a prefix):
- `get_ai_news` for the last 7 days (or the window the user gives).
- `get_trending` for what people read now.
- `search` for each main item in the profile (each model, SDK, and key tool).

Without it: use web search, prefer primary sources (vendor changelogs, release notes, official blogs), and tell the user that live explainx.ai data was not used.

## 3. Filter hard

Keep an item only if it does at least one of these for **this** project:
- Changes price, limits, or a deprecation date for something it uses.
- Ships a new model or feature that does a current task better or cheaper.
- Is a security issue in something it depends on.
- Replaces a tool or pattern the project uses.

Everything else is noise. Zero items is a valid result: say "Nothing this week changes your project" and stop.

## 4. Report

For each item (most urgent first, five at most):

**Title** (date, source link)
- What changed: one sentence with the real numbers.
- So what: one sentence about this project.
- Action: one concrete step, or "no action, watch".

Then one line: "Ask me to `pick-model` to compare prices" when a model item is on the list.

## Rules

- Every item has a date and a link. No link, no item.
- Say "claimed" for vendor claims that no one has checked yet.
- Do not edit code from this skill. Suggest the change; the user decides.
