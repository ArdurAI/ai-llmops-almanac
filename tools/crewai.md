# CrewAI

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Multi-Agent Framework
- **License**: Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Python-based; multi-agent collaboration; 45,900+ GitHub stars; open-source (MIT); CrewAI AMP managed platform; customers include PwC, IBM, NVIDIA, Capgemini; 60% of Fortune 500; $18M Series A (Oct 2024, Insight Partners)

---

## Overview

CrewAI is a Python-first open-source framework for orchestrating role-based autonomous AI agents that collaborate as a "crew" to accomplish complex tasks. Founded by João Moura in 2023 and built entirely from scratch with zero dependency on LangChain or other agent frameworks, CrewAI focuses on a simple, readable abstraction: you define agents with explicit roles (Researcher, Writer, Editor, Analyst), goals, backstories, and toolsets, then organize them into crews with sequential or hierarchical process modes. The framework handles task delegation, output passing between agents, memory management, and orchestration automatically. This role-based metaphor maps directly to how business teams think about staffing projects, making it accessible to non-ML engineers and explainable to stakeholders.

As of early 2026, CrewAI holds 45,900+ GitHub stars, powers over 100,000 certified developers, and runs 1.4 billion agentic automations per month. The framework is used by 60% of the Fortune 500, including PwC, IBM, NVIDIA, and Capgemini. In October 2024, CrewAI raised an $18M Series A led by Insight Partners with participation from boldstart ventures, Craft Ventures, and angels including Andrew Ng and HubSpot CTO Dharmesh Shah. This funding enabled the launch of CrewAI AMP (Agent Management Platform), a managed commercial offering with Studio (visual editor), managed hosting, observability, and enterprise governance features. The open-source framework remains free under MIT license and is entirely independent of the paid AMP platform.

CrewAI is LLM-agnostic, supporting OpenAI, Anthropic, Google Gemini, AWS Bedrock, Groq, Ollama for local models, and any model accessible through LiteLLM. Teams can mix models within a single crew — using cheaper models for research and premium models for final writing. The framework includes built-in memory backends (short-term, long-term, entity, contextual), CrewAI Flows for event-driven pipelines, and native tool-calling support. CrewAI Studio (in AMP Enterprise) allows non-engineers to assemble crews via drag-and-drop while generating real Python code that engineers can export and extend.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to first crew run | ~2-5 minutes | Quick pip install; first crew can run in under 10 lines of Python |
| Dependency count | Direct + transitive | ~15-30 direct | Lightweight framework with no LangChain dependency; heavier with tools/vector stores |
| Docker required? | Yes / No | Optional | Docker useful for deployment; not required for local development |
| Language runtime | Required version | Python 3.10+ | Python-only; no official JS/TS/Go SDK as of 2026 |
| Auth complexity | API key / OAuth / None | API key | LLM provider API keys (OpenAI, Anthropic, etc.); optional Braintrust/LangSmith tracing keys |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Install via pip or uv
pip install crewai
# or with tools
pip install 'crewai[tools]'

# Quick start example (from docs)
from crewai import Agent, Crew, Task

researcher = Agent(role="Researcher", goal="Research topic", backstory="...")
writer = Agent(role="Writer", goal="Write article", backstory="...")

task = Task(description="Research and write", expected_output="Article", agent=researcher)

