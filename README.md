# LLMOps Platforms & Workflow Automation Almanac

A living encyclopedia of LLMOps platforms, workflow automation, and prompt management tools. Updated **monthly** with fresh repo metadata, releases, landscape shifts, and independent benchmark results from the *"Platform Engineer's Quest for the Best"* series.

> Vendors publish their own benchmark numbers. Nobody reproduces them independently, and nobody evaluates tools the way a platform engineer has to live with them: ops burden, failure modes, scale curves, and cost. This almanac is the public record of that work.

**53 tools** — **Tier A**: 31 · **Tier B**: 22

## Tool Catalogue

Every tool below has a full deep-dive page in [`tools/`](tools/). Sorted by tier (A → B → C), then alphabetically.

| Tool | Type | License | Stars | Tier | Description | Detail |
|------|------|---------|-------|------|-------------|--------|
| **AgentOps** | Agent Monitoring | Open Source | — | A | Multi-framework; session replay, time-travel debugging; CrewAI, AutoGen, LangChain SDK | [`agentops.md`](tools/agentops.md) |
| **AutoGen** | Multi-Agent Framework | Open Source | — | A | AutoGen is a multi-agent conversational AI framework created by Microsoft Research in September 2023. It pioneered the paradigm of enabling… | [`autogen.md`](tools/autogen.md) |
| **Braintrust** | Evaluation Platform | Proprietary | — | A | Notion, Stripe, Vercel, Coursera, Dropbox, Zapier, Perplexity, Ramp, Replit; evaluation-driven development; Loop AI agent; 20+ native SDK… | [`braintrust.md`](tools/braintrust.md) |
| **Comet Opik** | Observability | Partially Open Source | — | A | Comet ecosystem; eval + tracing; built-in metrics; agent optimizer SDK; free + enterprise | [`comet-opik.md`](tools/comet-opik.md) |
| **CrewAI** | Multi-Agent Framework | Open Source | — | A | Python-based; multi-agent collaboration; 45,900+ GitHub stars; open-source (MIT); CrewAI AMP managed platform; customers include PwC, IBM, NVIDIA,… | [`crewai.md`](tools/crewai.md) |
| **Dify** | LLM App Builder | Modified Apache-2.0 | 142K | A | 142K stars; visual workflow, RAG, Agent; most-starred OSS; commercial restrictions on multi-tenant SaaS | [`dify.md`](tools/dify.md) |
| **DSPy** | Pipeline Optimization | MIT (Open Source, Stanford) | — | A | Research/enterprise; programmatic prompt optimization; eliminates manual prompt engineering | [`dspy.md`](tools/dspy.md) |
| **Flowise** | Visual LLM Builder | Apache-2.0 | 54.9K | A | 54.9K stars; drag-and-drop LLM flows; LangChain-native; self-hostable; owned by Workday | [`flowise.md`](tools/flowise.md) |
| **Gumloop** | AI-Native Automation | Proprietary | — | A | ~$70M funding ($50M Series B led by Benchmark, Mar 2026); 130+ nodes; multi-model routing; YC W24; SOC 2 Type II, GDPR; customers include Shopify,… | [`gumloop.md`](tools/gumloop.md) |
| **Haystack** | Document AI / RAG | Apache 2.0 (Open Source, deepset) | — | A | Enterprise; document processing, semantic search; deep vector DB integration; deepset Cloud | [`haystack.md`](tools/haystack.md) |
| **Helicone** | API Monitoring | Open Source | — | A | Lightweight; request logging, cost tracking, caching; proxy-based; zero-code integration | [`helicone.md`](tools/helicone.md) |
| **LangChain** | LLM Framework | MIT | 134K+ | A | 134K+ stars; 1,000+ pre-built integrations; building applications with LLMs via Python and JavaScript | [`langchain.md`](tools/langchain.md) |
| **Langfuse** | Observability | MIT (Open Source) | 16K+ | A | 16K+ stars; tracing, evals, prompt management; self-hostable; acquired by ClickHouse Jan 2026 | [`langfuse.md`](tools/langfuse.md) |
| **LangGraph** | Agent Orchestration | Open Source | 24,800 | A | LangChain ecosystem; stateful, cyclic multi-agent orchestration; Deep Agents for long-running workflows | [`langgraph.md`](tools/langgraph.md) |
| **LangSmith** | Observability | Proprietary (SaaS) | — | A | LangChain ecosystem; LangChain-native tracing, datasets; one-line integration; usage-based | [`langsmith.md`](tools/langsmith.md) |
| **LlamaIndex** | RAG Framework | Open Source (MIT) | 40K+ | A | Broad adoption; connecting LLMs with external data; central interface for data + LLM; 40K+ GitHub stars | [`llamaindex.md`](tools/llamaindex.md) |
| **Lunary** | Observability | Open Source / SaaS | — | A | Chatbot/RAG teams; LLM apps monitoring, prompt management; self-hostable; EU data center | [`lunary.md`](tools/lunary.md) |
| **Make** | Workflow Automation | Proprietary | — | A | 1,000+ integrations (3,000+ apps); visual canvas builder; filters, routers, iterators; error handling; AI agents; credit-based pricing; SOC 2 Type… | [`make.md`](tools/make.md) |
| **Mastra** | Agent Framework | Apache 2.0 (core); Mastra Enterprise License (ee/) | 24,600 | A | Modern TypeScript-first stack; workflow orchestration, memory, evals; built by the Gatsby team (YC W25) | [`mastra.md`](tools/mastra.md) |
| **MLflow** | MLOps/LLMOps | Open Source (Apache-2.0) | — | A | Linux Foundation; end-to-end GenAI lifecycle; only tool combining open-source, deep agent tracing | [`mlflow.md`](tools/mlflow.md) |
| **n8n** | Workflow Automation | Fair-code | 188K | A | 188K stars; 400+ integrations, AI agent nodes; self-hostable; Germany-based; EU-friendly | [`n8n.md`](tools/n8n.md) |
| **OpenAI Agents SDK** | Agent Framework | MIT (Open Source) | 19,000 | A | OpenAI ecosystem; lightweight agent building; tools, guardrails, handoffs; released March 2025 | [`openai-agents-sdk.md`](tools/openai-agents-sdk.md) |
| **Pezzo** | LLMOps Platform | Open Source | — | A | Developer-first; prompt design, version management, troubleshooting; two lines of code | [`pezzo.md`](tools/pezzo.md) |
| **PromptLayer** | Prompt Management | Proprietary | — | A | Prompt engineering; collaboration, testing, evaluation; no-code editor for non-technical | [`promptlayer.md`](tools/promptlayer.md) |
| **Pydantic AI** | Agent Framework | MIT (Open Source) | — | A | Python developers; type-safe agent development; Pydantic validation; FastAPI integration | [`pydantic-ai.md`](tools/pydantic-ai.md) |
| **Semantic Kernel** | Enterprise SDK | MIT | 27,000 | A | Microsoft ecosystem; process framework for durable agents; Python, C#, Java; Azure AI Foundry | [`semantic-kernel.md`](tools/semantic-kernel.md) |
| **Temporal** | Durable Execution | MIT (Open Source) | — | A | Long-running workflows; automatic retry, state persistence; production-grade for agents; Go-based | [`temporal.md`](tools/temporal.md) |
| **TruLens** | Evaluation | Open Source | — | A | Free; evaluation auditing; moderate tracing; completely free | [`trulens.md`](tools/trulens.md) |
| **Vellum** | Enterprise Orchestration | Proprietary | — | A | McKinsey, Coframe; experimentation, evaluation, deployment; A/B testing; SOC 2; 99.998% uptime | [`vellum.md`](tools/vellum.md) |
| **Zapier** | Workflow Automation | Proprietary | — | A | 7,000+ app integrations; no-code automation; AI steps, Zapier Agents, Tables, Interfaces; 3M+ users; 69% of Fortune 1000; SOC 2 Type II, SOC 3,… | [`zapier.md`](tools/zapier.md) |
| **ZenML** | MLOps Orchestration | Apache 2.0 (Open Source) | — | A | ML pipelines; LangChain & LlamaIndex integrations; orchestrating, experimenting, deploying | [`zenml.md`](tools/zenml.md) |
| **Adaline** | Prompt Management | Proprietary | — | B | Production teams; end-to-end prompt lifecycle; versioning, testing, deployment, monitoring | [`adaline.md`](tools/adaline.md) |
| **BISHENG** | Enterprise Platform | Open Source | — | B | China; 'Proudly made by Chinese'; Fortune 500 deployments; open-source alternative to Dify | [`bisheng.md`](tools/bisheng.md) |
| **Botpress** | Conversational | Open Source | — | B | Open-source dialog + LLM; modular; community extensible | [`botpress.md`](tools/botpress.md) |
| **Confident AI** | Prompt Management | Proprietary | — | B | Git-based; branching, commit, approval workflows; only platform with git-style branching | [`confident-ai.md`](tools/confident-ai.md) |
| **Coze** | No-code | Proprietary | — | B | ByteDance; 100K+ bots; zero-code Bot builder; Doubao model; multi-channel publish | [`coze.md`](tools/coze.md) |
| **FastGPT** | RAG Platform | Open Source | — | B | China; RAG-focused; knowledge base QA; workflow orchestration | [`fastgpt.md`](tools/fastgpt.md) |
| **Future AGI** | Evals + Guardrails | Open Source (Apache-2.0) | — | B | Enterprise; 50+ eval agents, 18 guardrails; text + voice simulation; traceAI library | [`future-agi.md`](tools/future-agi.md) |
| **HoneyHive** | Agent Monitoring | Proprietary | — | B | Production agents; flexible deployment (SaaS, hybrid, self-hosted); agent lifecycle monitoring | [`honeyhive.md`](tools/honeyhive.md) |
| **Humanloop** | Prompt Management | Proprietary | — | B | Prompt editing; polished editing experience; narrower observability; no span-level tracing | [`humanloop.md`](tools/humanloop.md) |
| **Langdock** | LLMOps Platform | Proprietary | — | B | Europe; enterprise LLM platform; compliance-focused; EU AI Act ready | [`langdock.md`](tools/langdock.md) |
| **Langflow** | Visual LLM Builder | Open Source | — | B | Active community; prototype LangChain flows; drag-and-drop components + chat interface | [`langflow.md`](tools/langflow.md) |
| **LangWatch** | Observability | Open Source | — | B | DSPy integration; agent testing, simulation; synthetic conversation testing; voice agent testing | [`langwatch.md`](tools/langwatch.md) |
| **Literal AI** | Observability | Proprietary | — | B | Multi-modal; LLM observability + evaluation; prompt templates, versioned deploys, human feedback | [`literal-ai.md`](tools/literal-ai.md) |
| **Maxim AI** | Compliance | Proprietary | — | B | Enterprise; SOC2/HIPAA-ready observability; drift detection, audit trails, auto-remediation | [`maxim-ai.md`](tools/maxim-ai.md) |
| **OpenLIT** | Observability | Open Source | — | B | OpenTelemetry-native; GenAI + LLM auto-instrumentation; token & cost usage; monitoring LLMs, VectorDBs | [`openlit.md`](tools/openlit.md) |
| **Orq.ai** | LLMOps Platform | Proprietary | — | B | Europe; LLM app development platform; experiment, evaluate, deploy | [`orqai.md`](tools/orqai.md) |
| **Parea AI** | Prompt Engineering | Proprietary | — | B | AI Engineers; LLM evaluation, observability, prompt playground; version-controlled enhanced prompt | [`parea-ai.md`](tools/parea-ai.md) |
| **Promptfoo** | Prompt Testing | Open Source | — | B | CI/CD; regression tests, prompt quality; open-source tool for testing & evaluating; CLI and CI/CD | [`promptfoo.md`](tools/promptfoo.md) |
| **PromptHub** | Prompt Management | Proprietary | — | B | Git-like workflow; versioning, branching, reviews; code-review workflow for prompts | [`prompthub.md`](tools/prompthub.md) |
| **RAGflow** | RAG Engine | Open Source | 80.7K+ | B | 80.7K+ stars; deep document understanding; complex PDF/table parsing; dedicated RAG backend | [`ragflow.md`](tools/ragflow.md) |
| **Relevance AI** | No-code | Proprietary | — | B | Drag-and-drop; zero coding; non-technical users | [`relevance-ai.md`](tools/relevance-ai.md) |
| **Voiceflow** | No-code | Proprietary | — | B | Visual agent builder; voice + chat; enterprise teams | [`voiceflow.md`](tools/voiceflow.md) |

