# AutoGen

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Multi-Agent Framework
- **License**: Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> AutoGen is a multi-agent conversational AI framework created by Microsoft Research in September 2023. It pioneered the paradigm of enabling multiple LLM agents to communicate through natural language conversations to solve complex tasks collaboratively. The framework introduced a layered architecture separating model clients, agent primitives, and orchestration patterns, including the influential AgentTool concept that allows wrapping entire agents as tools for other agents — enabling recursive, hierarchical orchestration. AutoGen was instrumental in popularizing multi-agent systems in the open-source community, reaching 55,300+ GitHub stars and 8,300+ forks by early 2026, with millions of monthly PyPI downloads and usage in over 4,000 repositories.

---

## Overview

In October 2025, Microsoft announced that both AutoGen and Semantic Kernel are entering maintenance mode. All new feature development has shifted to the Microsoft Agent Framework, which consolidates AutoGen's multi-agent orchestration with Semantic Kernel's production foundations into a unified enterprise-ready platform. AutoGen continues to receive bug fixes and security patches but will not receive new features. Microsoft directs new users to the Microsoft Agent Framework and provides migration guides for existing AutoGen deployments. The original AutoGen creators forked the project into AG2 in late 2024, which remains independently developed under community governance, though it is a separate project from Microsoft's roadmap.

AutoGen's architecture includes the Core API (message passing, event-driven agents, distributed runtime), AgentChat API (simplified API for rapid prototyping, familiar to v0.2 users), and Extensions API (LLM clients, code execution, tools). The ecosystem also includes AutoGen Studio (visual no-code GUI, explicitly not production-ready) and AutoGen Bench (benchmarking suite). The framework supports Python 3.10+ and .NET, with cross-language compatibility. It integrates with OpenAI, Azure OpenAI, Anthropic, and other providers through extension modules. As of September 2025, the latest stable version is v0.7.5. For new production projects, teams should evaluate the Microsoft Agent Framework (public preview October 2025, GA target Q1 2026) or alternatives like CrewAI, LangGraph, or Pydantic AI.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to first agent chat | ~5-10 minutes | Lightweight Python framework; quick install |
| Dependency count | Direct + transitive | ~10-20 direct | `autogen-agentchat`, `autogen-ext`, optional OpenAI/Anthropic clients |
| Docker required? | Yes / No | Optional | Useful for running AutoGen Studio or code execution environments; not required for basic usage |
| Language runtime | Required version | Python 3.10+ | Python-only; .NET support via AutoGen.Net for C# developers |
| Auth complexity | API key / OAuth / None | API key | LLM provider API keys (OpenAI, Azure OpenAI, Anthropic); optional for local/Ollama models |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Install AgentChat and OpenAI extension
pip install -U "autogen-agentchat" "autogen-ext[openai]"

# Optional: AutoGen Studio (visual GUI, NOT production-ready)
pip install -U "autogenstudio"

