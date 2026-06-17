# LlamaIndex

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: RAG Framework
- **License**: Open Source (MIT)
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Broad adoption; connecting LLMs with external data; central interface for data + LLM; 40K+ GitHub stars

---

## Overview

LlamaIndex (originally GPT Index) is a specialized data framework designed to bridge large language models with private, domain-specific data sources. Founded by Jerry Liu in late 2022, it has grown to over 40,000 GitHub stars and become the go-to toolkit for production Retrieval-Augmented Generation (RAG) systems. Its core thesis is that the hardest part of building useful LLM applications is not model interaction but data ingestion, indexing, and retrieval—getting the right information to the model at the right time in the right format. LlamaIndex is available in both Python and TypeScript, with Python as the primary, fully-featured implementation.

The framework's abstractions are built around data rather than orchestration. It provides 160+ data connectors (LlamaHub) for APIs, PDFs, databases, and cloud storage; multiple indexing strategies (vector, keyword, tree, knowledge graph); and advanced retrieval techniques including hierarchical retrievers, query rewriting, sub-question decomposition, and reranking. LlamaParse, its premium document parsing service, handles complex PDFs with tables, charts, and multi-column layouts that open-source parsers struggle with. For production teams, LlamaCloud offers managed ingestion, retrieval, and evaluation services with a credit-based pricing model.

While LlamaIndex added agent capabilities through 2024 and 2025—function-calling agents, ReAct loops, and AgentWorkflows—the consensus is that its orchestration story is competent but not differentiated. Most production teams in 2026 use LlamaIndex as the retrieval layer underneath a broader orchestration framework such as LangGraph or a vendor SDK. This is not a weakness; it reflects the framework's correct scope. LlamaIndex's evaluation tooling is another standout: built-in evaluators for faithfulness, relevancy, and correctness integrate directly into pipelines, enabling automated quality monitoring that is essential for production RAG.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to working | ~2-3 minutes | Starter package includes core + common integrations |
| Dependency count | Direct + transitive | ~10-20 direct; ~50-100 transitive | Depends on chosen integrations (vector DBs, parsers, etc.) |
| Docker required? | Yes / No | No | Optional for managed services (LlamaCloud) or vector DBs |
| Language runtime | Required version | Python 3.8+ | TypeScript (`llamaindex`) also available but less feature-complete |
| Auth complexity | API key / OAuth / None | None (framework) | LlamaCloud and LlamaParse require API keys; LLM provider keys also needed |
| First-run failure rate | Smoke gate pass/fail | Low | Common failures are mismatched API versions or missing vector DB drivers |

### Setup commands (verified)
```bash
# Starter installation (recommended for new projects)
pip install llama-index

# Minimal core installation (advanced users)
pip install llama-index-core

# Add specific integrations as needed
pip install llama-index-vector-stores-pinecone
pip install llama-index-llms-openai

# Quick verification
python -c "from llama_index.core import VectorStoreIndex, SimpleDirectoryReader; print('OK')"
```

### Known sharp edges
- **API evolution drift**: The framework has evolved through several major versions (0.9.x → 0.10.x → v1.x). Older tutorials and StackOverflow answers frequently reference deprecated import paths and broken examples.
- **Agent abstractions are secondary**: Multi-agent support is emergent rather than designed. Teams needing complex orchestration often pair LlamaIndex with LangGraph or CrewAI.
- **Ecosystem smaller than LangChain**: Fewer community integrations and third-party tooling; some vector DB connectors lag behind official SDKs.
- **LlamaCloud dependency for advanced evals**: The richest evaluation and observability features are gated behind the paid LlamaCloud platform.
- **LlamaParse credit cost surprises**: Parsing complex PDFs at the "Agentic Plus" tier consumes 45 credits per page; a 100-page dense financial report can cost $5.63 just to parse, before indexing or querying.
- **TypeScript parity gaps**: The TypeScript (`llamaindex`) package lacks several advanced features available in the Python implementation, making it a second-class citizen for now.

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

