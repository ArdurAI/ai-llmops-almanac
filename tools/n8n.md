# n8n

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Workflow Automation
- **License**: Fair-code
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> 188K stars; 400+ integrations, AI agent nodes; self-hostable; Germany-based; EU-friendly

---

## Overview

n8n (pronounced "n-eight-n") is a fair-code workflow automation platform founded in 2019 by Jan Oberhauser in Berlin, Germany. With approximately 174,000–188,000 GitHub stars and over 100 million Docker pulls, it is one of the most popular automation platforms in the open-source ecosystem. n8n combines a visual node-based editor with full JavaScript and Python code support, making it uniquely flexible for both no-code users and developers. The platform offers 400+ native integrations and over 1,200 integrations when including community nodes, with roughly 70 dedicated AI/LLM nodes.

n8n's core value proposition is execution-based pricing (not per-step) and total data sovereignty through self-hosting. Unlike proprietary tools such as Zapier or Make, n8n does not charge extra for complex multi-step workflows or premium apps. The platform supports general business automation alongside native AI capabilities including LangChain integration, agent builders, RAG support, and MCP protocol support. n8n is licensed under the Sustainable Use License (fair-code), which allows self-hosting and modification but prohibits reselling n8n as a competing SaaS product. The company has raised significant funding and serves a community of over 200,000 active users, with a Discord of 73,000+ members and weekly releases.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `git clone` to working | ~45–60 min | Docker Compose path for production; npm path for quick test |
| Dependency count | Direct + transitive | Moderate | TypeScript/Node.js + Vue.js frontend; PostgreSQL + Redis for production |
| Docker required? | Yes / No | Recommended | `docker.n8n.io/n8nio/n8n` official image; 100M+ pulls |
| Language runtime | Required version | Node.js 18+ | Self-hosted runs on Node.js; cloud is managed |
| Auth complexity | API key / OAuth / None | Basic auth via env vars | `N8N_BASIC_AUTH_ACTIVE`, `N8N_BASIC_AUTH_USER`, `N8N_BASIC_AUTH_PASSWORD` |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | SQLite default for dev; PostgreSQL + Redis strongly recommended for production |

### Setup commands (expected)
```bash
# Quick start via Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n

# Production: Docker Compose with PostgreSQL + Redis + persistent volumes
# See https://docs.n8n.io/hosting/installation/docker/
```

### Known sharp edges
- **Data loss on update:** Self-hosted instances using default SQLite without mapped Docker volumes can lose data during updates. Always map persistent storage to the host.
- **Self-hosting ops burden:** n8n's documentation states that self-hosting is best suited for advanced users due to misconfiguration risks. SSL, backups, firewall rules, and monitoring are the operator's responsibility.
- **Fair-code license nuance:** n8n is source-available under the Sustainable Use License, not OSI-approved open source. You cannot resell n8n as a competing SaaS product. Internal and commercial use is permitted.
- **Frequent minor releases:** Weekly releases mean version pinning is essential for production stability. Test updates in staging before applying to production.
- **Resource sizing:** Minimum 2 GB RAM / 2 CPU cores for small teams; 4 GB+ recommended. Heavy AI-node workloads or high concurrency require horizontal scaling with Redis queue mode.

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

> Raw results JSON: `benchmarks/llmops-platforms-n8n-<date>.json`

---

## Bug Notes

### Smoke gate findings
- Not yet tested

### Known issues (from community / docs)
- Data loss on update without persistent volumes: Self-hosted instances using SQLite without mapped Docker volumes lose all workflow data and credentials during container updates. This is a top community support issue.
- Frequent minor releases causing instability: n8n releases weekly. Teams without version pinning experience breakage from rapid updates. The recommended practice is to pin the Docker image tag and test in staging.
- Fair-code license confusion: Users frequently mistake n8n for fully open-source (OSI-approved). The Sustainable Use License prohibits reselling n8n as a SaaS, which creates legal ambiguity for agencies offering managed n8n hosting.
- Queue mode complexity: Scaling beyond a single instance requires Redis-backed queue mode with PostgreSQL. Setup is not trivial and requires understanding of n8n's worker architecture.
- Self-hosting not recommended for non-technical users: n8n's own documentation warns that self-hosting is best suited for advanced users. Security misconfigurations (exposed webhooks, missing SSL, weak basic auth) are common in community deployments.
- Expression syntax learning curve: n8n uses a custom JSON-based expression syntax (`{{ $json.field }}`) that confuses new users accustomed to JavaScript or Python. Debugging data structures between nodes is a frequent friction point.

