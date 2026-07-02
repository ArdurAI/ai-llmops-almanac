# Helicone

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: API Monitoring
- **License**: Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Lightweight; request logging, cost tracking, caching; proxy-based; zero-code integration

---

## Overview

Helicone is an open-source LLM observability platform built by Y Combinator W23 alumni, designed to provide lightweight, proxy-based monitoring for LLM applications. It operates as a transparent proxy between your application and LLM providers, capturing detailed request logs, cost tracking, latency metrics, and usage analytics with minimal integration effort. As of 2026, Helicone has processed over 14.2 trillion tokens and maintains 5,000+ GitHub stars.

The platform's key differentiator is its zero-code integration model: you change one line (the API base URL) or add a single header, and observability begins immediately. This makes it one of the fastest tools to adopt for teams needing immediate visibility into LLM usage. Helicone also doubles as an AI Gateway, offering built-in response caching (reducing API costs by 20-30% on duplicate requests), rate limiting, and automatic fallbacks across 100+ model providers including OpenAI, Anthropic, Google, and Groq.

Helicone is built on a modern architecture using Next.js (frontend), Cloudflare Workers (edge proxy), ClickHouse (analytics database), and Supabase (auth/app DB). The proxy adds approximately 50-80ms of latency per request. In March 2026, Helicone was acquired by Mintlify, though the platform continues to operate as a standalone product with active development.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | URL change to first logged request | <2 minutes | Proxy-based; no SDK installation required |
| Dependency count | Direct + transitive | 0 (proxy mode) | Or ~5-10 for SDK-based integration |
| Docker required? | Yes / No | No (for SaaS); Yes (for self-host) | Self-hosted: 4 containers via Docker Compose |
| Language runtime | Required version | Any (proxy) | Works with any HTTP-capable language |
| Auth complexity | API key / OAuth / None | API key | Free signup at helicone.ai generates key |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | To be measured in Quest smoke gate |

### Setup commands (expected)
```bash
# Proxy mode: change your OpenAI base URL
import openai
client = openai.OpenAI(
    base_url="https://oai.helicone.ai/v1",
    api_key=os.environ["OPENAI_API_KEY"],
    default_headers={"Helicone-Auth": f"Bearer {os.environ['HELICONE_API_KEY']}"}
)

# Or with the Helicone AI Gateway SDK
npm install @helicone/ai-sdk-provider

# Self-hosted (Docker)
git clone https://github.com/Helicone/helicone.git
cd helicone/docker
./helicone-compose.sh helicone up
```

Dashboard available at localhost:3000 for self-hosted or app.helicone.ai for cloud.

### Known sharp edges
- Proxy architecture adds 50-80ms latency to every LLM request; can become a critical-path dependency if Helicone is down
- Limited evaluation capabilities — manual scoring only, no auto-generated evals or LLM-as-judge built-in
- No issue tracking or lifecycle management for discovered problems
- Limited support for complex multi-turn agent workflows compared to SDK-native tools
- Self-hosted originally required 12 containers; now reduced to 4, but still requires ClickHouse and Supabase knowledge
- Acquired by Mintlify in March 2026; long-term product roadmap is uncertain though currently operational
- Request-level (not span-level) tracing means nested agent calls may appear flat in the dashboard

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

> Raw results JSON: `benchmarks/llmops-platforms-helicone-<date>.json`

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
- SaaS with seat-based and usage-based tiers; self-hosted is free and open source
- Free tier: 10,000 requests/month, 7-day retention, 1 user
- Pro: $79/month (unlimited seats, 1-month retention) — or $20-$25/seat/month in some plans
- Team: $799/month (SOC-2/HIPAA, 5 organizations, 3-month retention)
- Enterprise: Custom pricing (on-prem deployment, unlimited retention)

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0-$79/month | Free tier often sufficient for dev/staging |
| Medium (10-100 users) | $79-$799/month | Pro or Team depending on compliance needs |
| Large (100+ users) | $799+/month | Team or Enterprise; custom overage rates |
| Enterprise | Custom | On-prem/self-hosted available; contact sales |

### Hidden costs
- Proxy latency (50-80ms) may require caching or optimization for latency-sensitive apps
- Self-hosted requires managing ClickHouse, Supabase/PostgreSQL, and Redis infrastructure
- All data passes through third-party proxy in SaaS mode; potential compliance review needed
- AI Gateway features (credits, unified billing) may create vendor lock-in if heavily adopted

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Fully open-source self-hosted via Docker or Helm |
| Open source | Yes | Apache 2.0 license; full source on GitHub |
| Audit trail | Yes | Full request/response logging with metadata |
| Data residency controls | Yes | SaaS: US/EU data centers; self-hosted: full control |
| On-premise deployment | Yes | Enterprise tier supports on-prem; self-hosted always on-prem |
| Export format | JSON, CSV | Export logs and analytics via API or dashboard |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Type II certified for SaaS |
| GDPR | Yes | Compliant; EU data residency available |
| HIPAA | Yes | Team+ tier; self-hosted HIPAA depends on your infrastructure |
| ISO 27001 | TBD | Not explicitly listed; SOC 2 covers similar controls |
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
- [LiteLLM](TBD) — Gateway/router that pairs well with Helicone's observability proxy
- [LangChain](langchain.md) — Framework commonly monitored through Helicone proxy
- [OpenAI](openai-agents-sdk.md) — Primary provider supported via Helicone AI Gateway

