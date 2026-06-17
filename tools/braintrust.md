# Braintrust

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Evaluation Platform
- **License**: Proprietary
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Notion, Stripe, Vercel, Coursera, Dropbox, Zapier, Perplexity, Ramp, Replit; evaluation-driven development; Loop AI agent; 20+ native SDK integrations; Brainstore purpose-built database; $80M Series B (Feb 2026) at $800M valuation

---

## Overview

Braintrust is an AI observability and evaluation platform founded in 2023 by Ankur Goyal in California. It unifies production tracing, prompt experimentation, structured evaluation, and CI/CD quality gating in a single workspace. The platform is built around a proprietary database called Brainstore, purpose-engineered for high-throughput AI trace queries at scale. Braintrust is framework-agnostic and integrates natively with OpenAI, Anthropic, LangChain, Vercel AI SDK, CrewAI, AutoGen, Pydantic AI, and many others, offering native SDKs in Python, TypeScript, Go, Ruby, C#, and Java.

The platform's core philosophy is "evaluation-driven development" — teams define what "good" looks like before shipping, run experiments against real datasets, and score outputs with LLM-as-a-judge, code, or human annotators. The Loop AI agent assists by generating prompts, scorers, and datasets from plain-language instructions, reducing the engineering bottleneck in evaluation setup. Production traces can be converted into evaluation datasets with one click, turning real failures into regression tests rather than relying on synthetic examples.

Braintrust has raised approximately $125M in total funding, including an $80M Series B led by ICONIQ in February 2026 at an $800M valuation. Customers include Notion, Stripe, Vercel, Coursera, Dropbox, Zapier, Perplexity, Ramp, and Replit. The platform targets AI/ML engineers, product managers, and compliance teams shipping production LLM features.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | Sign-up to first eval | ~5-10 minutes | Web-based; no local install required for cloud use |
| Dependency count | SDK only | 2-3 direct (`braintrust`, `autoevals`) | Python/TypeScript via pip/npm |
| Docker required? | Yes / No | No | Fully managed cloud; self-hosted Enterprise available |
| Language runtime | Required version | Python 3.10+ or Node 18+ | SDK supports Go, Ruby, C#, Java |
| Auth complexity | API key / OAuth / None | API key | Generated from dashboard; SSO on Enterprise |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Python SDK
pip install braintrust autoevals
# or uv
uv add braintrust autoevals

# TypeScript SDK
npm install braintrust

# Run first eval
BRAINTRUST_API_KEY=<key> braintrust eval tutorial_eval.py
```

### Known sharp edges
- Proprietary platform with no open-source core; self-hosting gated behind Enterprise plan
- $249/month Pro plan may be expensive for small teams or individual developers
- Loop AI agent suggestions require human review; automated scorers can produce unexpected results on edge cases
- Advanced custom span views and facet configuration have a learning curve
- Brainstore query syntax (BTQL) differs from standard SQL; requires docs reference
- Initial organization setup and project tagging discipline needed for clean trace grouping at scale

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

> Raw results JSON: `benchmarks/llmops-platforms-braintrust-<date>.json`

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
- **Starter (Free):** $0/month — 1M trace spans, 10K scores/month, unlimited users, 3 projects, 1GB storage, 14-day retention, OAuth sign-in, SOC 2, community support
- **Pro:** $249/month — unlimited spans & scores, 5GB storage, 30-day retention, custom environments, custom trace views, S3 export, priority support
- **Enterprise:** Custom pricing — hybrid/self-hosted deployment, unlimited retention, custom policies, SSO/SAML, RBAC, shared Slack channel, SLA guarantees, dedicated support engineer

- **Usage overages:** Scores beyond included quota at $1.50–$2.50 per 1,000; data beyond included storage at $3–$4/GB; Topics LLM usage at $0.06/mtok input, $0.40/mtok output

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | ⏳ TBD | |
| Medium (10-100 users) | ⏳ TBD | |
| Large (100+ users) | ⏳ TBD | |
| Enterprise | ⏳ TBD | |

### Hidden costs
- ⏳ TBD (infrastructure, ops time, training, support)

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes (Enterprise) | Hybrid deployment available on Enterprise plan; data plane runs in customer's cloud |
| Open source | No | Proprietary platform; SDKs are open-source (Apache-2.0) but platform is not |
| Audit trail | Yes | Full execution logs, immutable trace history, user attribution |
| Data residency controls | Yes | Enterprise hybrid deployment enables region-specific data plane placement |
| On-premise deployment | Partial | Enterprise self-hosted / hybrid only; no fully air-gapped on-prem version advertised |
| Export format | JSON, CSV, S3 | Traces and datasets exportable as JSON/CSV; S3 auto-export on Pro+ |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Type II certified |
| GDPR | Yes | Compliant; DPA available; EU data residency via Enterprise hybrid |
| HIPAA | Yes | Compliant; BAA available on Enterprise |
| ISO 27001 | ⏳ TBD | Not publicly confirmed |
| EU AI Act | ⏳ TBD | Not publicly confirmed |
| FedRAMP | ⏳ TBD | Not publicly confirmed |

---

## Related Tools

### Tier A peers in same category
- [Dify](dify.md)
- [Flowise](flowise.md)
- [n8n](n8n.md)
- [Vellum](vellum.md)
- [PromptLayer](promptlayer.md)
- [Pezzo](pezzo.md)
- [Zapier](zapier.md)
- [Make](make.md)

### Complementary tools
- [Langfuse](langfuse.md) — alternative open-source observability stack
- [LangSmith](langsmith.md) — LangChain-native tracing and evaluation
- [Promptfoo](promptfoo.md) — CLI-first evaluation and red-teaming
- [OpenAI Agents SDK](openai-agents-sdk.md) — agent framework with native Braintrust integration
- [CrewAI](crewai.md) — multi-agent framework with Braintrust tracing support

### Alternatives to consider
- [Langfuse](langfuse.md) or [LangSmith](langsmith.md) when open-source or LangChain-native observability is preferred
- [Promptfoo](promptfoo.md) for teams prioritizing local CLI evaluation and red-teaming over hosted observability
- [Galileo AI](comet-opik.md) for packaged scoring and runtime guardrails rather than custom eval logic

---

## Links

- Official site: [https://www.braintrust.dev](https://www.braintrust.dev)
- GitHub: [https://github.com/braintrustdata](https://github.com/braintrustdata)
- Documentation: [https://www.braintrust.dev/docs](https://www.braintrust.dev/docs)
- Community / Discord: [https://www.braintrust.dev/discord](https://www.braintrust.dev/discord)
- Changelog: [https://www.braintrust.dev/docs/changelog](https://www.braintrust.dev/docs/changelog)
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
