import { useState, useRef } from "react";

const STAGES = ["router", "planner", "search", "researcher", "reviewer", "writer"];

const EXAMPLES = [
  "Compare FastAPI vs Django for production APIs",
  "What is retrieval augmented generation?",
  "LangGraph vs CrewAI for agentic workflows",
  "Rust vs Go for systems programming",
];

const styles = {
  root: {
    fontFamily: "'DM Mono', monospace",
    background: "#0e1117",
    minHeight: "100vh",
    color: "#c9cdd8",
    padding: "0",
  },
  wrap: {
    maxWidth: 780,
    margin: "0 auto",
    padding: "48px 24px 80px",
  },
  header: {
    marginBottom: 40,
  },
  title: {
    fontSize: 20,
    fontWeight: 600,
    color: "#e8eaf0",
    letterSpacing: "-0.3px",
    margin: 0,
    display: "flex",
    alignItems: "center",
    gap: 10,
  },
  titleDot: {
    width: 8,
    height: 8,
    borderRadius: "50%",
    background: "#4f8ef7",
    display: "inline-block",
  },
  subtitle: {
    fontSize: 12,
    color: "#4a5068",
    marginTop: 6,
    letterSpacing: "0.4px",
  },
  pipeline: {
    display: "flex",
    alignItems: "center",
    gap: 6,
    padding: "10px 16px",
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 8,
    marginBottom: 28,
    overflowX: "auto",
    scrollbarWidth: "none",
  },
  stageBase: {
    fontSize: 11,
    padding: "3px 8px",
    borderRadius: 4,
    border: "1px solid transparent",
    whiteSpace: "nowrap",
    flexShrink: 0,
    transition: "all 0.25s",
    color: "#3a3f55",
  },
  stageActive: {
    color: "#4f8ef7",
    background: "rgba(79,142,247,0.08)",
    borderColor: "rgba(79,142,247,0.2)",
  },
  stageDone: {
    color: "#3ecf8e",
  },
  stageSep: {
    color: "#1e2234",
    fontSize: 12,
    flexShrink: 0,
  },

  textarea: {
    width: "100%",
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 10,
    color: "#e8eaf0",
    fontFamily: "'DM Mono', monospace",
    fontSize: 14,
    padding: "14px 16px",
    resize: "none",
    outline: "none",
    lineHeight: 1.6,
    minHeight: 96,
    boxSizing: "border-box",
    transition: "border-color 0.2s",
  },
  submitRow: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    marginTop: 10,
  },
  examples: {
    display: "flex",
    flexWrap: "wrap",
    gap: 6,
  },
  exPill: {
    fontSize: 11,
    padding: "4px 10px",
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 20,
    color: "#3a3f55",
    cursor: "pointer",
    transition: "all 0.15s",
    fontFamily: "'DM Mono', monospace",
  },
  btn: {
    display: "flex",
    alignItems: "center",
    gap: 6,
    padding: "8px 18px",
    background: "#4f8ef7",
    border: "none",
    borderRadius: 7,
    color: "#fff",
    fontFamily: "'DM Mono', monospace",
    fontSize: 13,
    fontWeight: 600,
    cursor: "pointer",
    letterSpacing: "0.2px",
    transition: "opacity 0.15s",
  },
  loader: {
    display: "flex",
    alignItems: "center",
    gap: 12,
    padding: "16px 18px",
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 10,
    marginTop: 20,
  },
  loaderDots: {
    display: "flex",
    gap: 5,
  },
  loaderLabel: {
    fontSize: 12,
    color: "#4a5068",
  },
  errorBox: {
    display: "flex",
    gap: 10,
    padding: "14px 16px",
    background: "rgba(240,82,82,0.06)",
    border: "1px solid rgba(240,82,82,0.18)",
    borderRadius: 8,
    marginTop: 20,
    fontSize: 12,
    color: "#f05252",
    lineHeight: 1.5,
  },
  metaRow: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: 10,
    marginTop: 24,
    marginBottom: 14,
  },
  metaCard: {
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 8,
    padding: "10px 14px",
  },
  metaLabel: {
    fontSize: 10,
    color: "#3a3f55",
    textTransform: "uppercase",
    letterSpacing: "0.7px",
    marginBottom: 5,
  },
  metaValue: {
    fontSize: 13,
    color: "#e8eaf0",
    fontWeight: 600,
    overflow: "hidden",
    textOverflow: "ellipsis",
    whiteSpace: "nowrap",
  },
  badgeQuick: {
    display: "inline-block",
    padding: "2px 8px",
    background: "rgba(62,207,142,0.1)",
    border: "1px solid rgba(62,207,142,0.2)",
    borderRadius: 4,
    color: "#3ecf8e",
    fontSize: 11,
  },
  badgeDeep: {
    display: "inline-block",
    padding: "2px 8px",
    background: "rgba(79,142,247,0.1)",
    border: "1px solid rgba(79,142,247,0.2)",
    borderRadius: 4,
    color: "#4f8ef7",
    fontSize: 11,
  },
  reportCard: {
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 10,
    overflow: "hidden",
  },
  reportHeader: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    padding: "10px 16px",
    borderBottom: "1px solid #1e2234",
    background: "#0e1117",
  },
  reportHeaderLabel: {
    fontSize: 11,
    color: "#3a3f55",
    textTransform: "uppercase",
    letterSpacing: "0.6px",
  },
  copyBtn: {
    fontSize: 11,
    padding: "3px 10px",
    background: "transparent",
    border: "1px solid #1e2234",
    borderRadius: 5,
    color: "#3a3f55",
    cursor: "pointer",
    fontFamily: "'DM Mono', monospace",
    transition: "all 0.15s",
  },
  reportBody: {
    padding: "20px 22px",
    maxHeight: 500,
    overflowY: "auto",
    fontSize: 13,
    lineHeight: 1.85,
    whiteSpace: "pre-wrap",
    color: "#c9cdd8",
  },
  historySection: {
    marginTop: 40,
    borderTop: "1px solid #1e2234",
    paddingTop: 28,
  },
  sectionLabel: {
    fontSize: 10,
    color: "#3a3f55",
    textTransform: "uppercase",
    letterSpacing: "0.8px",
    marginBottom: 12,
  },
  histItem: {
    display: "flex",
    alignItems: "flex-start",
    gap: 10,
    padding: "10px 14px",
    background: "#13161e",
    border: "1px solid #1e2234",
    borderRadius: 8,
    marginBottom: 8,
    cursor: "pointer",
    transition: "border-color 0.15s",
  },
  histBadge: (c) => ({
    fontSize: 10,
    fontWeight: 700,
    padding: "3px 7px",
    borderRadius: 4,
    flexShrink: 0,
    background: c === "quick" ? "rgba(62,207,142,0.1)" : "rgba(79,142,247,0.1)",
    color: c === "quick" ? "#3ecf8e" : "#4f8ef7",
  }),
  histQuery: {
    fontSize: 12,
    color: "#c9cdd8",
    flex: 1,
    lineHeight: 1.4,
  },
  histTs: {
    fontSize: 11,
    color: "#3a3f55",
    whiteSpace: "nowrap",
    flexShrink: 0,
  },
};

