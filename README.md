# AFOQT Coach

Local study guide, quiz generator, and readiness tracker for the Air Force Officer Qualifying Test.

Default track is **cyber / software officer** (17X, software-adjacent 62E). Rated composites (Pilot / CSO / ABM) are on the score report but do not classify a cyber package, so the app deprioritizes them.

This is **not** official AFOQT content and does **not** contain live test items. Pair visual familiarization with official [OATTS](https://af-oatts.github.io/).

**Repo:** https://github.com/WGLewis0721/afoqt-coach-ai

---

## What you get

- **Study pack** a local LLM can use as grounding (`app/knowledge/`)
- **Quiz engine** from an original item bank (108 items across `app/questions/bank_*.json`), optional Ollama-generated extras
- **Readiness tracker** in `data/progress.json` (practice percent is not an official percentile)

Study bars used in the app (not published AFSC cut scores):

| Composite | Official floor | App study bar |
|---|---|---|
| Verbal | 15 | 55 |
| Quantitative | 10 | 70 |
| Academic Aptitude | none published | 65 |
| Pilot / CSO / ABM | n/a for 17X | ignored |

---

## Requirements

- macOS (primary target) — Windows also supported
- Python 3.11+
- Optional: [Ollama](https://ollama.com) for Coach chat and generated items
- Optional: [Docker](https://docker.com) to run everything in containers instead
- Optional: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) to run the install for you

---

## Install (Mac)

### Fast path — double-click

1. Download or `git clone` this repo.
2. Double-click **`Start AFOQT Coach.command`**.
3. First run installs everything automatically (a Terminal window will show progress) — after that it opens http://127.0.0.1:8765 in your browser by itself.
4. To stop it, close that Terminal window.

If macOS blocks it the first time ("cannot be opened because it is from an unidentified developer"): right-click the file → **Open** → **Open** again to confirm once.

### Fast path — Claude Code

Clone, open the folder in Claude Code, paste the prompt in [`COMPANION_PROMPT.md`](COMPANION_PROMPT.md).

### Manual

```bash
git clone https://github.com/WGLewis0721/afoqt-coach-ai.git
cd afoqt-coach-ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
chmod +x run.sh
./run.sh
```

Open http://127.0.0.1:8765

If `python3` is missing:

```bash
brew install python
```

### Local LLM (optional, recommended for Coach)

Quizzes and readiness work without this. Coach chat and “Add a few AI questions” need Ollama.

```bash
brew install ollama
brew services start ollama
# 16 GB RAM
ollama pull llama3.1
# 8 GB RAM
# ollama pull llama3.2
```

The app calls `http://127.0.0.1:11434`. Confirm:

```bash
curl -s http://127.0.0.1:11434/api/tags
curl -s http://127.0.0.1:8765/api/health
```

`health.ollama.ok` should be `true` once the daemon and a model are present.

---

## Install (Windows)

Double-click **`run.bat`** (first run installs a local `.venv` and dependencies, then starts the app and opens your browser). Or from PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File run.ps1
```

If Python isn't found, install it from [python.org](https://python.org/downloads) and check **"Add python.exe to PATH"** during setup.

---

## Install (Docker)

Runs the app and a local Ollama instance together, fully containerized — no Python or Ollama install needed on the host.

```bash
docker compose up -d
docker compose exec ollama ollama pull llama3.1   # one-time, for Coach chat
```

Open http://127.0.0.1:8765. Progress is persisted to `./data` on the host; pulled Ollama models persist in a named Docker volume.

To run the app container alone (against an Ollama already running on the host instead of a containerized one):

```bash
docker build -t afoqt-coach .
docker run -p 8765:8765 -v "$(pwd)/data:/app/data" -e OLLAMA_URL=http://host.docker.internal:11434 afoqt-coach
```

Stop everything with `docker compose down` (add `-v` to also delete the pulled Ollama models).

---

## Usage

1. Leave the track on **Cyber / software (17X, 62E)** unless you want a cockpit.
2. Baseline **Math Knowledge**, then **Arithmetic Reasoning**, then **Word Knowledge**.
3. Work the dashboard **Next actions** list.
4. Answer every item on test day (no guessing penalty), including rated sections you did not study.

```bash
curl -s http://127.0.0.1:8765/api/health
curl -s http://127.0.0.1:8765/api/readiness
```

Progress is local: `data/progress.json`. It is gitignored.

---

## Layout

```
afoqt-coach-ai/
  app/
    knowledge/                    LLM grounding (SYSTEM.md, CYBER_TRACK.md, …)
    questions/bank_verbal.json    original VA/WK/RC items
    questions/bank_quant.json     original AR/MK items
    questions/bank_other.json     original PS/AI/IC/BC/TR/SJ items
    questions/flashcards_*.json   flashcard decks (math, vocab, word parts, …)
    flashcards.py                 flashcard loader
    main.py                       FastAPI
  web/
    fonts/                       self-hosted webfonts (no CDN needed, works offline)
    index.html, styles.css, app.js
  data/                          created at runtime
  run.sh                         Mac/Linux launcher (CLI)
  Start AFOQT Coach.command      Mac launcher (double-click)
  run.ps1 / run.bat              Windows launcher
  Dockerfile / docker-compose.yml
  COMPANION_PROMPT.md            paste into Claude Code
  CLAUDE.md                      Claude Code project notes
```

`app/bank.py` loads `questions/bank.json` if you add one, otherwise it merges the `bank_*.json` shards. `app/flashcards.py` merges every `questions/flashcards_*.json` shard the same way.

Point Open WebUI or another local frontend at `app/knowledge/` and use `app/knowledge/SYSTEM.md` as the system prompt.

---

## Scoring reminder

Official AFOQT composites are **percentiles 1–99** against a reference population, not percent correct.

Typical published commissioning floors (confirm with your testing office):

- All line officers: Verbal **15**, Quantitative **10**
- 17X / other non-rated: those two only
- Pilot / RPA: Pilot **25**
- CSO: CSO **25**
- ABM: ABM **25**

Retake windows and super-score rules move. Verify current DAFMAN / local policy.

---

## Disclaimer

Original practice items only. Not affiliated with the U.S. Air Force. Do not treat practice percent as an official AFOQT percentile.