crew = Crew(agents=[researcher, writer], tasks=[task])
result = crew.kickoff()
```

### Known sharp edges
- **Hierarchical process unpredictability**: delegation chains can produce unexpected behavior without carefully defined role boundaries and task descriptions
- **Less suited to complex branching**: compared to LangGraph, CrewAI lacks explicit state-transition control and cyclic loop support; better for sequential/hierarchical than graph-based workflows
- **Debugging multi-agent runs**: requires external observability (LangSmith, Braintrust, or custom logging) as native debugging is limited
- **Memory configuration complexity**: short-term, long-term, entity, and contextual memory require proper vector store setup; misconfiguration leads to silent failures or irrelevant context injection
- **Tool compatibility**: while independent of LangChain, some community tools still assume LangChain interfaces; custom tool definitions require careful schema design
- **Python-only ecosystem**: no official JavaScript/TypeScript/Go SDK; non-Python stacks must wrap CrewAI in a Python microservice with HTTP API
- **AMP pricing gap**: no paid plan between free Basic (50 executions/month) and custom Enterprise; teams with steady volume often self-host open-source rather than pay $0.50 per extra execution
- **Rate limiting and cost runaway**: agent crews can trigger many sequential LLM calls; without token limits and cost tracking, bills can escalate quickly

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

> Raw results JSON: `benchmarks/llmops-platforms-crewai-<date>.json`

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
- **Open Source Framework:** Free forever — MIT license; self-hosted on any infrastructure; unlimited executions; full framework, Crews, Flows, Tools, Memory
- **Basic (AMP):** Free — 50 executions/month included, then $0.50 per extra execution; visual editor, AI copilot, GitHub integration, Studio, tracing, guardrails; unlimited users/projects
- **Enterprise (AMP):** Custom pricing — up to 30,000 executions/month included, then $0.50 per extra; CrewAI or private infrastructure, SSO, RBAC, on-site support and training, 50 development hours/month

- **Open-source costs**: LLM API costs are the primary expense; compute for self-hosting is minimal; vector stores (Pinecone, Weaviate, etc.) add infrastructure costs if memory is used
- **AMP costs**: execution-based billing at $0.50 per execution beyond the free tier; Enterprise contracts include dedicated infrastructure and professional services

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
| Self-hostable | Yes | Fully self-hostable open-source framework on any infrastructure (AWS, GCP, Azure, on-prem) |
| Open source | Yes | MIT license; core framework and SDKs are fully open-source |
| Audit trail | Yes | Execution logs, agent outputs, task completions logged; AMP adds enhanced observability and tracing |
| Data residency controls | Yes | Self-hosted deployments provide full data control; AMP Enterprise offers VPC/private infrastructure |
| On-premise deployment | Yes | Open-source framework deploys anywhere; AMP Enterprise offers on-prem/private cloud options |
| Export format | Python, JSON | Crew definitions are Python code; datasets and traces exportable as JSON; AMP Studio exports Python code |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | AMP Enterprise is SOC 2 Type II certified; open-source framework has no certification (self-hosted responsibility) |
| GDPR | Yes | AMP compliant; self-hosted deployments require user implementation |
| HIPAA | Partial | Possible via self-hosted open-source + BAA with LLM provider; not officially certified on AMP as of 2026 |
| ISO 27001 | ⏳ TBD | Not publicly confirmed for AMP; self-hosted responsibility |
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
- [LangSmith](langsmith.md) or [Langfuse](langfuse.md) — tracing and observability for multi-agent crew executions
- [Braintrust](braintrust.md) — evaluation and regression testing for crew outputs; native CrewAI integration
- [LiteLLM](comet-opik.md) — unified LLM API gateway for routing multiple providers within a single crew
- [Ollama](ragflow.md) — local model hosting for self-hosted CrewAI deployments without external API costs
- [Pydantic AI](pydantic-ai.md) — type-safe agent building for Python teams that need structured outputs alongside CrewAI orchestration

### Alternatives to consider
- [LangGraph](langgraph.md) when complex state transitions, cyclic loops, or fine-grained graph control are needed over role-based collaboration
- [AutoGen](autogen.md) for Microsoft-native ecosystems, recursive agent-as-tool composition, or research prototyping (note: maintenance mode as of Oct 2025)
- [OpenAI Agents SDK](openai-agents-sdk.md) for simple OpenAI-native agent workflows without multi-agent orchestration overhead
- [Semantic Kernel](semantic-kernel.md) for .NET/Microsoft shops requiring enterprise integration with Azure AI Foundry
- [Agno](comet-opik.md) or [Mastra](mastra.md) for ultra-lightweight Python agent frameworks with built-in UI

---

## Links

- Official site: [https://www.crewai.io](https://www.crewai.io)
- GitHub: [https://github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- Documentation: [https://docs.crewai.com](https://docs.crewai.com)
- Community / Discord: [https://www.crewai.com/community](https://www.crewai.com/community)
- CrewAI AMP: [https://app.crewai.com](https://app.crewai.com)
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