const STAGE_LABELS = {
  router: "Routing query…",
  planner: "Planning research tasks…",
  search: "Searching the web…",
  researcher: "Analysing findings…",
  reviewer: "Reviewing quality…",
  writer: "Writing final report…",
};

function Dot({ active }) {
  return (
    <span
      style={{
        display: "inline-block",
        width: 7,
        height: 7,
        borderRadius: "50%",
        background: active ? "#4f8ef7" : "currentColor",
        animation: active ? "pulse 1s infinite" : "none",
        marginRight: 5,
      }}
    />
  );
}

export default function ResearchAgent() {
  const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [activeStage, setActiveStage] = useState(null);
  const [doneStages, setDoneStages] = useState([]);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [history, setHistory] = useState([]);
  const [copyLabel, setCopyLabel] = useState("copy");
  const intervalRef = useRef(null);

  function startPipelineAnim() {
    let i = 0;
    setActiveStage(STAGES[0]);
    setDoneStages([]);
    intervalRef.current = setInterval(() => {
      i++;
      if (i >= STAGES.length) {
        clearInterval(intervalRef.current);
        return;
      }
      setDoneStages((prev) => [...prev, STAGES[i - 1]]);
      setActiveStage(STAGES[i]);
    }, 1800);
  }

  function stopPipeline(success) {
    clearInterval(intervalRef.current);
    if (success) {
      setDoneStages([...STAGES]);
      setActiveStage(null);
    } else {
      setActiveStage(null);
      setDoneStages([]);
    }
  }

  async function runResearch() {
    if (!query.trim() || loading) return;
    setLoading(true);
    setError(null);
    setResult(null);
    startPipelineAnim();
    const t0 = Date.now();
    try {
      const res = await fetch(`${API_URL.replace(/\/$/, "")}/research`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      if (data.error) throw new Error(data.error);
      const elapsed = ((Date.now() - t0) / 1000).toFixed(1);
      stopPipeline(true);
      const entry = { ...data, elapsed, ts: new Date() };
      setResult(entry);
      setHistory((h) => [entry, ...h].slice(0, 8));
    } catch (e) {
      stopPipeline(false);
      setError(e.message || "Request failed. Is the FastAPI server running?");
    }
    setLoading(false);
  }

  async function copyReport() {
    if (!result?.final_report) return;
    await navigator.clipboard.writeText(result.final_report).catch(() => {});
    setCopyLabel("copied!");
    setTimeout(() => setCopyLabel("copy"), 2000);
  }

  function getStageStyle(stage) {
    if (doneStages.includes(stage)) return { ...styles.stageBase, ...styles.stageDone };
    if (activeStage === stage) return { ...styles.stageBase, ...styles.stageActive };
    return styles.stageBase;
  }

  return (
    <>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&display=swap');
        * { box-sizing: border-box; }
        body { margin: 0; }
        textarea:focus { border-color: #4f8ef7 !important; }
        input:focus { border-color: #4f8ef7 !important; }
        @keyframes pulse { 0%,100%{opacity:0.4} 50%{opacity:1} }
        @keyframes bounce { 0%,60%,100%{transform:translateY(0);opacity:0.4} 30%{transform:translateY(-5px);opacity:1} }
        ::-webkit-scrollbar { width: 4px; } 
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #1e2234; border-radius: 2px; }
      `}</style>
      <div style={styles.root}>
        <div style={styles.wrap}>

          <div style={styles.header}>
            <h1 style={styles.title}>
              <span style={styles.titleDot} />
              Research Agent
            </h1>
            <p style={styles.subtitle}>langgraph · groq llama-3.3-70b · duckduckgo</p>
          </div>

          <div style={styles.pipeline}>
            {STAGES.map((s, i) => (
              <span key={s} style={{ display: "flex", alignItems: "center", gap: 6 }}>
                <span style={getStageStyle(s)}>
                  <Dot active={activeStage === s} />
                  {s}
                </span>
                {i < STAGES.length - 1 && <span style={styles.stageSep}>›</span>}
              </span>
            ))}
          </div>

          <textarea
            style={styles.textarea}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) runResearch(); }}
            placeholder='Ask anything — e.g. "Compare FastAPI vs Django for production APIs"'
            rows={3}
          />

          <div style={styles.submitRow}>
            <div style={styles.examples}>
              {EXAMPLES.map((ex) => (
                <span
                  key={ex}
                  style={styles.exPill}
                  onClick={() => setQuery(ex)}
                  onMouseEnter={(e) => { e.target.style.color = "#4f8ef7"; e.target.style.borderColor = "rgba(79,142,247,0.3)"; }}
                  onMouseLeave={(e) => { e.target.style.color = "#3a3f55"; e.target.style.borderColor = "#1e2234"; }}
                >
                  {ex.length > 28 ? ex.slice(0, 28) + "…" : ex}
                </span>
              ))}
            </div>
            <button
              style={{ ...styles.btn, opacity: loading || !query.trim() ? 0.45 : 1 }}
              onClick={runResearch}
              disabled={loading || !query.trim()}
            >
              {loading ? (
                <span style={{ display: "inline-block", width: 12, height: 12, border: "2px solid rgba(255,255,255,0.3)", borderTopColor: "#fff", borderRadius: "50%", animation: "spin 0.7s linear infinite" }} />
              ) : (
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              )}
              {loading ? "Running…" : "Run"}
            </button>
          </div>

          {loading && (
            <div style={styles.loader}>
              <div style={styles.loaderDots}>
                {[0, 1, 2].map((i) => (
                  <span key={i} style={{ display: "inline-block", width: 6, height: 6, borderRadius: "50%", background: "#4f8ef7", animation: `bounce 1.2s ${i * 0.2}s infinite` }} />
                ))}
              </div>
              <span style={styles.loaderLabel}>
                {activeStage ? STAGE_LABELS[activeStage] : "Processing…"}
              </span>
            </div>
          )}

          {error && (
            <div style={styles.errorBox}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{ flexShrink: 0, marginTop: 1 }}><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
              {error}
            </div>
          )}

          {result && (
            <>
              <div style={styles.metaRow}>
                <div style={styles.metaCard}>
                  <div style={styles.metaLabel}>Query</div>
                  <div style={styles.metaValue} title={result.query}>{result.query}</div>
                </div>
                <div style={styles.metaCard}>
                  <div style={styles.metaLabel}>Complexity</div>
                  <div style={result.complexity === "quick" ? styles.badgeQuick : styles.badgeDeep}>
                    {result.complexity}
                  </div>
                </div>
                <div style={styles.metaCard}>
                  <div style={styles.metaLabel}>Duration</div>
                  <div style={styles.metaValue}>{result.elapsed}s</div>
                </div>
              </div>

              <div style={styles.reportCard}>
                <div style={styles.reportHeader}>
                  <span style={styles.reportHeaderLabel}>report</span>
                  <button style={styles.copyBtn} onClick={copyReport}>{copyLabel}</button>
                </div>
                <div style={styles.reportBody}>{result.final_report}</div>
              </div>
            </>
          )}

          {history.length > 0 && (
            <div style={styles.historySection}>
              <div style={styles.sectionLabel}>History</div>
              {history.map((h, i) => (
                <div
                  key={i}
                  style={styles.histItem}
                  onClick={() => setResult(h)}
                  onMouseEnter={(e) => e.currentTarget.style.borderColor = "#2e3450"}
                  onMouseLeave={(e) => e.currentTarget.style.borderColor = "#1e2234"}
                >
                  <span style={styles.histBadge(h.complexity)}>{h.complexity === "quick" ? "Q" : "D"}</span>
                  <span style={styles.histQuery}>{h.query}</span>
                  <span style={styles.histTs}>{h.elapsed}s · {h.ts.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}</span>
                </div>
              ))}
            </div>
          )}

        </div>
      </div>
      <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
    </>
  );
}
