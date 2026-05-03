#!/usr/bin/env python3
"""
Rewrite https://wiki.starwarsnwn.com/en/... hrefs to paths relative to each HTML file,
and normalize internal links for Wiki.js (no .html / .md in href — storage files are
not the public URL).

Usage:
  python tools/relativize_internal_links.py              # fix absolute wiki URLs only
  python tools/relativize_internal_links.py --wikijs    # strip .html/.md from all internal href
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

WIKI_ROOT = Path(__file__).resolve().parent.parent

# href="https://wiki.../en/PATH" — PATH may include &amp; only as entity; stop before quote
HREF_WIKI = re.compile(
    r'https://wiki\.starwarsnwn\.com/en/([^"\'>\s]+)',
    re.IGNORECASE,
)


def build_index(root: Path) -> dict[str, Path]:
    idx: dict[str, Path] = {}
    for p in root.rglob("*"):
        if any(x in p.parts for x in (".git", "node_modules")):
            continue
        if p.suffix.lower() not in (".html", ".md"):
            continue
        rel = p.relative_to(root).as_posix()
        key = rel.rsplit(".", 1)[0].lower()
        prev = idx.get(key)
        if prev is not None and prev != p:
            print(f"WARN: duplicate wiki path {key!r}: {prev} vs {p}", file=sys.stderr)
        idx[key] = p
    return idx


def resolve_target(url_path: str, idx: dict[str, Path]) -> Path | None:
    url_path = unquote(url_path.strip("/"))
    if not url_path:
        return None
    if "#" in url_path:
        url_path = url_path.split("#", 1)[0]
    if "?" in url_path:
        url_path = url_path.split("?", 1)[0]
    key = url_path.lower()
    if key in idx:
        return idx[key]
    parts = url_path.split("/")
    # Wiki.js: /en/Gameplay/Gameplay often maps to root page Gameplay.html
    if len(parts) == 2 and parts[0].lower() == parts[1].lower():
        k2 = parts[0].lower()
        if k2 in idx:
            return idx[k2]
    return None


def normalize_wikijs_href_inner(inner: str) -> str:
    """Strip .html / .md from path segments for Wiki.js URLs (relative or root-relative)."""
    s = inner.strip()
    if not s:
        return inner
    if re.match(r"^[a-z][a-z0-9+.-]*:", s, re.I):
        return inner
    if s.startswith("//"):
        return inner

    base, frag = s, ""
    if "#" in s:
        base, frag = s.split("#", 1)
        frag = "#" + frag
    query = ""
    if "?" in base:
        base, query = base.split("?", 1)
        query = "?" + query

    def norm_seg(part: str) -> str:
        if part in (".", "..", ""):
            return part
        for ext in (".html", ".md"):
            if part.endswith(ext):
                return part[: -len(ext)]
        return part

    parts = base.split("/")
    parts = [norm_seg(p) for p in parts]
    return "/".join(parts) + query + frag


def rel_href(source: Path, target: Path) -> str:
    rel = os.path.relpath(target.resolve(), source.parent.resolve())
    posix = rel.replace(os.sep, "/")
    return normalize_wikijs_href_inner(posix)


def process_file(path: Path, idx: dict[str, Path], missing: list[tuple[Path, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False

    def repl(m: re.Match[str]) -> str:
        nonlocal changed
        raw = m.group(1)
        frag = ""
        lookup = raw
        if "#" in lookup:
            lookup, frag = lookup.split("#", 1)
            frag = "#" + frag
        tgt = resolve_target(lookup, idx)
        if tgt is None:
            missing.append((path, raw))
            return m.group(0)
        changed = True
        return rel_href(path, tgt) + frag

    new_text = HREF_WIKI.sub(repl, text)
    if changed:
        path.write_text(new_text, encoding="utf-8", newline="\n")
    return changed


HREF_ATTR = re.compile(r'(href=")([^"]+)(")')


def strip_wikijs_extensions_in_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    def repl(m: re.Match[str]) -> str:
        inner = m.group(2)
        new_inner = normalize_wikijs_href_inner(inner)
        if new_inner == inner:
            return m.group(0)
        return m.group(1) + new_inner + m.group(3)

    new_text = HREF_ATTR.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8", newline="\n")
        return True
    return False


def main_wikijs_strip() -> None:
    n = 0
    for p in sorted(WIKI_ROOT.rglob("*.html")):
        if ".git" in p.parts:
            continue
        if strip_wikijs_extensions_in_file(p):
            n += 1
    print(f"Wiki.js href normalization: updated {n} files.", file=sys.stderr)


def main() -> None:
    idx = build_index(WIKI_ROOT)
    missing: list[tuple[Path, str]] = []
    n_changed = 0
    for p in sorted(WIKI_ROOT.rglob("*.html")):
        if ".git" in p.parts:
            continue
        if process_file(p, idx, missing):
            n_changed += 1
    uniq = sorted({(str(a.relative_to(WIKI_ROOT)), b) for a, b in missing})
    for rel, raw in uniq:
        print(f"MISSING TARGET {raw!r} (referenced from {rel})", file=sys.stderr)
    print(f"Updated {n_changed} files.", file=sys.stderr)
    print(f"Unresolved link targets: {len(uniq)}", file=sys.stderr)
    if uniq:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--wikijs":
        main_wikijs_strip()
    else:
        main()
