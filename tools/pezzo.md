# Pezzo

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: LLMOps Platform
- **License**: Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Developer-first; prompt design, version management, troubleshooting; two lines of code

---

## Overview

Pezzo is an open-source, developer-first LLMOps platform licensed under Apache 2.0. Founded in 2023 and based in the United States, it focuses on streamlining prompt design, version management, instant delivery, and observability. Pezzo's signature integration promise is "two lines of code" to wrap an existing LLM client and gain centralized prompt management, request monitoring, and cost/latency tracking.

Pezzo is built on a modern cloud-native stack: a GraphQL API, PostgreSQL for relational metadata, ClickHouse for high-volume observability traces, Redis for caching, and Supertokens for authentication. The platform's standout feature is its "Time Travel" debugger, which allows developers to tweak a failed prompt and re-run it in-browser to verify fixes. Pezzo supports prompt versioning with environment-based deployments (e.g., Development, Staging, Production), enabling teams to update prompts without redeploying application code.

**Important advisory:** Multiple industry observers report that Pezzo's active development effectively ceased after June 2025, with no major commits or SDK updates in over nine months. The Python client has not been meaningfully updated since 2023 and is reportedly incompatible with modern features like structured output and tool-calling. Teams building new projects should treat Pezzo as a risky bet and consider more actively maintained alternatives such as Langfuse or Agenta for prompt management needs. Pezzo remains viable for small, Node.js-only teams that value self-hosting and the "Time Travel" debugging experience.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `git clone` to working | ~15–25 min | Docker Compose path for full stack; longer for development build from source |
| Dependency count | Direct + transitive | Moderate–High | PostgreSQL, ClickHouse, Redis, Supertokens, Node.js 18+, Prisma, GraphQL |
| Docker required? | Yes / No | Yes (recommended) | `docker-compose.infra.yaml` provided for dependencies; full stack Docker Compose available |
| Language runtime | Required version | Node.js 18+ | Server runs on Node.js; console is a separate frontend app |
| Auth complexity | API key / OAuth / None | API key + Supertokens | Self-hosted auth managed via Supertokens; cloud uses API keys |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | Multiple moving parts (DB migrations, GraphQL codegen, infra services) |

### Setup commands (expected)
```bash
# Clone and install dependencies
git clone https://github.com/pezzolabs/pezzo.git
cd pezzo
npm install

# Start infrastructure dependencies
docker-compose -f docker-compose.infra.yaml up

# Run DB migrations and start server
npx dotenv-cli -e apps/server/.env -- npx prisma migrate deploy --schema apps/server/prisma/schema.prisma
npx nx serve server

# In a separate terminal, start GraphQL codegen watcher and console
npm run graphql:codegen:watch
npx nx serve console
# Console accessible at http://localhost:4200
```

### Known sharp edges
- **Development stagnation risk:** Multiple independent reviewers (e.g., nolist.ai, March 2026) report that Pezzo's active development effectively ceased after June 2025, with no major commits or SDK updates in 9+ months. Teams should verify GitHub activity before committing.
- **Python SDK lag:** The Python client has not seen a meaningful update since 2023 and is reportedly incompatible with structured output and tool-calling features that became standard in 2025. Pezzo is effectively a Node.js/TypeScript-only ecosystem.
- **Multi-service complexity:** Self-hosting requires managing PostgreSQL, ClickHouse, Redis, and Supertokens. This is heavier than simpler single-container alternatives like Dify or Flowise.
- **GraphQL codegen dependency:** Development mode requires running a separate `graphql:codegen:watch` process, which adds friction to local development and can fail if the server is not already running.

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

> Raw results JSON: `benchmarks/llmops-platforms-pezzo-<date>.json`

---

## Bug Notes

### Smoke gate findings
- Not yet tested

### Known issues (from community / docs)
- **Development stagnation (critical):** Multiple independent sources (nolist.ai, community comparisons) report that Pezzo's active development effectively ceased after June 2025, with no major commits or SDK updates in 9+ months. Verify current GitHub activity before committing to a new project.
- Python SDK incompatibility: The Python client has not seen a meaningful update since 2023 and is reportedly incompatible with modern LLM features such as structured output and tool-calling. This makes Pezzo effectively a Node.js/TypeScript-only platform.
- Multi-service operational burden: Self-hosting requires managing PostgreSQL, ClickHouse, Redis, and Supertokens alongside the Pezzo server and console. This is significantly heavier than single-container alternatives like Dify or Flowise.
- GraphQL codegen friction: Local development requires running `graphql:codegen:watch` in a separate terminal, which adds setup friction and can fail silently if the server is not yet healthy.
- Small community and ecosystem: Unlike Dify or Langfuse, Pezzo has a limited community, fewer third-party integrations, and no active marketplace or plugin ecosystem.
- "Time Travel" debugger limitations: While praised for troubleshooting single prompt failures, it does not scale well to multi-turn conversations or complex agent loops.

