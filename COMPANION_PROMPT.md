# Companion prompt — paste into Claude Code

Copy everything inside the block below into a new Claude Code session on the Mac that already has Claude Code installed. Point Claude Code at this folder first (`cd` into `afoqt-coach`).

---

```
You are installing and launching AFOQT Coach on this Mac.

## Goal
Get a local study / quiz / readiness webapp running at http://127.0.0.1:8765 with a working Python venv. Optionally install Ollama and pull a local model so Coach mode works. Then verify the API and leave the server running.

This app is for the Air Force Officer Qualifying Test, default track cyber/software officer (17X / 62E). It is NOT official AFOQT content.

## Assumptions
- You may install anything needed (Homebrew packages, Python, Ollama, models).
- You may run commands, create a venv, and start background processes.
- Do not deploy this to the public internet. Bind to 127.0.0.1 only.
- Do not modify exam knowledge to invent official cut scores or live test items.
- Prefer project-local .venv over system Python.

## Do this in order

### 1. Locate the project
Find afoqt-coach/ (this folder). Confirm these exist:
- app/main.py
- app/knowledge/SYSTEM.md
- app/knowledge/CYBER_TRACK.md
- app/questions/bank.json
- web/index.html
- requirements.txt
- run.sh

If the user only has afoqt-coach.zip, unzip it to ~/AFOQT-Coach/afoqt-coach and work there.

### 2. Tooling
- Need python3.11+ . If missing: `brew install python`
- Need curl.
- chmod +x run.sh

### 3. Python env
From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Smoke import:

```bash
python -c "from app.bank import ITEMS; from app.config import DEFAULT_TRACK; print(len(ITEMS), DEFAULT_TRACK)"
```

Expect DEFAULT_TRACK == cyber_software and ITEMS >= 90.

### 4. Optional local LLM (do this unless the user says skip)
Check `which ollama`. If missing:

```bash
brew install ollama
```

Start the daemon if it is not up:

```bash
brew services start ollama || ollama serve
```

Wait until `curl -sf http://127.0.0.1:11434/api/tags` works.

Pick a model by RAM:
- 16 GB or more: `ollama pull llama3.1`
- 8 GB: `ollama pull llama3.2`
- tight disk: `ollama pull phi3`

Do not pull a 70B model.

### 5. Launch
If port 8765 is already taken by an old copy, kill that process.

```bash
source .venv/bin/activate
python -m uvicorn app.main:app --host 127.0.0.1 --port 8765 --reload
```

Keep it running in the background.

### 6. Verify
```bash
curl -s http://127.0.0.1:8765/api/health
curl -s http://127.0.0.1:8765/api/readiness
curl -s http://127.0.0.1:8765/api/knowledge?topic=cyber_software | head
```

health.ok must be true.
readiness.target_track should be cyber_software.
If Ollama is up, health.ollama.ok should be true and models should be non-empty.

Open http://127.0.0.1:8765 in the default browser (`open http://127.0.0.1:8765`).

### 7. Report back
Tell the user:
- project path
- Python version
- whether Ollama and which model
- URL
- that quizzes work offline even if Ollama failed
- first study move: timed Math Knowledge quiz, then Arithmetic Reasoning, then Word Knowledge

Do not start a long lecture about the AFOQT. The app already contains the study pack.
```

---

## Shorter variant (if the folder is already open in Claude Code)

```
Install and launch this AFOQT Coach project on this Mac.

Create .venv, pip install -r requirements.txt, chmod +x run.sh.
If python3 or brew tools are missing, install them.
If Ollama is missing, brew install ollama, start it, and pull llama3.1 (llama3.2 if RAM is 8GB).
Bind uvicorn to 127.0.0.1:8765 only, leave it running, curl /api/health and /api/readiness,
open the URL in the browser.
Default track is cyber/software. Do not expose the port publicly.
Do not add claimed official AFOQT items. Report path, model, and URL when done.
```
