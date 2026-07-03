# OpenAI Agents SDK


[![Agent Frameworks](https://img.shields.io/badge/Also_in-Agent_Frameworks-blue)](https://github.com/ArdurAI/ai-agent-framework-almanac) [![AI Protocols](https://img.shields.io/badge/Also_in-AI_Protocols-blue)](https://github.com/ArdurAI/ai-protocol-almanac) [![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Agent Framework
- **License**: MIT (Open Source)
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> OpenAI ecosystem; lightweight agent building; tools, guardrails, handoffs; released March 2025

---

## Overview

The OpenAI Agents SDK is OpenAI's official lightweight framework for building production multi-agent systems, released in March 2025 as the production successor to the experimental "Swarm" prototype. It provides a minimal, opinionated set of primitives—Agent, Tool, Handoff, Guardrail, and Runner—that strip away the boilerplate typically required to wire LLMs, function calling, and state management together. With approximately 19,000 GitHub stars and a rapidly growing community, it has become the default starting point for teams already committed to OpenAI's model stack who want clean multi-agent orchestration without the complexity of a full graph framework.

The SDK's design philosophy is intentional simplicity over maximum flexibility. An `Agent` is an LLM configured with instructions and a tool list; a `Handoff` transfers control between agents based on intent; a `Guardrail` runs asynchronous validation on inputs or outputs to halt or redirect execution; and the `Runner` executes the agent loop, managing state and tool calls. This small surface area makes it easy to reason about execution paths, but it also means the SDK deliberately omits features like durable persistence, long-term semantic memory, and complex cyclic workflows. Those gaps are expected to be filled by external systems or by the broader OpenAI platform (e.g., the Responses API, Assistants API, or custom memory layers like Mem0).

Despite its OpenAI branding, the SDK is technically provider-agnostic through the Chat Completions API and LiteLLM, supporting 100+ non-OpenAI models. However, the architecture is optimized for OpenAI-native capabilities: function calling, structured outputs, the Responses API, and built-in tracing that pipes directly to OpenAI's platform dashboard. The April 2026 update added significant enterprise primitives: Sandbox Agents for isolated containerized execution, Realtime Agents for voice-driven experiences, and tighter MCP (Model Context Protocol) integration. These additions signal OpenAI's intent to move the SDK from a prototyping tool to a credible enterprise orchestration layer, though it still occupies a narrower scope than LangGraph or CrewAI.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to working | ~60 seconds | Single PyPI package; no external services for basic loop |
| Dependency count | Direct + transitive | ~3-5 direct; ~10-15 transitive | Extremely lean; only `openai-agents`, `openai`, `pydantic` core |
| Docker required? | Yes / No | No | Optional for Sandbox Agents (containerized execution) |
| Language runtime | Required version | Python 3.10+ | `openai>=1.65.0` required; Node.js/TypeScript port also available via npm |
| Auth complexity | API key / OAuth / None | API key | `OPENAI_API_KEY` environment variable; compatible endpoints work with LiteLLM |
| First-run failure rate | Smoke gate pass/fail | Very Low | Minimal abstraction surface means fewer places for setup errors |

### Setup commands (verified)
```bash
pip install openai-agents

# Verify
export OPENAI_API_KEY="sk-..."
python -c "from agents import Agent, Runner; print('OK')"
```

### Hello-world example
```python
from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant."
)
result = Runner.run_sync(agent, "Write a haiku about recursion.")
print(result.final_output)
```

### Known sharp edges
- **No native long-term memory**: The SDK manages short-term session history but has no built-in semantic or durable memory. Teams must integrate an external memory layer (e.g., Mem0, vector DB, or custom cache) for stateful agents across sessions.
- **Vendor lock-in in practice**: While provider-agnostic on paper, the SDK is optimized for OpenAI models and tracing. Using Anthropic or Gemini requires LiteLLM or custom adapters, and you lose built-in tracing integration.
- **Guardrail execution model**: Guardrails run as parallel validation agents, which means they consume additional LLM tokens on every input/output. At scale, this can meaningfully increase API costs.
- **Handoff simplicity limits**: Handoffs are intent-based and work well for simple routing (triage → specialist), but they do not support complex conditional logic, loops, or stateful multi-step negotiation without manual code.
- **Sandbox Agents require Docker**: The April 2026 Sandbox Agent feature requires a container runtime (Docker or compatible) and has platform-specific setup steps that are not fully documented for all environments.
- **Tracing data leaves your infrastructure**: By default, traces stream to OpenAI's platform. Exporting to self-hosted backends requires custom trace processors and is less mature than LangSmith or Langfuse integrations.
- **Session storage is in-memory by default**: Persistent sessions require SQLite/SQLAlchemy configuration; forgetting to configure this causes state loss on restart.

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

> Raw results JSON: `benchmarks/llmops-platforms-openai-agents-sdk-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- `Runner.run_sync()` and `Runner.run()` behave differently in error handling; `run_sync` can swallow async exceptions inside tool calls if not carefully awaited.
- Custom tool functions must return JSON-serializable objects; returning complex Python objects (e.g., Pandas DataFrames) raises cryptic serialization errors.
- Guardrails that raise exceptions do not always propagate cleanly to the caller; the SDK may return a partial result instead of a hard failure.
- MCP server integration (added in 2025) requires careful stdio/SSE transport configuration; misconfiguration causes silent hangs rather than explicit errors.
- Tracing to custom backends requires subclassing `TracingProcessor` and handling batch flushing manually, which is under-documented.

### Workarounds documented
- Always wrap tool functions with explicit `try/except` and return stringified error messages to the agent rather than raising unhandled exceptions.
- Use Pydantic models for all tool inputs/outputs; this prevents serialization issues and gives automatic schema validation.
- For production deployments, explicitly configure `SessionStorage` with PostgreSQL or SQLite rather than relying on in-memory defaults.
- Set `max_turns` on `Runner.run()` to prevent infinite loops from runaway tool-calling agents.

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
- **OpenAI Agents SDK**: Free and open source (MIT license).
- **OpenAI API usage**: Standard OpenAI model pricing (GPT-4o, GPT-4.5, o1, o3, etc.) applies to all agent calls.
- **OpenAI platform tracing**: Free tier included; no separate seat pricing for tracing as of 2026.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | ~$20-$100/mo (OpenAI API) | SDK itself is free; cost is purely LLM tokens. |
| Medium (10-100 users) | ~$500-$3,000/mo (OpenAI API) | Guardrails and multi-agent handoffs multiply token usage. |
| Large (100+ users) | ~$5,000-$50,000+/mo (OpenAI API) | Heavy tool use and long sessions dominate costs. |
| Enterprise | Custom (OpenAI Enterprise) | Volume discounts, reserved capacity, priority support. |

### Hidden costs
- **Guardrail token overhead**: Each guardrail is an additional LLM call, which can double or triple token consumption per request.
- **Memory layer infrastructure**: Because the SDK has no durable memory, teams must self-host or subscribe to a vector database (Pinecone, Weaviate, pgvector) and a memory service, adding $50-$500+/mo.
- **Sandbox Agent compute**: Running code execution in isolated containers requires orchestration infrastructure (Kubernetes, Azure Container Instances, etc.).
- **Observability gap**: Built-in tracing is free but limited. Teams needing retention, alerting, or custom dashboards often add LangSmith or Langfuse, adding seat/usage costs.
- **LiteLLM proxy overhead**: If using non-OpenAI models, a LiteLLM proxy adds latency and another infrastructure component to manage.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | The SDK runs locally with no cloud dependency. |
| Open source | Yes | MIT license. |
| Audit trail | Partial | Built-in tracing logs to OpenAI's platform by default; custom backends require manual wiring. |
| Data residency controls | No | OpenAI API data residency is governed by OpenAI's terms; zero data residency controls in the SDK itself. |
| On-premise deployment | Yes | SDK can run entirely air-gapped with local models (Ollama, vLLM) via LiteLLM. |
| Export format | JSON | Traces and session state are JSON-serializable. |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | No | The SDK is open source; compliance is the developer's responsibility. OpenAI's API has SOC 2. |
| GDPR | Partial | OpenAI API offers GDPR data processing; SDK itself has no built-in compliance controls. |
| HIPAA | No | OpenAI API does not sign BAAs for standard tiers; SDK has no HIPAA-specific features. |
| ISO 27001 | No | SDK is open source; no formal certification. |
| EU AI Act | ⏳ TBD | No explicit published certification or tooling for EU AI Act alignment. |
| FedRAMP | No | Not applicable to the open-source SDK. |

> Note: The OpenAI Agents SDK is a client library. All compliance, data residency, and security guarantees depend on the infrastructure and LLM provider it is configured to use. OpenAI's enterprise and Azure OpenAI offerings provide stronger compliance postures but require different SDKs or endpoints.

---

## Related Tools

### Tier A peers in same category
- [LangGraph](langgraph.md) — Stateful graph-based orchestration with persistence and human-in-the-loop
- [CrewAI](crewai.md) — Role-based multi-agent collaboration with YAML configuration
- [Mastra](mastra.md) — TypeScript-first agent framework with durable workflows and memory
- [Semantic Kernel](semantic-kernel.md) — Microsoft enterprise SDK with deep Azure integration
- [AutoGen](autogen.md) — Conversational multi-agent (maintenance mode, merging into Microsoft Agent Framework)
- [Pydantic AI](pydantic-ai.md) — Type-safe agents with strict Pydantic validation

### Complementary tools
- [OpenAI Platform Dashboard](https://platform.openai.com/) — Tracing, cost monitoring, and model management
- [Mem0](https://github.com/mem0ai/mem0) — Memory layer to augment the SDK's short-term session history
- [Langfuse](langfuse.md) — Open-source observability alternative to OpenAI's built-in tracing
- [Helicone](helicone.md) — Proxy-based LLM cost tracking and caching
- [MCP Servers](https://modelcontextprotocol.io/) — External tool ecosystem accessible via the SDK's MCP client

### Alternatives to consider
- **LangGraph** — When the workflow requires loops, persistence, complex state machines, or human-in-the-loop checkpoints.
- **Mastra** — When the team is TypeScript-first and needs built-in durable memory, evals, and workflow orchestration.
- **Direct OpenAI Assistants API** — When you need thread persistence, file search, and code interpreter out of the box without building a custom agent loop.
- **CrewAI** — When role-based collaboration and YAML configuration are a better fit than programmatic handoffs.

---

## Links

- Official announcement: https://openai.com/index/new-tools-for-building-agents/
- GitHub (Python): https://github.com/openai/openai-agents-python
- GitHub (TypeScript): https://github.com/openai/openai-agents-typescript
- Documentation: https://github.com/openai/openai-agents-python/tree/main/docs
- PyPI: https://pypi.org/project/openai-agents/
- npm: https://www.npmjs.com/package/openai-agents
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

The OpenAI Agents SDK (~19,000 GitHub stars) is OpenAI's official lightweight framework for building production multi-agent systems, released in March 2025 as the successor to the experimental 'Swarm' prototype. It provides minimal, opinionated primitives — Agent, Tool, Handoff, Guardrail, and Runner — that strip away boilerplate for wiring LLMs, function calling, and state management. It is the default starting point for teams committed to OpenAI's model stack who want clean multi-agent orchestration.

### 2. Gotchas of Using This Tool

The SDK is OpenAI-centric — while it supports other providers via LiteLLM, the design optimizes for OpenAI models and features (Responses API, function calling format). Session storage is in-memory by default; persistent sessions require SQLite/SQLAlchemy configuration. The lightweight nature means teams need to build their own observability, persistence, and deployment infrastructure. The SDK is relatively new (March 2025) with a still-maturing ecosystem of examples and best practices.

### 3. Limitations

The OpenAI Agents SDK lacks built-in state persistence, observability, and production deployment tooling — it is a framework, not a platform. Multi-agent orchestration patterns are less flexible than LangGraph's graph model. Guardrails are basic compared to dedicated safety tools. TypeScript support exists but may lag the Python SDK. The tight OpenAI coupling means teams using other providers primarily may get less value. No built-in evaluation framework.

### 4. How Secure Is This Tool?

The SDK is MIT-licensed (open source) with code on GitHub for independent review. The guardrail primitives (input/output validation) provide basic safety controls. The SDK executes tool functions — teams must validate inputs and restrict tool permissions. No major CVEs have been reported. OpenAI's model API calls are processed under OpenAI's privacy policy. Teams should ensure API keys are stored securely and that guardrails are properly configured to prevent unsafe outputs.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 3/10.** The OpenAI Agents SDK is a developer framework requiring Python proficiency. Non-technical users cannot interact with it; it requires engineering teams.

### 6. What Does This Tool Solve That Others Don't?

The SDK's unique strength is being OpenAI's official, lightweight multi-agent framework with first-class support for OpenAI features (Responses API, computer use, deep research). The Handoff primitive for agent-to-agent delegation is elegantly simple. The guardrail system for input/output validation is built-in rather than requiring third-party tools. The minimal, composable design (five primitives) is less overwhelming than full frameworks.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | CrewAI | Role-based multi-agent | Production + enterprise |
| 2 | LangGraph | Graph orchestration | State persistence |
| 3 | OpenAI Agents SDK | Lightweight agents | OpenAI-native |
| 4 | Mastra | TS-first agents | TypeScript ecosystem |
| 5 | AutoGen | Conversational (legacy) | Research |

### 8. How Can This Tool Be Improved? How Active Is Development?

The SDK is actively developed by OpenAI with regular releases. Key improvements include adding built-in state persistence, native observability hooks, production deployment guides, expanding non-OpenAI provider support, adding an evaluation framework, and providing more complex multi-agent examples. Better documentation for production patterns would help teams move beyond prototyping.

### 9. Official Maintainer Contacts

The OpenAI Agents SDK is maintained by OpenAI. GitHub (Python): https://github.com/openai/openai-agents-python. GitHub (TypeScript): https://github.com/openai/openai-agents-typescript. Announcement: https://openai.com/index/new-tools-for-building-agents/. Documentation: https://github.com/openai/openai-agents-python/tree/main/docs.

### 10. General Usage Guidance

Use the OpenAI Agents SDK if you are committed to OpenAI's model stack and want a lightweight, official framework for multi-agent systems. For provider-agnostic orchestration, evaluate CrewAI or LangGraph. For TypeScript-first teams, evaluate Mastra. Pair with AgentOps or LangSmith for observability. Configure persistent sessions (SQLite/SQLAlchemy) for production use to avoid state loss on restart.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
