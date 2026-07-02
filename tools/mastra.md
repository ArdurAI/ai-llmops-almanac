# Mastra

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Agent Framework
- **License**: Apache 2.0 (core); Mastra Enterprise License (ee/)
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Modern TypeScript-first stack; workflow orchestration, memory, evals; built by the Gatsby team (YC W25)

---

## Overview

Mastra is an open-source, TypeScript-native framework for building production-ready AI agents, agentic workflows, and RAG pipelines. Created by the team behind Gatsby (Sam Bhagwat, Abhi Aiyer, Shane Thomas) and graduating from Y Combinator's Winter 2025 batch with $13M in funding, Mastra shipped its v1.0 release in January 2026 and has since accumulated over 24,600 GitHub stars and 300,000+ weekly npm downloads. It is widely regarded as the most cohesive TypeScript-first agent framework on the market, filling a gap that had left JavaScript developers assembling half a dozen separate libraries to achieve what Python teams could do with LangChain or LlamaIndex.

The framework ships six core primitives in a single package: **Agents** (autonomous LLM-driven decision makers with typed tools), **Workflows** (deterministic multi-step pipelines with branching, parallel execution, loops, and human-in-the-loop suspend/resume), **Memory** (a four-tier system covering message history, working memory, semantic recall via vector search, and observational memory), **RAG** (document chunking, embedding, vector store management, and reranking), **Evals** (model-graded, rule-based, and statistical evaluation harnesses), and **Observability** (built-in OpenTelemetry tracing). Mastra Studio, a local development UI running at `localhost:4111`, provides agent testing, workflow visualization, memory inspection, and trace replay without requiring any frontend code.

Mastra's design philosophy is explicitly "TypeScript-first, not TypeScript-as-an-afterthought." There is no Python SDK, and the team has stated this is by design. Every API uses Zod for type-safe schemas, sub-path imports keep bundles lean (`@mastra/core/agent`, `@mastra/core/workflows`), and deployment adapters exist for Vercel, Netlify, Cloudflare Workers, and standalone Node.js servers. The model router connects to 3,300+ models from 94 providers through a single interface with automatic fallbacks. Production users include Replit (which powers its agent builder), Factorial, Counsel Health, Cedar, and SoftBank. Mastra Cloud, a managed hosting platform, is in preview with usage-based pricing.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `npx create-mastra` to working | ~2-5 minutes | CLI scaffolds project structure, config, and example code automatically |
| Dependency count | Direct + transitive | ~5-10 direct; ~30-50 transitive | Core is lean; storage and vector DB adapters add more |
| Docker required? | Yes / No | No | Optional for PostgreSQL vector DB or containerized deployment |
| Language runtime | Required version | Node.js 22.13.0+ | Bun also supported; TypeScript 5.0+ recommended |
| Auth complexity | API key / OAuth / None | API key | LLM provider keys (OpenAI, Anthropic, etc.) via environment variables |
| First-run failure rate | Smoke gate pass/fail | Low | Most failures are Node version mismatches or missing `.env` files |

### Setup commands (verified)
```bash
# Interactive scaffolding (recommended)
npx create-mastra@latest

# Or add to existing project
npm install mastra@latest

# Core with sub-path imports
npm install @mastra/core

# Add storage, vector DB, or evals as needed
npm install @mastra/pg @mastra/pinecone @mastra/evals

# Quick verification
npx mastra --version
```

