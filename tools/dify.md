# Dify

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: LLM App Builder
- **License**: Modified Apache-2.0
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> 142K stars; visual workflow, RAG, Agent; most-starred OSS; commercial restrictions on multi-tenant SaaS

---

## Overview

Dify is an open-source LLM application development platform operated by LangGenius, Inc., first released in May 2023. With over 142,000 GitHub stars, it is the most-starred open-source LLM platform in the ecosystem. Dify combines a visual workflow builder, an agent framework, RAG (Retrieval-Augmented Generation) pipelines, and knowledge-base management into a unified environment. The platform supports five application types: chatbots, single-agent, text generation, chatflows, and workflows. In 2025, Dify introduced a v1.0 plugin ecosystem and marketplace, enabling extensible tools, strategies, and model integrations.

Dify is licensed under a modified Apache-2.0 license that permits commercial use with two key restrictions: (1) multi-tenant SaaS deployments require an explicit commercial license from LangGenius, and (2) the Dify logo and copyright information in the frontend may not be removed. The platform is available both as a cloud-hosted service and as a self-hosted community edition. The cloud service imposes limits on apps, requests, and memory based on the plan, while the self-hosted option is free and unlimited but requires Docker-based deployment. Dify offers native integrations with Langfuse for observability and supports OpenTelemetry tracing for production monitoring.

Dify positions itself as a "Backend-as-a-Service meets LLMOps" platform, targeting startup PMs validating AI features, platform teams seeking self-hostable stacks, and agencies assembling reusable AI workflows. Its visual editor covers common building blocks (LLM calls, retrieval, conditionals, HTTP requests, code nodes) and emphasizes a queue-based execution engine for resilience. RAG features include hybrid retrieval, configurable top-k, optional reranking, and integrations with vector stores such as pgvector, Milvus, Weaviate, and Qdrant.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `git clone` to working | ~10–15 min | Depends on Docker image pull speed and network |
| Dependency count | Direct + transitive | High (~10 containers) | api, worker, worker_beat, web, plugin_daemon, postgres, redis, weaviate, sandbox, nginx, ssrf_proxy |
| Docker required? | Yes / No | Yes | Docker Compose is the recommended path |
| Language runtime | Required version | Node.js 18+, Python 3.10+ | Backend is Python; frontend is Next.js |
| Auth complexity | API key / OAuth / None | Admin account setup | First-run wizard at `http://localhost/install` |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | Known issue: install page may spin on first boot |

### Setup commands (expected)
```bash
# Clone and deploy via Docker Compose
git clone --branch "$(curl -s https://api.github.com/repos/langgenius/dify/releases/latest | jq -r .tag_name)" https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
# Edit .env to set SECRET_KEY, DB credentials, and vector store choice
docker compose up -d
# Access UI at http://localhost/install and create admin account
```

### Known sharp edges
- **First-boot spinner:** The `localhost/install` page may hang on initial startup; refreshing or waiting for all containers to finish initializing usually resolves it.
- **Volume backups:** All Dify data lives in the `docker/volumes` folder. Upgrades require explicit backup and restore of this directory.
- **NumExpr warnings:** On machines with many cores, NumExpr may log a safe-thread-limit warning; this is cosmetic but can be silenced by setting `NUMEXPR_MAX_THREADS`.
- **Multi-tenant licensing:** Self-hosting is free, but operating a multi-tenant SaaS requires a commercial license from LangGenius.

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

> Raw results JSON: `benchmarks/llmops-platforms-dify-<date>.json`

---

## Bug Notes

### Smoke gate findings
- Not yet tested

### Known issues (from community / docs)
- First-boot `localhost/install` spinner: Multiple community reports (CSDN, blog posts) note that the initial install page may hang with a loading spinner on first Docker startup. Resolution: wait for all containers to fully initialize, then refresh.
- NumExpr threading warning: On machines with high core counts, NumExpr logs a safe-thread-limit warning. This is cosmetic but can be silenced by setting the `NUMEXPR_MAX_THREADS` environment variable.
- Volume backup requirement: Upgrading Dify requires explicitly backing up the `docker/volumes` directory; otherwise, data is lost during container recreation.
- Multi-tenant licensing ambiguity: Self-hosting is free, but operating a multi-tenant SaaS (multiple workspaces per installation) requires a commercial license from LangGenius. The boundary between "internal use" and "SaaS" is not always clear in practice.
- Ollama Docker networking: Users report confusion when connecting Dify (in Docker) to Ollama (running natively). The `BaseURL` must use `http://host.docker.internal:11434` instead of `localhost` or `127.0.0.1`.

