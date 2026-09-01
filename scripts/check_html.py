#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.duplicate_ids = []
        self.h1 = 0
        self.main = 0
        self.lang_ok = False
        self.title_depth = 0
        self.title_text = []
        self.images_missing_alt = 0
        self.links_missing_href = 0
        self.buttons = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html": self.lang_ok = bool(attrs.get("lang"))
        if tag == "h1": self.h1 += 1
        if tag == "main": self.main += 1
        if tag == "title": self.title_depth += 1
        if tag == "img" and "alt" not in attrs: self.images_missing_alt += 1
        if tag == "a" and not attrs.get("href"): self.links_missing_href += 1
        if "id" in attrs:
            if attrs["id"] in self.ids: self.duplicate_ids.append(attrs["id"])
            self.ids.add(attrs["id"])
    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth: self.title_depth -= 1
    def handle_data(self, data):
        if self.title_depth: self.title_text.append(data.strip())


def check(path: Path):
    parser = AuditParser()
    parser.feed(path.read_text(encoding="utf-8"))
    issues = []
    if not parser.lang_ok: issues.append("missing html lang")
    if parser.h1 != 1: issues.append(f"expected exactly one h1, found {parser.h1}")
    if parser.main != 1: issues.append(f"expected exactly one main, found {parser.main}")
    if not "".join(parser.title_text).strip(): issues.append("missing title text")
    if parser.images_missing_alt: issues.append(f"{parser.images_missing_alt} image(s) missing alt")
    if parser.links_missing_href: issues.append(f"{parser.links_missing_href} link(s) missing href")
    if parser.duplicate_ids: issues.append(f"duplicate ids: {', '.join(parser.duplicate_ids)}")
    return issues


def main():
    failures = 0
    files = sorted(SITE.rglob("*.html"))
    for path in files:
        issues = check(path)
        if issues:
            failures += 1
            print(f"FAIL {path.relative_to(SITE)}: {'; '.join(issues)}")
        else:
            print(f"PASS {path.relative_to(SITE)}")
    if failures:
        sys.exit(1)
    print(f"\nChecked {len(files)} HTML files successfully.")

if __name__ == "__main__":
    main()
