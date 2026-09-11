from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from .config import (
    COMPETITIVE,
    COMPOSITES,
    DATA_DIR,
    DEFAULT_TRACK,
    FLOORS,
    PROGRESS_PATH,
    SUBTESTS,
    TRACK_FOCUS,
    TRACK_SUBTEST_PRIORITY,
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_progress() -> dict[str, Any]:
    return {
        "target_track": DEFAULT_TRACK,
        "created": _now(),
        "events": [],
        "subtests": {
            key: {
                "attempts": 0,
                "correct": 0,
                "seen_ids": [],
                "miss_topics": {},
                "last_percent": None,
                "last_at": None,
            }
            for key in SUBTESTS
        },
    }


def load() -> dict[str, Any]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not PROGRESS_PATH.exists():
        data = default_progress()
        save(data)
        return data
    data = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
    base = default_progress()
    for k, v in base.items():
        if k not in data:
            data[k] = v
    for key in SUBTESTS:
        if key not in data["subtests"]:
            data["subtests"][key] = base["subtests"][key]
    return data


def save(data: dict[str, Any]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROGRESS_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


def set_track(track: str) -> dict[str, Any]:
    data = load()
    if track not in TRACK_FOCUS:
        track = "undecided"
    data["target_track"] = track
    save(data)
    return readiness(data)


def record_quiz(graded: dict[str, Any], subtest: str, elapsed_sec: float | None) -> dict[str, Any]:
    data = load()
    data["events"].append(
        {
            "at": _now(),
            "subtest": subtest,
            "correct": graded["correct"],
            "total": graded["total"],
            "percent": graded["percent"],
            "elapsed_sec": elapsed_sec,
        }
    )
    data["events"] = data["events"][-200:]
    by_sub: dict[str, list] = {}
    for r in graded["results"]:
        by_sub.setdefault(r["subtest"], []).append(r)
    for st, rows in by_sub.items():
        if st not in SUBTESTS:
            continue
        slot = data["subtests"].setdefault(
            st,
            {
                "attempts": 0,
                "correct": 0,
                "seen_ids": [],
                "miss_topics": {},
                "last_percent": None,
                "last_at": None,
            },
        )
        slot["attempts"] += len(rows)
        slot["correct"] += sum(1 for r in rows if r["correct"])
        for r in rows:
            if r["id"] not in slot["seen_ids"]:
                slot["seen_ids"].append(r["id"])
            if not r["correct"]:
                topic = r.get("topic") or "general"
                slot["miss_topics"][topic] = slot["miss_topics"].get(topic, 0) + 1
        slot["last_percent"] = round(100 * sum(1 for r in rows if r["correct"]) / len(rows), 1)
        slot["last_at"] = _now()
        slot["seen_ids"] = slot["seen_ids"][-200:]
    save(data)
    return readiness(data)


def _band(percent: float | None, attempts: int) -> str:
    if attempts < 5 or percent is None:
        return "untested"
    if percent >= 85:
        return "ready"
    if percent >= 70:
        return "borderline"
    return "weak"


def readiness(data: dict[str, Any] | None = None) -> dict[str, Any]:
    data = data or load()
    sub = {}
    for key, meta in SUBTESTS.items():
        slot = data["subtests"][key]
        attempts = slot["attempts"]
        pct = round(100 * slot["correct"] / attempts, 1) if attempts else None
        misses = sorted(slot.get("miss_topics", {}).items(), key=lambda kv: -kv[1])[:5]
        sub[key] = {
            **meta,
            "attempts": attempts,
            "correct": slot["correct"],
            "percent": pct,
            "last_percent": slot.get("last_percent"),
            "band": _band(pct, attempts),
            "top_miss_topics": [m[0] for m in misses],
        }

    composites = {}
    for name, parts in COMPOSITES.items():
        parts_data = [sub[p] for p in parts]
        tested = [p for p in parts_data if p["attempts"] >= 5]
        if not tested:
            band = "untested"
            pct = None
        else:
            pct = round(sum(p["percent"] for p in tested) / len(tested), 1)
            if len(tested) < len(parts):
                raw_band = _band(pct, 5)
                band = "borderline" if raw_band == "ready" else raw_band
                if any(p["band"] == "weak" for p in tested):
                    band = "weak"
            else:
                band = _band(pct, 5)
                if any(p["band"] == "weak" for p in parts_data):
                    band = "weak"
        composites[name] = {
            "parts": parts,
            "percent": pct,
            "band": band,
            "floor_percentile": FLOORS.get(name),
            "competitive_percentile": COMPETITIVE.get(name),
            "coverage": f"{len(tested)}/{len(parts)} subtests with >=5 items",
        }

    track = data.get("target_track", DEFAULT_TRACK)
    focus = TRACK_FOCUS.get(track, TRACK_FOCUS["cyber_software"])
    actions = []
    focus_subs = list(TRACK_SUBTEST_PRIORITY.get(track, []))
    for comp in focus:
        for part in COMPOSITES.get(comp, []):
            if part not in focus_subs:
                focus_subs.append(part)
    seen = set()
    ordered = []
    for k in focus_subs:
        if k not in seen and k in sub:
            seen.add(k)
            ordered.append(k)
    for k in ordered:
        band = sub[k]["band"]
        if band in ("weak", "untested", "borderline"):
            why = {
                "untested": "No baseline yet — this feeds the cyber/software board composites.",
                "weak": "Accuracy below 70%. This is a scored composite input.",
                "borderline": "Not locked. Technical packages want this at 85%+ practice.",
            }[band]
            miss = sub[k]["top_miss_topics"]
            extra = f" Miss tags: {', '.join(miss)}." if miss else ""
            actions.append(f"{sub[k]['label']}: {why}{extra}")
        if len(actions) >= 5:
            break
    if not actions:
        actions.append(
            "Primary composites are green. Keep two timed MK+AR sets and one VA/WK speed set per week. Rated subtests (AI/IC/TR/BC) do not move a 17X/62E package."
        )

    q = composites.get("quantitative", {})
    a = composites.get("academic", {})
    v = composites.get("verbal", {})
    tech_parts = [p for p in (q.get("percent"), a.get("percent"), v.get("percent")) if p is not None]
    tech_pct = None
    if len(tech_parts) >= 2 and q.get("percent") is not None:
        wq, wa, wv = 0.50, 0.35, 0.15
        qp = q.get("percent") or 0
        ap = a.get("percent") or qp
        vp = v.get("percent") or ap
        tech_pct = round(wq * qp + wa * ap + wv * vp, 1)
    composites["tech_board"] = {
        "parts": ["quantitative", "academic", "verbal"],
        "percent": tech_pct,
        "band": _band(tech_pct, 8 if tech_pct is not None else 0),
        "floor_percentile": None,
        "competitive_percentile": 70,
        "coverage": "weighted Quant 50% / Academic 35% / Verbal 15% (study proxy, not an official composite)",
    }

    primary = focus + (["tech_board"] if track in ("cyber_software", "nonrated", "undecided") else [])
    return {
        "target_track": track,
        "primary_composites": primary,
        "subtests": sub,
        "composites": composites,
        "next_actions": actions,
        "disclaimer": "Practice percent is not an official AFOQT percentile. Official scores are normed 1-99. Cyber/software boards use Verbal, Quantitative, and Academic Aptitude — not Pilot/CSO/ABM.",
        "event_count": len(data.get("events", [])),
    }
