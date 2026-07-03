# DSPy


[![Agent Frameworks](https://img.shields.io/badge/Also_in-Agent_Frameworks-blue)](https://github.com/ArdurAI/ai-agent-framework-almanac) [![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Pipeline Optimization
- **License**: MIT (Open Source, Stanford)
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Research/enterprise; programmatic prompt optimization; eliminates manual prompt engineering

---

## Overview

DSPy (Declarative Self-improving Python) is an open-source framework from the Stanford NLP group that fundamentally rethinks how developers build with language models. Instead of writing and tweaking prompt strings by hand, DSPy lets you declare what you want (input/output signatures), compose modular Python programs, and run optimizers that automatically compile the best prompts and few-shot examples. The framework treats prompts as learnable parameters, using algorithms like MIPROv2, GEPA, BootstrapFewShot, and BetterTogether to search for optimal instructions and demonstrations.

As of mid-2026, DSPy has approximately 34,000+ GitHub stars and is used in production at companies including Databricks, VMware, and JetBlue. The framework has evolved from a research prototype (ICLR 2024 Spotlight) to a production-ready 3.x line with support for agentic loops via ReAct modules, Pydantic integration for typed validation, and LiteLLM for model routing. DSPy's core thesis is that hand-prompting eventually plateaus, while optimizer-compiled programs consistently outperform manual engineering on evaluation benchmarks—documented cases include ReAct accuracy improving from 24% to 51% and RAG pipelines from 53% to 61% after optimization.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `pip install` to working | ~10-15 minutes | Requires Python 3.11+ and LLM API key |
| Dependency count | Direct + transitive | ~30-50 | Includes litellm, pydantic, optuna (optional since v3.2.0) |
| Docker required? | Yes / No | No | No official Docker setup; pure Python library |
| Language runtime | Required version | Python 3.11+ | 3.10 may work but 3.11+ recommended |
| Auth complexity | API key / OAuth / None | API key | Standard LLM provider keys via LiteLLM |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Standard installation
pip install dspy

# Or install from conda
conda install dspy dspy-ai -c conda-forge

# With optional optuna optimizer support
pip install "dspy[optuna]"

# Install latest from main branch
pip install git+https://github.com/stanfordnlp/dspy.git
```

### Known sharp edges
- **Dependency skew**: Users have reported installation failures on WSL and certain environments due to numpy and sqlalchemy version conflicts. Workaround: pin `numpy<2.0` and `sqlalchemy>=1.4`.
- **Steep learning curve**: The signature/optimizer paradigm is conceptually different from traditional prompt engineering. Teams often try to use DSPy like LangChain and skip the optimizer, which defeats the purpose.
- **Optimization costs money**: A single MIPROv2 optimization run on a GPT-4-class model with a sizable dev set can cost $20–100 in API tokens. Budget for this in production pipelines.
- **No Docker or containerized setup**: DSPy is a pure Python library with no official Docker image or deployment templates. Teams must build their own containerization.
- **API evolution**: DSPy has undergone major API changes between 2.x and 3.x. Tutorials and examples from early 2024 may be outdated.
- **Requires labeled data**: Optimizers need examples of good outputs. If you don't have evaluation data, DSPy cannot compile effectively.

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

> Raw results JSON: `benchmarks/llmops-platforms-dspy-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- **Import failures on certain Python versions**: Earlier versions had import issues on Python 3.10 due to syntax mismatches (resolved in recent releases).
- **Dependency conflicts**: numpy 2.x compatibility issues and sqlalchemy version mismatches reported on WSL/Windows.
- **Overfitting to compile metric**: Optimizers like MIPROv2 can overfit to the compile metric, causing hold-out scores to diverge from live-traffic scores. Mitigation: rotate training sets and use richer evaluation metrics.
- **Verbose BootstrapFewShot demos**: Compiled demonstrations can consume 60–80% of context budget. Mitigation: set `max_bootstrapped_demos=2`.
- **Pickle cache security**: Earlier versions used unrestricted pickle for disk cache. v3.2.0+ adds `dspy.configure_cache(restrict_pickle=True)` to prevent arbitrary code execution from malicious cache files.

### Workarounds documented
- Pin numpy and sqlalchemy versions for stable installation.
- Always run optimizers against a labeled dev set; skip optimization only for trivial tasks.
- Use restricted pickle cache in production environments.
- Keep training sets fresh and rotate them to prevent metric overfitting.

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
- **Optimization compute**: Pay per LLM API call during compilation. One MIPROv2 run: ~$20–100 on GPT-4-class models.
- **Runtime**: After optimization, DSPy programs typically use fewer tokens than hand-tuned prompts, reducing ongoing inference costs.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0–50 | Framework free; optimization costs minimal with small dev sets |
| Medium (10-100 users) | $0–200 | Optimization costs dominate; runtime savings accrue |
| Large (100+ users) | $0–500+ | Bulk optimization runs; significant runtime token savings possible |
| Enterprise | Custom | Depends on optimization frequency and model choices |

### Hidden costs
- **Optimization tokens**: The biggest hidden cost. Each compile pass generates many LLM calls.
- **Evaluation infrastructure**: You need labeled datasets and evaluation metrics to use DSPy effectively.
- **Learning curve**: Team onboarding time is higher than imperative frameworks like LangChain.
- **Re-optimization**: After model upgrades or task changes, programs may need re-compilation.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Pure Python library; runs anywhere |
| Open source | Yes | MIT license |
| Audit trail | Partial | Programs are versionable Python code; execution traces depend on external logging |
| Data residency controls | Partial | No built-in controls; depends on LLM provider routing |
| On-premise deployment | Yes | Can run fully on-premises with local LLMs via Ollama/vLLM |
| Export format | Python code, JSON | Optimized programs are plain Python; datasets exportable |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | No | Open source research framework; no formal SOC 2 |
| GDPR | Partial | Data handling depends on deployment and LLM provider |
| HIPAA | No | Not formally certified |
| ISO 27001 | No | Not applicable to open source library |
| EU AI Act | Partial | Model-agnostic; compliance depends on use case and model |
| FedRAMP | No | Not applicable |

> **Note**: DSPy is an open source Python library maintained by Stanford NLP. It does not hold compliance certifications. Security considerations include the optional restricted pickle cache (added v3.2.0) to mitigate arbitrary code execution from malicious cache files. Production deployments should implement their own security controls.

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
- [LangChain](langchain.md) — Often used together: LangChain for pipeline wiring, DSPy for prompt optimization
- [Pydantic AI](pydantic-ai.md) — Type-safe agent framework; DSPy can optimize its prompts
- [LiteLLM](litellm.md) — DSPy uses LiteLLM under the hood for model routing
- [Langfuse](langfuse.md) — Observability for DSPy pipelines in production
- [Weights & Biases](https://wandb.ai) — Experiment tracking for DSPy optimization runs

### Alternatives to consider
- [LangChain](langchain.md) — Easier to start; manual prompt engineering instead of optimization
- [Pydantic AI](pydantic-ai.md) — Type-safe agents without the optimization paradigm
- [TextGrad](https://github.com/vinid/textgrad) — Alternative optimization framework from Stanford NLP
- [Promptfoo](promptfoo.md) — Simpler evals and prompt testing without the full compilation model

---

## Links

- Official site: [https://dspy.ai](https://dspy.ai)
- GitHub: [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
- Documentation: [https://dspy-docs.vercel.app](https://dspy-docs.vercel.app)
- Papers: [DSPy ICLR 2024](https://arxiv.org/abs/2310.03714), [GEPA](https://arxiv.org/abs/2507.19457)
- Community / Discord: [DSPy Discord](https://discord.gg/dspy)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| 2026-04 | DSPy 3.2.0 released | Restricted pickle cache security fix; optuna moved to optional |
| 2025-12 | DSPy 3.x stable | Major API stabilization; GEPA optimizer added |
| 2025-07 | MIPROv2 optimizer | Multi-instruction proposal optimization released |
| 2024-05 | ICLR 2024 Spotlight | Academic paper published; framework gains traction |
| 2023-12 | Open source launch | Released by Stanford NLP group |

---

## Deep Analysis

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

DSPy is a Stanford NLP framework (MIT license, 34,000+ GitHub stars) that replaces manual prompt engineering with algorithmic optimization — compiling declarative LLM programs to automatically find the best prompts and few-shot examples. Used in production at Databricks, VMware, and JetBlue, it has demonstrated ReAct accuracy improvements from 24% to 51% and RAG pipeline improvements from 53% to 61% after optimization. DSPy is particularly valuable for teams that have plateaued with manual prompt engineering.

### 2. Gotchas of Using This Tool

DSPy has a steep learning curve — the mental model of declarative programming with signatures, modules, and optimizers is fundamentally different from ad-hoc prompt engineering. The optimization process (compiling) can be expensive in terms of LLM API calls, as it requires many evaluation iterations. Documentation, while improving, still assumes significant familiarity with NLP concepts. The framework's API has evolved significantly, and some tutorials reference outdated patterns.

### 3. Limitations

DSPy's optimization quality depends heavily on the quality of the evaluation metric and dataset — garbage in, garbage out applies strongly. The framework's support for complex agentic workflows (multi-step reasoning with tool use) is less mature than dedicated agent frameworks. Real-time/streaming use cases are not well-supported. The TypeScript ecosystem is non-existent; DSPy is Python-only. Integration with production observability tools requires custom work.

### 4. How Secure Is This Tool?

DSPy is MIT-licensed and fully open source, maintained by Stanford NLP. The framework does not handle sensitive data directly but executes LLM API calls with user-provided keys. No major CVEs have been reported. Teams should ensure API keys are stored securely (environment variables, secret managers) and that evaluation datasets do not contain PII that would be sent to LLM providers during optimization.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 2/10.** DSPy requires advanced Python programming and NLP knowledge. It is a research-grade framework inaccessible to non-technical users and even challenging for many developers without ML backgrounds.

### 6. What Does This Tool Solve That Others Don't?

DSPy is unique in its approach to prompt optimization — rather than hand-crafting prompts, it algorithmically searches for optimal prompts and few-shot examples using optimization techniques like BootstrapFewShot, MIPRO, and GEPA. This programmatic approach to prompt engineering has no direct equivalent in other frameworks. The published research (ICLR 2024 Spotlight) provides academic validation of its effectiveness.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | DSPy | Prompt optimization | Algorithmic compilation |
| 2 | LangChain | LLM framework | Integration breadth |
| 3 | LlamaIndex | RAG framework | Data connectors |
| 4 | TextGrad | Optimization (alt) | Gradient-based |
| 5 | Pydantic AI | Type-safe agents | Pydantic ecosystem |

### 8. How Can This Tool Be Improved? How Active Is Development?

DSPy is actively developed by Stanford NLP with regular releases and published research (ICLR 2024, GEPA paper 2025). Key improvements include better documentation for production use cases, TypeScript support, streaming support, deeper integration with observability tools, and simplified onboarding for developers new to the declarative paradigm. More real-world case studies would help demonstrate value beyond academic settings.

### 9. Official Maintainer Contacts

DSPy is maintained by Stanford NLP. GitHub: https://github.com/stanfordnlp/dspy. Website: https://dspy.ai. Documentation: https://dspy-docs.vercel.app. Papers: https://arxiv.org/abs/2310.03714 (ICLR 2024). The team is active on GitHub issues and Discord.

### 10. General Usage Guidance

Use DSPy if you have plateaued with manual prompt engineering and want algorithmic optimization of prompts and few-shot examples. The learning curve is significant, so invest time in the documentation and examples before production use. For teams that need simpler, integration-heavy frameworks, LangChain or LlamaIndex may be more appropriate. DSPy excels in accuracy-critical applications where prompt quality directly impacts business outcomes.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
