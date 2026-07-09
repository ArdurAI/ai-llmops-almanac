# Dify


[![Agent Frameworks](https://img.shields.io/badge/Also_in-Agent_Frameworks-blue)](https://github.com/ArdurAI/ai-agent-framework-almanac) [![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: LLM App Builder
- **License**: Modified Apache-2.0
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-07-09

> 148.3K stars; visual workflow, RAG, Agent; most-starred OSS; commercial restrictions on multi-tenant SaaS

---

## Overview

Dify is an open-source LLM application development platform operated by LangGenius, Inc., first released in May 2023. With over 148,000 GitHub stars, it is the most-starred open-source LLM platform in the ecosystem. Dify combines a visual workflow builder, an agent framework, RAG (Retrieval-Augmented Generation) pipelines, and knowledge-base management into a unified environment. The platform supports five application types: chatbots, single-agent, text generation, chatflows, and workflows. In 2025, Dify introduced a v1.0 plugin ecosystem and marketplace, enabling extensible tools, strategies, and model integrations.

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

## Deep Analysis

### Daily monitoring update — 2026-07-09

- **Adoption signal:** GitHub stars moved from 147,539 to 148,302 (+763). Star references in this file now use the new 148,302 baseline.
- **Community health:** Open issues decreased from 880 to 822 (-58). This is a positive backlog-reduction signal.

### 1. How Is This Tool Useful?

Dify is an open-source LLM application development platform (modified Apache 2.0, 148,000+ GitHub stars) that combines a visual workflow builder, agent framework, RAG pipelines, and knowledge-base management into a unified environment. As the most-starred open-source LLM platform, it supports five application types: chatbots, agents, text generation, chatflows, and workflows. Dify is particularly useful for teams that want a self-hostable, visual-first alternative to code-based frameworks.

### 2. Gotchas of Using This Tool

Dify's license (modified Apache 2.0) restricts commercial multi-tenant SaaS offerings — teams building products on Dify must carefully review the licensing terms. The platform's visual editor, while powerful, can become complex for non-trivial workflows and debugging visual flows is harder than debugging code. Initial Docker deployment can be slow, with the install page occasionally hanging on first boot. The plugin ecosystem (introduced in v1.0, 2025) is still maturing.

### 3. Limitations

Dify's multi-agent orchestration capabilities are less sophisticated than dedicated frameworks like CrewAI or LangGraph. The RAG pipeline configuration is less granular than specialized RAG tools like RagFlow or LlamaIndex. Performance monitoring and observability features are basic compared to Langfuse or LangSmith. The platform's API rate limiting and scalability under high concurrent load are not well-documented for self-hosted deployments.

### 4. How Secure Is This Tool?

Dify is open-source under a modified Apache 2.0 license, allowing independent security review. The platform supports on-premise deployment with full data control. No major CVEs have been reported as of early 2026. The platform provides API key management and basic RBAC. Teams deploying Dify should secure the PostgreSQL and Redis backends, use HTTPS, and follow container security best practices. The modified license's commercial restrictions should be reviewed by legal counsel.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 7/10.** Dify's visual workflow builder makes LLM application creation accessible to semi-technical users. Non-technical users can create basic chatbots and workflows, though complex configurations still require developer assistance.

### 6. What Does This Tool Solve That Others Don't?

Dify's unique strength is its unified platform approach — combining visual workflow building, RAG, agent orchestration, and knowledge management in a single self-hostable product. The 148,000+ GitHub stars and large community provide extensive integrations and templates. Its 'Backend-as-a-Service meets LLMOps' positioning with API endpoints for every app type is distinctive. The v1.0 plugin marketplace creates an ecosystem for extensibility.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Dify | LLM app builder | Most-starred OSS |
| 2 | Flowise | Visual LLM builder | LangChain-native |
| 3 | Langflow | Visual flows | IBM-backed |
| 4 | n8n | Workflow automation | 400+ integrations |
| 5 | Coze | No-code bot builder | Free + multi-channel |

### 8. How Can This Tool Be Improved? How Active Is Development?

Dify is very actively developed by LangGenius with frequent releases and a large community. Key improvements include deeper multi-agent orchestration, more granular RAG configuration, built-in observability (or tighter Langfuse integration), better performance documentation, and clearer enterprise pricing for the cloud version. The plugin marketplace needs more curated and verified plugins.

### 9. Official Maintainer Contacts

Dify is maintained by LangGenius, Inc. GitHub: https://github.com/langgenius/dify. Website: https://dify.ai. Documentation: https://docs.dify.ai. Discord: https://discord.gg/8Tpq4AcN (official Dify Discord).

### 10. General Usage Guidance

Use Dify if you want a self-hostable, visual-first LLM app builder with strong community support. Carefully review the modified Apache 2.0 license before commercial use. For code-first development, evaluate LangChain or LlamaIndex. For deeper RAG capabilities, consider RagFlow. Start with Docker Compose for local development, then scale to Kubernetes for production.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
