# Flowise

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Visual LLM Builder
- **License**: Apache-2.0
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> 54.9K stars; drag-and-drop LLM flows; LangChain-native; self-hostable; owned by Workday

---

## Overview

Flowise is an open-source, low-code platform for building AI agents and LLM workflows visually, often described as a "Figma for AI." Founded in 2023 by Henry Heng and Chung Yau Ong and backed by Y Combinator (S23), it wraps LangChain complexity into drag-and-drop components for RAG pipelines, chatbots, and multi-agent systems. Flowise has accumulated roughly 49,000–55,000 GitHub stars and is used by Fortune 500 companies including Deloitte and Accenture, as well as thousands of smaller teams. In August 2025, Workday acquired Flowise to embed its visual agent builder into Workday's HR and finance platform, signaling enterprise-grade adoption of no-code LLM tooling.

Flowise's architecture is built on TypeScript, Node.js, and React. It supports 100+ integrations across LLMs, vector databases, document loaders, and third-party tools. The platform offers both a visual canvas for non-technical users and programmatic APIs/SDKs for developers. Completed flows can be published as REST APIs or embeddable JavaScript widgets, making it accessible to fractional engineers and client teams without deep AI backgrounds. Flowise includes human-in-the-loop checkpoints, execution tracing, and observability integrations with Prometheus, OpenTelemetry, and Grafana. It is licensed under Apache 2.0 and is fully self-hostable via Docker or direct Node.js installation.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `git clone` to working | ~5–10 min | `npm install -g flowise` or Docker pull |
| Dependency count | Direct + transitive | Moderate | Node.js monorepo: server, ui, components, api-documentation |
| Docker required? | Yes / No | Optional | Docker Compose recommended for production; npm works for quick start |
| Language runtime | Required version | Node.js 18.15+ | PNPM preferred for development builds |
| Auth complexity | API key / OAuth / None | API key (LLM providers) | No built-in auth for self-hosted community edition |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | Node heap OOM during build is a known issue on smaller VMs |

### Setup commands (expected)
```bash
# Quick start via npm
npm install -g flowise
npx flowise start
# Or Docker Compose (recommended for production)
git clone https://github.com/FlowiseAI/Flowise.git
cd Flowise/docker
cp .env.example .env
docker compose up -d
# Access UI at http://localhost:3000
```

### Known sharp edges
- **SQLite concurrency:** The default SQLite database causes data loss under concurrent writes. Production deployments must switch to PostgreSQL.
- **No native loops:** Flowise supports only If/Else branching; there are no native loop or iteration nodes, which limits complex multi-step agentic orchestration.
- **Node.js heap exhaustion:** Building from source can trigger `JavaScript heap out of memory` on machines with <4 GB RAM. Workaround: `export NODE_OPTIONS="--max-old-space-size=4096"` before `pnpm build`.
- **Visual debugging at scale:** As multi-agent flows grow, the canvas becomes difficult to trace and debug. Execution traces help but the UI does not collapse or zoom effectively for large graphs.
- **Enterprise features paywalled:** RBAC, SSO, and audit logging are locked behind the paid Enterprise tier even for self-hosted deployments.

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

> Raw results JSON: `benchmarks/llmops-platforms-flowise-<date>.json`

---

## Bug Notes

### Smoke gate findings
- Not yet tested

### Known issues (from community / docs)
- SQLite data loss under concurrency: Flowise defaults to SQLite, which is not safe for concurrent writes. Production deployments must switch to PostgreSQL to avoid data corruption. This is documented but easy to miss during quick-start setup.
- Node.js heap exhaustion during build: Building from source on machines with <4 GB RAM frequently triggers `JavaScript heap out of memory`. The workaround (`--max-old-space-size=4096`) is documented in the GitHub repo but not surfaced in the quick-start guide.
- No native loop nodes: Flowise supports only If/Else branching. Users requiring iteration (e.g., processing a list of items) must embed Python/JavaScript code nodes or use external orchestration, which complicates visual debugging.
- Enterprise features paywalled on self-host: RBAC, SSO, and audit logging are locked behind the Enterprise tier even when self-hosted. This surprises teams expecting fully open-source enterprise features.
- Workday acquisition roadmap uncertainty: Community concern that Workday's enterprise HR/finance focus may deprioritize general-purpose community features. No concrete deprecation announced, but direction is watched closely.

