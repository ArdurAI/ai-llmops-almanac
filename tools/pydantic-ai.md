# Pydantic AI

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Agent Framework
- **License**: MIT (Open Source)
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Python developers; type-safe agent development; Pydantic validation; FastAPI integration

---

## Overview

Pydantic AI is a Python-first agent framework created by the Pydantic team, designed to bring the same type-safety and developer ergonomics that made Pydantic and FastAPI successful to the generative AI era. It treats agent outputs as structured, typed data rather than free-form text, using Pydantic models for validation, dependency injection, and schema enforcement. The framework is model-agnostic, with built-in support for OpenAI, Anthropic, Google Gemini, Mistral, Cohere, AWS Bedrock, Groq, and Ollama.

The framework emphasizes production-grade features out of the box: structured streaming responses, real-time observability via Pydantic Logfire, automated evaluation via Pydantic Evals, and graph-based multi-agent workflows through Pydantic Graph. A notable 2025 integration with Temporal enables durable execution for long-running agents, persisting state across crashes and retries. Pydantic AI's dependency injection system allows clean separation of tools, data sources, and validators, making it particularly attractive to teams already invested in the Pydantic/FastAPI ecosystem.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to working | ~5 minutes | Requires only Python 3.10+ and an API key |
| Dependency count | Direct + transitive | ~20-80 | Varies heavily by model extras; slim install available |
| Docker required? | Yes / No | No | Optional for production deployments |
| Language runtime | Required version | Python 3.10+ | 3.11+ recommended for best async support |
| Auth complexity | API key / OAuth / None | API key | Standard LLM provider keys; no proprietary auth |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Full installation with all model providers
pip install pydantic-ai

# Or slim install for a specific model
pip install "pydantic-ai-slim[openai]"

# Install with examples
pip install "pydantic-ai[examples]"

# Optional: install with evals and logfire
pip install "pydantic-ai[evals,logfire]"
```

### Known sharp edges
- **SSRF vulnerability (CVE-2026-25580)**: Versions 0.0.26 through 1.55.x had a server-side request forgery vulnerability in URL download functionality. Patched in 1.56.0. Upgrade immediately if accepting untrusted message histories.
- **XSS vulnerability (CVE-2026-25640)**: Versions 1.34.0 through 1.50.x had a stored XSS via path traversal in the Web UI CDN URL. Patched in 1.51.0. Affects deployments using `Agent.to_web` or `clai web`.
- **Monorepo dependency skew**: Installing directly from Git (`git+https://github.com/pydantic/pydantic-ai.git`) can fail due to internal package version mismatches between `pydantic-ai`, `pydantic-ai-slim`, and extras. Prefer PyPI releases.
- **Rapid release cadence**: Pydantic AI releases frequently (minor versions every 1-2 weeks). This can cause dependency conflicts in large projects. Pin versions in production.
- **Databricks ML runtime incompatibility**: Library mismatches with Databricks ML runtimes (e.g., 16.3ML) have been reported. May require custom environment setup.
- **InMemoryDocumentStore**: Only for prototyping; production requires a real document store (Elasticsearch, Weaviate, Qdrant, pgvector).

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

> Raw results JSON: `benchmarks/llmops-platforms-pydantic-ai-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- **CVE-2026-25580**: SSRF in URL download (affects 0.0.26–1.55.x). Fix: upgrade to ≥1.56.0.
- **CVE-2026-25640**: Stored XSS in Web UI (affects 1.34.0–1.50.x). Fix: upgrade to ≥1.51.0.
- Dependency resolution issues when installing from source rather than PyPI.
- Databricks ML runtime compatibility issues with certain dependency versions.

### Workarounds documented
- Use `pip install --upgrade pydantic-ai>=1.56.0` for SSRF fix.
- Use PyPI releases rather than Git installs for stable dependency resolution.
- For Databricks, use a custom virtual environment with manually pinned dependencies.

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
- **Open source**: Free (MIT license). No licensing fees.
- **Pydantic Logfire**: Observability platform with free tier; paid tiers for production scale.
- **Pydantic Evals**: Free evaluation framework included.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0 | Open source only; pay only for LLM API usage |
| Medium (10-100 users) | $0 | Framework free; Logfire costs depend on trace volume |
| Large (100+ users) | $0 | Framework free; observability and compute costs external |
| Enterprise | $0 | Framework free; enterprise support available via Pydantic commercial |

### Hidden costs
- LLM API costs are the dominant cost factor.
- Pydantic Logfire for production observability adds platform cost at scale.
- Engineering time for type schema design and validation logic.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Fully open source; deploy anywhere |
| Open source | Yes | MIT license |
| Audit trail | Partial | Via Pydantic Logfire integration; not built-in to framework |
| Data residency controls | Partial | No built-in controls; depends on LLM provider choice |
| On-premise deployment | Yes | Can run entirely on-premises with local LLMs |
| Export format | JSON, Pydantic models | Traces and evals exportable via Logfire |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | No | Open source library; no formal SOC 2 for the framework itself |
| GDPR | Partial | Data handling depends on deployment and LLM provider choice |
| HIPAA | No | Not formally certified; assess based on deployment |
| ISO 27001 | No | Not applicable to open source library |
| EU AI Act | Partial | Model-agnostic; compliance depends on use case and model |
| FedRAMP | No | Not applicable to open source library |

> **Note**: As an open source Python library, Pydantic AI itself does not hold compliance certifications. Compliance posture depends on the deployment environment, LLM provider, and any observability backend (e.g., Pydantic Logfire) used. Two CVEs were disclosed and patched in 2026 (SSRF and XSS), demonstrating active security response.

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
- [Pydantic Logfire](https://logfire.pydantic.dev) — Observability and tracing for Pydantic AI agents
- [Pydantic Evals](https://pydantic.dev/docs/evals/) — Evaluation framework for AI systems
- [Temporal](temporal.md) — Durable execution for long-running Pydantic AI workflows
- [FastAPI](https://fastapi.tiangolo.com) — Natural deployment target for Pydantic AI services

### Alternatives to consider
- [LangChain](langchain.md) — Broader ecosystem but less type-safe
- [DSPy](dspy.md) — Programmatic prompt optimization rather than agent framework
- [CrewAI](crewai.md) — Multi-agent role-based crews without Pydantic type system
- [OpenAI Agents SDK](openai-agents-sdk.md) — Simpler but OpenAI-specific

---

## Links

- Official site: [https://ai.pydantic.dev](https://ai.pydantic.dev)
- GitHub: [https://github.com/pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- Documentation: [https://pydantic.dev/docs/ai/](https://pydantic.dev/docs/ai/)
- PyPI: [https://pypi.org/project/pydantic-ai](https://pypi.org/project/pydantic-ai)
- Community / Slack: [Pydantic Slack](https://pydantic.dev/docs/ai/project/contributing/)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| 2026-02 | CVE-2026-25580 patched | SSRF vulnerability fixed in v1.56.0 |
| 2026-01 | CVE-2026-25640 patched | XSS vulnerability fixed in v1.51.0 |
| 2025-11 | Temporal integration announced | Pydantic AI + Temporal for durable agents |
| 2024 | Initial release | Pydantic AI launched by Pydantic team |

---

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
