# LangSmith

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Observability
- **License**: Proprietary (SaaS)
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> LangChain ecosystem; LangChain-native tracing, datasets; one-line integration; usage-based

---

## Overview

LangSmith is the official observability and evaluation platform built by LangChain, Inc., designed specifically for teams building with LangChain, LangGraph, and other LLM frameworks. It provides end-to-end tracing, debugging, evaluation, prompt management, and monitoring for LLM applications and agentic workflows. As of 2026, LangSmith has become the de facto standard for serious agentic AI development, with over 250,000 user signups and 25,000 monthly active teams.

The platform captures every step of an LLM pipeline execution as a structured trace, including inputs, outputs, intermediate steps, token usage, latency, and cost. LangSmith's trace tree visualization makes it possible to inspect complex agent runs, identify hallucinations, debug loops, and understand where execution diverges from expected behavior. The platform also includes dataset management, annotation queues for human feedback, online/offline evaluation with LLM-as-judge metrics, and a Prompt Hub for collaborative prompt engineering.

LangSmith is deeply integrated with the LangChain ecosystem but also supports framework-agnostic tracing via its Python and JavaScript SDKs. In 2025, it added OpenTelemetry-compatible trace ingestion, making it interoperable with broader observability stacks. The platform is available as a managed cloud service (US and EU regions) or as a self-hosted Enterprise deployment on Kubernetes.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to first trace | ~2 minutes | Set two env vars, add decorator, run code |
| Dependency count | Direct + transitive | ~15-20 (Python SDK) | Lightweight SDK; UI is cloud-hosted |
| Docker required? | Yes / No | No | For SaaS usage; self-hosted Enterprise requires K8s |
| Language runtime | Required version | Python 3.8+ or Node 18+ | SDKs available for both ecosystems |
| Auth complexity | API key / OAuth / None | API key | Free signup at smith.langchain.com generates key |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | To be measured in Quest smoke gate |

### Setup commands (expected)
```bash
# Install SDK
pip install langsmith

# Set environment variables
export LANGCHAIN_API_KEY="ls-..."
export LANGCHAIN_TRACING_V2="true"

# In your LangChain/LangGraph code, tracing is automatic
# Or use the @traceable decorator for any Python function
from langsmith import traceable

@traceable
def my_function():
    return "hello"
```

For LangGraph apps, simply set `LANGCHAIN_TRACING_V2=true` and all runs are captured automatically. The LangSmith dashboard is available immediately at smith.langchain.com.

### Known sharp edges
- The free Developer tier is strictly limited to 5,000 traces/month and a single seat; exceeding the limit causes traces to be dropped without warning
- 14-day retention on the free tier makes historical debugging impossible for long-running issues
- Self-hosting is exclusively an Enterprise tier add-on; teams cannot self-host without a custom sales agreement
- Extended retention (400 days) costs 9-10x more than base retention ($4.50-$5.00 per 1,000 traces vs $0.50)
- Framework-native integration is strongest with LangChain/LangGraph; teams using other frameworks (CrewAI, AutoGen) may find integration less seamless
- The Agent Builder feature on free tier caps at 1 agent with 50 runs monthly

---

## Benchmark Results

### Standard benchmarks
| Benchmark | Tool Score | Baseline | Published Claim | Verified | Notes |
|-----------|-----------|----------|-----------------|----------|-------|
| ⏳ TBD | | | | | |

### Custom PlatformOps benchmarks
| Dimension | Score (1-10) | Raw Value | Notes |
|-----------|-------------|-----------|-------|
| Accuracy | ⏳ TBD | | |
| Latency | ⏳ TBD | | |
| Token economics | ⏳ TBD | | |
| Scale behavior | ⏳ TBD | | |
| Ops burden | ⏳ TBD | | |
| Developer experience | ⏳ TBD | | |
| Data sovereignty | ⏳ TBD | | |

### Stress suite results
| Stress Test | Result | Notes |
|-------------|--------|-------|
| Contradiction storm | ⏳ TBD | |
| Near-duplicate flood | ⏳ TBD | |
| Concurrent writers | ⏳ TBD | |
| Kill-the-backing-store | ⏳ TBD | |
| Cost-runaway measurement | ⏳ TBD | |

