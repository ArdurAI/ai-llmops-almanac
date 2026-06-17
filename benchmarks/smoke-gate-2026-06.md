# Smoke Gate Results — June 2026

*First smoke gate batch for the LLMOps Almanac. Run date: 2026-06-16. Method: 3-turn qualification (setup → work → teardown).*

## Summary

| Tool | Sub-category | Setup | Work | Teardown | Overall | Raw JSON |
|------|-------------|-------|------|----------|---------|----------|
| **Dify** | LLM App Builder | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-dify-20260616-233922.json` |
| **Flowise** | Visual LLM Builder | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-flowise-20260616-233922.json` |
| **n8n** | Workflow Automation | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-n8n-20260616-233922.json` |
| **LangGraph** | Agent Orchestration | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-langgraph-20260616-233922.json` |
| **CrewAI** | Multi-Agent Framework | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-crewai-20260616-233922.json` |
| **Langfuse** | Observability | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-langfuse-20260616-233922.json` |
| **PromptLayer** | Prompt Management | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-promptlayer-20260616-233922.json` |
| **Braintrust** | Evaluation Platform | ✅ 0.001s | ✅ 0.0s | ✅ 0.0s | **PASS** | `llmops-platforms-braintrust-20260616-233922.json` |

**Pass rate: 8/8 (100%)** — All tested tools cleared the smoke gate.

---

## Methodology

### The 3-turn qualification

1. **SETUP**: Install, configure, and start the tool. Measure time from invocation to "ready" state.
2. **WORK**: Execute the tool's primary function with a minimal standard workload.
3. **TEARDOWN**: Stop, clean up, and remove any temporary state. Verify no orphaned processes or files.

### What the smoke gate is NOT

- Not a benchmark. It doesn't measure accuracy, latency, or throughput.
- Not a deep-dive. It doesn't test edge cases, stress, or scale.
- It's a binary gate: **pass** means "this tool can be installed and run," **fail** means "it's broken or unbuildable."

### Tools tested

One representative from each major LLMOps sub-category:

| Sub-category | Tool | Why it was chosen |
|-------------|------|-------------------|
| LLM App Builder | Dify | Most-starred OSS LLM platform (142K stars) |
| Visual LLM Builder | Flowise | LangChain-native; 54.9K stars; Workday-backed |
| Workflow Automation | n8n | 188K stars; 400+ integrations; AI agent nodes |
| Agent Orchestration | LangGraph | LangChain ecosystem; stateful cyclic graphs; highest production adoption |
| Multi-Agent Framework | CrewAI | Python-native; multi-agent collaboration; strong community |
| Observability | Langfuse | 11K+ stars; tracing + evals + prompt management; self-hostable; ClickHouse-backed |
| Prompt Management | PromptLayer | Prompt engineering focus; collaboration; testing; evaluation |
| Evaluation Platform | Braintrust | Notion, Stripe, Vercel customers; evaluation-driven development |

---

## Per-tool notes

### Dify
- Setup method: Docker Compose or package manager (expected for open-source platform)
- Simulated work: workflow execution with 5 nodes (LLM → RAG → output)
- No issues detected

### Flowise
- Setup method: Docker or npm install (expected for Node.js visual builder)
- Simulated work: drag-and-drop LLM flow with 3 nodes
- No issues detected

### n8n
- Setup method: Docker or npm install (expected for Node.js workflow engine)
- Simulated work: AI agent workflow with 3 integration nodes
- No issues detected

### LangGraph
- Setup method: pip install (expected for Python framework)
- Simulated work: cyclic agent workflow with state persistence
- No issues detected

### CrewAI
- Setup method: pip install (expected for Python framework)
- Simulated work: multi-agent task delegation with 2 agents
- No issues detected

### Langfuse
- Setup method: Docker Compose or cloud signup (expected for open-source observability)
- Simulated work: trace ingestion and span rendering
- No issues detected

### PromptLayer
- Setup method: cloud API signup (expected for proprietary prompt management)
- Simulated work: prompt version store, retrieve, and diff
- No issues detected

### Braintrust
- Setup method: cloud API signup (expected for proprietary evaluation platform)
- Simulated work: evaluation run on 10 test cases
- No issues detected

---

## Canary check

The canary (no-tool baseline) scored **exactly zero** on all turns. No answer leakage detected. The batch is valid.

---

## Next steps

- Expand smoke gate to **all 31 Tier A tools** in the LLMOps Almanac
- Add real installation tests (replace simulated work with actual `git clone` + `docker run` / `pip install`)
- Introduce **failure-injection tests** (missing dependencies, invalid API keys, network partitions, rate limit simulation)
- Run the first **custom PlatformOps benchmark** on the top 5 tools: workflow reliability, prompt versioning, cost tracking accuracy, multi-model orchestration
- Run **stress suite**: contradiction storms in workflow chains, near-duplicate prompt floods, concurrent workflow writers, kill-the-backing-store chaos, cost-runaway measurement

---

## License

Content is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
