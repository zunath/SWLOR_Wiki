#!/usr/bin/env python3
"""
Rewrite internal wiki hrefs for Wiki.js (trailing-slash safe):
  - Internal targets use locale-relative hrefs: ../ repeated once per source path segment + target path
    (e.g. from /en/rules use ../PvP-Rules, not /en/PvP-Rules or bare PvP-Rules — those break when the URL is /en/rules/).
  - Normalizes https://anyhost/en/... and legacy /en/... the same way (no domain in output).

Also normalizes segments for Wiki.js (no .html / .md in href).

Usage:
  python tools/relativize_internal_links.py              # normalize all internal hrefs
  python tools/relativize_internal_links.py --wikijs    # strip .html/.md from all internal href
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

WIKI_ROOT = Path(__file__).resolve().parent.parent

HREF_ATTR = re.compile(r'(href=")([^"]+)(")')


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
    # Short paths like /en/combat-skills → Gameplay/combat-skills.html
    if len(parts) == 1 and parts[0]:
        gk = f"gameplay/{parts[0].lower()}"
        if gk in idx:
            return idx[gk]
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


def _wiki_url_path(target: Path) -> str:
    return target.relative_to(WIKI_ROOT).as_posix().rsplit(".", 1)[0]


def _wiki_path_depth(source: Path) -> int:
    """Number of /en/... URL segments for this file (mirrors repo path without extension)."""
    rel = source.relative_to(WIKI_ROOT).as_posix()
    stemmed = rel.rsplit(".", 1)[0]
    if not stemmed:
        return 1
    return len(stemmed.split("/"))


def rel_href(source: Path, target: Path) -> str:
    """Wiki.js-safe relative links: ../ × (depth of source slug) + target slug path.

    Root-relative /en/foo breaks when the live URL is /en/page/ (trailing slash): the browser
    resolves bare ``foo`` under the page folder. A single ../ per path segment reaches /en/ first.
    """
    try:
        depth = _wiki_path_depth(source)
        tgt = _wiki_url_path(target)
        prefix = "../" * depth
        return normalize_wikijs_href_inner(prefix + tgt)
    except ValueError:
        pass
    rel = os.path.relpath(target.resolve(), source.parent.resolve())
    return normalize_wikijs_href_inner(rel.replace(os.sep, "/"))


def _path_key_from_repo_rel(rel: str) -> str:
    rel = rel.replace("\\", "/").strip("/")
    if not rel:
        return ""
    lower = rel.lower()
    for ext in (".html", ".md"):
        if lower.endswith(ext):
            return lower[: -len(ext)]
    return lower


def _resolve_fs_candidate(cand: Path) -> Path | None:
    """Map a path under WIKI_ROOT to an existing .html/.md wiki page."""
    if cand.is_file():
        if cand.suffix.lower() in (".html", ".md"):
            return cand
        return None
    for ext in (".html", ".md"):
        p = cand.with_suffix(ext)
        if p.is_file():
            return p
    return None


def normalize_internal_href(
    source: Path,
    inner: str,
    idx: dict[str, Path],
    missing: list[tuple[Path, str]],
) -> str:
    """Return stable href inner (path + optional ?query + #frag) for wiki-internal targets."""
    inner_strip = inner.strip()
    if not inner_strip:
        return inner

    decoded = inner_strip.replace("&amp;", "&")
    base_full, frag = decoded, ""
    if "#" in base_full:
        base_full, frag = base_full.split("#", 1)
        frag = "#" + frag
    query = ""
    if "?" in base_full:
        base_full, query = base_full.split("?", 1)
        query = "?" + query

    base = base_full.strip()
    if not base:
        return inner

    low = base.lower()
    if low.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return inner
    if low.startswith(("http://", "https://")):
        u = urlparse(base)
        if u.scheme in ("http", "https") and u.netloc:
            p = u.path or ""
            if p == "/en":
                return inner
            if p.startswith("/en/"):
                tail = unquote(p[4:].strip("/"))
            else:
                return inner
            if not tail:
                return inner
            tgt = resolve_target(tail, idx)
            if tgt is None:
                missing.append((source, inner))
                return inner
            return rel_href(source, tgt) + query + frag
        return inner

    if base.startswith("//"):
        return inner

    if base.startswith("/en/") or low == "/en":
        path_part = base[4:].lstrip("/") if base.startswith("/en/") else ""
        if not path_part:
            return inner
        tgt = resolve_target(path_part, idx)
        if tgt is None:
            missing.append((source, inner))
            return inner
        return rel_href(source, tgt) + query + frag

    if base.startswith("/"):
        path_part = unquote(base.lstrip("/"))
        tgt = resolve_target(path_part, idx)
        if tgt is None:
            return inner
        return rel_href(source, tgt) + query + frag

    try:
        raw_rel = unquote(base)
        cand = (source.parent / raw_rel).resolve()
        cand.relative_to(WIKI_ROOT.resolve())
    except (OSError, ValueError):
        return inner

    tgt = _resolve_fs_candidate(cand)
    if tgt is None:
        rel_try = cand.relative_to(WIKI_ROOT).as_posix()
        k = _path_key_from_repo_rel(rel_try)
        if k and k in idx:
            tgt = idx[k]
    if tgt is None:
        missing.append((source, inner))
        return inner
    return rel_href(source, tgt) + query + frag


def process_file(path: Path, idx: dict[str, Path], missing: list[tuple[Path, str]]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    def repl_href_attr(m: re.Match[str]) -> str:
        inner = m.group(2)
        new_inner = normalize_internal_href(path, inner, idx, missing)
        if new_inner == inner:
            return m.group(0)
        return m.group(1) + new_inner + m.group(3)

    text = HREF_ATTR.sub(repl_href_attr, text)

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


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