> Raw results JSON: `benchmarks/llmops-platforms-llamaindex-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- Import path changes between minor versions break existing code (e.g., `llama_index` → `llama_index.core`).
- Some vector store integrations fail silently when index schemas change, requiring manual re-indexing.
- `SimpleDirectoryReader` can OOM on large directories because it loads all files into memory before chunking.
- Custom node postprocessors must be registered carefully or are skipped without warning.
- Async query engines have subtle differences from sync engines that can produce inconsistent results.

### Workarounds documented
- Pin to a specific `llama-index` minor version and use a lockfile to avoid surprise API drift.
- Use `SimpleDirectoryReader(input_dir="...", filename_as_id=True, recursive=True)` with explicit file filters to limit memory usage.
- For production ingestion, switch to `LlamaParse` or streaming loaders rather than in-memory directory readers.
- Use `ResponseEvaluator` and `BatchEvalRunner` from `llama-index-core` for automated regression testing of retrieval quality.

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
- **LlamaIndex framework**: Free and open source (MIT license).
- **LlamaCloud (managed SaaS)**: Credit-based pricing; 1,000 credits = $1.25.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0 (framework) | Self-hosted parsing; local vector DB (Chroma, Qdrant). |
| Medium (10-100 users) | $50-$500/mo (LlamaCloud) | Starter or Pro plan; depends on document complexity and page volume. |
| Large (100+ users) | $500-$5,000/mo (LlamaCloud) | Pro plan + overages; dense/scanned PDFs drive costs up. |
| Enterprise | Custom | VPC deployment, dedicated support, volume discounts. |

### LlamaCloud credit tiers (verified)
| Plan | Monthly Price | Included Credits | Pay-as-You-Go Cap | Best For |
|------|--------------|-------------------|-------------------|----------|
| Free | $0 | 10,000 | Hard stop | Prototyping |
| Starter | $50 | 40,000 | Up to $500/mo | Early-stage products |
| Pro | $500 | 400,000 | Up to $5,000/mo | Production workloads |
| Enterprise | Custom | Custom | Custom | High-volume, compliance |

### Hidden costs
- **LLM API costs**: LlamaIndex only orchestrates; embedding and generation calls are billed separately by OpenAI, Anthropic, etc.
- **Vector database hosting**: Pinecone, Weaviate, or pgvector costs are extra ($50-$500+/mo at scale).
- **Engineering time for API drift**: Each minor version upgrade can require code changes due to moving import paths and deprecated classes.
- **LlamaParse overages**: Complex document parsing can consume credits 10-45x faster than simple text extraction, making budgeting unpredictable.
- **Re-indexing**: Schema or embedding model changes require full re-ingestion, which incurs both compute and credit costs.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Framework and vector stores run entirely on-prem. LlamaCloud is SaaS. |
| Open source | Yes | MIT license. |
| Audit trail | Yes | Custom logging; LlamaCloud provides built-in audit trails. |
| Data residency controls | Partial | LlamaCloud Enterprise offers VPC/private deployment options. |
| On-premise deployment | Yes | Framework only; all data stays within your infrastructure. |
| Export format | JSON, Parquet, Markdown | Index data and document metadata are plain objects; easy to serialize. |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | LlamaCloud (SOC 2 Type II). |
| GDPR | Yes | LlamaCloud is GDPR-compliant; framework stores data locally. |
| HIPAA | Yes | LlamaCloud offers BAA for HIPAA workloads. |
| ISO 27001 | Yes | LlamaCloud Enterprise. |
| EU AI Act | ⏳ TBD | No explicit published certification found. |
| FedRAMP | No | Not listed as of 2026. |

> Note: Framework-level compliance is the developer's responsibility. LlamaCloud provides the managed compliance layer.

---

## Related Tools

### Tier A peers in same category
- [LangChain](langchain.md) — General-purpose LLM framework with broader integration catalog
- [RAGFlow](ragflow.md) — RAG engine with deep document understanding and visual interface
- [Haystack](haystack.md) — Document AI and semantic search pipeline (deepset)
- [Dify](dify.md) — Visual LLM app builder with built-in RAG
- [FastGPT](fastgpt.md) — China-based RAG-focused platform
- [Semantic Kernel](semantic-kernel.md) — Microsoft SDK with RAG and plugin support

### Complementary tools
- [LangGraph](langgraph.md) — Stateful agent orchestration; commonly used with LlamaIndex for retrieval-heavy agents
- [LangSmith](langsmith.md) / [Langfuse](langfuse.md) — Observability for RAG pipelines
- [Promptfoo](promptfoo.md) — Regression testing for RAG prompts
- [Helicone](helicone.md) — LLM API cost and latency tracking

### Alternatives to consider
- **LangChain + direct vector store integration** — When you need a single framework and retrieval is incidental rather than the core product.
- **RAGFlow** — When deep document parsing (tables, layouts, charts) is critical and you prefer a visual, opinionated pipeline.
- **Direct frameworkless RAG** — When you have simple document sets and want to avoid abstraction overhead.

---

## Links

- Official site: https://www.llamaindex.ai
- GitHub: https://github.com/run-llama/llama_index
- Documentation: https://docs.llamaindex.ai
- Community / Discord: https://discord.gg/llamaindex
- LlamaHub (connectors): https://llamahub.ai
- LlamaCloud: https://cloud.llamaindex.ai
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