### Known sharp edges
- **API surface shifting post-1.0**: Independent reviews note that the API surface was still evolving rapidly after the v1.0 release. Teams should pin to exact minor versions and review changelogs before upgrading.
- **No visual workflow builder**: Mastra Studio visualizes workflow execution and memory state for debugging, but workflows are code-defined only. There is no drag-and-drop canvas for non-technical users.
- **Opinionated defaults can become restrictive**: Community feedback (GitHub issues #8726, #2968) indicates that teams with workflows diverging from Mastra's assumptions may find the framework fighting them. This is a deliberate tradeoff for speed on the happy path.
- **Younger ecosystem than Python alternatives**: While growing fast, the integration catalog is smaller than LangChain's. Teams needing exotic vector DBs or legacy enterprise connectors may need to write custom adapters.
- **Enterprise RBAC is commercial**: Role-based access control and certain advanced governance features are gated behind the Mastra Enterprise License (source-available, not Apache 2.0).
- **Memory storage configuration complexity**: The four-tier memory system is powerful but requires careful storage backend configuration (LibSQL/Turso default, PostgreSQL, MongoDB, Upstash, etc.) to avoid performance bottlenecks.
- **Zod version compatibility**: Mastra uses Zod v4 for schemas. Projects using Zod v3 may encounter type conflicts or need to upgrade.

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

> Raw results JSON: `benchmarks/llmops-platforms-mastra-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- Workflow `.suspend()` / `.resume()` gates require explicit state serialization; complex state objects that are not JSON-serializable can fail to resume after a human-in-the-loop pause.
- OpenTelemetry bridge is marked experimental as of March 2026; bidirectional context propagation with existing observability stacks may drop spans.
- `@mastra/core` sub-path imports require modern bundlers (Vite, Rollup, esbuild); older webpack configs may need aliases.
- Vector store migration between adapters (e.g., Turso → Pinecone) is not automated; index rebuilds are required.
- Mastra Cloud (managed hosting) is in preview; production SLAs and regional availability are not yet published.

### Workarounds documented
- Use `superjson` or custom serializers for non-JSON state objects in suspend/resume workflows.
- Pin `@mastra/core` to an exact version in `package.json` and upgrade only after reviewing the release notes.
- For Next.js deployments, use the `output: 'standalone'` configuration to ensure server adapters bundle correctly.
- Use `mastra build` to pre-compile the project before deploying to Vercel or Cloudflare Workers to avoid cold-start issues.

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
- **Mastra core framework**: Free and open source (Apache 2.0).
- **Mastra Enterprise License**: Source-available license for advanced RBAC, governance, and support features.
- **Mastra Cloud**: Managed hosting in preview; usage-based pricing. Estimated entry point from $250/mo based on third-party reporting.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0 (framework) + ~$50-$100/mo (infra) | Node.js runtime + vector DB (Turso free tier or local Chroma). |
| Medium (10-100 users) | $0 (framework) + ~$200-$500/mo (infra) | PostgreSQL + Pinecone/Qdrant + hosting. |
| Large (100+ users) | $0 (framework) + ~$1,000-$5,000/mo (infra) | Mastra Cloud or self-hosted Kubernetes; multiple vector DBs. |
| Enterprise | Custom (Mastra Enterprise + Cloud) | Dedicated support, SLA, advanced RBAC, custom deployment. |

### Hidden costs
- **Vector database hosting**: Vector DB costs (Pinecone, Qdrant, Astra, etc.) are separate and can dominate infrastructure bills at scale.
- **Storage backend proliferation**: Mastra supports many storage adapters (PostgreSQL, MongoDB, DynamoDB, MSSQL, Cloudflare D1, etc.), but teams often end up running multiple databases for memory, workflows, and observability.
- **LLM API costs**: Framework is free, but the model router's automatic fallback and retry can increase token consumption if not capped.
- **TypeScript talent premium**: TypeScript developers are often more expensive than Python developers; this is a labor-market cost, not a product cost.
- **Eval compute**: Running `@mastra/evals` model-graded scorers on large datasets can generate significant LLM token costs during CI/CD.
- **Mastra Cloud preview risk**: No published SLA as of 2026; production deployments should consider self-hosting or waiting for GA.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Framework, Studio, and all agents run on any Node.js runtime. Mastra Cloud is SaaS. |
| Open source | Yes (core) | Apache 2.0 for core framework. Enterprise features are source-available under a commercial license. |
| Audit trail | Yes | OpenTelemetry traces can be exported to any backend; Mastra Studio stores local run history. |
| Data residency controls | Partial | Self-hosted deployment gives full control. Mastra Cloud residency policies not yet published. |
| On-premise deployment | Yes | Full framework runs air-gapped with local models (Ollama, vLLM) and local vector stores. |
| Export format | JSON, SQLite, PostgreSQL | Workflow state, memory, and traces are JSON-serializable; storage backends expose standard SQL. |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | ⏳ TBD | Mastra Cloud may pursue SOC 2; framework itself is open source with no certification. |
| GDPR | Partial | Self-hosted deployment allows full GDPR control. Mastra Cloud policies not yet published. |
| HIPAA | No | No explicit HIPAA compliance tooling or BAA available as of 2026. |
| ISO 27001 | ⏳ TBD | No published certification found for Mastra Cloud or framework. |
| EU AI Act | ⏳ TBD | No explicit published alignment or certification. |
| FedRAMP | No | Not applicable to open-source framework. |

> Note: Mastra is a young framework (launched 2025, v1.0 January 2026). Compliance certifications are likely pending for the managed Cloud offering. Self-hosted deployments place compliance responsibility on the developer's infrastructure.

---

## Related Tools

### Tier A peers in same category
- [LangChain](langchain.md) — Cross-platform LLM framework with 1,000+ integrations
- [LangGraph](langgraph.md) — Stateful graph-based agent orchestration from the LangChain team
- [OpenAI Agents SDK](openai-agents-sdk.md) — Lightweight OpenAI-native multi-agent primitives
- [CrewAI](crewai.md) — Role-based multi-agent collaboration (Python)
- [Semantic Kernel](semantic-kernel.md) — Microsoft enterprise SDK with deep Azure integration
- [Pydantic AI](pydantic-ai.md) — Type-safe Python agents with strict validation

### Complementary tools
- [Vercel AI SDK](https://sdk.vercel.ai/) — Low-level model routing and streaming; Mastra is built on top of it
- [Langfuse](langfuse.md) — Open-source observability; Mastra's OpenTelemetry bridge can export to it
- [Braintrust](braintrust.md) — Evaluation platform; can consume Mastra eval outputs
- [ClickHouse](https://clickhouse.com/) — Recommended observability storage for high-traffic Mastra deployments
- [Zod](https://zod.dev/) — Schema validation library used throughout Mastra's API

### Alternatives to consider
- **LangChain.js** — When you need the largest JavaScript integration catalog and can tolerate type leaks and less cohesive architecture.
- **Vercel AI SDK alone** — When you only need a chat completion behind a button and don't need workflows, memory, or evals.
- **Temporal / Inngest** — When workflows are deterministic, long-running, and LLM reasoning is incidental rather than the core loop.
- **Direct Next.js API routes + OpenAI SDK** — When the project is a simple prototype and the overhead of a full agent framework is unnecessary.

---

## Links

- Official site: https://mastra.ai
- GitHub: https://github.com/mastra-ai/mastra
- Documentation: https://mastra.ai/docs
- npm: https://www.npmjs.com/package/mastra
- Mastra Studio: https://mastra.ai/docs/local-dev/mastra-studio
- Discord community: https://discord.gg/mastra (5,500+ members as of 2026)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | Deep-dive content added | Overview, setup, pricing, sharp edges, and links populated from web research. |
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |

---

## Deep Analysis

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

Mastra is an open-source, TypeScript-native framework for building production AI agents, workflows, and RAG pipelines (24,600+ GitHub stars, 300,000+ weekly npm downloads). Created by the Gatsby team (Sam Bhagwat, Abhi Aiyer) and YC W25-backed with $13M funding, it shipped v1.0 in January 2026. It is the most cohesive TypeScript-first agent framework, filling the gap that left JavaScript developers assembling multiple libraries to achieve what Python teams could do with LangChain.

### 2. Gotchas of Using This Tool

Mastra is a relatively new framework (v1.0 in January 2026), meaning the ecosystem is still maturing and production case studies are limited. The opinionated defaults can become restrictive — community feedback (GitHub issues #8726, #2968) indicates teams with workflows diverging from Mastra's assumptions may find the framework fighting them. Documentation is growing but some edge cases are underdocumented. The TypeScript-only focus excludes Python-centric teams.

### 3. Limitations

Mastra is TypeScript-only — there is no Python SDK. The framework's ecosystem of integrations, while growing, is smaller than LangChain's 1,000+. Advanced RAG capabilities are less mature than LlamaIndex or Haystack. Multi-agent orchestration patterns are less battle-tested than CrewAI or LangGraph. The young age means fewer long-term production deployments to validate reliability. Some features may have undocumented limitations.

### 4. How Secure Is This Tool?

Mastra is open-source (Elastic License 2.0) with the code on GitHub for independent review. The framework executes tool functions and makes LLM API calls — teams should validate inputs and restrict tool permissions. No major CVEs have been reported as of early 2026. The framework is designed for deployment to Vercel, Cloudflare Workers, and other serverless platforms — teams should follow platform-specific security best practices.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 3/10.** Mastra is a developer framework requiring TypeScript/JavaScript proficiency. Non-technical users cannot use it directly; it requires engineering teams.

### 6. What Does This Tool Solve That Others Don't?

Mastra's unique strength is being the first truly cohesive TypeScript-first agent framework — built from the ground up for the JS/TS ecosystem rather than being a port from Python. The unified API for agents, workflows, RAG, and evaluation in TypeScript addresses a real gap. The deployment-first design (Vercel, Cloudflare Workers, Node.js) with `mastra build` for cold-start optimization is distinctive. The Gatsby team's experience with large-scale JS frameworks shows in the DX.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | CrewAI | Multi-agent (Python) | Production + enterprise |
| 2 | LangGraph | Graph orchestration | State persistence |
| 3 | Mastra | TS-first agents | TypeScript ecosystem |
| 4 | OpenAI Agents SDK | Lightweight agents | OpenAI-native |
| 5 | Pydantic AI | Type-safe agents | Pydantic ecosystem |

### 8. How Can This Tool Be Improved? How Active Is Development?

Mastra is very actively developed with frequent releases and a growing community (300K+ weekly npm downloads). Key improvements include expanding the integration ecosystem, adding Python SDK parity, deepening RAG capabilities, publishing more production case studies, improving documentation for edge cases, and reducing opinionated defaults for flexible workflows.

### 9. Official Maintainer Contacts

Mastra is maintained by Mastra AI Inc. GitHub: https://github.com/mastra-ai/mastra. Website: https://mastra.ai. Documentation: https://mastra.ai/docs. npm: https://www.npmjs.com/package/mastra. Discord is active.

### 10. General Usage Guidance

Use Mastra if you are a TypeScript-first team building AI agents and workflows. It is the best option for JS/TS developers who want a cohesive framework without assembling multiple libraries. For Python teams, evaluate CrewAI or LangGraph. Start with the quickstart, use `mastra build` for production, and deploy to Vercel or Cloudflare Workers for optimal cold-start performance.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
