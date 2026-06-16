# Implementation Guide

How the LLMOps almanac is built, how to add a tool, how to update an edition, and how the data pipeline works.

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [The Data Pipeline](#the-data-pipeline)
3. [Adding a New LLMOps Tool](#adding-a-new-llmops-tool)
4. [Updating an Edition](#updating-an-edition)
5. [The Roster JSON Schema](#the-roster-json-schema)
6. [Directory Conventions](#directory-conventions)
7. [Building the Adapter](#building-the-adapter)
8. [Automation](#automation)

---

## Repository Structure

```
ai-llmops-almanac/
├── README.md                          # Project overview + roster at a glance
├── INTENT.md                          # Philosophy, design principles, governance
├── IMPLEMENTATION.md                  # This file
├── TESTING.md                         # Benchmark methodology, harness details
├── TROUBLESHOOTING.md                 # Common issues, debugging, FAQ
├── CONTRIBUTING.md                    # How to contribute
├── architecture.md                    # Stack architecture + test philosophy
├── SETUP.md                           # How to push to GitHub
├── .gitignore
│
├── editions/                          # Monthly editions
│   └── 2026-06.md                   # Founding edition
│
├── benchmarks/                        # Benchmark results (rolling)
│   └── (populated as results land)
│
├── methodology/
│   └── benchmark-harness.md         # Detailed harness spec for LLMOps
│
├── data/
│   └── roster.json                  # Machine-readable catalog (LLMOps tools)
│
├── tools/                             # Per-tool deep-dive pages (placeholder)
│   └── (populated as deep-dives are written)
│
└── assets/                            # Charts, diagrams, screenshots
    └── (populated by editions)
```

## The Data Pipeline

The almanac data flows through four stages:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Discovery      │────▶│  Triage         │────▶│  Research       │────▶│  Publication    │
│  (find tools)   │     │  (decide entry) │     │  (deep dive)    │     │  (write edition) │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Stage 1: Discovery

LLMOps tools are discovered through:
- **Monthly research swarm**: 8-10 parallel agents search for new tools in workflow orchestration, prompt management, and AI observability
- **Community submissions**: Issues, PRs, email, social media
- **Vendor announcements**: Funding rounds, product launches, major releases (e.g., new workflow engine versions, prompt versioning features)
- **GitHub trending**: New repos with significant star growth in LLMOps-related topics
- **Conference talks**: Papers, demos, blog posts from AI engineering conferences (e.g., AI Engineer Summit, LLM Conference)

### Stage 2: Triage

A tool enters the roster if it meets ALL of these criteria:
1. **Seriousness**: Not a toy/demo. Must have a real use case, real users, or real funding. Must actually orchestrate workflows, manage prompts, or track LLM operations — not just be a thin wrapper around an API.
2. **Activity**: Last push or release within 6 months. Exceptions for "stable/mature" tools (e.g., established workflow engines with slow release cycles).
3. **Documentation**: Must have a README, docs, or at least a landing page explaining what it does. Must document workflow patterns, prompt versioning behavior, or cost tracking features.
4. **Accessibility**: Must be accessible to test (open source, free tier, or evaluation license available). Self-hosted options are preferred for ops-burden testing.
5. **Scope**: Must fit the LLMOps category definition. A general-purpose automation tool (e.g., generic RPA) doesn't enter unless it has specific LLM orchestration features. A generic observability tool doesn't enter unless it has LLM-specific tracing.

A tool is **excluded** if:
- It's a fork with no meaningful divergence from the parent
- It's a thin wrapper around another tool with no added LLMOps value
- It has no users, no community, and no evidence of real-world LLM workflow usage
- It requires an enterprise-only license with no evaluation path

### Stage 3: Research

For each new tool, we collect:
- Name, type, license, language, GitHub URL, stars
- Last push date, release cadence
- Key features: workflow engine type (visual graph, code-based, hybrid), prompt versioning support, multi-model routing, cost tracking, observability/tracing
- Known bugs and sharp edges (from smoke gate): workflow execution failures, prompt version drift, cost tracking discrepancies
- Community health (issues, PRs, maintainer responsiveness)

This data is stored in `data/roster.json` and summarized in the edition.

### Stage 4: Publication

The edition is a markdown file that includes:
- Landscape at a glance table
- Per-subcategory findings and trends (workflow orchestration, prompt management, observability)
- New tools added and tools removed
- Notable releases and acquisitions
- Quest diary (what was tested this month: workflows, prompts, cost tracking)

## Adding a New LLMOps Tool

### Step 1: Verify the tool meets triage criteria

Check: seriousness, activity, documentation, accessibility, scope. Ensure it actually fits LLMOps (orchestration, prompt management, or LLM observability) and not generic automation or generic observability.

### Step 2: Add to the roster JSON

Edit `data/roster.json` and add the tool to the appropriate category:

```json
{
  "name": "ToolName",
  "type": "Workflow Engine | Prompt Manager | LLM Observability | Orchestration Platform | Cost Tracker",
  "license": "License",
  "region": "Region",
  "tier": "A|B|C",
  "notes": "One-line description and key differentiators (e.g., visual workflow builder, semantic prompt versioning, multi-model fallback routing)"
}
```

**Tier assignment rules**:
- **Tier A**: Market leader in LLMOps, widest adoption for workflow orchestration or prompt management, or strongest technical merit. Must be actively maintained and have real production LLM workflow usage.
- **Tier B**: Solid option, actively maintained, but not the market leader. Good for specific use cases (e.g., code-first workflow engines, specialized prompt versioning tools).
- **Tier C**: Niche, early-stage, or specialized. Worth knowing about but not a default choice for general LLMOps.

### Step 3: Update the edition

Add the tool to the appropriate category section in `editions/YYYY-MM.md`. If the tool is Tier A, add it to the roster-at-a-glance table in the README.

### Step 4: Update the category README

If the tool is Tier A, update the tier list in the relevant cross-reference category (e.g., `categories/llmops-platforms/README.md` or `categories/prompt-management/README.md`).

### Step 5: Run the smoke gate

Before the tool is officially "in," it must pass the smoke gate (see TESTING.md). If it fails, document the failure in the edition and assign it to Tier C with a note about the blocker.

The LLMOps-specific smoke gate is:
1. **Turn 1**: Define and store a workflow (or prompt) in the tool
2. **Turn 2**: Execute the workflow (or retrieve the prompt version)
3. **Turn 3**: Verify the output, trace the execution, and check for data loss or version drift

## Updating an Edition

### Monthly update checklist

```
□ Check for new LLMOps tools (discovery phase)
□ Triage new tools (add to roster or reject)
□ Update metadata for existing tools (stars, last push, releases)
□ Flag tools for removal (dead/abandoned)
□ Run smoke gate for new tools
□ Run benchmark updates for re-tested tools (workflow reliability, prompt versioning, cost tracking)
□ Draft the edition markdown
□ Update README roster-at-a-glance
□ Update category READMEs
□ Commit and push
```

### Edition markdown template

```markdown
# Edition YYYY-MM — [Title]

*Research conducted YYYY-MM-DD. [Context about this month].*

## The landscape at a glance

| Category | Tool Count | New This Month | Notable Changes |
|----------|-----------|----------------|-----------------|

## [Subcategory] — [Theme]

### Tier A roster
[table]

### Findings
[bullets]

## Quest diary — [Month] [Year]

- [what was done: workflows tested, prompt versioning stress-tested, cost tracking validated]

## Coming next month

[what's planned]

## License
Content is licensed CC BY 4.0.
```

## The Roster JSON Schema

```json
{
  "meta": {
    "name": "LLMOps Platforms & Workflow Automation Almanac Roster",
    "version": "YYYY-MM",
    "generated_at": "ISO-8601 timestamp",
    "total_tools": number,
    "categories": number,
    "research_method": "description"
  },
  "categories": {
    "workflow-orchestration": {
      "name": "Workflow Orchestration",
      "description": "Tools for building, deploying, and executing LLM-powered workflows and agent graphs",
      "estimated_total": number,
      "tools": [
        {
          "name": "Tool Name",
          "type": "Workflow Engine | Orchestration Platform",
          "license": "License",
          "region": "Region",
          "tier": "A|B|C",
          "notes": "Description"
        }
      ]
    },
    "prompt-management": {
      "name": "Prompt Management",
      "description": "Tools for versioning, deploying, and tracking prompts across environments",
      "estimated_total": number,
      "tools": [
        {
          "name": "Tool Name",
          "type": "Prompt Manager | Prompt Registry",
          "license": "License",
          "region": "Region",
          "tier": "A|B|C",
          "notes": "Description"
        }
      ]
    },
    "llm-observability": {
      "name": "LLM Observability",
      "description": "Tools for tracing, evaluating, and monitoring LLM calls and workflow executions",
      "estimated_total": number,
      "tools": [
        {
          "name": "Tool Name",
          "type": "LLM Observability | Cost Tracker | Tracing Platform",
          "license": "License",
          "region": "Region",
          "tier": "A|B|C",
          "notes": "Description"
        }
      ]
    }
  }
}
```

**Field definitions**:
- `name`: The tool's common name. Use the name the tool calls itself.
- `type`: What kind of LLMOps tool is it? (e.g., "Workflow Engine", "Prompt Manager", "LLM Observability", "Orchestration Platform", "Cost Tracker")
- `license`: The primary license. Use SPDX identifiers where possible.
- `region`: Where the tool is primarily developed (US, EU, China, Global, etc.)
- `tier`: A, B, or C (see tier rules above)
- `notes`: One-line description with key differentiators. Keep under 100 chars. Mention workflow type, prompt versioning, or cost tracking if relevant.

## Directory Conventions

### `editions/`
- One file per month: `YYYY-MM.md`
- Never delete old editions. The history is part of the record.
- New editions are appended; old editions are never rewritten.

### `data/`
- `roster.json` is the single source of truth for the LLMOps tool catalog.
- It is machine-generated from the research process.
- It should be valid JSON at all times.

### `benchmarks/`
- One file per benchmark run: `<category>-<suite>-<date>.md`
- Raw JSON files alongside the markdown: `<category>-<suite>-<date>.json`
- Raw data is never deleted. It is the audit trail.
- LLMOps-specific suites: `workflow-reliability`, `prompt-versioning`, `cost-tracking`, `multi-model-orchestration`

### `tools/`
- One file per tool: `<name>.md`
- Contains deep-dive analysis: setup experience, benchmark results, bug notes, comparison with peers
- Populated as deep-dives are written (not all tools have a page immediately)

### `assets/`
- Images, charts, diagrams referenced by editions and benchmarks
- Named descriptively: `workflow-latency-2026-06.png`, `cost-tracking-accuracy-2026-06.png`, `prompt-version-drift-2026-06.png`

### `methodology/`
- The benchmark harness specification for LLMOps testing
- Frozen before any results are generated
- Changes require an RFC and a public announcement

## Building the Adapter

When a new LLMOps tool is added to the roster and is ready for benchmarking, an adapter must be built. The adapter is the bridge between the tool's API and the harness's fixed interface.

### The LLMOps CategoryAdapter contract

```python
class LLMOpsAdapter(CategoryAdapter):
    def setup(self) -> None:
        """Install, configure, and start the LLMOps platform."""
        pass
    
    def define_workflow(self, workflow_spec) -> WorkflowHandle:
        """Define a workflow graph (or agent chain) in the tool."""
        pass
    
    def deploy_prompt(self, prompt, version_tag) -> PromptHandle:
        """Store and version a prompt in the tool."""
        pass
    
    def await_ready(self) -> None:
        """Wait for async workflow deployment or prompt indexing to complete. Measure lag."""
        pass
    
    def execute_workflow(self, workflow_handle, inputs) -> ExecutionResult:
        """Execute the workflow and return the result plus trace."""
        pass
    
    def retrieve_prompt(self, prompt_handle, version) -> Prompt:
        """Retrieve a specific prompt version."""
        pass
    
    def get_cost_report(self, execution_result) -> CostReport:
        """Return the tool's predicted cost for the execution."""
        pass
    
    def teardown(self) -> None:
        """Clean up, measure resource usage."""
        pass
```

### Adapter rules

1. The adapter must be **pure** — it should not modify the tool's behavior, only interface with it.
2. The adapter must be **documented** — every step should be explainable in plain English.
3. The adapter must be **reproducible** — running it twice on the same machine should produce the same setup.
4. The adapter must be **isolated** — it should not depend on other tools' adapters.
5. The adapter code is **published** in the benchmark harness repo (separate from the almanac repo).

### Adapter sub-patterns for LLMOps

#### Workflow Execution Adapter

Handles the translation from the harness's standard workflow graph to the tool's specific representation:
- **Visual graph tools** (e.g., Flowise, n8n): The adapter constructs the JSON/graph representation programmatically
- **Code-based tools** (e.g., LangChain, LlamaIndex): The adapter writes the orchestration code and executes it
- **Hybrid tools** (e.g., Dify): The adapter uses the API to create workflows and then triggers them

#### Prompt Versioning Adapter

Handles prompt storage, versioning, retrieval, and diffing:
- Must support: store prompt → tag version → retrieve by tag → verify content matches
- Must test: concurrent updates, rollback to previous version, deployment to production

#### Cost Tracking Adapter

Handles cost prediction and reconciliation:
- Must support: execute workflow → get predicted cost from tool → compare against actual provider API billing
- Must test: multi-model routing cost accuracy, token-count estimation, budget alert triggers

### Example adapter (pseudocode)

```python
class DifyAdapter(LLMOpsAdapter):
    def __init__(self, config):
        self.config = config
        self.base_url = "http://localhost:3001"
    
    def setup(self):
        subprocess.run(["docker", "compose", "up", "-d"], cwd=self.config.dify_dir)
        self.client = DifyClient(self.base_url, api_key=self.config.api_key)
    
    def define_workflow(self, workflow_spec):
        # Create a workflow app via Dify API
        app = self.client.create_workflow_app(name=workflow_spec.name)
        # Build the graph from the spec
        for node in workflow_spec.nodes:
            self.client.add_node(app.id, node)
        for edge in workflow_spec.edges:
            self.client.add_edge(app.id, edge)
        return WorkflowHandle(app.id)
    
    def deploy_prompt(self, prompt, version_tag):
        # Store prompt in Dify's prompt management
        prompt_id = self.client.create_prompt(name=prompt.name, content=prompt.content)
        self.client.tag_version(prompt_id, version_tag)
        return PromptHandle(prompt_id, version_tag)
    
    def await_ready(self):
        # Wait for workflow to be publishable
        while not self.client.is_workflow_ready(app_id):
            time.sleep(0.5)
    
    def execute_workflow(self, workflow_handle, inputs):
        result = self.client.run_workflow(workflow_handle.id, inputs=inputs)
        return ExecutionResult(
            output=result.output,
            trace=result.trace,
            latency=result.latency,
            token_count=result.token_count
        )
    
    def get_cost_report(self, execution_result):
        return self.client.get_cost_report(execution_result.trace_id)
    
    def teardown(self):
        subprocess.run(["docker", "compose", "down"], cwd=self.config.dify_dir)
```

## Automation

### Monthly update cron

The monthly update is run by a scheduled job:
- **Trigger**: `cron` expression `0 7 15 * *` (monthly, 15th at 7:00 AM)
- **Action**: Runs a research agent to discover new LLMOps tools, update metadata, and draft the next edition
- **Output**: Commits to the repo with the updated roster and new edition

### GitHub Actions (optional)

For automatic metadata refresh (GitHub stars, last push dates), a GitHub Actions workflow can be configured:

```yaml
name: Monthly Metadata Refresh
on:
  schedule:
    - cron: '0 7 1 * *'
  workflow_dispatch:
jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Refresh metadata
        run: python scripts/refresh_metadata.py
      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -m "Monthly metadata refresh: $(date +%Y-%m)" || echo "No changes"
          git push
```

## License

Content: CC BY 4.0  
Code: MIT
