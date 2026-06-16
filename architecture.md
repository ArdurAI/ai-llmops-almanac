# Architecture: LLMOps Platforms & Workflow Automation

How the llmops platforms & workflow automation landscape is shaped, and how the Quest tests it.

## The landscape at a glance

| Tool | Tier | License | Focus | Notes |
|------|------|---------|-------|-------|
| Dify | A | Modified Apache-2.0 | LLM App Builder | 142K stars; visual workflow, RAG, Agent; most-starred OSS; c |
| Flowise | A | Apache-2.0 | Visual LLM Builder | 54.9K stars; drag-and-drop LLM flows; LangChain-native; self |
| n8n | A | Fair-code | Workflow Automation | 188K stars; 400+ integrations, AI agent nodes; self-hostable |
| Vellum | A | Proprietary | Enterprise Orchestration | McKinsey, Coframe; experimentation, evaluation, deployment;  |
| PromptLayer | A | Proprietary | Prompt Management | Prompt engineering; collaboration, testing, evaluation; no-c |
| Pezzo | A | Open Source | LLMOps Platform | Developer-first; prompt design, version management, troubles |
| Braintrust | A | Proprietary | Evaluation Platform | Notion, Stripe, Vercel; evaluation-driven development; Loop  |
| Zapier | A | Proprietary | Workflow Automation | 7,000+ app integrations; no-code automation; AI steps, Zapie |
| Make | A | Proprietary | Workflow Automation | 1,000+ integrations; visual canvas builder; filters, routers |
| Gumloop | A | Proprietary | AI-Native Automation | ~$60M funding; 130+ nodes; multi-model routing; Skills for a |
| CrewAI | A | Open Source | Multi-Agent Framework | Python-based; multi-agent collaboration; custom pricing; age |
| AutoGen | A | Open Source | Multi-Agent Framework | Microsoft Research; autonomous task execution; self-promptin |
| LangChain | A | MIT | LLM Framework | 134K stars; 1,000+ pre-built integrations; building applicat |
| LangGraph | A | Open Source | Agent Orchestration | LangChain ecosystem; stateful, cyclic multi-agent orchestrat |
| LlamaIndex | A | Open Source | RAG Framework | Broad adoption; connecting LLMs with external data; central  |
| Semantic Kernel | A | MIT | Enterprise SDK | Microsoft ecosystem; process framework for durable agents; P |
| OpenAI Agents SDK | A | Proprietary | Agent Framework | OpenAI ecosystem; lightweight agent building; tools, guardra |
| Mastra | A | Open Source | Agent Framework | Modern stack; TypeScript-first; workflow orchestration, memo |
| Pydantic AI | A | Open Source | Agent Framework | Python developers; type-safe agent development; Pydantic val |
| DSPy | A | Open Source (Stanford) | Pipeline Optimization | Research/enterprise; programmatic prompt optimization; elimi |
| Haystack | A | Open Source (deepset) | Document AI/RAG | Enterprise; document processing, semantic search; deep vecto |
| ZenML | A | Open Source | MLOps Orchestration | ML pipelines; LangChain & LlamaIndex integrations; orchestra |
| Temporal | A | Open Source | Durable Execution | Long-running workflows; automatic retry, state persistence;  |
| Langfuse | A | Open Source (MIT) | Observability | 11K+ stars; tracing, evals, prompt management; self-hostable |
| LangSmith | A | Proprietary (SaaS) | Observability | LangChain ecosystem; LangChain-native tracing, datasets; one |
| MLflow | A | Open Source (Apache-2.0) | MLOps/LLMOps | Linux Foundation; end-to-end GenAI lifecycle; only tool comb |
| Helicone | A | Open Source | API Monitoring | Lightweight; request logging, cost tracking, caching; proxy- |
| Comet Opik | A | Partially Open Source | Observability | Comet ecosystem; eval + tracing; built-in metrics; agent opt |
| AgentOps | A | Open Source | Agent Monitoring | Multi-framework; session replay, time-travel debugging; Crew |
| TruLens | A | Open Source | Evaluation | Free; evaluation auditing; moderate tracing; completely free |
| Lunary | A | Open Source / SaaS | Observability | Chatbot/RAG teams; LLM apps monitoring, prompt management; s |

## How the Quest tests a tool

Same harness for all entries; the judge was frozen before any tool ran:

```
Adapter[frozen CategoryAdapter contract]
  ├── setup()    → install, configure
  ├── load()     → ingest workload
  ├── await_ready() → async barrier
  ├── query()    → run test, get response
  └── teardown() → cleanup, measure
       ↓
Telemetry: latency · tokens · $ · ops notes
       ↓
Grading: deterministic + LLM judge (frozen prompts)
       ↓
Raw results JSON (published)
```

The `await_ready()` barrier is where async designs get their cost measured instead of hidden.

## License

Content is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
