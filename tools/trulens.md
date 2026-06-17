# TruLens

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Evaluation
- **License**: Open Source
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Free; evaluation auditing; moderate tracing; completely free

---

## Overview

TruLens is an open-source evaluation and tracing framework for LLM applications, originally developed by TruEra and now maintained within Snowflake following TruEra's acquisition in May 2024. It is entirely free and self-hostable, with no paid tier or proprietary cloud lock-in. TruLens pioneered the "RAG Triad" — a structured evaluation framework covering context relevance, groundedness, and answer relevance — which has become a standard reference for RAG application quality assessment.

The platform combines OpenTelemetry-based tracing with comprehensive evaluation metrics, allowing teams to attach scores to individual spans (retrieval, generation, tool usage) within a trace. This gives a complete picture of exactly where a pipeline is failing. TruLens provides seven purpose-built evaluators for agentic systems: Logical Consistency, Execution Efficiency, Plan Adherence, Plan Quality, Tool Selection, Tool Calling, and Tool Quality. It also supports batch evaluation via its Run API and inline evaluation during application execution.

TruLens is trusted by Equinix, Tribble, KBC Group, Snowflake, CubeServ, and Datec, and has reached 3,000+ GitHub stars. It supports integrations with LangChain, LlamaIndex, and any OpenTelemetry-compatible backend (Jaeger, Grafana Tempo, Datadog). The framework is entirely Python-based and requires more initial setup than some alternatives, but offers unmatched flexibility for teams that need evaluation and tracing in a single, completely free workflow.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to first eval | ~10-15 minutes | More setup than proxy tools; requires instrumentation decorators |
| Dependency count | Direct + transitive | ~15-25 (trulens-core + providers + frameworks) | Install provider packages per LLM backend (openai, litellm, bedrock, etc.) |
| Docker required? | Yes / No | No | Can run entirely in-process; no server needed |
| Language runtime | Required version | Python 3.8+ | Python only; no official JavaScript/TypeScript SDK |
| Auth complexity | API key / OAuth / None | None / API key | Local eval needs no auth; cloud feedback may need keys |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | To be measured in Quest smoke gate |

### Setup commands (expected)
```bash
# Install core + OpenAI provider
pip install trulens-core trulens-providers-openai

# Or with LangChain integration
pip install trulens trulens-apps-langchain

# In your Python code
from trulens.core.otel.instrument import instrument
from trulens.otel.semconv.trace import SpanAttributes

class MyRAG:
    @instrument(
        span_type=SpanAttributes.SpanType.RETRIEVAL,
        attributes={SpanAttributes.RETRIEVAL.QUERY_TEXT: "query"}
    )
    def retrieve(self, query: str) -> list:
        ...
```

TruLens dashboard can be launched locally or traces can be exported to any OTLP-compatible backend (Jaeger, Grafana Tempo, Datadog).

### Known sharp edges
- Steeper learning curve than RAGAS or DeepEval; OpenTelemetry instrumentation requires understanding span types and attributes
- Python-only; teams with Node.js/TypeScript backends must use OpenTelemetry instrumentation directly and export to TruLens
- Snowflake acquisition (May 2024) means long-term roadmap is influenced by Snowflake's Cortex strategy; TruLens remains open source but prioritization may shift
- Feedback function API is expressive but requires careful prompt engineering for LLM-as-judge evaluators
- Batch evaluation Run API (2.8+) is powerful but documentation is still catching up to rapid releases
- No built-in cost tracking or prompt management; purely evaluation + tracing focused

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

> Raw results JSON: `benchmarks/llmops-platforms-trulens-<date>.json`

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
- Fully open source (free); no paid tiers or licensing fees
- No cloud service offered; all usage is self-hosted or in-process
- You pay only for your own infrastructure and LLM API credits for judge evaluations

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0/month | Run entirely in-process; no server needed |
| Medium (10-100 users) | $0-$200/month | Shared dashboard or OTEL export to existing infrastructure |
| Large (100+ users) | $200-$1,000/month | Requires scalable OTEL backend (Jaeger, Grafana, Datadog) |
| Enterprise | $0 + infra | No vendor licensing; infrastructure is your responsibility |

### Hidden costs
- LLM-as-judge evaluations consume your own API credits (OpenAI, Anthropic, etc.) — can be expensive at scale
- OpenTelemetry backend infrastructure if you want centralized storage (Jaeger, Grafana Tempo, ClickHouse)
- Python-only ecosystem; JavaScript/TypeScript teams need additional OTEL instrumentation effort
- Snowflake acquisition means long-term support model is evolving; community maintenance dependency

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Fully self-hosted; runs in-process or exports to your OTEL backend |
| Open source | Yes | Fully open source; no proprietary components |
| Audit trail | Yes | Full trace and evaluation logs via OTEL export or local DB |
| Data residency controls | Yes | Complete control; no third-party data transmission required |
| On-premise deployment | Yes | Runs entirely air-gapped; no internet required for core evaluation |
| Export format | OTEL, JSON, Python | Export to Jaeger, Grafana, Datadog, or direct programmatic access |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | N/A | Self-hosted; compliance is your responsibility |
| GDPR | Partial | Self-hosted = your responsibility; no vendor data processing |
| HIPAA | Partial | Self-hosted = your responsibility; no BAA needed from vendor |
| ISO 27001 | N/A | Self-hosted; not applicable |
| EU AI Act | Partial | Evaluation framework supports evidence requirements; no explicit mapping |
| FedRAMP | N/A | Self-hosted; can be deployed in FedRAMP environments by customer |

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
- [LangChain](langchain.md) — Framework with TruLens integration for tracing
- [LlamaIndex](llamaindex.md) — RAG framework with native TruLens evaluation support
- [OpenTelemetry](TBD) — Export TruLens traces to your existing observability stack

### Alternatives to consider
- [Comet Opik](comet-opik.md) — Hosted evaluation + tracing with dashboard; easier setup
- [RAGAS](TBD) — Lighter evaluation framework specifically for RAG
- [DeepEval](confident-ai.md) — Python unit-test style evaluation with broader metrics
- [Langfuse](langfuse.md) — Better if you need tracing + evaluation in one open-source platform

---

## Links

- Official site: https://trulens.org
- GitHub: https://github.com/truera/trulens
- Documentation: https://www.trulens.org/getting_started/
- Community / Slack: https://truera.com/ai-quality-education/
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