### Workarounds documented
- Switch to PostgreSQL by setting `DATABASE_PATH` or using the Docker Compose PostgreSQL configuration.
- Increase Node heap size: `export NODE_OPTIONS="--max-old-space-size=4096"` before building.

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
- **Self-hosted (Community):** Free forever under Apache 2.0; no usage limits.
- **Cloud Free:** Limited to 2 flows; suitable for evaluation.
- **Cloud Starter:** $35/month — expanded flows and team features.
- **Cloud Pro:** $65/month — higher limits, priority support.
- **Cloud Enterprise:** Custom pricing — SSO, RBAC, audit logging, dedicated support, custom SLAs.
- **Workday-embedded:** Pricing determined by Workday ecosystem (not publicly listed).

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0–$35/mo | Self-hosted free or Cloud Starter |
| Medium (10-100 users) | $65–$500/mo | Cloud Pro or self-hosted + infrastructure |
| Large (100+ users) | $500–$2,000/mo | Enterprise cloud or self-hosted + ops overhead |
| Enterprise | Custom | Workday partnership or direct Enterprise contract |

### Hidden costs
- **Infrastructure:** Self-hosted requires Node.js server, PostgreSQL (recommended), and Redis for queue scaling.
- **LLM API costs:** Separate provider billing (OpenAI, Anthropic, etc.) is not included.
- **Enterprise feature paywall:** RBAC, SSO, and audit logging require Enterprise tier even on self-hosted deployments.
- **Ops time:** Self-hosted production needs DB administration, backups, SSL, and update management.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Docker and npm installation supported; full control over data |
| Open source | Yes (Apache-2.0) | Full source code available; Workday acquisition has not changed license |
| Audit trail | Partial | Execution traces and Prometheus/OpenTelemetry metrics available; formal audit logs require Enterprise tier |
| Data residency controls | Yes | Self-hosted deployment keeps data on-premise |
| On-premise deployment | Yes | Docker or direct Node.js installation on private infrastructure |
| Export format | JSON / API | Flows exportable via API; DB export via PostgreSQL/SQLite |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | ⏳ TBD | No independent attestation found for Flowise specifically; Workday corporate SOC 2 may cover hosted offerings |
| GDPR | Yes | EU-friendly; self-hosting provides full control |
| HIPAA | No | No BAA or HIPAA-specific documentation found |
| ISO 27001 | ⏳ TBD | Not publicly attested |
| EU AI Act | ⏳ TBD | Not documented |
| FedRAMP | No | Not listed |

---

## Related Tools

### Tier A peers in same category
- [Dify](dify.md)
- [n8n](n8n.md)
- [Vellum](vellum.md)
- [PromptLayer](promptlayer.md)
- [Pezzo](pezzo.md)
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)
- [Make](make.md)

### Complementary tools
- **LangChain** — Flowise is built on LangChain; custom nodes can leverage LangChain's ecosystem directly
- **Ollama** — Local LLM hosting; frequently paired with Flowise for private model inference
- **Pinecone / Chroma / Weaviate / Qdrant** — Vector databases for RAG pipelines
- **Prometheus / Grafana / OpenTelemetry** — Monitoring and observability stack for production deployments

### Alternatives to consider
- **Langflow** — Python-based visual LLM builder; choose if your team prefers Python and DataStax ecosystem integration
- **Dify** — More comprehensive LLMOps platform; choose if you need built-in agent orchestration, plugin marketplace, and deeper observability
- **Uplizd** — Production-scale LangChain builder with multi-tenancy; choose if you need SaaS hosting with customer isolation and 99.9% LLM cost savings via caching

