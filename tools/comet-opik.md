# Comet Opik

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Observability
- **License**: Partially Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Comet ecosystem; eval + tracing; built-in metrics; agent optimizer SDK; free + enterprise

---

## Overview

Opik (built by Comet ML) is an open-source LLM evaluation and observability platform released under the Apache 2.0 license. It provides comprehensive tracing, automated evaluations, production monitoring, and prompt management for LLM applications, RAG systems, and agentic workflows. The platform is designed to cover the full lifecycle from development debugging through production monitoring, with both a managed cloud version and self-hosted deployment via Docker Compose or Kubernetes.

Opik differentiates itself through its deep evaluation toolkit, including 20+ built-in LLM-as-a-judge metrics for hallucination detection, RAG quality assessment, and agent-specific scoring. It also includes an Agent Optimization SDK with Bayesian optimization algorithms for tuning prompts and tool selection, and Guardrails for toxicity, PII, and custom policy enforcement. The platform handles 40+ million traces per day at production scale and supports multimodal logging (images, video, audio).

As part of the Comet ecosystem, Opik connects to Comet ML's broader experiment tracking platform, giving teams a unified view across traditional ML and LLM workloads. However, Opik can be used entirely independently of Comet. It integrates with 60+ tools including OpenAI, Anthropic, LangChain, LangGraph, CrewAI, LlamaIndex, DSPy, and LiteLLM, with SDKs for Python and TypeScript. The platform has 5,000+ GitHub stars (with some sources citing 18,000+ across the broader Comet ecosystem) and is actively maintained by a team with deep roots in ML experiment tracking.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to first trace | ~5 minutes | Cloud: API key + pip install; Self-hosted: Docker Compose up |
| Dependency count | Direct + transitive | ~10-15 (opik + provider) | Install only provider packages you need (openai, litellm, etc.) |
| Docker required? | Yes / No | No (cloud); Yes (self-hosted) | One-command self-host: `./opik.sh` |
| Language runtime | Required version | Python 3.8+ or Node 18+ | TypeScript SDK available for Node/Deno/Edge |
| Auth complexity | API key / OAuth / None | API key (cloud) / None (self-hosted) | Free Comet account generates API key; self-hosted needs no auth |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | To be measured in Quest smoke gate |

### Setup commands (expected)
```bash
# Cloud setup (fastest)
pip install opik && opik configure
# Enter API key from comet.com → Opik tab

# In your Python code
import opik
from opik.integrations.openai import track_openai
import openai

opik.configure(api_key='COMET_KEY')
client = track_openai(openai.OpenAI())
client.chat.completions.create(model='gpt-4o', messages=[{'role':'user','content':'hi'}])

# Self-hosted (Docker)
git clone https://github.com/comet-ml/opik.git
cd opik && ./opik.sh
# Dashboard at http://localhost:5173
```

### Known sharp edges
- Open-source self-hosted requires managing ClickHouse and PostgreSQL; some users report setup complexity on non-standard environments
- The product is relatively young compared to LangSmith/Langfuse; ecosystem guides and third-party integrations are thinner
- Agent Optimizer and Guardrails features are promising but still maturing; may require custom tuning
- Comet ecosystem connection can be confusing; Opik is independent but branding sometimes blurs the boundary
- Cloud free tier has quota limits; heavy production use requires Pro plan or self-hosting
- Some advanced features (SSO, RBAC) only available in enterprise cloud or require self-hosted OIDC configuration

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

> Raw results JSON: `benchmarks/llmops-platforms-comet-opik-<date>.json`

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
- Two-track: Opik OSS (free, self-hosted) + Opik Cloud (free tier + Pro)
- Self-hosted: free and unlimited; pay only infrastructure costs
- Cloud free: 25,000 spans/month, 60-day retention, unlimited team members
- Cloud Pro: $39/month (100,000 spans, extended retention), overage $5/100K spans
- Enterprise: custom pricing; includes SSO, RBAC, priority support

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0/month | Self-hosted free or cloud free tier sufficient |
| Medium (10-100 users) | $0-$500/month | Self-hosted infrastructure ($200-$500) or 2-3 Pro seats |
| Large (100+ users) | $500-$2,000/month | Self-hosted K8s + ClickHouse or multiple Pro seats + overage |
| Enterprise | Custom | Contact Comet sales; includes dedicated support |

### Hidden costs
- Self-hosted: ClickHouse and PostgreSQL infrastructure ops time
- LLM-as-judge evaluations consume your own API credits (OpenAI, Anthropic, etc.)
- Comet ML platform integration is separate pricing if you want unified ML + LLM dashboards
- Migration from CometLLM legacy may require code changes

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Full Docker Compose or Kubernetes deployment; all features unlocked |
| Open source | Yes | Apache 2.0 license; no feature gates in OSS |
| Audit trail | Yes | Full trace and evaluation logs via API or database query |
| Data residency controls | Yes | Self-hosted: full control; Cloud: data stored in Comet infrastructure |
| On-premise deployment | Yes | K8s Helm chart available; runs entirely air-gapped |
| Export format | JSON, CSV, API | opik export CLI; direct DB access in self-hosted |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Comet platform certified; self-hosted responsibility is yours |
| GDPR | Yes | Cloud GDPR compliant; self-hosted: your responsibility |
| HIPAA | Yes | Enterprise cloud; self-hosted: your infrastructure + BAA |
| ISO 27001 | Yes | Comet platform certified |
| EU AI Act | Partial | Audit trails and eval logs support evidence requirements |
| FedRAMP | TBD | Not publicly listed |

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
- [Comet ML](TBD) — Traditional ML experiment tracking; unified dashboard with Opik
- [LangChain](langchain.md) — Framework with native Opik integration for tracing
- [OpenAI](openai-agents-sdk.md) — Model provider commonly evaluated via Opik

### Alternatives to consider
- [Langfuse](langfuse.md) — More mature open-source community; better for data sovereignty
- [LangSmith](langsmith.md) — Better LangChain-native experience with less setup overhead
- [TruLens](trulens.md) — Free evaluation-only framework if you don't need hosted dashboard
- [Braintrust](braintrust.md) — Stronger evaluation datasets and enterprise features

---

## Links

- Official site: https://comet.com/site/products/opik/
- GitHub: https://github.com/comet-ml/opik
- Documentation: https://www.comet.com/docs/opik/
- Community / Slack: https://comet.com/site/community/
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