### Alternatives to consider
- [Langfuse](langfuse.md) — Open-source, SDK-based, no proxy latency; better for deep tracing
- [LangSmith](langsmith.md) — Better for LangChain-native teams needing evaluation workflows
- [Portkey](TBD) — Similar proxy-based gateway with stronger routing capabilities
- [Braintrust](braintrust.md) — Better evaluation and dataset management

---

## Links

- Official site: https://helicone.ai
- GitHub: https://github.com/Helicone/helicone
- Documentation: https://docs.helicone.ai
- Community / Discord: https://discord.helicone.ai
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

Helicone is an open-source LLM observability platform (Apache 2.0, 5,000+ GitHub stars, YC W23) that provides lightweight, proxy-based monitoring for LLM applications. It has processed over 14.2 trillion tokens and operates as a transparent proxy between applications and LLM providers, capturing request logs, cost tracking, latency metrics, and usage analytics with minimal integration effort. The proxy-based approach means no SDK changes are required — just a base URL change.

### 2. Gotchas of Using This Tool

Helicone's proxy-based architecture adds a network hop, introducing latency (typically 5-20ms) to every LLM call. The proxy can become a single point of failure if not properly configured with fallbacks. Rate limiting and caching features, while useful, require careful configuration to avoid breaking real-time use cases. The free tier has limits on request volume and retention period. Some advanced features (custom metrics, alerts) require paid plans.

### 3. Limitations

Helicone's observability is request/response-focused — it lacks deep agent session tracing compared to AgentOps or LangSmith. The evaluation framework is minimal compared to Braintrust or Langfuse. Self-hosting requires managing the proxy infrastructure, ClickHouse database, and dashboard separately. The platform's prompt management features are basic. Integration with non-OpenAI providers is less mature.

### 4. How Secure Is This Tool?

Helicone is open-source under Apache 2.0, allowing independent security review. The proxy handles all LLM traffic, meaning it processes API keys and request/response data — teams must secure the proxy deployment. Helicone Cloud is SOC 2 Type II compliant. No major CVEs have been reported. Teams self-hosting should encrypt the ClickHouse database, use HTTPS for the proxy, and restrict dashboard access with authentication.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 4/10.** Helicone is a developer tool requiring API integration knowledge. The dashboard is usable by semi-technical users for monitoring, but setup requires engineering support.

### 6. What Does This Tool Solve That Others Don't?

Helicone's unique strength is its zero-code proxy-based approach — changing a base URL enables full observability without SDK modifications, making it the fastest way to add monitoring to existing LLM applications. The 14.2 trillion tokens processed demonstrate massive scale validation. Built-in caching and rate limiting provide cost optimization that observability-only tools lack. The transparent proxy model also enables cost attribution and budget enforcement.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Langfuse | Open-source observability | Self-hostable + evals |
| 2 | LangSmith | Full LLMOps tracing | Ecosystem depth |
| 3 | Helicone | Proxy monitoring | Zero-code + caching |
| 4 | Lunary | Chatbot observability | Quick setup |
| 5 | OpenLIT | OpenTelemetry-native | OTel ecosystem |

### 8. How Can This Tool Be Improved? How Active Is Development?

Helicone is actively developed by the YC W23 team with regular releases. Key improvements include deeper agent tracing, expanding the evaluation framework, improving multi-provider support, simplifying self-hosting, and adding custom metric support on lower tiers. Performance optimization to reduce proxy latency would benefit latency-sensitive use cases.

### 9. Official Maintainer Contacts

Helicone is maintained by Helicone Inc. GitHub: https://github.com/Helicone/helicone. Website: https://helicone.ai. Documentation: https://docs.helicone.ai. Discord: https://discord.helicone.ai.

### 10. General Usage Guidance

Use Helicone if you want zero-code LLM observability with cost tracking and caching, especially for existing applications where SDK changes are impractical. For deeper observability with evaluation features, evaluate Langfuse. For agent-specific tracing, evaluate AgentOps or LangSmith. Start with the proxy-based approach for quick wins, then layer in SDKs for deeper tracing as needed.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
