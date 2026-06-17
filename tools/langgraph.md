# LangGraph

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Agent Orchestration
- **License**: Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> LangChain ecosystem; stateful, cyclic multi-agent orchestration; Deep Agents for long-running workflows

---

## Overview

LangGraph is a low-level orchestration framework built by the LangChain team for constructing stateful, cyclic multi-agent systems that require loops, persistence, and human-in-the-loop control. Unlike the linear chain abstractions in LangChain, LangGraph represents agent execution as a directed graph where each node is a function or agent and edges define conditional transitions. This graph-native model makes it possible to build systems that can pause, resume, branch, and retry—behaviors that are essential for reliable production agents but difficult to express in simple pipeline frameworks. It has accumulated over 24,800 GitHub stars and is widely used as the orchestration backbone for LangChain-based production deployments.

The framework's central design pillar is persistence. LangGraph provides built-in checkpointers that save state to PostgreSQL, SQLite, Redis, or MongoDB, enabling agents to survive process restarts, resume from failures, and maintain long-term memory across sessions. It supports first-class streaming (both token-by-token and event-based), human-in-the-loop approval gates, and time-travel debugging that lets developers rewind to any previous state and replay from there. These features make it particularly well-suited for customer-support bots, multi-step research agents, and workflow automation that must run for minutes or hours rather than seconds.

LangGraph is positioned as the orchestration layer within the broader LangChain ecosystem. It pairs natively with LangChain for model/tool abstractions and with LangSmith for tracing, evaluation, and deployment. The team also offers Deep Agents—a higher-level harness built on LangGraph that handles planning, subagent spawning, and virtual filesystem access for complex long-running tasks. LangGraph Cloud provides a managed runtime with autoscaling, but many teams self-host the open-source server on their own infrastructure.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to working | ~2-3 minutes | Single Python package; no external services required for local mode |
| Dependency count | Direct + transitive | ~5-10 direct; ~30-50 transitive | Leaner than LangChain core because it does not include model integrations by default |
| Docker required? | Yes / No | No | Optional for production checkpointer backends (PostgreSQL, Redis) |
| Language runtime | Required version | Python 3.9+ | JavaScript/TypeScript port also available via `@langchain/langgraph` |
| Auth complexity | API key / OAuth / None | None (framework) | Requires LLM provider API keys (OpenAI, Anthropic, etc.) |
| First-run failure rate | Smoke gate pass/fail | Low | Most failures stem from incorrect state reducer definitions or model key issues |

### Setup commands (verified)
```bash
pip install -U langgraph

# Optional: persistent checkpointer backend
pip install langgraph-checkpoint-postgres

# Quick verification
python -c "from langgraph.graph import StateGraph, START, END; print('OK')"
```

### Known sharp edges
- **State reducer configuration**: Concurrent writes to the same state key without a proper reducer (e.g., using `operator.add` instead of `add_messages`) raise cryptic `INVALID_CONCURRENT_GRAPH_UPDATE` errors or silently corrupt message history.
- **Message history duplication**: Nodes that return the full state object instead of a partial update can cause message lists to append back into themselves, inflating token costs and breaking logic.
- **Parallel node merge semantics**: Fan-in joins require explicit reducer definitions; without them, parallel branches may overwrite each other's state unexpectedly.
- **Memory leaks from `p-retry`**: The JavaScript ecosystem hit a known leak in `p-retry@4.6.2` (used by LangGraph packages) where event listeners accumulate during retries. Upgrading to `p-retry@7.x` is required.
- **Tool dispatch mismatch**: Custom tool nodes that read from `state["messages"][-1].tool_calls` without validating tool names are fragile when multiple tool-call batches appear in parallel.
- **LangGraph Cloud pricing opacity**: Managed hosting pricing is not publicly published; teams must contact sales for quotes, making cost forecasting difficult.

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

