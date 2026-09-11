# AFOQT Coach — Claude Code project notes

Local FastAPI + static UI study app for the Air Force Officer Qualifying Test.

Default mission: raise **Quantitative, Academic Aptitude, and Verbal** for a **cyber / software (17X, 62E)** officer package. Rated composites (Pilot / CSO / ABM) are present but dimmed and should not steal study time.

## Run

```bash
chmod +x run.sh
./run.sh
```

App: http://127.0.0.1:8765
Health: http://127.0.0.1:8765/api/health
Ollama (optional): http://127.0.0.1:11434

## Layout

- `app/main.py` — FastAPI
- `app/knowledge/` — LLM grounding corpus. `SYSTEM.md` is the tutor contract. `CYBER_TRACK.md` is the default track.
- `app/questions/bank.json` — original practice items only. Never add claimed official AFOQT items.
- `web/` — dashboard
- `data/progress.json` — created at runtime. Local only.

## Guardrails

- Official scores are percentiles 1–99, not percent correct. Do not invent a conversion table.
- No calculator on the real test. Keep explanations no-calculator.
- Do not scrape or reproduce live AFOQT forms.
- Confirm policy (retakes, waivers, unit cuts) as “verify locally.”
- Prefer installing with Homebrew + a project `.venv`. Do not use system Python packages if a venv works.
