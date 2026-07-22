#!/usr/bin/env python3
"""Small, dependency-free structural validator for Cognitive OS v0.

It deliberately does not call a model and does not decide whether a claim is true.
It checks only repository hygiene and the presence of governance guardrails.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED = [
    "00_KONTRAKT_PRACY_Z_AI.md",
    "01_KOMPAS.md",
    "02_KANON.md",
    "03_AKTYWNY.md",
    "DECYZJE.md",
    "PARKING.md",
    "BACKLOG.md",
    "BRAMA_BUDOWANIA.md",
    "DOWODY.md",
    "INCYDENTY.md",
    "08_PAKIET_WERYFIKACYJNY.md",
    "09_CLOSER_SESJI.md",
    "99_HANDOFF.md",
]

HEADINGS = {
    "01_KOMPAS.md": ["## Aktywny cel", "## Najbliższy dowód lub działanie", "## Otwarte pytania"],
    "02_KANON.md": ["## Zasady stałe", "## Hierarchia źródeł"],
    "03_AKTYWNY.md": ["## Rezultat", "## Czego nie dodajemy", "## Definicja ukończenia (Definition of Done)", "## Jeden następny krok"],
    "BRAMA_BUDOWANIA.md": ["## A. Problem", "## C. Alternatywy i zakres wyszukiwania", "## G. Decyzja bramy"],
    "08_PAKIET_WERYFIKACYJNY.md": ["## 3. Tezy", "## 5. Atak kontradyktoryjny", "## 8. Werdykt ograniczony zakresem", "## 9. Decyzja człowieka"],
    "09_CLOSER_SESJI.md": ["## DECYZJE", "## WIEDZA / DOWODY", "## NASTĘPNY KROK", "## KONTROLA ZAMKNIĘCIA"],
    "99_HANDOFF.md": ["## Aktualny cel", "## Jeden następny krok", "## Pliki źródłowe"],
}

SECRET_PATTERNS = [
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"(?i)\b(password|passwd|secret)\s*[:=]\s*\S+"),
]

ID_RE = re.compile(r"\b(?:DEC|EVD|INC|PARK|BL)-\d{4}-\d{3}\b")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cos_dir", type=Path, help="ścieżka do katalogu COS")
    parser.add_argument("--strict", action="store_true", help="ostrzeżenia traktuj jak błędy")
    args = parser.parse_args()

    root = args.cos_dir.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"ERROR: katalog nie istnieje: {root}")
        return 2

    contents: dict[str, str] = {}
    for name in REQUIRED:
        path = root / name
        if not path.is_file():
            errors.append(f"brak wymaganego pliku: {name}")
            continue
        text = read(path)
        contents[name] = text
        if not text.strip():
            errors.append(f"pusty plik: {name}")
        if not frontmatter(text):
            warnings.append(f"brak lub niepełny front matter: {name}")

        for heading in HEADINGS.get(name, []):
            if heading not in text:
                errors.append(f"{name}: brak sekcji {heading}")

        if "TODO" in text or "YYYY-MM-DD" in text or "<!-- ... -->" in text:
            warnings.append(f"{name}: zawiera placeholder; uzupełnij przed użyciem")

        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"{name}: możliwy sekret lub hasło — usuń przed commitem")

    if not (root / "SESJE").is_dir():
        errors.append("brak katalogu SESJE/")

    # Duplicate IDs in headings are usually a copy/paste error. References in
    # tables, prose and cross-links are intentionally allowed.
    seen: dict[str, tuple[str, int]] = {}
    for name, text in contents.items():
        for line_no, line in enumerate(text.splitlines(), 1):
            stripped = line.lstrip()
            if not stripped.startswith("#") or stripped.startswith("<!--"):
                continue
            for identifier in ID_RE.findall(line):
                if identifier in seen:
                    prev_name, prev_line = seen[identifier]
                    warnings.append(
                        f"powtórzone ID {identifier}: {prev_name}:{prev_line} oraz {name}:{line_no}"
                    )
                else:
                    seen[identifier] = (name, line_no)

    handoff = contents.get("99_HANDOFF.md", "")
    if "source_commit_or_hash: UNKNOWN" in handoff:
        warnings.append("99_HANDOFF.md: source_commit_or_hash nadal UNKNOWN")

    closer = contents.get("09_CLOSER_SESJI.md", "")
    if "NO_STATE_CHANGE" not in closer and "DECYZJE" in closer:
        warnings.append("09_CLOSER_SESJI.md: upewnij się, że brak zmiany stanu jest jawnie oznaczony, jeśli dotyczy")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors or (args.strict and warnings):
        print(f"FAIL: {len(errors)} błędów, {len(warnings)} ostrzeżeń")
        return 1

    print(f"OK: {len(contents)} plików sprawdzonych, {len(warnings)} ostrzeżeń")
    return 0


if __name__ == "__main__":
    sys.exit(main())
