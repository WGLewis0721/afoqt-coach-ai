const $ = (s) => document.querySelector(s);

const state = {
  meta: null,
  quiz: null,
  startedAt: null,
  timerId: null,
  remaining: 0,
  chat: [],
};

document.querySelectorAll(".tabs button").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tabs button").forEach((b) => b.classList.remove("on"));
    document.querySelectorAll(".panel").forEach((p) => p.classList.remove("on"));
    btn.classList.add("on");
    $("#tab-" + btn.dataset.tab).classList.add("on");
  });
});

async function api(path, opts) {
  const res = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

function bandEl(band) {
  return `<span class="band ${band}">${band}</span>`;
}

async function refreshHealth() {
  try {
    const h = await api("/api/health");
    const el = $("#llmStatus");
    if (h.ollama && h.ollama.ok) {
      const models = (h.ollama.models || []).join(", ") || "model ready";
      el.textContent = "Ollama: " + models;
      el.style.color = "#3d9a6a";
    } else {
      el.textContent = "Ollama offline — bank quizzes still work";
      el.style.color = "#d4a017";
    }
  } catch {
    $("#llmStatus").textContent = "API down";
  }
}

async function refreshReady() {
  const r = await api("/api/readiness");
  $("#track").value = r.target_track || "undecided";
  $("#disclaimer").textContent = r.disclaimer;
  const primary = new Set(r.primary_composites || ["quantitative", "academic", "verbal", "tech_board"]);
  const order = ["tech_board", "quantitative", "academic", "verbal", "pilot", "cso", "abm"];
  const names = order.filter((n) => r.composites[n]).concat(Object.keys(r.composites).filter((n) => !order.includes(n)));
  const cards = names
    .map((name) => {
      const c = r.composites[name];
      const pct = c.percent == null ? "\u2014" : c.percent + "% practice";
      const floor = c.floor_percentile != null ? `floor ${c.floor_percentile}ile` : "no published floor";
      const comp = c.competitive_percentile != null ? ` \u00b7 study bar ~${c.competitive_percentile}+` : "";
      const dim = primary.has(name) ? "" : " dim";
      const tag = primary.has(name) ? "" : `<div class="muted">not used for cyber/software classification</div>`;
      return `<div class="card${dim}"><h3>${name.replace("_", " ")}</h3>${bandEl(c.band)}<div>${pct}</div><div class="muted">${c.coverage}<br/>${floor}${comp}</div>${tag}</div>`;
    })
    .join("");
  $("#composites").innerHTML = cards;
  $("#actions").innerHTML = (r.next_actions || []).map((a) => `<li>${a}</li>`).join("");
  const rows = Object.entries(r.subtests)
    .map(([key, s]) => {
      const pct = s.percent == null ? "\u2014" : s.percent + "%";
      return `<tr><td>${s.code}</td><td>${s.label}</td><td>${s.items} / ${s.minutes}m</td><td>${s.attempts}</td><td>${pct}</td><td>${bandEl(s.band)}</td><td>${(s.top_miss_topics || []).join(", ")}</td></tr>`;
    })
    .join("");
  $("#subtests").innerHTML = `<table><thead><tr><th>ID</th><th>Subtest</th><th>Real pace</th><th>Logged</th><th>Acc</th><th>Band</th><th>Miss tags</th></tr></thead><tbody>${rows}</tbody></table>`;
}

function fillSelects(meta) {
  const subs = Object.entries(meta.subtests);
  const quiz = $("#quizSub");
  const coach = $("#coachSub");
  quiz.innerHTML = `<option value="mixed">Mixed</option>` + subs.map(([k, v]) => `<option value="${k}">${v.code} — ${v.label}</option>`).join("");
  coach.innerHTML = `<option value="">General</option>` + subs.map(([k, v]) => `<option value="${k}">${v.label}</option>`).join("");
}

$("#track").addEventListener("change", async (e) => {
  await api("/api/track", { method: "POST", body: JSON.stringify({ target_track: e.target.value }) });
  refreshReady();
});

$("#resetBtn").addEventListener("click", async () => {
  if (!confirm("Wipe local readiness history?")) return;
  await api("/api/reset", { method: "POST" });
  refreshReady();
});

async function loadStudyPack() {
  const topic = $("#studyTopic").value;
  $("#studyOut").textContent = "Loading pack\u2026";
  const pack = await api("/api/knowledge?topic=" + encodeURIComponent(topic));
  $("#studyOut").textContent = pack.content.replace(/^\n+/, "");
}

$("#studyTopic").addEventListener("change", loadStudyPack);

$("#studyAsk").addEventListener("click", async () => {
  const topic = $("#studyTopic").value;
  $("#studyOut").textContent = "Coaching\u2026";
  const messages = [
    {
      role: "user",
      content:
        "Teach this AFOQT section as a compact study brief: key rules, 2 worked examples, and the real-test pace. Then give me 3 check questions with answers at the bottom.",
    },
  ];
  const res = await api("/api/chat", {
    method: "POST",
    body: JSON.stringify({ messages, subtest: topic }),
  });
  $("#studyOut").textContent = (res.provider === "fallback" ? "[offline excerpt]\n\n" : "") + res.content;
});

function stopTimer() {
  if (state.timerId) clearInterval(state.timerId);
  state.timerId = null;
}

function tick() {
  state.remaining -= 1;
  const el = $("#timer");
  if (el) el.textContent = formatTime(Math.max(0, state.remaining));
  if (state.remaining <= 0) {
    stopTimer();
    submitQuiz(true);
  }
}

function formatTime(s) {
  const m = Math.floor(s / 60);
  const r = s % 60;
  return `${m}:${String(r).padStart(2, "0")}`;
}

$("#startQuiz").addEventListener("click", startQuiz);

async function startQuiz() {
  stopTimer();
  const body = {
    subtest: $("#quizSub").value,
    n: Number($("#quizN").value),
    difficulty: $("#quizDiff").value,
    use_llm: $("#quizLlm").checked,
  };
  $("#quizBox").textContent = "Building quiz\u2026";
  const quiz = await api("/api/quiz", { method: "POST", body: JSON.stringify(body) });
  state.quiz = quiz;
  state.startedAt = Date.now();
  const timed = $("#quizTimed").checked;
  state.remaining = timed ? quiz.timed_seconds : 0;
  $("#quizMeta").innerHTML = timed
    ? `${quiz.items.length} items \u00b7 target ${quiz.target_pace_sec_per_item}s each \u00b7 <span class="timer" id="timer">${formatTime(state.remaining)}</span>`
    : `${quiz.items.length} items \u00b7 untimed \u00b7 target ${quiz.target_pace_sec_per_item}s each`;
  $("#quizBox").innerHTML =
    quiz.items
      .map((item, idx) => {
        const choices = (item.choices || [])
          .map((c) => `<label class="choice"><input type="radio" name="q${idx}" value="${c.trim()[0]}" /> ${c}</label>`)
          .join("");
        const vis = item.visual ? `<pre>${item.visual}</pre>` : "";
        return `<div class="q" data-id="${item.id}" data-idx="${idx}"><div class="stem">${idx + 1}. ${item.stem}</div>${vis}${choices}</div>`;
      })
      .join("") + `<button id="submitQuiz">Score it</button>`;
  $("#submitQuiz").addEventListener("click", () => submitQuiz(false));
  if (timed) state.timerId = setInterval(tick, 1000);
}

async function submitQuiz(auto) {
  if (!state.quiz) return;
  stopTimer();
  const responses = state.quiz.items.map((item, idx) => {
    const picked = document.querySelector(`input[name="q${idx}"]:checked`);
    return { id: item.id, selected: picked ? picked.value : "", time_sec: null };
  });
  const elapsed = (Date.now() - state.startedAt) / 1000;
  const out = await api("/api/grade", {
    method: "POST",
    body: JSON.stringify({
      subtest: state.quiz.subtest,
      quiz_id: state.quiz.quiz_id,
      elapsed_sec: elapsed,
      responses,
    }),
  });
  const g = out.graded;
  $("#quizMeta").innerHTML = `${auto ? "Time. " : ""}Score ${g.correct}/${g.total} (${g.percent}%). ${elapsed.toFixed(0)}s elapsed.`;
  document.querySelectorAll(".q").forEach((box) => {
    const id = box.dataset.id;
    const row = g.results.find((r) => r.id === id);
    if (!row) return;
    box.querySelectorAll(".choice").forEach((lab) => {
      const val = lab.querySelector("input").value;
      if (val === row.answer) lab.classList.add("right");
      if (val === row.selected && !row.correct) lab.classList.add("wrong");
    });
    const note = document.createElement("div");
    note.className = "muted";
    note.textContent = (row.correct ? "Correct. " : `Answer ${row.answer}. `) + row.explanation;
    box.appendChild(note);
  });
  const btn = $("#submitQuiz");
  if (btn) btn.remove();
  refreshReady();
}

$("#chatForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = $("#chatInput").value.trim();
  if (!text) return;
  $("#chatInput").value = "";
  state.chat.push({ role: "user", content: text });
  renderChat();
  const res = await api("/api/chat", {
    method: "POST",
    body: JSON.stringify({ messages: state.chat, subtest: $("#coachSub").value || null }),
  });
  state.chat.push({ role: "assistant", content: res.content });
  renderChat();
});

function renderChat() {
  $("#chatLog").innerHTML = state.chat
    .map((m) => `<div class="bubble ${m.role === "user" ? "user" : "bot"}">${escapeHtml(m.content)}</div>`)
    .join("");
  $("#chatLog").scrollTop = $("#chatLog").scrollHeight;
}

function escapeHtml(s) {
  return s.replace(/[&<>]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
}

(async function init() {
  await refreshHealth();
  state.meta = await api("/api/meta");
  fillSelects(state.meta);
  await refreshReady();
  try { await loadStudyPack(); } catch (e) { /* pack loads when Study tab is used */ }
})();