### Workarounds documented
- Always map `~/.n8n` to a Docker volume and use PostgreSQL + Redis for production.
- Pin Docker image tags (e.g., `docker.n8n.io/n8nio/n8n:1.42.1`) and update via a staged rollout.
- Use community templates (2,000+) to accelerate workflow building and avoid expression syntax errors.

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
- **Self-hosted (Community):** Free forever under fair-code license; unlimited workflows, unlimited executions, all integrations. No subscription fees.
- **n8n Cloud Starter:** ~€20/month — managed hosting, basic team features.
- **n8n Cloud Pro:** ~€50/month — higher execution volume, advanced features.
- **n8n Cloud Enterprise:** Custom pricing — dedicated support, SSO, audit logs, custom SLAs.
- **Execution-based billing:** Cloud plans bill by workflow executions, not per-step (cheaper than Zapier/Make for complex flows).

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0–$20/mo | Self-hosted on a $5–$12 VPS or Cloud Starter |
| Medium (10-100 users) | $50–$500/mo | Cloud Pro or self-hosted with PostgreSQL + Redis on VPS |
| Large (100+ users) | $500–$2,000/mo | Self-hosted with queue workers, load balancing, or Enterprise cloud |
| Enterprise | Custom | Dedicated cloud instance or on-prem Kubernetes with enterprise support |

### Hidden costs
- **Infrastructure:** Self-hosted requires a VPS or cloud VM ($5–$200+/mo), plus PostgreSQL and Redis for production.
- **Ops overhead:** Self-hosting demands Docker/server management, backups, SSL, monitoring, and version pinning.
- **LLM API costs:** AI-node usage incurs separate provider charges (OpenAI, Anthropic, etc.).
- **Migration cost:** Switching from Zapier/Make to n8n requires re-building workflows and training staff on expressions/data structures.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Docker, npm, or Kubernetes deployment; full data control |
| Open source | Partial (Fair-code) | Source-available under Sustainable Use License; not OSI-approved open source |
| Audit trail | Yes | Built-in execution logs; PostgreSQL retains full history |
| Data residency controls | Yes | Self-hosted deployment keeps all data on customer's infrastructure |
| On-premise deployment | Yes | Can run on private servers, air-gapped networks, or sovereign cloud |
| Export format | JSON / API | Workflows and credentials exportable; full DB export via PostgreSQL |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Cloud version is SOC 2 Type II compliant; self-hosted compliance is customer's responsibility |
| GDPR | Yes | EU-based company (Berlin); built-in GDPR-friendly data handling practices |
| HIPAA | No | No BAA or HIPAA-specific documentation found for self-hosted or cloud |
| ISO 27001 | ⏳ TBD | Not publicly attested |
| EU AI Act | ⏳ TBD | Not documented |
| FedRAMP | No | Not listed |

---

## Related Tools

### Tier A peers in same category
- [Dify](dify.md)
- [Flowise](flowise.md)
- [Vellum](vellum.md)
- [PromptLayer](promptlayer.md)
- [Pezzo](pezzo.md)
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)
- [Make](make.md)

### Complementary tools
- **Langfuse** — LLM observability and tracing; integrates with n8n AI nodes for production monitoring
- **Ollama / LocalAI** — Self-hosted LLM inference; commonly triggered via n8n HTTP or AI nodes
- **Supabase / PostgreSQL** — Database backend for n8n workflows and data persistence
- **Redis** — Required for n8n queue mode and caching at scale

### Alternatives to consider
- **Zapier** — Easier for non-technical users and simple one-to-one integrations; choose if you don't need custom code or data sovereignty
- **Make (Integromat)** — More visual and module-focused than Zapier; good for marketing and CRM automations where n8n's learning curve is too steep
- **Temporal** — Code-first durable workflow orchestration; choose if you need long-running, failure-resistant workflows in Go/Java/Python/TypeScript without a visual editor
- **Activepieces** — MIT-licensed alternative; choose if you need a fully OSI-approved open-source automation platform rather than fair-code

---

## Links

- Official site: [https://n8n.io](https://n8n.io)
- GitHub: [https://github.com/n8n-io/n8n](https://github.com/n8n-io/n8n)
- Documentation: [https://docs.n8n.io](https://docs.n8n.io)
- Community / Forum: [https://community.n8n.io](https://community.n8n.io)
- Community / Discord: [https://discord.gg/n8n](https://discord.gg/n8n) (official Discord, ~73,000 members)
- Template Marketplace: [https://n8n.io/workflows](https://n8n.io/workflows)
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
