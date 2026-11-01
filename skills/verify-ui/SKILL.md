---
name: verify-ui
description: Check a UI change in a real browser before calling it done. Starts or finds the dev server, opens the changed pages, takes screenshots at phone and desktop widths in light and dark mode, reads console errors, and looks for layout bugs that typecheck and curl miss. Use after any change to pages, components, or styles, or when the user says "check it visually", "screenshot it", "does it look right", or "verify the UI".
---

# Verify UI

Goal: you saw the change working before the user does. A clean typecheck does not prove a page looks right.

## 1. Get a running page

- Find the dev command (`package.json` scripts, README). If a dev server already runs, use it. Do not start a second one on another port without telling the user.
- Find the exact routes the change affects. Include one page that only uses a shared component you changed.
- For a page behind login, ask the user for a test account or a way in. Do not bypass auth.

## 2. Look at it

Use what the session has: Playwright, a browser automation tool, or a headless browser script. For each route take screenshots at:
- 390 px wide (phone) and 1280 px wide (desktop).
- Light and dark mode, if the site has both.
- One interaction state that matters (menu open, form error, empty list, loading).

Read every screenshot. Do not only save it.

## 3. Check

- Text that overflows, is clipped, or overlaps.
- Horizontal scroll on the phone width.
- Text that is hard to read on its background (most common in dark mode).
- Images that are missing, stretched, or very slow.
- Console errors and failed network requests (read the console log).
- The change itself: is the new thing there and does it do what was asked?

## 4. Fix and repeat

Fix what you found, take new screenshots, and compare. Stop after three rounds and report what remains.

## 5. Report

Pages checked, widths and modes, the problems found and fixed, and anything still open. Attach or link the final screenshots. Delete temporary screenshots that are not useful to keep, and never commit them unless asked.