> Raw results JSON: `benchmarks/llmops-platforms-langsmith-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- ⏳ To be researched

### Workarounds documented
- ⏳ To be validated

---

## Comparison with Peers

| Dimension | This Tool | Peer A | Peer B | Notes |
|-----------|-----------|--------|--------|-------|
| Accuracy | ⏳ | ⏳ | ⏳ | |
| Latency | ⏳ | ⏳ | ⏳ | |
| Cost | ⏳ | ⏳ | ⏳ | |
| Ops burden | ⏳ | ⏳ | ⏳ | |
| Scale ceiling | ⏳ | ⏳ | ⏳ | |
| Community | ⏳ | ⏳ | ⏳ | |

---

## Cost Analysis

### Pricing model
- SaaS subscription with per-seat pricing + per-trace overage
- Free Developer tier: 5,000 traces/month, 14-day retention, 1 seat
- Plus tier: $39/seat/month, 10,000 traces included, 400-day retention
- Enterprise: Custom pricing (~$100K+/year typical), self-hosting, unlimited traces, custom SLA

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $117-$390/month | 3-10 seats on Plus; moderate trace volume |
| Medium (10-100 users) | $2,000-$10,000/month | 50+ seats; 500K-1M traces; overage adds up |
| Large (100+ users) | $10,000+/month | Enterprise custom; volume discounts apply |
| Enterprise | Custom | Self-hosted infrastructure + licensing |

### Hidden costs
- Extended retention (400-day) costs 9-10x base rate ($4.50-$5.00 per 1,000 vs $0.50)
- Implementation: 40-80 hours estimated for proper instrumentation ($6,000-$12,000 at $150/hr)
- Export/archival pipeline development: 20-40 hours
- Self-hosted Enterprise requires Kubernetes cluster (16+ vCPUs, 64+ GB RAM) + managed DB services ($950-$1,150/month infrastructure minimum)
- Monitoring setup and ongoing maintenance: 5-10 hours/month

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Partial | Enterprise tier only; requires custom sales agreement |
| Open source | No | Proprietary SaaS; self-hosted is closed-source binary |
| Audit trail | Yes | Full trace logs available; export via API |
| Data residency controls | Yes | US or EU cloud regions (Plus+); Enterprise allows custom |
| On-premise deployment | Yes | Enterprise self-hosted on AWS, GCP, or Azure |
| Export format | JSON, CSV | Full trace data export via API; bulk data export in Plus+ |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Type II | Independently audited |
| GDPR | Yes | EU region available; DPA available on request |
| HIPAA | Yes | Enterprise only; BAA required |
| ISO 27001 | Yes | Certified |
| EU AI Act | Partial | Compliance posture strong; explicit EU AI Act mapping not publicly detailed |
| FedRAMP | TBD | Not publicly listed; Enterprise may support via custom engagement |

---

## Related Tools

### Tier A peers in same category
- [Dify](dify.md)
- [Flowise](flowise.md)
- [n8n](n8n.md)
- [Vellum](vellum.md)
- [PromptLayer](promptlayer.md)
- [Pezzo](pezzo.md)
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)

### Complementary tools
- [LangChain](langchain.md) — Core framework that LangSmith is built to observe
- [LangGraph](langgraph.md) — Graph-based agent orchestration; LangSmith traces LangGraph natively
- [OpenAI](openai-agents-sdk.md) — Model provider commonly traced via LangSmith

### Alternatives to consider
- [Langfuse](langfuse.md) — Open-source alternative with no per-seat pricing; better for data sovereignty
- [Helicone](helicone.md) — Faster proxy-based setup for teams not using LangChain
- [Braintrust](braintrust.md) — Stronger evaluation focus for ML-heavy teams
- [MLflow](mlflow.md) — Better for teams mixing traditional ML and LLM workloads

---

## Links

- Official site: https://smith.langchain.com
- GitHub: https://github.com/langchain-ai/langsmith-sdk
- Documentation: https://docs.smith.langchain.com
- Community / Discord: https://discord.gg/langchain (LangSmith channel)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| | | |

---

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