# Optional: .NET support
# dotnet add package AutoGen.Core
```

### Known sharp edges
- **Maintenance mode**: AutoGen receives bug fixes and security patches only — no new features; Microsoft directs all new development to Microsoft Agent Framework (MAF)
- **AutoGen Studio not production-ready**: documentation explicitly warns it lacks authentication, security hardening, and deployment tooling; meant for prototyping only
- **Python 3.10+ requirement**: creates deployment friction in enterprise environments standardized on older Python versions; some cloud platforms have limited support for newer runtimes
- **Steep learning curve**: requires understanding agents, tools, message passing, and orchestration patterns simultaneously; simpler frameworks like CrewAI get productive faster for basic use cases
- **Migration complexity**: Microsoft rebuilt AutoGen as v0.4 with completely different architecture from v0.2; AG2 community fork maintains original PyPI packages but diverges from Microsoft roadmap
- **Three-path fragmentation**: AutoGen v0.2 (AG2 fork), AutoGen v0.4 (maintenance mode), and Microsoft Agent Framework (new direction) create confusion and migration risk
- **No enterprise support**: community-managed with limited response times; no SLA or dedicated support for production issues
- **Cost runaway**: multi-agent conversations can trigger many LLM rounds; without explicit termination conditions and token budgets, API costs escalate unpredictably

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

> Raw results JSON: `benchmarks/llmops-platforms-autogen-<date>.json`

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
- **Open Source Framework:** Free — MIT license; self-hosted; user pays only for compute and LLM API usage
- **Azure deployment costs:** If running on Azure (recommended for production), standard Azure compute and OpenAI/Azure OpenAI API costs apply
- **No managed platform:** AutoGen has no commercial SaaS offering; all operational costs are infrastructure and API tokens
- **Microsoft Agent Framework (successor):** Will have Azure AI Foundry Agent Service pricing when GA (public preview as of Oct 2025); managed service pricing TBD

- **Primary costs**: LLM API tokens (OpenAI, Azure OpenAI, Anthropic); Azure compute (VMs, Container Apps, AKS) for hosting agents; optional vector stores for memory backends
- **Hidden costs**: engineering time for security hardening, authentication, deployment automation, and observability (all must be built custom since AutoGen Studio is not production-ready)

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
| Self-hostable | Yes | Fully self-hosted on any infrastructure; no managed cloud dependency |
| Open source | Yes | MIT license; full source code available on GitHub; commercial use permitted |
| Audit trail | Partial | Basic logging via Python logging; production-grade audit trails require custom implementation |
| Data residency controls | Yes | Self-hosted deployments provide full data control; data never leaves your infrastructure unless configured |
| On-premise deployment | Yes | Can run fully air-gapped on local servers or private clouds with local models (Ollama, vLLM) |
| Export format | Python, JSON | Agent configurations are Python code; conversation histories and traces exportable as JSON |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | No | No formal SOC 2 certification; security posture is self-managed in open-source deployments |
| GDPR | Partial | Self-hosted deployments can be GDPR-compliant by design; no platform-level DPA or certification |
| HIPAA | Partial | Possible via self-hosted + air-gapped deployment + local models + BAA with LLM provider; not certified |
| ISO 27001 | No | No formal certification; Microsoft Agent Framework (successor) may pursue enterprise certifications |
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
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)

### Complementary tools
- [LangSmith](langsmith.md) or [Langfuse](langfuse.md) — tracing and observability for multi-agent conversations and tool calls
- [Braintrust](braintrust.md) — evaluation and regression testing for AutoGen agent outputs; native AutoGen integration available
- [LiteLLM](comet-opik.md) — unified LLM API gateway for routing multiple providers through AutoGen's model clients
- [Ollama](ragflow.md) — local model hosting for air-gapped or cost-sensitive AutoGen deployments
- [Temporal](temporal.md) — durable execution and workflow orchestration for long-running multi-agent processes

### Alternatives to consider
- **Microsoft Agent Framework** for new production projects requiring Microsoft-backed enterprise support, graph-based workflows, checkpointing, and OpenTelemetry observability
- [CrewAI](crewai.md) for role-based multi-agent collaboration with faster onboarding, larger community, and active feature development
- [LangGraph](langgraph.md) for stateful graph-based agent workflows with explicit state transitions and cyclic loops
- [Semantic Kernel](semantic-kernel.md) for .NET/Microsoft ecosystems needing production-grade LLM integration with enterprise governance
- [Pydantic AI](pydantic-ai.md) for type-safe, structured-output Python agents with simpler deployment requirements

---

## Links

- Official site: [https://microsoft.github.io/autogen](https://microsoft.github.io/autogen) (maintenance mode docs)
- GitHub: [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)
- Microsoft Agent Framework (successor): [https://github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- Documentation: [https://microsoft.github.io/autogen/stable](https://microsoft.github.io/autogen/stable)
- Community / Discord: [https://discord.gg/autogen](https://discord.gg/autogen) (community-managed; limited Microsoft response)
- AG2 Community Fork: [https://github.com/ag2ai/ag2](https://github.com/ag2ai/ag2)
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
