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

## Deep Analysis

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

Lunary is an open-source LLM observability platform (1,395+ GitHub stars) that provides tracing, prompt management, and monitoring specifically optimized for chatbot use cases. It is SOC 2 Type II and ISO 27001 certified, with EU data center options for GDPR compliance. The platform is designed for quick setup (under two minutes) and offers a free tier covering 10,000 events per month with 30-day retention. It is particularly useful for teams building chatbots that need fast time-to-value observability.

### 2. Gotchas of Using This Tool

Lunary's community is significantly smaller than Langfuse (1,395 stars vs 16,000+), meaning fewer community-contributed integrations and templates. The platform's feature breadth is narrower than more established alternatives. Self-hosting via Kubernetes or Docker adds operational complexity. The free tier's 10,000 events/month limit is quickly consumed by active development. Advanced features may require paid plans.

### 3. Limitations

Lunary's evaluation framework is minimal compared to Braintrust or Langfuse. The platform's agent tracing capabilities are less specialized than AgentOps. Integration with non-chatbot LLM applications may require custom work. The smaller community means limited community support and fewer third-party tutorials. Advanced analytics and custom metrics are less mature than larger platforms.

### 4. How Secure Is This Tool?

Lunary is SOC 2 Type II and ISO 27001 certified — strong security credentials for a smaller platform. The platform supports EU data center deployment for GDPR compliance. Self-hosting via Kubernetes or Docker provides full data control. Data is encrypted at rest and in transit. No major CVEs have been reported. The open-source nature allows independent security review.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 4/10.** Lunary is a developer tool requiring API integration. The dashboard is usable by semi-technical users for monitoring, but setup requires engineering support.

### 6. What Does This Tool Solve That Others Don't?

Lunary's unique strength is its chatbot-optimized observability with fast setup (under two minutes) and strong compliance credentials (SOC 2 + ISO 27001). The EU data center option for GDPR compliance addresses a need that many US-based alternatives don't prioritize. The platform's focus on chatbot-specific metrics (conversation quality, user satisfaction) differentiates it from general LLM observability tools.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Langfuse | Open-source observability | Self-hostable + free |
| 2 | LangSmith | Full LLMOps tracing | Ecosystem depth |
| 3 | Helicone | Proxy monitoring | Zero-code |
| 4 | Lunary | Chatbot observability | SOC 2 + ISO 27001 |
| 5 | LangWatch | Monitoring insights | Cost optimization |

### 8. How Can This Tool Be Improved? How Active Is Development?

Lunary is actively developed with regular releases. Key improvements include expanding the evaluation framework, deepening agent tracing, growing the community, expanding framework integrations, improving documentation, and adding more pre-built templates. The strong compliance certifications should be more prominently marketed.

### 9. Official Maintainer Contacts

Lunary is maintained by Lunary AI. GitHub: https://github.com/lunary-ai/lunary. Website: https://lunary.ai. Documentation: https://docs.lunary.ai.

### 10. General Usage Guidance

Use Lunary if you need chatbot-focused observability with fast setup and strong compliance (SOC 2 + ISO 27001). The free tier (10,000 events/month) is good for prototyping. For open-source self-hosting with more features, evaluate Langfuse. For zero-code monitoring, evaluate Helicone. The EU data center option makes Lunary attractive for GDPR-sensitive deployments.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