### Workarounds documented
- Set `NUMEXPR_MAX_THREADS=16` in environment to suppress NumExpr warnings.
- Use `docker compose down` + backup `volumes/` before any Dify upgrade.

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
- **Cloud Sandbox (Free):** 200 OpenAI calls (trial), suitable for individuals and exploration.
- **Cloud Professional:** $59/month — 5,000 message credits/month, expanded features for small teams.
- **Cloud Team:** $159/month — collaborative projects with more resources.
- **Cloud Enterprise:** Custom pricing — SSO, advanced security, dedicated support, custom limits.
- **Self-hosted Community:** Free, unlimited usage, full data control. Requires Docker deployment and self-management.
- **Self-hosted Enterprise:** Commercial license — multi-tenancy, priority support, custom branding. Contact business@dify.ai for licensing.
- **AWS Premium (AMI):** VPC-deployable AMI option for private environments.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0–$159/mo | Free self-hosted or Cloud Sandbox/Professional |
| Medium (10-100 users) | $159–$1,000/mo | Team tier or self-hosted with infrastructure costs |
| Large (100+ users) | $1,000–$5,000/mo | Enterprise cloud or self-hosted + ops team overhead |
| Enterprise | Custom | Commercial license + AWS AMI + dedicated support |

### Hidden costs
- **Infrastructure:** Self-hosted requires servers, PostgreSQL, Redis, vector DB, and backup storage.
- **LLM API costs:** Dify does not mark up provider calls; OpenAI/Anthropic/Azure costs are separate.
- **Commercial license:** Multi-tenant SaaS use requires explicit licensing from LangGenius.
- **Ops time:** Self-hosted deployments need a team to manage Docker, networking, SSL, and updates.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Docker Compose and Kubernetes deployment supported; full data control |
| Open source | Yes (Modified Apache-2.0) | Multi-tenant SaaS use requires commercial license; logo/copyright must remain in frontend |
| Audit trail | Yes | Built-in request logging and Langfuse integration |
| Data residency controls | Yes | Self-hosted deployment keeps all data on customer's infrastructure |
| On-premise deployment | Yes | Docker/Kubernetes on private servers or VPC; AWS Premium AMI also available |
| Export format | JSON / API | Workflows and prompts exportable via API; full DB export via PostgreSQL dump |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | ⏳ TBD | No public attestation found as of mid-2025; enterprise buyers should request during procurement |
| GDPR | Yes | EU-friendly data handling; self-hosting provides full control |
| HIPAA | No | No BAA or HIPAA-specific documentation found |
| ISO 27001 | ⏳ TBD | Not publicly attested |
| EU AI Act | ⏳ TBD | Compliance posture not documented |
| FedRAMP | No | Not listed |

---

## Related Tools

### Tier A peers in same category
- [Flowise](flowise.md)
- [n8n](n8n.md)
- [Vellum](vellum.md)
- [PromptLayer](promptlayer.md)
- [Pezzo](pezzo.md)
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)
- [Make](make.md)

### Complementary tools
- **Langfuse** — Observability and tracing for Dify workflows (native integration available)
- **Ollama** — Local LLM hosting; commonly paired with Dify for on-premise model serving
- **Milvus / Zilliz** — Vector database; community guides for enhanced RAG performance
- **OpenTelemetry** — Production tracing and metrics collection

### Alternatives to consider
- **Langflow** — Python-based visual LLM builder; good alternative if your team prefers Python over Dify's JavaScript/TypeScript stack
- **Botpress** — Conversation-first platform; choose if your primary need is chatbots rather than general workflow orchestration
- **Flowise** — Simpler LangChain-native builder; better for rapid prototyping when you don't need Dify's full LLMOps feature set

---

## Links

- Official site: [https://dify.ai](https://dify.ai)
- GitHub: [https://github.com/langgenius/dify](https://github.com/langgenius/dify)
- Documentation: [https://docs.dify.ai](https://docs.dify.ai)
- Community / Discord: [https://discord.gg/8Tpq4AcN](https://discord.gg/8Tpq4AcN) (Dify official Discord)
- Blog: [https://dify.ai/blog](https://dify.ai/blog)
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