---

## Links

- Official site: [https://flowiseai.com](https://flowiseai.com)
- GitHub: [https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- Documentation: [https://docs.flowiseai.com](https://docs.flowiseai.com)
- Community / Discord: [https://discord.gg/jbaHfsRVBW](https://discord.gg/jbaHfsRVBW) (Flowise official Discord, ~12,400 members)
- Workday acquisition announcement: [https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise](https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise)
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

Flowise is an open-source, low-code platform (Apache 2.0, ~49,000-55,000 GitHub stars) for building AI agents and LLM workflows visually — often described as a 'Figma for AI.' Founded in 2023 and Y Combinator S23-backed, it wraps LangChain complexity into drag-and-drop components for RAG pipelines, chatbots, and multi-agent systems. Acquired by Workday in August 2025, it is used by Fortune 500 companies including Deloitte and Accenture.

### 2. Gotchas of Using This Tool

Flowise's visual builder, while intuitive for prototyping, becomes difficult to debug for complex workflows — visual canvas debugging is inherently harder than code-based debugging. The platform wraps LangChain, meaning it inherits LangChain's abstraction complexity and breaking changes. Performance with large workflows (many nodes) can degrade. The Workday acquisition has raised questions about the future of the open-source community edition vs. the enterprise product.

### 3. Limitations

Flowise is tightly coupled to LangChain, meaning its capabilities are bounded by LangChain's feature set. Custom components require JavaScript/TypeScript knowledge, creating a barrier for non-technical users who want to extend beyond pre-built components. The platform's observability features are basic compared to Langfuse or LangSmith. Version control for visual workflows is challenging — canvas state is stored as JSON, making diffs hard to review.

### 4. How Secure Is This Tool?

Flowise is open-source under Apache 2.0, allowing independent security review. The platform supports credential management for API keys with encryption. A security advisory (CVE-2024-xxxxx class vulnerabilities in the authentication middleware) was identified and patched in 2024 — teams should ensure they run the latest version. The Workday acquisition may bring enterprise-grade security practices. Teams self-hosting should secure the database backend and API endpoints.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 6/10.** Flowise's drag-and-drop interface is accessible to semi-technical users for building simple chatbots. Non-technical users can create basic flows, but complex configurations require developer support.

### 6. What Does This Tool Solve That Others Don't?

Flowise's unique strength is its visual-first approach to LangChain orchestration — the drag-and-drop canvas makes LangChain accessible to users who find the code API intimidating. The Workday acquisition validates its enterprise readiness. The large component library (wrapping LangChain integrations) and the ability to export flows as APIs differentiate it from code-only frameworks.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Dify | LLM app builder | Most-starred OSS |
| 2 | Flowise | Visual LLM builder | LangChain-native |
| 3 | Langflow | Visual flows | IBM-backed |
| 4 | n8n | Workflow automation | 400+ integrations |
| 5 | Coze | No-code bot builder | Free + multi-channel |

### 8. How Can This Tool Be Improved? How Active Is Development?

Flowise is actively developed, though the Workday acquisition's impact on the open-source roadmap is uncertain. Key improvements include decoupling from LangChain's breaking changes, improving canvas performance for large workflows, adding native observability, implementing version control for visual flows, and clarifying the open-source vs. enterprise feature split post-acquisition.

### 9. Official Maintainer Contacts

Flowise is maintained by the Flowise team (now part of Workday). GitHub: https://github.com/FlowiseAI/Flowise. Website: https://flowiseai.com. Documentation: https://docs.flowiseai.com. Discord: https://discord.gg/jbaHfsRVBW (~12,400 members).

### 10. General Usage Guidance

Use Flowise if you want a visual, drag-and-drop approach to building LLM applications and are already committed to the LangChain ecosystem. The Workday acquisition provides enterprise confidence but monitor the open-source roadmap. For a more comprehensive platform, evaluate Dify. For code-first development, use LangChain directly. Secure credentials and keep the platform updated to avoid known vulnerabilities.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
