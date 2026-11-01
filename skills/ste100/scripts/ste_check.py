#!/usr/bin/env python3
"""Flag common ASD-STE100 rule breaks and AI-slop patterns in Markdown or text.

Usage:
  python3 ste_check.py FILE [FILE ...]
  python3 ste_check.py --procedure FILE     # use the 20-word limit for every sentence
  cat FILE | python3 ste_check.py -

This is a review aid, not a compliance check. It has false positives
(for example "string" ends in -ing) and cannot judge meaning. Standard library only.
"""

import re
import sys

PROC_LIMIT = 20
DESC_LIMIT = 25
PARA_LIMIT = 6

HEDGES = {"should", "would", "may", "might", "could", "perhaps", "possibly", "potentially"}
SLOP_WORDS = {
    "delve", "delves", "tapestry", "testament", "intricate", "meticulous", "meticulously",
    "pivotal", "vibrant", "showcase", "showcases", "showcasing", "underscore", "underscores",
    "realm", "foster", "fosters", "fostering", "embark", "multifaceted", "seamless", "seamlessly",
    "robust", "groundbreaking", "revolutionary", "game-changer", "game-changing", "cutting-edge",
    "supercharge", "unlock", "unlocks", "elevate", "leverage", "leverages", "leveraging",
    "utilize", "utilizes", "utilizing", "facilitate", "facilitates", "commence", "boasts",
    "renowned", "nestled", "additionally", "furthermore", "moreover",
}
SLOP_PHRASES = [
    "it's worth noting", "it is worth noting", "it's important to note", "it is important to note",
    "in today's", "evolving landscape", "stands as", "serves as", "plays a pivotal role",
    "a testament to", "not just", "great question", "i hope this helps", "let me know if",
    "in conclusion", "to sum up", "as an ai", "in order to", "studies show", "experts say",
    "feel free to",
]
# Common nouns and names that end in -ing and are fine.
ING_OK = {
    "string", "thing", "something", "anything", "nothing", "everything", "ring", "king",
    "spring", "bring", "during", "morning", "evening", "ceiling", "setting", "settings",
    "logging", "building", "routing", "pricing", "meaning", "warning", "warnings", "heading",
    "headings", "training", "rendering", "caching", "billing", "onboarding", "thinking",
    "learning", "programming", "marketing", "testing", "swing", "wing", "sing", "sting",
}
PASSIVE = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?(\w+ed|built|done|made|given|taken|written|run|sent|shown|kept|set|put|found|known)\b",
    re.I,
)
CONTRACTION = re.compile(r"\b\w+'(t|re|ve|ll|d|s)\b", re.I)


def strip_markdown(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # fenced code
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)  # frontmatter
    text = re.sub(r"`[^`]*`", "CODE", text)  # inline code counts as one word
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)  # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> label
    text = re.sub(r"<[^>]+>", "", text)  # html / jsx
    return text


def paragraphs(text):
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip() and not l.strip().startswith("|")]
        if not lines or all(l.lstrip().startswith("#") for l in lines):
            continue
        is_list = all(re.match(r"\s*([-*+]|\d+[.)])\s", l) for l in lines)
        yield " ".join(l.strip() for l in lines), is_list, lines


def sentences(par):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"*(])", par)
    return [p.strip() for p in parts if p.strip()]


def words(sentence):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'/._-]*", sentence)


def is_procedure(sentence, in_list):
    s = re.sub(r"^\s*([-*+]|\d+[.)])\s*", "", sentence)
    s = re.sub(r"^\**[A-Za-z]+:\**\s*", "", s)  # "Note:" / "**Caution:**"
    first = (s.split() or [""])[0].lower().strip("*")
    imperative = first in {
        "add", "check", "click", "copy", "create", "delete", "do", "edit", "enter", "install",
        "make", "move", "open", "push", "put", "read", "remove", "run", "select", "set", "start",
        "stop", "type", "use", "write", "if", "when", "before", "after", "make", "commit",
        "restart", "update", "go", "keep", "find", "replace", "save", "send", "test", "build",
    }
    return in_list or imperative


def check(text, name, force_procedure):
    issues = []
    for par, is_list, lines in paragraphs(strip_markdown(text)):
        sents = []
        for line in (lines if is_list else [par]):
            sents.extend(sentences(line.strip()))
        if not is_list and len(sents) > PARA_LIMIT:
            issues.append(("paragraph", f"{len(sents)} sentences (limit {PARA_LIMIT})", sents[0][:70]))
        for s in sents:
            w = words(s)
            low = [x.lower().strip(".,:!?\"'()*") for x in w]
            proc = force_procedure or is_procedure(s, is_list)
            limit = PROC_LIMIT if proc else DESC_LIMIT
            if len(w) > limit:
                kind = "procedure" if proc else "descriptive"
                issues.append(("length", f"{len(w)} words ({kind} limit {limit})", s))
            if ";" in s:
                issues.append(("semicolon", "use two sentences", s))
            hedges = sorted(HEDGES.intersection(low))
            if hedges:
                issues.append(("hedge", ", ".join(hedges), s))
            ings = sorted({x for x in low if x.endswith("ing") and len(x) > 4 and x not in ING_OK})
            if ings:
                issues.append(("-ing", ", ".join(ings), s))
            m = PASSIVE.search(s)
            if m:
                issues.append(("passive?", m.group(0), s))
            if CONTRACTION.search(s):
                issues.append(("contraction", CONTRACTION.search(s).group(0), s))
            slop = sorted(SLOP_WORDS.intersection(low))
            ls = s.lower()
            slop += [p for p in SLOP_PHRASES if p in ls]
            if slop:
                issues.append(("slop", ", ".join(slop), s))
            if s.count("—") >= 2:
                issues.append(("em dash", f"{s.count(chr(0x2014))} em dashes", s))
    for kind, detail, s in issues:
        short = s if len(s) <= 110 else s[:107] + "..."
        print(f"{name}: [{kind}] {detail}\n    {short}")
    return len(issues)


def main(argv):
    force = "--procedure" in argv
    files = [a for a in argv if a != "--procedure"]
    if not files:
        print(__doc__)
        return 2
    total = 0
    for f in files:
        text = sys.stdin.read() if f == "-" else open(f, encoding="utf-8").read()
        total += check(text, f, force)
    print(f"\n{total} item(s) to review. Not every item is an error.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