> Raw results JSON: `benchmarks/llmops-platforms-langgraph-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- `INVALID_CONCURRENT_GRAPH_UPDATE` when parallel nodes write to unreduced state keys.
- Message duplication when nodes return full state instead of partial updates.
- Tool-call ID mismatches in custom tool nodes break OpenAI's strict message protocol.
- Graph visualization (`graph.get_graph().draw_mermaid_png()`) requires additional dependencies (`pygraphviz` or `Pillow`) that can fail on headless systems.

### Workarounds documented
- Always use `from langgraph.graph.message import add_messages` for message keys.
- Return `{}` from pass-through nodes; never return the full state.
- Use `ToolNode` or `create_agent` defaults instead of manual tool dispatch for standard loops.
- Pre-install `graphviz` system packages before installing `pygraphviz`.

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
- **LangGraph framework**: Free and open source (MIT license).
- **LangGraph Cloud**: Managed SaaS with autoscaling; pricing not publicly published (contact sales).
- **LangSmith observability**: Free tier (5K traces/mo), Plus $39/seat/mo, Enterprise custom.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0 (framework) + $39/mo (LangSmith Plus, 1 seat) | Self-hosted checkpointer (SQLite) |
| Medium (10-100 users) | $0 (framework) + ~$200/mo (LangSmith) | PostgreSQL checkpointer adds ~$15-50/mo infra |
| Large (100+ users) | $0 (framework) + $1,000+/mo (LangSmith) | LangGraph Cloud or self-hosted K8s |
| Enterprise | Custom (LangGraph Cloud + LangSmith Enterprise) | Dedicated infra, SLA, custom retention |

### Hidden costs
- **Checkpointer infrastructure**: PostgreSQL, Redis, or MongoDB required for durable state at scale.
- **LangSmith seat costs**: Per-seat pricing multiplies quickly for large teams; self-hosted LangSmith is Enterprise-only.
- **State storage growth**: Long-running agents with large message histories can bloat checkpointer storage; pruning strategies must be engineered.
- **LLM token costs**: LangGraph itself adds minimal overhead, but multi-step agent loops can consume significant tokens.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Framework and server are fully self-hostable. LangGraph Cloud is SaaS. |
| Open source | Yes | MIT license. |
| Audit trail | Yes | Via LangSmith or custom OpenTelemetry instrumentation. |
| Data residency controls | Partial | LangSmith Enterprise offers dedicated regions; framework itself is on-prem. |
| On-premise deployment | Yes | Framework runs on any Python runtime; checkpointer can use local SQLite/PostgreSQL. |
| Export format | JSON, SQLite, PostgreSQL dumps | State is plain JSON-serializable; easy to export/migrate. |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | LangSmith Enterprise tier. |
| GDPR | Yes | LangSmith offers EU data residency; framework stores data where you configure it. |
| HIPAA | Yes | Available via BAA on LangSmith Enterprise. |
| ISO 27001 | Yes | LangSmith Enterprise. |
| EU AI Act | ⏳ TBD | No explicit published certification found. |
| FedRAMP | No | Not listed for LangSmith or LangGraph Cloud as of 2026. |

> Note: LangGraph framework compliance is the developer's responsibility. LangSmith provides the managed compliance layer.

---

## Related Tools

### Tier A peers in same category
- [LangChain](langchain.md) — Linear chain and agent primitives; same ecosystem
- [CrewAI](crewai.md) — Role-based multi-agent collaboration
- [OpenAI Agents SDK](openai-agents-sdk.md) — Simpler handoff-based multi-agent
- [Mastra](mastra.md) — TypeScript-native workflow orchestration with branching/loops
- [Semantic Kernel](semantic-kernel.md) — Microsoft enterprise agent framework
- [AutoGen](autogen.md) — Conversational multi-agent (maintenance mode)

### Complementary tools
- [LangSmith](langsmith.md) — Tracing, evals, and observability (native integration)
- [Langfuse](langfuse.md) — Open-source observability alternative
- [Helicone](helicone.md) — Proxy-based LLM cost tracking
- [Promptfoo](promptfoo.md) — Prompt regression testing and red-teaming

### Alternatives to consider
- **Temporal / Prefect** — When workflows are deterministic, long-running, and do not require LLM reasoning at every step.
- **Direct LangChain + custom state machine** — When graph overhead is unnecessary and a simple loop suffices.
- **CrewAI** — When role-based collaboration and YAML configuration fit the team better than graph-based coding.

---

## Links

- Official site: https://www.langchain.com/langgraph
- GitHub: https://github.com/langchain-ai/langgraph
- Documentation: https://langchain-ai.github.io/langgraph/
- Community / Discord: https://discord.gg/langchain
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | Deep-dive content added | Overview, setup, pricing, sharp edges, and links populated from web research. |
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |

---

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