## Tool Categories

### AI-Native Automation (1)
**Gumloop**

### API Monitoring (1)
**Helicone**

### Agent Framework (3)
**Mastra** · **OpenAI Agents SDK** · **Pydantic AI**

### Agent Monitoring (2)
**AgentOps** · **HoneyHive**

### Agent Orchestration (1)
**LangGraph**

### Compliance (1)
**Maxim AI**

### Conversational (1)
**Botpress**

### Document AI / RAG (1)
**Haystack**

### Durable Execution (1)
**Temporal**

### Enterprise Orchestration (1)
**Vellum**

### Enterprise Platform (1)
**BISHENG**

### Enterprise SDK (1)
**Semantic Kernel**

### Evals + Guardrails (1)
**Future AGI**

### Evaluation (1)
**TruLens**

### Evaluation Platform (1)
**Braintrust**

### LLM App Builder (1)
**Dify**

### LLM Framework (1)
**LangChain**

### LLMOps Platform (3)
**Langdock** · **Orq.ai** · **Pezzo**

### MLOps Orchestration (1)
**ZenML**

### MLOps/LLMOps (1)
**MLflow**

### Multi-Agent Framework (2)
**AutoGen** · **CrewAI**

### No-code (3)
**Coze** · **Relevance AI** · **Voiceflow**

