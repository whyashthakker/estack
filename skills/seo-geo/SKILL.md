---
name: seo-geo
description: Make a page rank in Google and get cited by AI answer engines (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews). Audits or writes the page with an answer-first structure, specific numbers with sources, FAQ and article schema, clean meta tags, internal links, and crawl access for AI bots. Use when the user mentions SEO, GEO, AI search visibility, "rank for", "get cited by ChatGPT", schema, JSON-LD, meta tags, or indexing.
---

# SEO + GEO

Two readers decide if a page wins: a search engine that ranks it, and an AI engine that quotes it. Both reward the same thing: a page that answers a real question clearly, with facts it can prove.

## 1. Pick the question

- One page, one main question. Write it the way a person types or asks it ("how much does Claude Code cost", not "Claude Code pricing considerations").
- Check demand if you have a keyword tool or Search Console. If not, use the search engine's own suggestions and "People also ask".
- Check what ranks now. Your page must be better than the top result on at least one thing: newer, more specific, tested by hand, or simpler.

## 2. Structure for quoting

- **Answer first.** The first 40 to 60 words under the H1 answer the question directly, with a number if there is one. An AI engine often quotes this block.
- **Headings as questions** people ask. Each section starts with its direct answer, then the detail.
- **Specific facts with sources.** Numbers, dates, names, each linked to a primary source. Pages with clear stats and citations get quoted more.
- **Tables** for comparisons and prices. **Lists** for steps.
- **Date it.** Show "Updated <date>" and keep it true.
- **Show who wrote it** and why they know (author bio, hands-on testing).

## 3. Technical checks

- Title under about 60 characters with the main term near the start. Meta description under about 155 characters that answers, not teases.
- One H1. Descriptive URL slug.
- JSON-LD: `Article` or `BlogPosting` (headline, author, datePublished, dateModified, image), `FAQPage` for a real FAQ section, `BreadcrumbList`. Validate it. Never mark up content that is not on the page.
- Canonical URL set. No duplicate pages competing for one question.
- `robots.txt` does not block AI crawlers you want (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended) unless the owner chose to block them. Ask before you change this.
- Images: modern format (WebP or AVIF), compressed, descriptive alt text, width and height set.
- An `llms.txt` file is optional and cheap. Add it only if the site wants one.

## 4. Links

- Link out to primary sources.
- Link in: add the new page to 2 to 5 related pages on the same site, with anchor text that says what the target is. Add links back from those pages too.

## 5. Report

For an audit: a list of fixes, worst first, each with the exact change. For a new page: the page, the schema, and the list of internal links you added. Do not promise rankings. Say what to measure (impressions, clicks, AI citations) and when to check again (2 to 4 weeks).
