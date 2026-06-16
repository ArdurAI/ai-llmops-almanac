# Testing & Benchmarking

How the LLMOps almanac tests tools, what the harness does, how scoring works, and how to reproduce results.

## Table of Contents

1. [The Three Benchmark Types](#the-three-benchmark-types)
2. [The Seven Dimensions](#the-seven-dimensions)
3. [The Harness Architecture](#the-harness-architecture)
4. [The Canary](#the-canary)
5. [Standard Benchmarks](#standard-benchmarks)
6. [LLMOps Custom Benchmarks](#llmops-custom-benchmarks)
7. [Stress Suite](#stress-suite)
8. [Cross-Category Integration Tests](#cross-category-integration-tests)
9. [Scoring](#scoring)
10. [Reproducibility](#reproducibility)
11. [Failure Mode Taxonomy](#failure-mode-taxonomy)

---

## The Three Benchmark Types

Every LLMOps tool is tested across three types of benchmarks:

| Type | Purpose | Frequency |
|------|---------|-----------|
| **Standard benchmarks** | Verify vendor claims with published test suites | Every benchmark run |
| **LLMOps custom benchmarks** | Test ops reality: workflow setup, reliability, prompt versioning, cost tracking | Every benchmark run |
| **Cross-category integration tests** | Test how LLMOps tools work together in a full stack | Quarterly |

## The Seven Dimensions

Every tool is scored 0-100 on each dimension. The final score is a weighted average, but the per-dimension scores are always published.

| Dimension | Weight | What it measures | How it's tested |
|-----------|--------|-----------------|-----------------|
| **Accuracy / Quality** | 25% | Workflow execution accuracy, prompt version fidelity, multi-model routing correctness | Custom workflow test suites + prompt versioning accuracy tests |
| **Latency** | 15% | Workflow completion time, prompt retrieval latency, trace rendering latency | Instrumented measurements; p50, p95, p99 of end-to-end workflow completion |
| **Token Economics** | 15% | Cost tracking accuracy, token-usage estimation, pricing predictability | Standardized multi-model workflows; predicted vs. actual cost reconciliation |
| **Scale Behavior** | 15% | Concurrent workflow execution, prompt cache hit rates, model fallback under rate limits | Load tests; saturation curves; degradation points for workflow throughput |
| **Ops Burden** | 15% | Platform setup time, workflow migration pain, prompt deployment complexity | Measured setup time; smoke-gate sweep; dependency matrix for LLMOps tools |
| **Developer Experience** | 10% | Prompt versioning UX, workflow graph builder quality, trace/debugging clarity, documentation | Structured rubric; community health metrics; prompt diff/rollback usability tests |
| **Data Sovereignty** | 5% | Self-hosted workflow engine viability, audit trails for prompt changes, exportability of workflows | Feature matrix; EU AI Act / GDPR / SOC 2 mapping for prompt data |

### Why these weights?

The weights reflect what an LLMOps engineer actually cares about. Workflow execution accuracy is the most important — a tool that executes workflows incorrectly or loses prompt versions is useless regardless of how fast or cheap it is. But ops burden is nearly as important because a tool that consumes your team's life maintaining workflow graphs is not worth the accuracy gain.

Weights are reviewed annually. Changes require an RFC and a public comment period.

## The Harness Architecture

```
┌─────────────────────────────────────────┐
│  LLMOpsAdapter (frozen contract)        │
│  ├── setup()   → install, configure      │
│  ├── define_workflow() → create graph    │
│  ├── deploy_prompt() → version prompt     │
│  ├── await_ready() → async barrier       │
│  ├── execute_workflow() → run, get trace  │
│  ├── retrieve_prompt() → get version      │
│  ├── get_cost_report() → predicted cost   │
│  └── teardown() → cleanup, measure       │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Telemetry Collector                    │
│  ├── workflow latency (p50/p95/p99)     │
│  ├── prompt retrieval latency             │
│  ├── token count & cost (predicted vs.   │
│  │    actual from provider APIs)          │
│  ├── memory & CPU usage during execution  │
│  ├── error rate & failure mode taxonomy   │
│  └── ops notes (setup time, deps, bugs)   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Grading Pipeline                         │
│  ├── Deterministic grader (exact match)  │
│  ├── LLM judge (frozen prompts, SHA-256)  │
│  ├── Second pass (confidence < 0.7)       │
│  └── Failure mode taxonomy                │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Results Publisher                        │
│  ├── Raw JSON (per workflow, per run)   │
│  ├── Summary tables (per tool)            │
│  ├── Cross-verification analysis          │
│  └── Insight extraction                   │
└─────────────────────────────────────────┘
```

### The `await_ready()` barrier

This is where async-ingestion designs get their cost measured instead of hidden. Many LLMOps platforms (workflow engines with background graph compilation, prompt managers with async indexing, cost trackers with delayed aggregation) claim "fast" write paths because the actual work happens in the background. The `await_ready()` barrier forces the tool to finish all background work before the workflow is executed or the prompt is retrieved, so the true latency is measured.

### The Telemetry Collector

Every adapter call is instrumented:
- **Latency**: `time.monotonic()` around every call; p50, p95, p99 computed across all workflow runs
- **Tokens**: If the tool uses LLM APIs, token counts are captured from API responses and compared against the tool's own cost estimates
- **Cost**: Token counts × provider pricing; or measured cloud spend for self-hosted tools; compared against the tool's predicted cost
- **Memory**: `psutil` or container metrics for memory usage during workflow execution
- **CPU**: CPU utilization during the run
- **Errors**: Every exception, timeout, workflow execution failure, or prompt version mismatch is logged with full traceback
- **Ops notes**: Human observations about setup friction, dependency conflicts, workflow graph debugging difficulty, documentation quality

## The Canary

The first run of every batch is the **no-tool baseline** through the identical pipeline. If the benchmark leaked answers anywhere, the canary would score above zero on answerable categories.

**Canary rules**:
- The canary must score exactly **0.000** on all answerable categories (workflow accuracy, prompt version fidelity, cost tracking)
- The canary must score exactly **1.000** on abstention categories (it should abstain on everything)
- If the canary fails, the entire batch is invalid and must be rerun
- The canary run is published alongside the real results
- The canary adapter is a no-op: setup does nothing, no workflow is defined, no prompt is stored, execution returns nothing, teardown does nothing

## Standard Benchmarks

### By LLMOps subcategory

| Subcategory | Benchmark | What it tests | Source |
|-------------|-----------|-------------|--------|
| Workflow Orchestration | Custom workflow reliability | Workflow execution accuracy on multi-step LLM chains | Custom harness |
| Workflow Orchestration | GAIA (agent subset) | General AI Assistant task completion via workflows | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) |
| Workflow Orchestration | SWE-bench (agent subset) | Agent-based code generation via workflow tools | [SWE-bench](https://github.com/princeton-nlp/SWE-bench) |
| Prompt Management | Prompt version fidelity | Exact content preservation across version tags | Custom harness |
| Prompt Management | Prompt deployment latency | Time from store to production-ready prompt | Custom harness |
| LLM Observability | RAGAS | RAG evaluation accuracy (for observability tools with eval features) | [RAGAS](https://github.com/explodinggradients/ragas) |
| LLM Observability | DeepEval | LLM evaluation metrics | [DeepEval](https://github.com/confident-ai/deepeval) |
| Cost Tracking | Cost reconciliation accuracy | Predicted vs. actual cost across providers | Custom harness |
| Cost Tracking | Token estimation accuracy | Estimated vs. actual token counts | Custom harness |
| Multi-Model Orchestration | Model fallback reliability | Graceful degradation when primary model fails | Custom harness |
| Multi-Model Orchestration | Routing accuracy | Correct model selected for task type | Custom harness |

### Published vs. reproduced

Every standard benchmark ranking ships a table:

| Tool | Published Claim | Our Result | Delta | Verdict |
|------|----------------|------------|-------|---------|
| Tool A | 95% workflow accuracy | 92% workflow accuracy | -3% | ✅ Close |
| Tool B | "fastest prompt retrieval" | 3rd of 8 | — | ⚠️ Misleading |
| Tool C | No claim | 87% cost tracking | N/A | — |

## LLMOps Custom Benchmarks

### Setup experience

**Measured**:
- Time from `git clone` to first executing workflow
- Number of dependency conflicts when installing alongside other roster LLMOps tools
- Time to resolve dependency conflicts
- Number of undocumented steps required (e.g., API key setup for multiple providers, Docker Compose configuration)
- Time to find the answer in the docs when stuck

**Scored on**:
- Sub-5 minutes: 90-100
- 5-30 minutes: 70-89
- 30-60 minutes: 50-69
- 60+ minutes or unresolved: 0-49

### Smoke gate

Every LLMOps tool must pass an identical 3-turn scenario before entering the roster:

```
Turn 1: Create a workflow (or store a prompt version)
Turn 2: Execute the workflow (or retrieve the prompt version)
Turn 3: Verify the output, trace the execution, and check for version drift or data loss
```

**Pass criteria**:
- No crashes, no silent failures, no workflow execution data loss, no prompt version drift
- Results must be deterministic (same input → same workflow output)
- Tool must handle the basic case without workarounds
- Prompt versions must be exactly retrievable by tag
- Workflow traces must show all execution steps

**What the smoke gate surfaced** (from LLMOps testing, as examples):
- Workflow execution bugs: Nodes silently skipped when upstream node fails, producing partial outputs
- Prompt version drift: Tool stores a prompt but retrieves a slightly different version (whitespace normalized, template variables altered)
- Cost tracking discrepancies: Platform reports $0.12 but actual OpenAI billing shows $0.19
- Cross-workflow contamination: Tool writing workflow state to a global shared store
- Model fallback failures: When primary model rate-limits, workflow crashes instead of switching to backup
- Cloud tethers: "Self-hosted" workflow engine still calling cloud APIs for execution
- Write-path spread: Workflow deployment takes sub-second to ~45 seconds for 3 turns depending on graph complexity

### Stress suite

| Test | What it does | What it reveals |
|------|-------------|---------------|
| **Contradiction storms** | Rapidly deploy contradictory prompt versions | How the tool handles conflicting prompt deployments and rollback |
| **Near-duplicate floods** | Store thousands of similar prompts | Deduplication quality, prompt index bloat, retrieval latency degradation |
| **Temporal paradoxes** | Execute workflows that change state over time | Temporal reasoning accuracy in workflow traces, state consistency |
| **Concurrent writers** | Multiple threads/agents writing workflows simultaneously | Race conditions, locking, workflow graph consistency |
| **Kill-the-backing-store** | Crash the database/service mid-workflow | Recovery, data integrity, workflow resume/replay capability |
| **Cost-runaway** | Run multi-model workflows at maximum scale for 1 hour | Cost predictability, billing accuracy, budget alert reliability |
| **Prompt version stress** | Create 100+ versions of a single prompt, then roll back | Version history performance, rollback accuracy, storage bloat |
| **Model fallback stress** | Simulate provider rate limits and outages | Fallback reliability, timeout handling, graceful degradation |

### Upgrade path

**Tested**:
- Can you upgrade from version N to N+1 without rewriting all workflows?
- Are there breaking changes in the workflow graph API?
- Are there breaking changes in prompt versioning format?
- Is there a migration guide for workflows and prompts?
- Does the tool maintain backward compatibility for deployed workflows?

### Debugging experience

**Tested**:
- When a workflow node fails, can you find out why in <5 minutes?
- Are error messages clear and actionable for workflow execution failures?
- Is there a trace/debug mode showing intermediate node outputs?
- Are there known issues documented for common workflow patterns?
- Can you trace the execution path through a multi-model workflow chain?
- Can you diff prompt versions and see exactly what changed?

## Cross-Category Integration Tests

These tests run quarterly and check how LLMOps tools work together with other categories in a realistic stack:

| Integration | What it tests | Tools involved |
|-------------|-------------|--------------|
| **Workflow + Vector DB + Model Serving** | Full RAG workflow with retrieval, inference, and tracing | LLMOps workflow engine, vector DB, inference engine |
| **Prompt Manager + Agent Framework** | Can the prompt manager deploy prompts to the agent framework? | Prompt management tool, agent framework |
| **LLM Observability + Model Serving** | Does observability add <50ms latency to inference calls? | Observability tool, inference engine |
| **Workflow + Security Guardrails** | Do guardrails block malicious workflows without breaking execution? | LLMOps workflow engine, security guardrail tool |
| **Protocol + LLMOps categories** | MCP server compliance for workflow and prompt management tools | Protocol implementation, LLMOps tools |

## Scoring

### Per-dimension scoring

Each dimension is scored 0-100 using a rubric. The rubric is published before any scoring happens.

**Example: Accuracy rubric for LLMOps**

| Score | Criteria |
|-------|----------|
| 90-100 | ≥95% workflow execution accuracy; prompt versions 100% retrievable; no critical failures in stress suite |
| 80-89 | 85-95% workflow accuracy; minor prompt version drift; minor failures in stress suite |
| 70-79 | 75-85% workflow accuracy; some prompt version mismatches; some stress suite failures |
| 60-69 | 65-75% workflow accuracy; frequent prompt version drift; frequent stress suite failures |
| 50-59 | 55-65% workflow accuracy; significant reliability issues; cost tracking often incorrect |
| 0-49 | <55% workflow accuracy or fundamentally unreliable; prompt versioning broken; cost tracking unusable |

### Composite score

The composite score is a weighted average of the seven dimensions:

```
Composite = (Accuracy × 0.25) + (Latency × 0.15) + (TokenEconomics × 0.15) +
            (ScaleBehavior × 0.15) + (OpsBurden × 0.15) + (DevEx × 0.10) +
            (DataSovereignty × 0.05)
```

The composite is used for ranking, but the per-dimension scores are always published. A tool with a high composite but low ops burden score is a warning sign — it may be powerful but painful to maintain.

### Confidence intervals

Every score is reported with a confidence interval computed from the standard error across runs. If the intervals overlap between two tools, the difference is not statistically significant.

## Reproducibility

### How to reproduce a benchmark

1. Clone the benchmark harness repo (published separately)
2. Check out the exact commit used for the run (recorded in the results JSON)
3. Install the exact dependencies (lockfile is published)
4. Run the harness with the same adapter and same seed
5. Compare your results to the published results

### What is frozen

| Element | How it's frozen | Where to find it |
|---------|---------------|------------------|
| Judge model | Pinned model name and version | `results.json` metadata |
| Judge prompts | SHA-256 hash | `methodology/benchmark-harness.md` |
| Control variables | Documented values | `results.json` metadata |
| Random seeds | Published integer | `results.json` metadata |
| Adapter code | Published in harness repo | Separate repo |
| Test workloads | Published JSON files | `benchmarks/` directory |
| Workflow test graphs | Published graph definitions | `benchmarks/` directory |
| Prompt test sets | Published prompt content + expected versions | `benchmarks/` directory |

### What is NOT frozen (and why)

| Element | Why it changes | How we handle it |
|---------|---------------|------------------|
| Tool versions | Tools update | We re-run benchmarks for new versions; old results are archived |
| Provider pricing | Cloud pricing changes | Cost is computed at runtime using current pricing; historical results are annotated |
| Provider API behavior | Model providers change rate limits, response formats | We document when provider changes affect results; adapter is updated to handle new formats |
| Hardware | We may upgrade machines | Hardware spec is recorded in `results.json`; results are hardware-specific |

## Failure Mode Taxonomy

Every failure is classified into a taxonomy. This helps identify patterns across tools and categories.

| Category | Failure Modes |
|----------|--------------|
| **Setup** | `install_failed`, `dependency_conflict`, `config_error`, `missing_env_var`, `docs_incomplete`, `provider_api_key_missing` |
| **Workflow Execution** | `workflow_timeout`, `node_crash`, `node_skipped`, `wrong_output`, `state_loss`, `graph_corruption`, `async_lag` |
| **Prompt Versioning** | `version_drift`, `rollback_failure`, `concurrent_write_conflict`, `tag_resolution_error`, `prompt_not_found` |
| **Cost Tracking** | `cost_underestimate`, `cost_overestimate`, `token_count_mismatch`, `provider_pricing_outdated`, `budget_alert_missed` |
| **Multi-Model Orchestration** | `model_fallback_failure`, `routing_error`, `provider_timeout`, `rate_limit_hit`, `api_format_mismatch` |
| **Scale** | `throughput_degradation`, `memory_leak`, `cpu_spike`, `connection_pool_exhaustion`, `prompt_cache_miss` |
| **Ops** | `upgrade_breaking`, `workflow_migration_failed`, `undocumented_behavior`, `debug_opacity`, `community_unresponsive` |
| **Security** | `prompt_injection`, `data_leakage`, `pii_exposure`, `workflow_spoofing`, `unauthorized_prompt_access` |
| **Integration** | `mcp_noncompliant`, `a2a_noncompliant`, `auth_failure`, `protocol_mismatch`, `provider_integration_broken` |

## License

Content: CC BY 4.0  
Code: MIT