### Workarounds documented
- Node.js/TypeScript teams can use the actively maintained client; Python teams should evaluate alternatives (Langfuse, Agenta) for prompt management.
- Use the Docker Compose full-stack path rather than development-mode `nx serve` to avoid GraphQL codegen complexity in production deployments.
- Monitor the GitHub repository's commit history and issue tracker before making a long-term commitment.

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
- **Cloud Free:** $0 — 10,000 requests/month, suitable for small projects and evaluation.
- **Cloud Pro:** $99/month — higher request limits, advanced features.
- **Self-hosted (Community):** Free forever under Apache 2.0; all core features, no usage limits, full data control.
- **Enterprise:** Custom pricing — dedicated support, custom SLAs, advanced security features.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0–$99/mo | Cloud Free or Pro; self-hosted free with infrastructure cost |
| Medium (10-100 users) | $99–$500/mo | Cloud Pro or self-hosted with PostgreSQL/ClickHouse/Redis |
| Large (100+ users) | $500–$2,000/mo | Self-hosted with dedicated infra or Enterprise cloud |
| Enterprise | Custom | Annual contract, dedicated support |

### Hidden costs
- **Infrastructure (self-hosted):** PostgreSQL, ClickHouse, Redis, and Supertokens require dedicated compute and storage. ClickHouse in particular can be resource-intensive for high-volume observability traces.
- **Ops time:** Managing four separate backend services (DB, analytics, cache, auth) plus the Pezzo server and console requires DevOps expertise.
- **Stagnation risk:** If development has indeed stalled, teams may face unpatched vulnerabilities or compatibility issues with future LLM provider APIs, creating technical-debt remediation costs.
- **Limited ecosystem:** The small community and inactive Python SDK mean teams may need to build custom integrations rather than relying on community plugins.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Full Docker Compose stack available; all data stays on customer infrastructure |
| Open source | Yes (Apache-2.0) | Fully permissive license; no commercial restrictions |
| Audit trail | Yes | ClickHouse stores high-volume observability traces; PostgreSQL stores metadata |
| Data residency controls | Yes | Self-hosted deployment provides complete data control |
| On-premise deployment | Yes | Docker Compose on private servers or sovereign cloud |
| Export format | JSON / API / DB dump | Prompts and requests exportable via GraphQL API; full DB export via PostgreSQL/ClickHouse |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | No | No public attestation or documentation found |
| GDPR | ⏳ TBD | Not explicitly documented; self-hosting provides control but no official GDPR guidance |
| HIPAA | No | No BAA or HIPAA-specific documentation found |
| ISO 27001 | No | Not publicly attested |
| EU AI Act | ⏳ TBD | Not documented |
| FedRAMP | No | Not listed |

---

## Related Tools

### Tier A peers in same category
- [Dify](dify.md)
- [Flowise](flowise.md)
- [n8n](n8n.md)
- [Vellum](vellum.md)
- [PromptLayer](promptlayer.md)
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)
- [Make](make.md)

### Complementary tools
- **OpenAI** — Primary LLM provider for Pezzo client SDK; `PezzoOpenAI` wrapper is the most documented integration
- **PostgreSQL / ClickHouse / Redis** — Infrastructure dependencies; Pezzo relies on these for metadata, observability, and caching
- **Supertokens** — Authentication provider used in Pezzo's self-hosted stack

### Alternatives to consider
- **Langfuse** — Active open-source alternative with superior feature parity and ongoing development; strongly recommended over Pezzo for new projects
- **Agenta** — MIT-licensed open-source LLMOps platform with active community; choose if you need broader language support and maintained SDKs
- **Dify** — Full visual workflow builder + prompt management; choose if you need more than just prompt management and observability
- **PromptLayer** — Managed SaaS prompt management; choose if you prefer not to self-host and need non-technical user collaboration

---

## Links

- Official site: [https://pezzo.ai](https://pezzo.ai)
- GitHub: [https://github.com/pezzolabs/pezzo](https://github.com/pezzolabs/pezzo)
- Documentation: [https://docs.pezzo.ai](https://docs.pezzo.ai)
- Community / Discord: ⏳ (no public community Discord found)
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
