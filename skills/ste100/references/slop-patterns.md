# Slop patterns

Patterns that make text read as machine-written, with fixes. Built mainly from Wikipedia's editor guide "Signs of AI writing" (checked November 2026), plus patterns we see in our own agent output.

Two warnings from that guide apply here:
- No single pattern proves a text is AI-written. Many people write this way too.
- The real problems are accuracy and sourcing. Fix the pattern because it wastes the reader's time. Then check the facts.

## Content

| Pattern | Examples | Fix |
|---|---|---|
| Inflated significance and legacy | "stands as a testament to", "plays a pivotal role", "underscores its importance", "marks a turning point", "indelible mark", "setting the stage for", "in the evolving landscape of" | State the fact. If the significance is real, give the number or the result that proves it. |
| Superficial analysis in trailing "-ing" clauses | "..., highlighting the need for better tools", "..., ensuring reliability", "..., fostering collaboration", "..., offering valuable insights" | Delete the clause, or write a second sentence with a real claim and its evidence. |
| Promotional tone | "boasts", "vibrant", "rich", "profound", "showcasing", "groundbreaking", "renowned", "diverse array", "nestled in the heart of", "commitment to excellence" | Describe what it does. Remove adjectives that carry no fact. |
| Hype words | "revolutionary", "game-changer", "cutting-edge", "seamless", "robust", "powerful", "unlock", "supercharge", "elevate", "next-level" | Say what changes, with a number if you have one. |
| Vague attribution | "experts argue", "industry reports suggest", "observers have noted", "studies show", "some critics say" | Name the source and link it, or remove the claim. |
| Vague connection | "in connection with", "associated with", "connected to" when the link is not stated | Say what the link is: "caused", "is part of", "replaced". |
| Formulaic challenge or outlook sections | "Despite its success, X faces challenges...", "Challenges and Future Outlook", "Despite these challenges..." | Write a section only if there is a specific, sourced problem. Name it. |
| Summary of the summary | "In conclusion", "Overall", "To sum up", "In summary" after a short text | Delete, or end on the one action that matters. |

## Language

| Pattern | Examples | Fix |
|---|---|---|
| AI vocabulary clusters | "delve", "tapestry", "testament", "intricate", "meticulous", "crucial", "pivotal", "vibrant", "showcase", "underscore", "realm", "landscape" (abstract), "navigate" (abstract), "foster", "embark", "multifaceted", "nuanced" | Use the plain word or delete. One of these alone is fine. A cluster is the signal. |
| Paragraph-opening transitions | "Additionally,", "Furthermore,", "Moreover,", "Notably," at the start of most paragraphs | Delete. Order the paragraphs so the link is clear. |
| Copula avoidance | "serves as", "stands as", "functions as", "acts as", "features", "boasts", "offers" in place of "is", "are", "has" | Use "is", "are", "has". |
| Negative parallelisms | "It's not just X, it's Y", "not X, but Y", "Y rather than X", "no X, no Y, just Z" | State Y directly. Mention X only if a reader really believes X. |
| Rule of three by habit | "fast, reliable, and scalable", "clear, concise, and compelling" | Keep only the items you can prove. One is fine. |
| Hedge stacks | "may potentially", "could possibly help to somewhat", "it might be worth considering" | State how sure you are once: "This works in most cases." |
| Elegant variation | "the tool... the utility... the solution... the platform" for one thing | One name for one thing (STE word rule). |
| "Refers to" leads | "X refers to a framework that..." when the text is about X, not the word | "X is a framework that..." |

## Communication meant for the user, left in the text

| Pattern | Examples | Fix |
|---|---|---|
| Empty openers | "Great question!", "Certainly!", "Absolutely!", "Sure, here is..." | Start with the answer. |
| Empty closers | "I hope this helps!", "Let me know if you have any other questions", "Feel free to reach out" | Delete. |
| Flattery and fake agreement | "You're absolutely right!", "What a great idea!" | Agree or disagree with a reason. |
| Chatbot artifacts | "As an AI language model", "Here is a revised version:", "as of my last knowledge update", offering several labeled versions when one was asked for | Delete. Give the one result. |
| Placeholders | "[Insert date]", "YYYY-MM-DD", "example.com" left in final text | Fill in the real value or remove the line. |
| Restating the question | "You asked about X. X is..." | Answer. |

## Formatting

| Pattern | Examples | Fix |
|---|---|---|
| Bold everywhere | Bold on every other phrase | Bold only the one thing a skimmer must see. |
| Emoji bullets and headers | "🚀 Key Features", "✅ Benefits" | Remove unless the site's style uses them. |
| Headings over tiny sections | A heading above every two-line paragraph | Merge short sections. |
| Em dash chains | "The tool — which is new — works — mostly" | Use periods and commas. Split the sentence. |
| Markdown where it does not render | `**bold**` or `##` in plain-text fields, emails, commit messages | Use the target's own format. |

## Citations

| Pattern | Fix |
|---|---|
| Links that do not exist or point to unrelated pages | Open each link before you cite it. |
| Links to search results instead of the source | Link the primary source. |
| `utm_source=` and other tracking parameters | Remove them. |
| A claim and a citation that do not match | Read the cited page. Change the claim or the citation. |