### Observability (7)
**Comet Opik** · **Langfuse** · **LangSmith** · **LangWatch** · **Literal AI** · **Lunary** · **OpenLIT**

### Pipeline Optimization (1)
**DSPy**

### Prompt Engineering (1)
**Parea AI**

### Prompt Management (5)
**Adaline** · **Confident AI** · **Humanloop** · **PromptHub** · **PromptLayer**

### Prompt Testing (1)
**Promptfoo**

### RAG Engine (1)
**RAGflow**

### RAG Framework (1)
**LlamaIndex**

### RAG Platform (1)
**FastGPT**

### Visual LLM Builder (2)
**Flowise** · **Langflow**

### Workflow Automation (3)
**Make** · **n8n** · **Zapier**

## Quick Start

```bash
git clone https://github.com/ArdurAI/ai-llmops-almanac.git
cd ai-llmops-almanac
```

| You want… | Go to |
|-----------|-------|
| The state of the landscape right now | The latest file in [`editions/`](editions/) |
| Everything we know about one tool | [`tools/<name>.md`](tools/) |
| Machine-readable roster + metadata | [`data/`](data/) |
| Architecture diagrams | [`architecture.md`](architecture.md) |
| Benchmark results (rolling) | [`benchmarks/`](benchmarks/) |
| How tools are tested and ranked | [`methodology/benchmark-harness.md`](methodology/benchmark-harness.md) |
| Project intent & philosophy | [`INTENT.md`](INTENT.md) |
| Implementation guide | [`IMPLEMENTATION.md`](IMPLEMENTATION.md) |
| Testing methodology | [`TESTING.md`](TESTING.md) |
| Troubleshooting | [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) |

## Methodology

Results published here come from a frozen-before-results harness. Full details in [`methodology/benchmark-harness.md`](methodology/benchmark-harness.md):

- Standard benchmarks for comparability with published claims — every ranking ships a *published vs. reproduced* table.
- A custom **PlatformOps** benchmark: testing on infrastructure work — setup, reliability, scale, cost.
- A stress suite: contradiction storms, near-duplicate floods, concurrent writers, kill-the-backing-store chaos, cost-runaway measurement.
- Seven scored dimensions: accuracy, latency, token economics, scale behavior, **ops burden**, developer experience, data sovereignty.

The judge model, prompts (SHA-256-frozen), and control variables were fixed before any tool ran. Raw results JSON is published with every ranking.

## Contributing

We welcome contributions — new tools, data fixes, ranking challenges, and benchmark reproductions. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on how to add a tool, fix data, or challenge a ranking.

## Recent Edition

📖 **[Read the latest edition →](editions/2026-07.md)**

One edition per month under `editions/YYYY-MM.md`: refreshed metadata, notable releases, new entrants triaged in or out, and a diary of what was tested.

---

## License

Content is licensed **CC BY 4.0** — share and adapt with attribution to **ArdurAI**.

---

**Authored by Team Ardur · CC BY 4.0**
