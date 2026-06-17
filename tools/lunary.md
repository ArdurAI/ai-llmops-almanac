# Lunary

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Observability
- **License**: Open Source / SaaS
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Chatbot/RAG teams; LLM apps monitoring, prompt management; self-hostable; EU data center

---

## Overview

Lunary is an open-source LLM observability platform optimized for chatbot and RAG pipeline teams, released under the Apache 2.0 license. It provides conversation replay, user journey tracking, topic classification, prompt versioning with A/B testing, and performance analytics — all designed around the needs of conversational AI applications. The platform is particularly strong for JavaScript/TypeScript environments, offering SDKs for Node.js, Deno, Vercel Edge, and Cloudflare Workers alongside Python.

Lunary's "Radar" feature automatically categorizes LLM responses based on predefined criteria, making it easy to audit outputs at scale. Its prompt management system supports version control, team collaboration, and side-by-side testing like Git branches. The platform also includes guardrails to prevent malicious prompts and protect against sensitive data breaches, plus real-time alerts when agents fail to meet performance thresholds.

With 1,395+ GitHub stars, Lunary is smaller than some competitors but punches above its weight for chatbot-specific use cases. It can be deployed via Lunary Cloud or self-hosted within your own VPC using Kubernetes or Docker. The platform is SOC 2 Type II and ISO 27001 certified, with EU data center options for GDPR compliance. Setup is advertised as under two minutes, and the free tier covers 10,000 events per month with 30-day retention.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` or `npm install` to first trace | ~2 minutes | One-line SDK integration for Python/JS |
| Dependency count | Direct + transitive | ~3-5 (lunary + openai) | Very lightweight SDK |
| Docker required? | Yes / No | No (cloud); Yes (self-hosted) | Self-hosted: Docker Compose or Kubernetes |
| Language runtime | Required version | Python 3.8+ or Node 18+ | Strong TypeScript/JS support including Edge runtimes |
| Auth complexity | API key / OAuth / None | API key | Free signup at lunary.ai generates key |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | To be measured in Quest smoke gate |

### Setup commands (expected)
```bash
# Python
pip install lunary

import lunary
from openai import OpenAI

client = OpenAI()
lunary.monitor(client)

chat_completion = client.chat.completions.create(
  messages=[{"role": "user", "content": "Hello"}],
  model="gpt-4o"
)

# JavaScript/TypeScript
npm install lunary
import { monitor } from "lunary";
monitor(openaiClient);

# Self-hosted (Docker)
# See https://lunary.ai/docs/self-hosting for docker-compose.yml
```

Dashboard available at app.lunary.ai or localhost for self-hosted.

### Known sharp edges
- Smaller community and ecosystem compared to Langfuse/LangSmith (1,395 GitHub stars vs 19,000+ for Langfuse)
- Narrower feature set than full-stack observability platforms; focused on chatbot/RAG use cases
- Some advanced features (SSO, PII masking, data warehouse connectors) require Enterprise tier
- Docker Compose support was community-requested and took time to arrive; some self-hosting gaps may remain
- Agent tracing is present but less mature than dedicated agent tools like AgentOps or LangSmith
- Limited evaluation capabilities compared to TruLens or Braintrust; more monitoring than rigorous eval

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

> Raw results JSON: `benchmarks/llmops-platforms-lunary-<date>.json`

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
- SaaS + open-source self-hosted; core platform is 100% open source
- Free tier: 10,000 events/month, 3 projects, 30-day retention, 1 seat
- Team: $20/user/month, 50,000 events/month, 1-year history, 10 seats, AI Playground
- Enterprise: custom, self-hosted, SSO, PII masking, SLA, data warehouse connectors

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0-$200/month | Free tier for prototyping; Team tier for small teams |
| Medium (10-100 users) | $200-$2,000/month | Team tier for most; overage at $10/50K events |
| Large (100+ users) | Custom | Enterprise with self-hosted, SSO, dedicated support |
| Enterprise | Custom | Self-hosted in your VPC; Kubernetes or Docker |

### Hidden costs
- Self-hosted requires managing PostgreSQL, Redis, and app infrastructure
- AI Playground queries cost $0.05 per query beyond 1,000/month on Team tier
- Data warehouse connectors (Enterprise) may require integration engineering
- Smaller community means fewer Stack Overflow answers; support reliance on Team/Enterprise tiers

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Full Docker Compose or Kubernetes deployment in your VPC |
| Open source | Yes | Apache 2.0 license; core platform fully open source |
| Audit trail | Yes | Full logs and event history; exportable via API |
| Data residency controls | Yes | EU data center available; self-hosted = full control |
| On-premise deployment | Yes | Kubernetes or Docker in your own cloud/account |
| Export format | JSON, CSV | API export; database access in self-hosted |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Type II certified (external audit) |
| GDPR | Yes | EU data center; GDPR compliant; self-hosted = your responsibility |
| HIPAA | Partial | Not explicitly listed; self-hosted may support HIPAA with BAA |
| ISO 27001 | Yes | ISO 27001:2022 certified |
| EU AI Act | Partial | Audit trail supports evidence; explicit mapping not detailed |
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
- [LangChain](langchain.md) — Framework with Lunary SDK integration
- [OpenAI](openai-agents-sdk.md) — Primary model provider supported by Lunary
- [Vercel AI SDK](TBD) — Edge deployment commonly paired with Lunary's JS SDK

### Alternatives to consider
- [Langfuse](langfuse.md) — Larger open-source community; more mature tracing
- [LangSmith](langsmith.md) — Better for LangChain-native evaluation and prompt management
- [Helicone](helicone.md) — Faster proxy-based setup if you don't need chatbot-specific features
- [Braintrust](braintrust.md) — Stronger evaluation and dataset management for ML teams

---

## Links

- Official site: https://lunary.ai
- GitHub: https://github.com/lunary-ai/lunary
- Documentation: https://docs.lunary.ai
- Community / Discord: TBD
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
