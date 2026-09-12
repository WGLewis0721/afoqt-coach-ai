# Companion prompt — paste into Claude Code

She just needs to: open this folder in Claude Code, then paste everything in the
box below into the chat. Claude Code does the rest, and finishes by giving her
a plain-English guide for turning the app on, off, updating it, and using it.

---

```
You are installing and launching AFOQT Coach for the person you're talking to
right now. Assume she is not a programmer — don't ask her to run terminal
commands herself unless something below genuinely requires her input.

This app is a local study / quiz / flashcard / readiness tracker for the Air
Force Officer Qualifying Test, default track cyber/software officer (17X /
62E). It is NOT official AFOQT content and must never claim to be.

## Ground rules
- Everything runs locally. Never bind anything to more than 127.0.0.1.
- Never deploy this to the public internet.
- Never invent official AFOQT cut scores, live test items, or policy details
  not already in app/knowledge/. If she asks something the app doesn't cover,
  say so plainly instead of guessing.
- Prefer the project's own scripts over hand-rolled commands — they already
  handle the venv, dependencies, and browser opening correctly.
- If a step fails, don't just retry blindly — read the actual error and fix
  the real cause (missing Python, port already in use, etc.) before moving on.

## 1. Confirm you're in the right place
Check these exist relative to your current directory:
- app/main.py
- app/flashcards.py
- web/index.html
- requirements.txt
- run.sh
- Start AFOQT Coach.command  (macOS launcher)
- run.ps1 / run.bat          (Windows launcher, if she's on Windows)
- Dockerfile / docker-compose.yml

If none of that exists, ask her where the project folder or zip is before
doing anything else.

## 2. Set it up and start it
On macOS (the normal case):

```bash
chmod +x run.sh "Start AFOQT Coach.command"
./run.sh
```

This creates `.venv`, installs `requirements.txt` into it, and starts the
server at http://127.0.0.1:8765. Run it in the background (or in a way you can
keep monitoring) rather than leaving it attached and blocking your only
shell — you still need to run health checks next.

If `python3` is missing: `brew install python` (installs Homebrew first if
needed — see https://brew.sh — then retry).

If port 8765 is already in use by an old copy, find and stop that process
first rather than picking a different port; the frontend and any bookmarks
assume 8765.

### Optional: local LLM for the Coach chat feature
Quizzes, flashcards, and readiness tracking all work with zero setup. Only
the "Coach" chat tab and "Add a few AI questions" need a local LLM:

```bash
brew install ollama
brew services start ollama
ollama pull llama3.1     # needs ~16GB RAM; use llama3.2 if the Mac has less
```

This step can take a while to download the model — that's completely normal,
not a hang. If she's watching, mention that once the app is open, the Coach
tab and Learn tab's "Explain this to me" button both have a little bubble-pop
mini-game that appears automatically during any wait like this.

Skip this step entirely if she says she doesn't want it — the app is fully
useful without it.

## 3. Verify it actually works
```bash
curl -s http://127.0.0.1:8765/api/health
curl -s http://127.0.0.1:8765/api/readiness
curl -s http://127.0.0.1:8765/api/flashcards | head -c 200
```
`health.ok` must be `true`. If Ollama was installed, `health.ollama.ok` should
also become `true` once the model finishes pulling (may take a few minutes
after `ollama pull` completes).

Open it for her: `open http://127.0.0.1:8765`

Click through once yourself: the tabs are My Progress, Learn, Flashcards,
Practice, and Coach. Confirm the page actually loads with content (not a blank
page or an error) before telling her it's done.

## 4. Leave her with a simple, friendly how-to
This is the most important part — don't skip it or make it a wall of text.
Once everything above is verified working, write her a short, warm message
(not a technical readme dump) covering exactly these four things:

**Turning it on** — Double-click `Start AFOQT Coach.command` in the project
folder. A small Terminal window will open; that's normal, just leave it be.
Her browser will open to the app automatically after a few seconds.

**Turning it off** — Close that Terminal window (or click into it and press
Control+C). That stops the app. Her progress is saved automatically and will
still be there next time.

**Updating it** — If you (or she) ever pull new changes into this folder,
just turn it off and back on again (close the Terminal window, double-click
the launcher again) — no reinstall needed unless a brand-new dependency was
added, in which case re-run `./run.sh` once from a terminal instead of the
`.command` file so it can reinstall.

**Using it** — One or two lines per tab, in plain language:
- *My Progress* — her dashboard: overall readiness, what to study next.
- *Learn* — the full study guide, organized by topic.
- *Flashcards* — quick-fire vocab, formulas, and definitions.
- *Practice* — timed or untimed quizzes, by section or mixed, with adjustable
  difficulty.
- *Coach* — a chat tutor she can ask for explanations or quick drills (only
  live if Ollama is installed and running).

Keep the whole message short enough that she'd actually read it — a few
sentences per section, not paragraphs. Do not lecture her about the AFOQT
itself; the app already has that covered.
```
