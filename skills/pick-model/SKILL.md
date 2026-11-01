---
name: pick-model
description: Choose the right AI model for each task in a project or workflow using current prices, not memory. Finds where models are used, groups calls by task type, compares live prices from the explainx.ai MCP server, and recommends a model per task with the cost change. Use when the user asks "which model should I use", "this is too expensive", "cut my AI bill", "cheaper model for X", or sets up subagents, bots, or pipelines that call LLMs.
---

# Pick model

Goal: each task runs on the cheapest model that does it well enough. The strongest model on everything wastes money. The cheapest model on everything wastes time on bad output.

## 1. Find the calls

Search the code and config for model use: model IDs, provider SDK calls, agent and subagent definitions, cron jobs and bots. For each call, write down:
- Task (what it does, in five words).
- Current model.
- Rough volume (per day or per run) and size (short prompt or long context).
- How bad a weak answer is: **low** (draft, sorted later), **medium** (user sees it), **high** (money, security, code that ships, public posts).

## 2. Get current prices

With the explainx.ai MCP server: call `compare_model_prices` for the candidate models, and `search_ai_directory` or `get_ai_directory_entry` for model details. Prices change often. Never use prices from memory. Without the server, use the providers' pricing pages and give the date you read them.

Router prices can differ from direct provider prices. Say which one you used.

## 3. Match model to task

| Task type | Usual fit |
|---|---|
| Bulk, mechanical (classify, extract, tag, reformat) | Smallest fast model that passes a 10-sample check |
| Writing people read (posts, emails, summaries) | Mid-tier model; strongest only for high-stakes text |
| Code that ships, security review, hard reasoning | Strongest model, or mid-tier plus a strong-model review |
| Long documents | The model with the best price per long-context token, not the best price per short prompt |

Run a small test before a big switch: the same 5 to 10 real inputs on the old and new model, side by side. Show the user the outputs, not only the scores.

## 4. Report

A table: task, current model, recommended model, monthly cost before and after (show the math), and risk. Then the total saving. Do not change config until the user agrees. When they agree, make the change in one place (a config constant or env var) so it is easy to switch back.
