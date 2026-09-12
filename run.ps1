# AFOQT Coach - Windows launcher
# Double-click run.bat, or run this file with: powershell -ExecutionPolicy Bypass -File run.ps1

$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python was not found." -ForegroundColor Red
    Write-Host "Install it from https://python.org/downloads - during setup, check the box that says 'Add python.exe to PATH'." -ForegroundColor Yellow
    Read-Host "Press Enter to close"
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "First-time setup, this can take a minute..." -ForegroundColor Cyan
    python -m venv .venv
}

Write-Host "Checking dependencies..." -ForegroundColor Cyan
& ".\.venv\Scripts\python.exe" -m pip install -q --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -q -r requirements.txt

$env:PYTHONUNBUFFERED = "1"

Write-Host ""
Write-Host "Starting AFOQT Coach..." -ForegroundColor Cyan
Write-Host "Optional, for the Coach chat feature: install Ollama from https://ollama.com, then run 'ollama pull llama3.1'." -ForegroundColor DarkGray
Write-Host ""

$proc = Start-Process -FilePath ".\.venv\Scripts\python.exe" `
    -ArgumentList "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8765" `
    -PassThru -NoNewWindow

$ready = $false
for ($i = 0; $i -lt 40; $i++) {
    Start-Sleep -Milliseconds 500
    try {
        $r = Invoke-WebRequest -Uri "http://127.0.0.1:8765/api/health" -TimeoutSec 1 -UseBasicParsing
        if ($r.StatusCode -eq 200) { $ready = $true; break }
    } catch {}
}

if ($ready) {
    Start-Process "http://127.0.0.1:8765"
    Write-Host "AFOQT Coach is running at http://127.0.0.1:8765" -ForegroundColor Green
} else {
    Write-Host "The app is taking longer than expected to start. Open http://127.0.0.1:8765 in your browser once it's ready." -ForegroundColor Yellow
}
Write-Host "Close this window (or press Ctrl+C) to stop it." -ForegroundColor DarkGray

Wait-Process -Id $proc.Id
