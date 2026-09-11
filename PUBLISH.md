# Publish this folder to GitHub

Repo already exists and is almost empty:
https://github.com/WGLewis0721/afoqt-coach-ai

Paste into Claude Code from inside this project folder:

```
Publish this project to https://github.com/WGLewis0721/afoqt-coach-ai on branch main.

Rules:
- Do not commit .venv, data/progress.json, __pycache__, .DS_Store
- Keep .gitignore
- Overwrite the stub README with the README.md already in this folder
- If the remote has only the placeholder README, replace it
- git add -A, commit with message: "Initial AFOQT Coach app for cyber/software track"
- git push -u origin main
- If auth fails, use gh auth login or the user's existing GitHub credentials. Do not print tokens.
- After push, print the repo URL and confirm README is on main.
```

Manual equivalent:

```bash
cd /path/to/afoqt-coach
git init
git remote add origin https://github.com/WGLewis0721/afoqt-coach-ai.git
git fetch origin
git checkout -B main
git add .
git status
git commit -m "Initial AFOQT Coach app for cyber/software track"
git push -u origin main
```

If `main` already has a commit, pull with allow-unrelated-histories or force-push only if you own the repo and the only remote file is the stub README:

```bash
git pull origin main --allow-unrelated-histories
# resolve README if needed, keep the local full README
git push -u origin main
```
