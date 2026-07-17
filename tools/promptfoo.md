# Promptfoo


[![Observability](https://img.shields.io/badge/Also_in-Observability-blue)](https://github.com/ArdurAI/ai-observability-almanac) [![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Prompt Testing
- **License**: Open Source
- **Region**: N/A
- **Tier**: B
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-07-17

> CI/CD; regression tests, prompt quality; open-source tool for testing & evaluating; CLI and CI/CD

---

## Overview

CI/CD; regression tests, prompt quality; open-source tool for testing & evaluating; CLI and CI/CD

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `git clone` to working | ⏳ TBD | To be measured in Quest smoke gate |
| Dependency count | Direct + transitive | ⏳ TBD | |
| Docker required? | Yes / No | ⏳ TBD | |
| Language runtime | Required version | ⏳ TBD | |
| Auth complexity | API key / OAuth / None | ⏳ TBD | |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# Typical installation path — verify before documenting
```

### Known sharp edges
- ⏳ To be discovered in smoke gate

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

> Raw results JSON: `benchmarks/llmops-platforms-promptfoo-<date>.json`

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
- ⏳ TBD

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
| Self-hostable | Yes / No / Partial | |
| Open source | Yes / No | |
| Audit trail | Yes / No | |
| Data residency controls | Yes / No | |
| On-premise deployment | Yes / No | |
| Export format | ⏳ TBD | |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | ⏳ TBD | |
| GDPR | ⏳ TBD | |
| HIPAA | ⏳ TBD | |
| ISO 27001 | ⏳ TBD | |
| EU AI Act | ⏳ TBD | |
| FedRAMP | ⏳ TBD | |

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
- ⏳ TBD (tools commonly used together)

### Alternatives to consider
- ⏳ TBD (when this tool is not the right fit)

---

## Links

- Official site: ⏳
- GitHub: ⏳
- Documentation: ⏳
- Community / Discord: ⏳
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| | | |

---

## Deep Analysis

### Daily monitoring update — 2026-07-17

- **Latest release:** `0.121.19` (2026-07-14): Adds Bedrock GPT-5.6 frontier provider support.

### Daily monitoring update — 2026-07-09

- **Latest release:** `0.121.18` (2026-07-08): adds a Node.js 20 support-cutoff campaign and associated release housekeeping.

### 1. How Is This Tool Useful?

Promptfoo is an open-source CLI-based tool for testing and evaluating LLM outputs, prompts, and model configurations. It enables teams to write test suites as YAML/JSON configurations that run prompts against multiple models, assert expected behaviors, and catch regressions before deployment. The tool is particularly useful for teams that want CI/CD-integrated, deterministic testing of LLM behavior without a full observability platform.

### 2. Gotchas of Using This Tool

Promptfoo's CLI-first approach requires developer involvement — non-technical team members cannot easily participate in evaluation. The tool focuses on testing rather than production observability, so teams need a separate tool for runtime monitoring. YAML/JSON test configuration can become verbose for complex test scenarios. The assertion library, while growing, may require custom JavaScript for domain-specific evaluation. Integration with production observability stacks requires custom work.

### 3. Limitations

Promptfoo is a testing tool, not a full LLMOps platform — it lacks production tracing, real-time monitoring, and prompt version management. The evaluation is batch-oriented rather than real-time. Multi-agent workflow testing is not natively supported. The TypeScript/JavaScript ecosystem is primary; Python support is secondary. Large-scale evaluation across many models can incur significant API costs. The platform does not provide a hosted dashboard or collaboration features.

### 4. How Secure Is This Tool?

Promptfoo is open-source (MIT license) with the code on GitHub for independent review. The tool runs locally or in CI/CD — no data is sent to external servers unless the team configures it. No major CVEs have been reported. API keys for LLM providers are read from environment variables. Teams should ensure test configurations do not contain sensitive data that would be sent to LLM providers during evaluation runs.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 4/10.** Promptfoo is a developer tool requiring CLI and YAML/JSON proficiency. Non-technical users cannot use it; it integrates into developer workflows and CI/CD pipelines.

### 6. What Does This Tool Solve That Others Don't?

Promptfoo's unique strength is being a lightweight, CLI-native testing tool that integrates seamlessly into CI/CD pipelines — running prompt and model tests as part of the development workflow. The YAML-based test configuration with assertion types (contains, equals, is-json, llm-rubric, etc.) is intuitive for developers. The ability to test against multiple models simultaneously helps teams choose the best model for each use case. The fully open-source, local-first approach avoids vendor lock-in.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Braintrust | Evaluation platform | Eval workflows |
| 2 | LangSmith | Full LLMOps + testing | Ecosystem depth |
| 3 | Promptfoo | CLI testing | Open-source + CI/CD |
| 4 | Confident AI | AI QA + compliance | Regulated industries |
| 5 | HoneyHive | Agent testing | Test suites |

### 8. How Can This Tool Be Improved? How Active Is Development?

Promptfoo is actively developed with regular releases on GitHub. Key improvements include adding a web dashboard for non-developer collaboration, expanding the assertion library, adding Python SDK parity, deepening agent workflow testing, adding production monitoring features, and improving documentation for CI/CD integration patterns.

### 9. Official Maintainer Contacts

Promptfoo is maintained by the Promptfoo team. GitHub: https://github.com/promptfoo/promptfoo. Website: https://www.promptfoo.dev. Documentation: https://www.promptfoo.dev/docs. The team is active on GitHub issues.

### 10. General Usage Guidance

Use Promptfoo if you want lightweight, CI/CD-integrated testing of LLM outputs and prompts. It excels as a developer tool for catching regressions before deployment. For production observability, pair with Langfuse or LangSmith. For more comprehensive evaluation with a web UI, evaluate Braintrust. Start by writing test cases for your most critical prompts, then integrate into your CI pipeline.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.

---

*Authored by Team Ardur · CC BY 4.0*
