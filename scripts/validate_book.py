#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import argparse
import ast
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = (REPO_ROOT / "README.md", REPO_ROOT / "docs")
FENCE_RE = re.compile(r"^(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

EXTERNAL_SCHEMES = ("http://", "https://")
LOCAL_SCHEMES = ("mailto:",)
PYTHON_FENCE_LANGS = {"python"}


@dataclass
class ValidationError:
    path: Path
    line: int
    message: str


@dataclass
class FenceBlock:
    path: Path
    language: str
    start_line: int
    lines: list[str]


def iter_markdown_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix == ".md":
            files.append(path)
    return sorted({file.resolve() for file in files})


def slugify_heading(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    normalized = normalized.lower().strip()
    normalized = re.sub(r"[^\w\s-]", "", normalized)
    normalized = re.sub(r"\s+", "-", normalized)
    normalized = re.sub(r"-{2,}", "-", normalized)
    return normalized.strip("-")


def parse_markdown(path: Path) -> tuple[set[str], list[FenceBlock], list[tuple[int, str]]]:
    headings: set[str] = set()
    fences: list[FenceBlock] = []
    links: list[tuple[int, str]] = []

    in_fence = False
    fence_delim = ""
    fence_lang = ""
    fence_start = 0
    fence_lines: list[str] = []

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if in_fence:
            if line == fence_delim:
                fences.append(
                    FenceBlock(
                        path=path,
                        language=fence_lang,
                        start_line=fence_start + 1,
                        lines=fence_lines.copy(),
                    )
                )
                in_fence = False
                fence_delim = ""
                fence_lang = ""
                fence_start = 0
                fence_lines.clear()
                continue

            fence_lines.append(line)
            continue

        fence_match = FENCE_RE.match(line)
        if fence_match:
            in_fence = True
            fence_delim = fence_match.group("fence")
            info = fence_match.group("info").strip()
            fence_lang = info.split()[0].lower() if info else ""
            fence_start = lineno
            fence_lines.clear()
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            slug = slugify_heading(heading_match.group(2))
            if slug:
                headings.add(slug)

        for target in LINK_RE.findall(line):
            links.append((lineno, target))

    return headings, fences, links


def validate_python_fences(fences: Iterable[FenceBlock]) -> list[ValidationError]:
    errors: list[ValidationError] = []
    for fence in fences:
        if fence.language not in PYTHON_FENCE_LANGS:
            continue

        code = "\n".join(fence.lines).rstrip() + "\n"
        try:
            ast.parse(code, filename=str(fence.path))
        except SyntaxError as exc:
            line = fence.start_line + max((exc.lineno or 1) - 1, 0)
            detail = exc.msg
            if exc.text and exc.text.strip():
                detail = f"{detail}: {exc.text.strip()}"
            errors.append(ValidationError(path=fence.path, line=line, message=f"Python fence syntax error: {detail}"))

    return errors


def validate_links(
    markdown_data: dict[Path, tuple[set[str], list[FenceBlock], list[tuple[int, str]]]],
    check_external: bool,
) -> list[ValidationError]:
    errors: list[ValidationError] = []

    for path, (headings, _fences, links) in markdown_data.items():
        for lineno, target in links:
            if target.startswith(LOCAL_SCHEMES):
                continue

            if target.startswith("#"):
                anchor = target[1:]
                if anchor and anchor not in headings:
                    errors.append(ValidationError(path=path, line=lineno, message=f"Missing local anchor: #{anchor}"))
                continue

            if target.startswith(EXTERNAL_SCHEMES):
                if check_external:
                    error = check_external_link(path, lineno, target)
                    if error:
                        errors.append(error)
                continue

            if "://" in target:
                continue

            target_path, _, anchor = target.partition("#")
            resolved = (path.parent / urllib.parse.unquote(target_path)).resolve()
            if not resolved.exists():
                errors.append(
                    ValidationError(
                        path=path,
                        line=lineno,
                        message=f"Broken relative link: {target}",
                    )
                )
                continue

            if anchor and resolved.suffix == ".md":
                target_headings = markdown_data.get(resolved, (set(), [], []))[0]
                if anchor not in target_headings:
                    errors.append(
                        ValidationError(
                            path=path,
                            line=lineno,
                            message=f"Missing anchor in {target_path}: #{anchor}",
                        )
                    )

    return errors


def check_external_link(path: Path, lineno: int, target: str) -> ValidationError | None:
    request = urllib.request.Request(target, headers={"User-Agent": "book-validator/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            status = getattr(response, "status", 200)
            if status >= 400:
                return ValidationError(path=path, line=lineno, message=f"External link returned HTTP {status}: {target}")
    except urllib.error.HTTPError as exc:
        return ValidationError(path=path, line=lineno, message=f"External link returned HTTP {exc.code}: {target}")
    except urllib.error.URLError as exc:
        return ValidationError(path=path, line=lineno, message=f"External link check failed: {target} ({exc.reason})")
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Markdown links and Python code fences for the book.")
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=list(DEFAULT_PATHS),
        help="Markdown files or directories to validate. Defaults to README.md and docs/.",
    )
    parser.add_argument(
        "--check-external-links",
        action="store_true",
        help="Also check external HTTP/HTTPS links. This is slower and may be flaky in CI.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = iter_markdown_files([path if path.is_absolute() else REPO_ROOT / path for path in args.paths])
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    markdown_data = {path: parse_markdown(path) for path in files}
    errors: list[ValidationError] = []

    for _path, (_headings, fences, _links) in markdown_data.items():
        errors.extend(validate_python_fences(fences))

    errors.extend(validate_links(markdown_data, check_external=args.check_external_links))
    errors.sort(key=lambda item: (str(item.path), item.line, item.message))

    if errors:
        for error in errors:
            rel = error.path.relative_to(REPO_ROOT)
            print(f"{rel}:{error.line}: {error.message}", file=sys.stderr)
        print(f"\nValidation failed with {len(errors)} issue(s).", file=sys.stderr)
        return 1

    print(
        f"Validated {len(files)} Markdown files, "
        f"{sum(len(fences) for _headings, fences, _links in markdown_data.values())} fenced blocks, "
        f"and {sum(len(links) for _headings, _fences, links in markdown_data.values())} Markdown links."
    )
    if args.check_external_links:
        print("External link checks were enabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
