# Project Intent & Philosophy

## Why this almanac exists

The LLMOps landscape is exploding. Every week, a new workflow builder, prompt management platform, or orchestration framework launches, a blog post claims 10x reliability gains, and a vendor announces the next revolution in "AI-powered automation." But **nobody independently verifies these claims**. The benchmarks are self-reported, the comparisons are marketing, and the "best tool" lists are affiliate SEO.

This almanac is the **public record of independent verification** for LLMOps platforms, workflow orchestration, and prompt management tools. It exists because platform engineers and AI operations teams need a single source of truth that answers:

- Does this workflow actually execute reliably in production?
- How accurate is its prompt versioning and traceability?
- Can it orchestrate multiple models without silent failures?
- What's the real cost of running it at scale — and does its cost tracking match reality?
- What's the ops burden of maintaining complex workflow graphs?
- How does it fail when a model provider changes its API or rate limits?
- Can you trust the vendor's benchmark numbers on workflow execution accuracy?

## Core principles

### 1. Frozen methodology before results

The harness, judge model, prompts, scoring rubric, and workflow test suites are **fixed and published before any tool is tested**. This prevents "cherry-picking" the methodology that favors a particular vendor. If a tool doesn't fit the harness, we adapt the adapter — not the rules.

### 2. Ops-first evaluation

Most LLMOps benchmarks measure workflow accuracy or prompt retrieval quality. We measure **what an AI operations engineer actually lives with**:
- Time from `git clone` to first executing workflow
- Dependency conflicts when installing alongside other LLMOps tools
- Time to debug when a workflow node silently fails mid-execution
- Upgrade pain when version N → N+1 breaks all your workflow graphs
- Cost predictability when token usage spikes across multi-model chains
- Prompt version drift when a deployed prompt changes without traceability

### 3. Raw data is always published

Every benchmark run produces a JSON file with every workflow definition, every execution trace, every prompt version, every token count, every latency measurement, and every cost estimate. These raw files are published alongside the summary. If you disagree with a ranking, you can re-analyze the data yourself.

### 4. No tool is above criticism

Every tool on the roster has been through a smoke gate. Every tool has bugs — workflow execution failures, prompt versioning gaps, cost tracking discrepancies. We document them honestly. A vendor relationship or sponsorship does not influence rankings. The only way a tool improves its score is by actually improving.

### 5. Living document, not a static snapshot

The almanac is updated monthly. Tools enter and exit the roster. Scores change as tools improve or degrade. The "founding edition" is a snapshot; the current edition is the truth.

## Design philosophy

### The two-bar test

Every LLMOps tool must clear two bars to justify its existence:
1. **Beat the naive baseline** on workflow execution accuracy / prompt traceability / multi-model orchestration
2. **Beat the full-capability baseline** on cost / ops burden / complexity

If a tool can't do both, it has no reason to exist as infrastructure. A tool that is 5% better at workflow visualization but 10x more complex to operate than a Python script with API calls is not worth adopting.

### The seven dimensions

We score every LLMOps tool on seven dimensions because no single number captures "good LLMOps infrastructure":

| Dimension | Why it matters | LLMOps-specific meaning |
|-----------|---------------|------------------------|
| **Accuracy** | Does it produce correct outputs? | Workflow execution accuracy: does the workflow complete with the correct result? Does prompt versioning preserve exact prompt content? Does multi-model routing send requests to the right model? |
| **Latency** | Does it respond fast enough for real use? | Workflow completion time (end-to-end, not just model inference time). Prompt retrieval latency. Trace rendering latency for debugging. |
| **Token economics** | Does it cost what you expect? | Cost tracking accuracy: does the platform's reported cost match actual provider billing? Token-usage estimation quality. Budget alert reliability. |
| **Scale behavior** | What happens when you 10x the load? | Concurrent workflow execution: does throughput degrade linearly? Prompt cache hit rates under load. Cost-tracking precision at high volume. Model fallback behavior under rate limits. |
| **Ops burden** | How much of your life does it consume? | Platform setup complexity. Workflow graph debugging difficulty. Prompt migration pain when changing versions. Multi-provider API key management overhead. Upgrade breakage of existing workflows. |
| **Developer experience** | Is it pleasant or painful to use? | Prompt versioning UX: is it easy to diff, rollback, and deploy prompts? Workflow graph builder quality. Trace/debugging interface clarity. Documentation completeness for orchestration patterns. |
| **Data sovereignty** | Can you run it yourself? Audit it? | Self-hosted deployment viability for workflow engines. Audit trails for prompt changes and workflow executions. Compliance alignment for prompt data (GDPR, SOC 2). Exportability of workflow definitions and prompt libraries. |

