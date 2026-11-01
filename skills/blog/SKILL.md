---
name: blog
description: Research and write a blog post that readers trust and AI engines cite. Reads the site's existing posts to match voice and format, researches from primary sources (and what practitioners say), writes an answer-first post with real numbers and citations, adds an FAQ, optimized images, and internal links both ways, then validates it. Use when the user wants to write, draft, research, update, or edit a blog post or article.
---

# Blog

Goal: the best page on the internet for one question, written in the site's own voice.

## 1. Learn the site

- Read 3 to 5 recent posts in the same category. Note the frontmatter fields, heading style, length, components, tone, and how they link.
- Find the content folder, the image folder, and any validation script (`package.json` scripts, `scripts/`). You will run it at the end.
- Search existing posts for the same topic. If one exists, **update it** instead of writing a duplicate. Ask the user if unsure.

## 2. Research

- Go to the primary source first: the announcement, the docs, the paper, the repo, the changelog. Read it, not a summary of it.
- Get the source's own images, charts, or video when the license allows, and credit them. Real screenshots beat stock art.
- Find what practitioners say (Hacker News, Reddit, GitHub issues, forums). Report it as "users report ...", attributed and linked, never as fact.
- Write down every number with its source link. A number without a source does not go in the post.
- Separate what is **claimed** (vendor says) from what is **verified** (tested, measured, reproduced).

## 3. Write

- **Title:** the question or the outcome, with the named product or company.
- **First paragraph:** answer the question in 2 to 3 sentences with the key number. No warm-up.
- **Body:** question-style H2s, each starting with its short answer. Tables for comparisons. Steps as numbered lists. Code blocks that run.
- **"What people are saying"** section when there is real discussion.
- **FAQ:** 4 to 6 real questions with short, direct answers. Add `FAQPage` schema if the site supports it.
- **Voice:** match the site. Plain words, short sentences. No hype words ("revolutionary", "game-changer"). No invented first-person stories.

## 4. Media

- Reuse an existing image from the site's library when one fits; write new alt text.
- Convert images to WebP and compress them. Compress video before you embed it.
- Every image gets alt text that says what it shows.

## 5. Link

- 3 to 6 internal links from the new post to related posts and pages.
- Add a link **to** the new post from 2 to 4 related existing posts. This is required, not optional.
- External links to primary sources.

## 6. Validate and hand off

Run the site's validation and build checks for content (frontmatter, MDX compile, broken links). Fix what fails. Then report: file path, title, the main question, sources used, and the posts you linked from. Use `ship` to publish and `social` or `short` to promote.
