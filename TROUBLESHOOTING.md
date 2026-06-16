# Troubleshooting & Debugging

How to understand the LLMOps codebase, debug issues, and resolve common problems when working with the almanac.

## Table of Contents

1. [Understanding the Codebase](#understanding-the-codebase)
2. [Common Issues](#common-issues)
3. [Debugging the Data Pipeline](#debugging-the-data-pipeline)
4. [Debugging Benchmark Runs](#debugging-benchmark-runs)
5. [FAQ](#faq)
6. [Getting Help](#getting-help)

---

## Understanding the Codebase

### High-level flow

```
Research Agents → Research Output (Markdown) →
  Python Script → roster.json (Structured Data) →
    Manual Review → Edition Markdown →
      Git Commit → GitHub Publication
```

### Key files and their roles

| File | Role | When to read it |
|------|------|-----------------|
| `README.md` | Project overview, quick reference | First thing you read |
| `INTENT.md` | Philosophy, why we do things this way | When you disagree with a decision |
| `IMPLEMENTATION.md` | How things are built, how to add LLMOps tools | When you want to contribute |
| `TESTING.md` | Benchmark methodology, scoring for LLMOps | When you want to reproduce or challenge a result |
| `TROUBLESHOOTING.md` | This file | When something is broken |
| `architecture.md` | Stack architecture diagram | When you want to understand the big picture |
| `editions/YYYY-MM.md` | Monthly snapshot of the LLMOps landscape | When you want historical data |
| `data/roster.json` | Machine-readable catalog | When you want to query or analyze the data |
| `methodology/benchmark-harness.md` | Harness specification for LLMOps | When you want to build an adapter or run benchmarks |

### The data model

The LLMOps almanac is fundamentally a **directed graph** of data:

```
Research findings → Tool metadata → Roster JSON → Edition Markdown → README
                                      ↓
                               Benchmark results → Per-tool pages
```

- **Research findings** are the raw output of the research swarm. They're saved in `research/` (not in the public repo).
- **Tool metadata** is extracted from research and stored in `data/roster.json`.
- **Roster JSON** is the single source of truth. Everything else derives from it.
- **Edition markdown** is human-written based on the roster and research.
- **README** is auto-generated from the roster and the latest edition.

### Understanding `data/roster.json`

This is the most important file in the repo. It is the single source of truth for the LLMOps tool catalog.

**Structure**:
```json
{
  "meta": { ... },
  "categories": {
    "workflow-orchestration": { ... },
    "prompt-management": { ... },
    "llm-observability": { ... }
  }
}
```

**How to query it**:
```bash
# Find all Tier A workflow orchestration tools
jq '.categories."workflow-orchestration".tools[] | select(.tier == "A") | .name' data/roster.json

# Count tools by tier across all LLMOps subcategories
jq '.categories | to_entries[] | .value.tools | group_by(.tier) | map({tier: .[0].tier, count: length})' data/roster.json

# Find all MIT-licensed tools
jq '.. | objects | select(.license == "MIT") | .name' data/roster.json

# Find all prompt management tools
jq '.categories."prompt-management".tools[] | .name' data/roster.json
```

### The edition markdown

Editions are **human-written** summaries, not machine-generated. They are based on the roster but include analysis, interpretation, and narrative that a machine can't produce.

**How editions are structured**:
1. Front matter: date, research method, context
2. Landscape at a glance: summary table
3. Per-subcategory sections: workflow orchestration, prompt management, LLM observability — findings, roster, analysis
4. Quest diary: what was tested this month (workflows, prompts, cost tracking)
5. Cross-category findings: patterns that span LLMOps subcategories

### The benchmark harness (separate repo)

The actual benchmark code lives in a separate repository. The almanac repo contains:
- The methodology specification
- The results (JSON + markdown)
- The adapters (interface definitions)

The harness repo contains:
- The runner code
- The LLMOps adapter implementations (workflow, prompt, cost tracking)
- The judge model integration
- The telemetry collector

**Why separate?** Because the harness is code that runs, and the almanac is data that is published. They have different lifecycles and different audiences.

## Common Issues

### Issue: `roster.json` is invalid JSON

**Symptoms**:
- `jq` fails to parse it
- GitHub Actions fails on JSON validation
- Python `json.load()` raises `JSONDecodeError`

**Diagnosis**:
```bash
python3 -c "import json; json.load(open('data/roster.json'))"
```

**Resolution**:
1. Find the line with the error: `python3 -m json.tool data/roster.json`
2. Common causes: trailing commas, unescaped quotes, incorrect nesting
3. Fix the JSON and re-validate
4. Consider using a JSON linter in your editor

### Issue: Edition markdown has broken links

**Symptoms**:
- Links to tools return 404
- Links to benchmarks don't exist yet
- Relative links work locally but break on GitHub

**Diagnosis**:
```bash
# Check all links in the repo
find . -name "*.md" -exec grep -oP '\[.*?\]\(.*?\)' {} + | grep -v "http" | grep -v "mailto"
```

**Resolution**:
1. For internal links, use relative paths: `../data/roster.json`
2. For external links, verify the URL is correct
3. For tools without a per-tool page yet, link to their homepage or GitHub repo
4. Run a link checker as part of CI

### Issue: Tier assignment is wrong

**Symptoms**:
- A tool is Tier A but has no production LLMOps usage
- A tool is Tier C but is widely adopted for workflow orchestration
- A tool's tier changed without explanation

**Diagnosis**:
1. Check the tier assignment rules in `IMPLEMENTATION.md`
2. Verify the tool's adoption, activity, and community health
3. Check the edition notes for the rationale

**Resolution**:
1. File an issue with evidence (GitHub stars, last push, production references, workflow orchestration adoption)
2. The tier will be reviewed in the next edition cycle
3. Tiers are not changed mid-edition; they are updated at edition boundaries

### Issue: Benchmark results can't be reproduced

**Symptoms**:
- Running the harness produces different workflow results
- The adapter fails with a different tool version
- The judge model is unavailable
- Workflow execution fails due to provider API changes

**Diagnosis**:
1. Check the `results.json` metadata for the exact commit, seed, and hardware
2. Check if the tool version has changed since the published run
3. Verify the judge model is accessible
4. Check if the underlying model provider API has changed (rate limits, response format, pricing)

**Resolution**:
1. Use the exact commit and dependencies from the results metadata
2. If the tool version changed, the results are for a different version — this is expected
3. If the judge model changed, that's a methodology issue — file an issue
4. If the provider API changed, the adapter may need updating — check `TROUBLESHOOTING.md` for provider-specific notes

### Issue: Adapter fails on workflow graph parsing

**Symptoms**:
- `define_workflow()` crashes with "invalid graph structure"
- Workflow nodes are not connected correctly
- The tool rejects the workflow definition with a schema error

**Diagnosis**:
1. Check the tool's workflow graph schema documentation
2. Verify the adapter is using the correct API version
3. Check if the tool requires specific node types or edge properties

**Common fixes**:
- Missing required node properties → Update the adapter to include them
- Wrong API version → Pin the tool version or update the adapter
- Graph schema mismatch → Check the tool's changelog for breaking changes
- Visual graph tools need specific coordinates → Add layout metadata to the adapter

### Issue: Benchmark results inconsistent due to model provider changes

**Symptoms**:
- Same workflow, same tool, different results across runs
- Token counts vary between runs
- Cost tracking accuracy suddenly degrades
- Model responses differ even with temperature=0

**Diagnosis**:
1. Check if the model provider updated their API (new model version, different tokenization)
2. Check if pricing changed since the last run
3. Check if rate limiting affects workflow execution timing

**Resolution**:
1. Provider API changes are documented in the edition notes
2. Update the adapter to handle new response formats
3. Re-run cost reconciliation with current pricing
4. If results are fundamentally different due to provider changes, note the provider version in the results metadata

### Issue: Prompt format incompatibilities

**Symptoms**:
- Prompts stored in one tool don't work when migrated to another
- Template variables (e.g., `{{variable}}` vs `{variable}`) are incompatible
- Prompt version retrieval returns normalized content that doesn't match the original

**Diagnosis**:
1. Check the tool's prompt template syntax
2. Check if the tool performs automatic normalization (whitespace, encoding)
3. Compare stored vs. retrieved prompt content byte-by-byte

**Resolution**:
1. Use the tool's documented template syntax in the adapter
2. Document normalization behavior in the adapter notes
3. If the tool silently alters prompts, classify as `version_drift` in the failure taxonomy

### Issue: Research agent missed an LLMOps tool

**Symptoms**:
- A well-known workflow engine is not in the roster
- A prompt management tool from a specific region is missing
- A newly launched LLMOps platform is not in the latest edition

**Diagnosis**:
1. Check if the tool meets triage criteria in `IMPLEMENTATION.md`
2. Check if it was added in a previous edition and later removed
3. Check if it falls outside the search scope (e.g., it's categorized as generic automation rather than LLMOps)

**Resolution**:
1. File an issue with the tool name, URL, and evidence of adoption/activity
2. The tool will be triaged for the next edition
3. If it meets criteria, it will be added

### Issue: Monthly update cron failed

**Symptoms**:
- No new edition was published on the 15th
- The cron job is missing from the scheduler
- The research agent timed out

**Diagnosis**:
```bash
# Check cron status
cron status

# Check the cron job list
# (use the Kimi Work cron interface)
```

**Resolution**:
1. Check if the cron job is still registered
2. Check if the research agent timed out (increase timeout if needed)
3. Manually trigger the update if the cron missed a cycle
4. Check the workspace path in the cron job configuration

### Issue: GitHub push fails

**Symptoms**:
- `git push` returns 403 or 401
- The remote is not configured
- The branch is behind origin

**Diagnosis**:
```bash
git remote -v
git status
git log --oneline -5
```

**Resolution**:
1. Verify the remote URL is correct: `git remote set-url origin https://github.com/ArdurAI/...`
2. Verify GitHub CLI auth: `gh auth status`
3. If behind origin, pull first: `git pull origin main`
4. If there are conflicts, resolve them manually

## Debugging the Data Pipeline

### Research output → roster.json

**Problem**: Research agents produce markdown, but the roster JSON is incomplete or wrong.

**Debug steps**:
1. Read the research output files in `research/` (local workspace, not in the repo)
2. Check if the Python extraction script correctly parsed the tool tables
3. Check if tools were dropped during triage (check the triage log)
4. Verify the JSON schema is correct

**Common bugs**:
- Tool names with special characters break JSON parsing → Escape them properly
- Tools with no tier get dropped → Default to Tier C if unsure
- Tools with no notes get empty strings → Add a minimal note
- LLMOps tools miscategorized as generic automation → Check the `type` field

### roster.json → edition markdown

**Problem**: The edition doesn't reflect the roster.

**Debug steps**:
1. Compare the tool counts in the roster vs. the edition
2. Check if the edition was written before the roster was updated
3. Check if tools were manually edited in the edition but not in the roster

**Resolution**:
1. The edition should be derived from the roster, not the other way around
2. If the edition has manual additions, ensure they are also in the roster
3. The edition is a human-readable summary; the roster is the source of truth

### Edition markdown → README

**Problem**: The README roster-at-a-glance doesn't match the latest edition.

**Debug steps**:
1. Check which edition is referenced in the README
2. Check if the README was updated after the edition was published

**Resolution**:
1. The README should always reference the latest edition
2. Update the README when a new edition is published
3. Consider automating README updates from the roster JSON

## Debugging Benchmark Runs

### The adapter fails

**Symptoms**:
- `setup()` crashes (e.g., Docker Compose fails for self-hosted workflow engines)
- `define_workflow()` throws an exception (e.g., invalid graph schema)
- `execute_workflow()` returns nothing or garbage (e.g., workflow node silently fails)
- `get_cost_report()` returns mismatched values

**Debug steps**:
1. Run the adapter in isolation (without the harness)
2. Check the tool's documentation for setup requirements (API keys, Docker, provider credentials)
3. Check if environment variables are set (multiple provider API keys are often needed)
4. Check if the tool version matches what the adapter expects

**Common fixes**:
- Missing Docker daemon → Start Docker
- Missing API key → Set the environment variable for the required model provider
- Wrong tool version → Update the adapter or pin the version
- Dependency conflict → Use a virtual environment or container
- Workflow graph schema changed → Update the adapter's graph construction logic
- Provider API key expired → Renew and re-run

### The canary fails

**Symptoms**:
- The no-tool baseline scores above zero on workflow accuracy
- The abstention score is not 1.000
- Cost tracking shows non-zero values for the canary

**Debug steps**:
1. Check if the benchmark workload has leaked answers
2. Check if the grading pipeline has a bug
3. Check if the random seed was set
4. Check if the canary adapter is truly a no-op

**Resolution**:
1. If the workload leaked answers, redesign the workload
2. If the grader has a bug, fix the grader and rerun all tests
3. This is a critical failure — the entire batch is invalid

### Results are inconsistent

**Symptoms**:
- Same tool, same test, different workflow results across runs
- Scores vary by more than the confidence interval
- Prompt version retrieval returns different content on different runs
- Cost tracking varies despite identical inputs

**Debug steps**:
1. Check if the tool has non-deterministic behavior (temperature > 0, async timing, model provider jitter)
2. Check if the hardware was different between runs
3. Check if the tool version changed between runs
4. Check if the model provider's API behavior changed (e.g., different model version deployed)

**Resolution**:
1. Set temperature to 0 for all LLM calls in the adapter
2. Record hardware specs in the results metadata
3. Pin tool versions and record them
4. Record the model provider version and API behavior in the results metadata
5. If provider non-determinism is the cause, document it and increase the confidence interval

## FAQ

### Q: Why is tool X not in the roster?

A: Either it doesn't meet triage criteria, it hasn't been discovered yet, or it was removed for inactivity. File an issue with evidence and we'll triage it.

### Q: Why did tool X's score change?

A: Either the tool was updated, the methodology was refined, we found a bug in our previous test, or the underlying model provider behavior changed. All four are valid reasons. Check the edition notes for the rationale.

### Q: Can I run the benchmarks myself?

A: Yes. The harness is published separately. Clone it, install dependencies, and run the adapter for the tool you want to test. Note that LLMOps benchmarks often require multiple model provider API keys. See `TESTING.md` for reproducibility instructions.

### Q: How do I challenge a ranking?

A: File an issue with specific evidence. Check the raw results JSON, the adapter code, and the judge prompts. If you find a real problem, we'll re-run or update the methodology.

### Q: Can I add a tool to the roster?

A: Yes. See `CONTRIBUTING.md` for instructions. The tool must meet triage criteria and pass the LLMOps smoke gate (create workflow, execute workflow, verify output and trace).

### Q: Why is this a separate category almanac?

A: LLMOps is deep enough to warrant its own dedicated repo with per-tool pages, category-specific benchmarks (workflow reliability, prompt versioning, cost tracking), and focused community. The parent almanac is the master catalog.

### Q: How often are benchmarks re-run?

A: Standard: every quarter for LLMOps tools. Stress: annually. Integration: quarterly. If a tool releases a major version (especially one affecting workflow execution or prompt versioning), we may re-run early.

### Q: What's the difference between Tier A, B, and C?

A: Tier A = market leader or strongest technical merit for LLMOps. Tier B = solid option, specific use cases (e.g., code-first workflow engines). Tier C = niche, early-stage, or specialized. See `IMPLEMENTATION.md` for full rules.

### Q: Why do results vary when model providers change their APIs?

A: LLMOps tools depend on underlying model providers. When a provider changes pricing, tokenization, or response formats, the tool's behavior can change even if the tool itself didn't update. We document provider versions in the results metadata and note significant changes in edition notes.

### Q: Can vendors sponsor the almanac?

A: No. The almanac is independently funded. Sponsorship would compromise the core mission. Vendors can improve their scores by actually improving their tools.

## Getting Help

### File an issue

GitHub issues are the primary support channel. Use the appropriate template:

- **Tool request**: "Add [Tool Name] to LLMOps"
- **Data correction**: "[Tool Name] metadata is wrong: [what's wrong]"
- **Benchmark challenge**: "Challenge [Tool Name] ranking on [Dimension]: [evidence]"
- **Bug report**: "[Bug description] in [file/process]"
- **Feature request**: "[Feature description] for [use case]"

### Discussion

GitHub Discussions are for:
- General questions about the LLMOps almanac
- Sharing experiences with tools on the roster
- Proposing methodology changes
- Community announcements

### Email

For private or sensitive inquiries: Use the contact info in the ArdurAI org profile.

## License

Content: CC BY 4.0