### The adapter pattern

Every LLMOps tool is tested through a **CategoryAdapter** — a frozen interface that the tool must satisfy. The adapter handles workflow setup, prompt ingestion, workflow execution, and teardown. This means:
- Tools are tested identically
- The adapter is the only thing that changes per tool
- New tools can be added without changing the harness
- The adapter is published and open for review

The LLMOps adapter extends the base adapter with three specific sub-adapters:
- **WorkflowExecutionAdapter**: Defines, deploys, and executes a workflow graph
- **PromptVersioningAdapter**: Stores, versions, retrieves, and diffs prompts
- **CostTrackingAdapter**: Records predicted costs and compares against actual provider billing

### The canary

Every benchmark batch starts with a **no-tool baseline** (the "canary"). If the benchmark leaked answers anywhere, the canary would score above zero. The canary must score exactly zero — this is a hard invariant. If it doesn't, the entire batch is invalid.

For LLMOps, the canary is a no-op workflow: setup does nothing, no workflow is defined, no prompt is stored, execution returns nothing, teardown does nothing. The canary must score zero on workflow accuracy and one on abstention.

## Who this is for

- **AI Platform Engineers** evaluating which LLMOps platform to adopt for workflow orchestration
- **MLOps / LLMOps teams** choosing between prompt management, tracing, and observability tools
- **CTOs/CIOs** making build-vs-buy decisions on AI workflow infrastructure with actual data
- **Open-source maintainers** of workflow engines or prompt management tools who want independent benchmarking
- **Researchers** studying the LLMOps and AI orchestration landscape
- **Vendors** who want to improve their tools based on real evidence

## What this is NOT

- Not a marketing site for any vendor
- Not a "best of" list based on GitHub stars or funding rounds
- Not a tutorial on how to use any LLMOps tool
- Not a replacement for your own due diligence
- Not a static document that never changes

## The "Quest"

The "LLMOps Engineer's Quest for the Best" is the ongoing effort to test, measure, and rank every tool on the roster. It's not a one-time effort. It's a continuous process of:
1. **Discovery** — finding new LLMOps tools via research, community, and submissions
2. **Triage** — deciding if a tool is serious enough to enter the roster
3. **Smoke gate** — running every tool through an identical 3-turn scenario to catch bugs
4. **Benchmark** — running standard + custom + stress tests for workflows, prompts, and cost tracking
5. **Publication** — publishing raw data + summary + per-tool deep-dives
6. **Iteration** — re-testing as tools update, as methodology improves, as new benchmarks emerge

## How to challenge a result

If you believe a ranking or score is wrong:
1. Check the **raw results JSON** — the data is public
2. Check the **adapter implementation** — the adapter code is public
3. Check the **judge prompts** — the prompts are frozen and public
4. File an issue with a specific claim and evidence
5. We'll re-run the test or update the methodology if warranted

## Governance

- **ArdurAI** maintains the almanac and runs the Quest
- **Methodology changes** require a public RFC and at least one edition cycle of notice
- **Tool additions/removals** are decided by the triage criteria (stars, last push, community activity, seriousness)
- **Benchmark results** are machine-generated; summaries are human-reviewed for fairness
- **Conflicts of interest** are disclosed (e.g., ArdurAI contributes to some tools on the roster); mitigation is identical harness for all

## License

Content: CC BY 4.0  
Harness code: MIT  
Raw data: CC BY 4.0
