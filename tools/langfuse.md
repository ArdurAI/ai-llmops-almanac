# Langfuse


[![Observability](https://img.shields.io/badge/Also_in-Observability-blue)](https://github.com/ArdurAI/ai-observability-almanac) [![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Observability
- **License**: MIT (Open Source)
- **Region**: EU (Germany) + USA (San Francisco)
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> 16K+ stars; tracing, evals, prompt management; self-hostable; acquired by ClickHouse Jan 2026

---

## Overview

Langfuse is the leading open-source AI engineering platform for LLM observability, evaluations, and prompt management. Founded in Berlin in 2023 by Marc Klingen, Maximilian Deichmann, and Clemens Rawert, the company went through Y Combinator's W23 batch and raised a $4M seed round from Lightspeed Venture Partners, General Catalyst, and YC. In January 2026, Langfuse was acquired by ClickHouse, Inc. (a $15B company) as part of ClickHouse's expansion into AI infrastructure, bringing the full Langfuse team and codebase into a larger data-platform organization.

Langfuse provides a unified platform for tracing multi-step agent workflows, managing prompt versions, running LLM-as-judge evaluations, and collecting human feedback. It is framework-agnostic, with native integrations for LangChain, LangGraph, OpenAI SDK, CrewAI, AutoGen, and LiteLLM, plus OpenTelemetry support for custom instrumentation. The platform handles >80 million traces per day on its Cloud offering and is trusted by 19 of the Fortune 50 and 63 of the Fortune 500. The codebase is fully open source under the MIT license, with the same code running in the free self-hosted version and the managed Cloud service.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | Cloud signup to first trace | ~2 minutes | Sign up at cloud.langfuse.com, no credit card |
| Time to first result | Self-hosted Docker to first trace | ~5 minutes | `docker compose up` after git clone |
| Dependency count | Direct + transitive | ~15-30 | Python SDK is lightweight; server requires Postgres+ClickHouse+Redis |
| Docker required? | Yes / No | Optional | Required for self-hosting; not needed for Cloud |
| Language runtime | Required version | Python 3.9+ / Node 18+ | SDKs available for Python, JavaScript, Go |
| Auth complexity | API key / OAuth / None | API key | Cloud: sign up with Google/GitHub/AzureAD; self-host: configurable |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Cloud (fastest path)
# Sign up at https://cloud.langfuse.com
# Get API keys and set environment variables:
export LANGFUSE_PUBLIC_KEY=pk-...
export LANGFUSE_SECRET_KEY=sk-...

# Python SDK
pip install langfuse

# Self-hosted (Docker Compose)
git clone --depth=1 https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up

# Self-hosted (Kubernetes / production)
# Helm chart available: https://langfuse.com/docs/deployment/self-host
```

### Known sharp edges
- **Self-hosting infrastructure complexity**: Production self-hosting requires managing ClickHouse, PostgreSQL, Redis/Valkey, and S3-compatible object storage. This is a non-trivial operational burden.
- **Timezone requirement**: All infrastructure components (ClickHouse and Postgres) must run with timezone set to UTC. Non-UTC timezones cause queries to return incorrect or empty results.
- **Enterprise features gated**: Self-hosted OSS includes all core features, but enterprise add-ons (SSO, RBAC, audit logs, SCIM, data retention policies) require a commercial license key.
- **Multi-modal traces still maturing**: Vision and audio tracing is available but less polished than text tracing as of mid-2026.
- **ClickHouse dependency**: The v3 architecture migrated from PostgreSQL to ClickHouse for trace storage. Teams self-hosting must now run ClickHouse, which adds infrastructure overhead compared to earlier versions.
- **Event volume limits on free Cloud**: Free Cloud tier is generous (50K events/month), but high-volume production workloads will hit limits quickly.

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

> Raw results JSON: `benchmarks/llmops-platforms-langfuse-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- **UTC timezone enforcement**: ClickHouse and Postgres must run in UTC. This is a common configuration error in self-hosted deployments.
- **High-throughput ingestion**: Langfuse v3 moved to ClickHouse to handle high-throughput traces. Teams migrating from v2 must re-architect their storage layer.
- **License key confusion**: Pre-built Docker images include enterprise code in `/ee` directories, but features are disabled without a license key. Some users worry about compliance; the team confirms no license key means no execution of enterprise code.
- **OpenTelemetry span mapping**: While OTel support is comprehensive, mapping custom OTel spans to Langfuse's trace/observation/score model can require custom attribute conventions.
- **Prompt versioning edge cases**: Prompt versioning works well for managed deployments, but fetching the "latest" prompt without proper release management can cause production drift.

### Workarounds documented
- Always set ClickHouse and Postgres containers to UTC timezone (`TZ=UTC`).
- Use the official Helm chart or Terraform templates for production self-hosting rather than manual Docker Compose.
- For enterprise features on self-hosted, contact Langfuse/ClickHouse sales for a license key.
- Use explicit prompt release labels rather than "latest" in production code.

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
- **Open Source (self-hosted)**: Free (MIT license). All core features unlimited. You pay for your own infrastructure.
- **Langfuse Cloud — Hobby**: Free. Up to 50K events/month. No credit card required.
- **Langfuse Cloud — Pro**: ~$29–59/month. Higher event limits, team features, priority support.
- **Langfuse Cloud — Enterprise**: Custom pricing. Includes SSO, RBAC, audit logs, dedicated support, SLA, SOC 2/ISO 27001 reports.
- **Self-hosted Enterprise**: Custom pricing. License key for enterprise features (RBAC, SSO, SCIM, audit logs) on your own infrastructure.
- **Startup / Open Source discounts**: $300/month credits for qualifying open source projects, startups, and educational users.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0 | Hobby Cloud tier or self-hosted Docker |
| Medium (10-100 users) | $0–200/mo | Self-hosted (infra cost only) or Pro Cloud |
| Large (100+ users) | $200–2,000+/mo | Enterprise Cloud or self-hosted with ClickHouse cluster |
| Enterprise | Custom | Enterprise Cloud or self-hosted with commercial license |

### Hidden costs
- **Self-hosting infrastructure**: ClickHouse + Postgres + Redis + S3 is the minimum production stack. This requires DevOps expertise and compute costs.
- **Event volume**: Each LLM call, tool call, and agent step generates events. High-volume agents can accumulate millions of events quickly.
- **LLM-as-judge evals**: Running evaluations via LLM judges consumes additional tokens and adds to LLM API costs.
- **Data retention**: Long trace retention requires storage scaling; ClickHouse handles this well but costs grow with data volume.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Fully open source; can run entirely on-premises or in your VPC |
| Open source | Yes | MIT license; all core features available without license keys |
| Audit trail | Yes | Full trace history, prompt versioning, and evaluation scores |
| Data residency controls | Yes | Self-hosted gives full control; Cloud supports EU regions |
| On-premise deployment | Yes | Helm charts, Terraform for AWS/Azure/GCP, Docker Compose for local |
| Export format | JSON, CSV, Blob Storage | Batch export to S3/GCS; API access to all data |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | SOC 2 Type II certified (Langfuse Cloud) |
| GDPR | Yes | GDPR compliant (Langfuse Cloud); EU-based team |
| HIPAA | Partial | HIPAA alignment claimed for Cloud; not formally certified for OSS self-hosted |
| ISO 27001 | Yes | ISO 27001 certified (Langfuse Cloud) |
| EU AI Act | Partial | EU-based; compliance depends on specific use case |
| FedRAMP | No | Not formally FedRAMP authorized |

> **Note**: SOC 2 Type II, ISO 27001, and GDPR compliance apply to Langfuse Cloud. The self-hosted open source version does not carry formal compliance certifications. Organizations with strict compliance requirements can use Langfuse Cloud or implement their own controls on self-hosted deployments. The acquisition by ClickHouse (January 2026) adds enterprise-grade infrastructure backing to the Cloud offering.

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
- [LangChain](langchain.md) — Langfuse has native callback handler for LangChain/LangGraph tracing
- [Pydantic AI](pydantic-ai.md) — Can be instrumented via OpenTelemetry or custom callbacks to Langfuse
- [OpenAI SDK](https://github.com/openai/openai-python) — Native Langfuse integration for OpenAI API calls
- [LiteLLM](litellm.md) — Proxy-based logging into Langfuse
- [ClickHouse](https://clickhouse.com) — Underlying OLAP database for Langfuse v3; now same company
- [Helicone](https://helicone.ai) — Alternative proxy-based observability; often compared to Langfuse
- [LangSmith](https://smith.langchain.com) — LangChain-native observability; competitive alternative
- [Braintrust](https://braintrust.dev) — Evaluation-focused alternative with CI/CD integration

### Alternatives to consider
- [LangSmith](langsmith.md) — Best if your stack is 100% LangChain/LangGraph; deeper native integration
- [Helicone](https://helicone.ai) — One-line proxy integration (change base URL); fastest setup but less rich agent tracing
- [Braintrust](braintrust.md) — Evaluation-first platform with stronger CI/CD and release-gating features
- [Phoenix](https://phoenix.arize.com) — OpenTelemetry-native; good for teams already using Arize MLOps
- [PromptLayer](promptlayer.md) — Simpler prompt management and logging; less comprehensive than Langfuse

---

## Links

- Official site: [https://langfuse.com](https://langfuse.com)
- GitHub: [https://github.com/langfuse/langfuse](https://github.com/langfuse/langfuse)
- Documentation: [https://langfuse.com/docs](https://langfuse.com/docs)
- Cloud: [https://cloud.langfuse.com](https://cloud.langfuse.com)
- Changelog: [https://langfuse.com/changelog](https://langfuse.com/changelog)
- Enterprise: [https://langfuse.com/enterprise](https://langfuse.com/enterprise)
- Self-hosting guide: [https://langfuse.com/docs/deployment/self-host](https://langfuse.com/docs/deployment/self-host)
- Community / Discord: [Langfuse Discord](https://discord.langfuse.com)
- Company handbook: [https://langfuse.com/handbook](https://langfuse.com/handbook)
- Acquisition announcement: [https://langfuse.com/blog/joining-clickhouse](https://langfuse.com/blog/joining-clickhouse)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| 2026-01-16 | Acquired by ClickHouse | Langfuse team joins ClickHouse; $400M Series D context |
| 2025-12 | Langfuse v3 shipped | Migrated core data layer from PostgreSQL to ClickHouse |
| 2025-06 | All features open sourced | LLM-as-judge, playground, experiments, annotations under MIT |
| 2025-04 | 10,000 GitHub stars reached | Rapid growth in open source adoption |
| 2023-11 | Seed funding | $4M from Lightspeed, General Catalyst, Y Combinator |
| 2023-01 | Y Combinator W23 batch | Founded by Marc Klingen, Max Deichmann, Clemens Rawert |

---

## Deep Analysis

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

Langfuse is an open-source LLM observability platform (MIT license, 16,000+ GitHub stars) that provides tracing, prompt management, evaluation, and analytics for LLM applications. Acquired by ClickHouse in January 2026, it is the leading open-source alternative to LangSmith with self-hosting via Docker Compose or Kubernetes. The platform supports OpenTelemetry-native tracing, cost analytics, and integrates with LangChain, OpenAI SDK, LiteLLM, and other major frameworks.

### 2. Gotchas of Using This Tool

Self-hosted Langfuse requires managing PostgreSQL and ClickHouse infrastructure, which adds operational complexity. The free cloud tier has limits on event volume and retention. Prompt management features, while functional, are less polished than dedicated tools like PromptLayer. The ClickHouse acquisition has raised questions about the project's independence and future direction. Advanced analytics require ClickHouse expertise for custom queries.

### 3. Limitations

Langfuse's evaluation framework is less code-flexible than Braintrust's custom scorers. Agent tracing depth is not as specialized as AgentOps. The self-hosted version's UI performance depends on ClickHouse query performance. Multi-region deployment is not well-documented. The platform's prompt testing capabilities are basic compared to Promptfoo. Advanced alerting requires custom configuration.

### 4. How Secure Is This Tool?

Langfuse is MIT-licensed and fully open source, allowing independent security review. The self-hosted version provides full data control. The cloud platform is SOC 2 Type II compliant and GDPR compliant. Data is encrypted at rest and in transit. No major CVEs have been reported. The ClickHouse acquisition brings additional enterprise security resources. Teams self-hosting should secure PostgreSQL, ClickHouse, and the web application.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 4/10.** Langfuse is a developer tool requiring integration with LLM applications. The dashboard is usable by semi-technical users for monitoring, but setup requires engineering support.

### 6. What Does This Tool Solve That Others Don't?

Langfuse's unique strength is being the leading fully open-source LLM observability platform with self-hosting, comprehensive tracing, prompt management, and evaluation in one package. The OpenTelemetry-native architecture provides vendor-neutral observability. The ClickHouse backend enables high-performance analytics at scale. The generous cloud free tier (50,000 events/month) and open-source self-hosting make it accessible to teams of all sizes.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Langfuse | Open-source observability | Self-hostable + free |
| 2 | LangSmith | Full LLMOps tracing | Ecosystem depth |
| 3 | Braintrust | Evaluation platform | Eval workflows |
| 4 | Comet Opik | ML + LLM observability | Comet ecosystem |
| 5 | Helicone | Proxy monitoring | Zero-code |

### 8. How Can This Tool Be Improved? How Active Is Development?

Langfuse is very actively developed with frequent releases and ClickHouse backing. Key improvements include simplifying self-hosting (managed ClickHouse), deepening agent tracing, expanding evaluation features, improving prompt management UX, adding more pre-built integrations, and clarifying the open-source vs. cloud roadmap post-ClickHouse acquisition.

### 9. Official Maintainer Contacts

Langfuse is maintained by Langfuse (now part of ClickHouse). GitHub: https://github.com/langfuse/langfuse. Website: https://langfuse.com. Documentation: https://langfuse.com/docs. Cloud: https://cloud.langfuse.com. Discord and GitHub issues are actively monitored.

### 10. General Usage Guidance

Use Langfuse if you want an open-source, self-hostable LLM observability platform with tracing, evaluation, and prompt management. The cloud free tier (50,000 events/month) is excellent for prototyping. For deeper LangChain integration, evaluate LangSmith. For evaluation-first workflows, evaluate Braintrust. For zero-code monitoring, evaluate Helicone. Self-host using Docker Compose for production with data residency requirements.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
