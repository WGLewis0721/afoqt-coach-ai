from __future__ import annotations

from pathlib import Path

from .config import KNOWLEDGE_DIR, KNOWLEDGE_ROUTES


def read_file(name: str) -> str:
    path = KNOWLEDGE_DIR / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def system_prompt() -> str:
    return read_file("SYSTEM.md")


def all_knowledge() -> str:
    parts = []
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        parts.append(f"\n\n# FILE {path.name}\n\n{path.read_text(encoding='utf-8')}")
    return "".join(parts)


def retrieve(query: str, subtest: str | None = None, budget_chars: int = 14000) -> str:
    names: list[str] = []
    if subtest and subtest in KNOWLEDGE_ROUTES:
        names.extend(KNOWLEDGE_ROUTES[subtest])
    q = (query or "").lower()
    mapping = [
        (("analog", "verbal pair", "bridge"), "VERBAL.md"),
        (("vocab", "synonym", "prefix", "root"), "VERBAL.md"),
        (("passage", "reading", "main idea", "inference"), "VERBAL.md"),
        (("algebra", "geometry", "percent", "ratio", "word problem", "math"), "MATH.md"),
        (("newton", "ohm", "pH", "kinetic", "science", "chemistry"), "SCIENCE.md"),
        (("aileron", "stall", "lift", "runway", "attitude", "aviation", "pitot"), "AVIATION.md"),
        (("block", "table reading", "coordinate", "spatial"), "SPATIAL.md"),
        (("situational", "core value", "integrity", "sdi", "personality"), "OFFICER_JUDGMENT.md"),
        (("composite", "percentile", "pilot", "cso", "abm", "minimum", "pcsm"), "OVERVIEW.md"),
        (("cyber", "17x", "17d", "17s", "software", "62e", "quant 70", "non-rated"), "CYBER_TRACK.md"),
        (("test day", "guess", "calendar", "pace"), "TEST_DAY.md"),
    ]
    for keys, fname in mapping:
        if any(k in q for k in keys) and fname not in names:
            names.append(fname)
    if not names:
        names = ["CYBER_TRACK.md", "OVERVIEW.md"]
    if "OVERVIEW.md" not in names:
        names.append("OVERVIEW.md")
    chunks = []
    used = 0
    for name in names:
        text = read_file(name)
        if not text:
            continue
        piece = f"\n\n# FILE {name}\n\n{text}"
        if used + len(piece) > budget_chars:
            remain = budget_chars - used
            if remain > 400:
                chunks.append(piece[:remain])
            break
        chunks.append(piece)
        used += len(piece)
    return "".join(chunks)
