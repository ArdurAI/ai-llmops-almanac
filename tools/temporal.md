# Temporal

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Durable Execution
- **License**: MIT (Open Source)
- **Region**: USA (Seattle)
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Long-running workflows; automatic retry, state persistence; production-grade for agents; Go-based

---

## Overview

Temporal is a durable execution platform built by Temporal Technologies in Seattle, founded in 2019 by the original creators of Uber's Cadence workflow engine. It is the most mature and widely adopted technology in the emerging durable execution category. The core premise is simple but powerful: developers write business logic as plain code in their preferred language (Go, Java, Python, TypeScript, .NET, PHP, Ruby), and Temporal automatically persists the complete running state of every workflow. If a process crashes, a server restarts, or a network flakes, the workflow resumes exactly where it left off without any manual recovery code.

Temporal is particularly compelling for AI agent workloads because agent loops are inherently long-running, multi-step, and failure-prone. A Temporal workflow can run an agent loop for hours or days, automatically retrying individual LLM calls or tool executions, persisting state across restarts, and handling signals and timers. The platform is production-grade: it powers 1,500+ paying customers including Nvidia, Netflix, Snap, and Stripe, and has a $5 billion valuation following a $300M Series D in 2025 led by a16z. The server is written in Go, but the polyglot SDKs are all production-ready, with Go and Java being the most mature and Python/TypeScript rapidly catching up.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | CLI install to working | ~5 minutes | `brew install temporal` + `temporal server start-dev` |
| Dependency count | Direct + transitive | Varies by SDK | SDK-specific; Temporal server is a single binary |
| Docker required? | Yes / No | Optional | Pre-built Docker images available; CLI runs locally without Docker |
| Language runtime | Required version | SDK-dependent | Python 3.9+, Go 1.21+, Node 18+, Java 11+ |
| Auth complexity | API key / OAuth / None | None (local) / mTLS (Cloud) | Local dev server has no auth; Cloud uses mTLS |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# macOS / Linux - install CLI
brew install temporal

# Start local development server
temporal server start-dev

# Open Web UI
open http://localhost:8233

# Docker alternative
docker run --rm -p 7233:7233 -p 8233:8233 temporalio/server:latest

# Python SDK
pip install temporalio

# Go SDK
go get go.temporal.io/sdk

# TypeScript SDK
npm install @temporalio/client @temporalio/worker
```

### Known sharp edges
- **Action-based billing surprise**: Temporal Cloud bills per "action" (workflow starts, activity executions, signals, timers). Workflows often generate 10–50x more actions than anticipated. One developer reported a $500 bill for 13,000 workflow executions due to action multiplication. Budget conservatively.
- **Not for simple request-response**: If an operation completes in a single HTTP request cycle, Temporal adds unnecessary complexity and latency. Don't use it for CRUD endpoints.
- **Sub-millisecond latency limitations**: Temporal's event-sourcing model adds overhead. For hot-path latency-critical operations, direct service calls are faster.
- **Workflow history limits**: Long-running workflows with many steps can hit history size limits, requiring the "Continue-As-New" pattern to reset the history while preserving state.
- **Learning curve**: Durable execution is a different mental model from traditional request/response or queue-based processing. Teams need time to internalize workflows, activities, and signals.
- **Tiny team overhead**: For a 2-person team with 3 microservices, a well-configured SQS queue with dead-letter handling may be simpler. Temporal pays off when reliability plumbing consumes >20% of engineering time.
- **Self-hosting complexity**: Running the open-source Temporal server in production requires managing Cassandra/PostgreSQL, Elasticsearch, and multiple services. Not trivial for small teams.

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

> Raw results JSON: `benchmarks/llmops-platforms-temporal-<date>.json`

---

## Bug Notes

### Smoke gate findings
- ⏳ Not yet tested

### Known issues (from community / docs)
- **Action count explosion**: The most common cost surprise. Each activity retry, signal, and timer counts as an action. Loops with many iterations generate many actions.
- **Workflow history growth**: Workflows that accumulate thousands of events become slow to replay. The "Continue-As-New" pattern is required but adds complexity.
- **Worker connection limits**: Workers maintain persistent gRPC connections to the server. Large worker pools can hit connection limits or load-balancer issues.
- **Temporal ignores business errors**: Temporal handles infrastructure failures (crashes, restarts) but does not handle business logic errors (e.g., insufficient funds). Developers must still code business error handling.
- **Cross-SDK workflow compatibility**: Workflow histories produced by different language SDKs are not interchangeable. You cannot safely have Go and Python workers on the same task queue for the same workflow type.

### Workarounds documented
- Use the Temporal Cloud pricing calculator aggressively; assume 5–10x the naive action count.
- Implement "Continue-As-New" for long-running workflows before history limits are reached.
- Use separate task queues per SDK language to avoid cross-SDK compatibility issues.
- Monitor workflow execution counts and action usage in the Web UI or Cloud metrics.

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
- **Open source (self-hosted)**: Free (MIT license). You manage the server, database, and infrastructure.
- **Temporal Cloud — Essentials**: $100/month. Includes 1M actions, 1GB active storage, 40GB retained storage, business-hours support.
- **Temporal Cloud — Business**: $500/month. Includes 2.5M actions, 2.5GB active storage, 100GB retained storage, SAML SSO, SCIM, 2-hour P0 response.
- **Temporal Cloud — Enterprise / Mission Critical**: Custom pricing. Includes custom allocations, 24/7 support, 99.99% SLA, 15-minute P0 response, dedicated TAM.
- **Startup Program**: $6,000 in free credits for companies with <$30M funding.
- **Universal free trial**: $1,000 in credits for 90 days for all new accounts.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-10 users) | $0–100/mo | Self-hosted free; Cloud Essentials for dev/test |
| Medium (10-100 users) | $500–2,000/mo | Cloud Business; action count becomes dominant factor |
| Large (100+ users) | $2,000–10,000+/mo | Enterprise tier; action multiplication is the cost driver |
| Enterprise | Custom | Mission Critical for high-availability requirements |

### Hidden costs
- **Action multiplication**: The #1 hidden cost. A workflow with 10 activities, 3 retries each, and 2 signals = 50+ actions per execution.
- **Self-hosting infrastructure**: Running open-source Temporal requires PostgreSQL/MySQL, Elasticsearch, and multiple server instances.
- **Learning curve**: Teams need 2–4 weeks to internalize the durable execution model.
- **Worker fleet**: Production deployments need a pool of worker processes running 24/7.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Yes | Fully open source; deploy on any infrastructure |
| Open source | Yes | MIT license |
| Audit trail | Yes | Complete workflow execution history persisted and queryable |
| Data residency controls | Yes | Cloud supports configurable regions; self-hosting gives full control |
| On-premise deployment | Yes | Full support for on-premises and air-gapped deployments |
| Export format | JSON, protobuf | Workflow histories and state exportable via API |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | SOC 2 Type II certified (Temporal Cloud) |
| GDPR | Yes | GDPR compliant (Temporal Cloud) |
| HIPAA | Yes | HIPAA compliant (Temporal Cloud) |
| ISO 27001 | Partial | No explicit ISO 27001 claim found; SOC 2 Type II covers similar ground |
| EU AI Act | Partial | Durable execution is infrastructure-agnostic; compliance depends on use case |
| FedRAMP | No | Not formally FedRAMP authorized as of 2026 |

> **Note**: Compliance certifications apply to Temporal Cloud. The open source Temporal server does not hold formal certifications. Organizations with strict compliance requirements can self-host and implement their own controls, or use Temporal Cloud with its certified security posture. The platform provides mTLS encryption, data encryption at rest, and configurable retention (1–90 days) on Cloud.

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
- [Pydantic AI](pydantic-ai.md) — Type-safe agent framework; integrates with Temporal for durable agent loops
- [OpenAI Agents SDK](openai-agents-sdk.md) — Can be wrapped in Temporal workflows for durability
- [LangGraph](langgraph.md) — Stateful agent graphs; Temporal provides the durable execution layer underneath
- [Cadence](https://cadenceworkflow.io) — Uber's predecessor engine; Temporal is the successor
- [AWS Step Functions](https://aws.amazon.com/step-functions) — Cloud-native alternative; less flexible than Temporal
- [DBOS](https://dbos.dev) — Emerging durable execution system with database-native approach

### Alternatives to consider
- [Cadence](https://cadenceworkflow.io) — Predecessor to Temporal; still maintained at Uber but community has consolidated around Temporal
- [AWS Step Functions](https://aws.amazon.com/step-functions) — Simpler, fully managed, but less flexible and vendor-locked
- [Apache Airflow](https://airflow.apache.org) — Batch workflow orchestration; not designed for long-running stateful processes
- [Restate](https://restate.dev) — Emerging lightweight alternative focused on cloud-native durable execution
- [Prefect](https://www.prefect.io) — Modern Python workflow orchestration; lacks durable state persistence for long-running workflows

---

## Links

- Official site: [https://temporal.io](https://temporal.io)
- GitHub: [https://github.com/temporalio/temporal](https://github.com/temporalio/temporal)
- Documentation: [https://docs.temporal.io](https://docs.temporal.io)
- Temporal Cloud: [https://cloud.temporal.io](https://cloud.temporal.io)
- Community / Slack: [Temporal Slack](https://temporal.io/slack)
- Community Forum: [https://community.temporal.io](https://community.temporal.io)
- Replay Conference: [https://replay.temporal.io](https://replay.temporal.io)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| 2025 | Series D funding | $300M led by a16z; $5B valuation |
| 2025 | Serverless Workers announced | At Replay 2026; new deployment model |
| 2024 | Python SDK maturity | Python SDK reaches production parity with Go/Java |
| 2019 | Temporal founded | By creators of Uber Cadence |
| 2018 | Cadence at Uber | Original open-source workflow engine |

---

## Deep Analysis

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

Temporal is a durable execution platform (Temporal Technologies, Seattle, founded 2019 by Uber Cadence creators) that automatically persists the complete running state of every workflow. If a process crashes, a server restarts, or a network flakes, the workflow resumes exactly where it left off without manual recovery code. It powers 1,500+ paying customers including Nvidia, Netflix, Snap, and Stripe, with a $5B valuation after a $300M Series D in 2025 led by a16z.

### 2. Gotchas of Using This Tool

Temporal has a steep learning curve — the mental model of durable execution, activities, workflows, workers, and signals is fundamentally different from traditional request-response architectures. The platform requires running a Temporal server cluster for production, which adds infrastructure complexity. Development requires understanding event sourcing concepts. Debugging workflow replay and non-deterministic errors can be challenging for teams new to the paradigm. The polyglot SDKs have varying maturity levels.

### 3. Limitations

Temporal is a general-purpose durable execution platform, not an AI-specific tool — it requires custom integration with LLM providers and agent frameworks. The Go and Java SDKs are most mature; Python and TypeScript are rapidly catching up. The platform does not provide native LLM observability or prompt management. Self-hosting Temporal Server requires significant infrastructure (database, persistence backend). The learning curve may be excessive for simple use cases that don't require durability guarantees.

### 4. How Secure Is This Tool?

Temporal is open-source (MIT license) with code on GitHub for independent review. The platform supports mTLS for server-to-server and client-to-server communication. Temporal Cloud is SOC 2 Type II compliant and offers data residency options. No major CVEs have been reported for the core platform. Teams self-hosting should secure the database backend (PostgreSQL/MySQL/Cassandra), enable mTLS, and restrict access to the Temporal Web UI. The $5B valuation and enterprise customer base validate production security.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 2/10.** Temporal is an infrastructure platform requiring deep engineering expertise in distributed systems. Non-technical users cannot interact with it; it requires experienced engineering teams.

### 6. What Does This Tool Solve That Others Don't?

Temporal's unique strength is its battle-tested durable execution model — the ability to run workflows for hours or days that automatically survive failures, restarts, and network issues. For AI agent workloads, this means agent loops can run reliably with automatic retry of individual LLM calls, state persistence across restarts, and signal-based human-in-the-loop interaction. The 1,500+ paying customers including Netflix, Snap, and Stripe provide unmatched production validation. No other tool in the LLMOps space provides this level of execution reliability.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Temporal | Durable execution | Reliability at scale |
| 2 | LangGraph | Graph orchestration | State persistence |
| 3 | CrewAI | Multi-agent | Production + enterprise |
| 4 | n8n | Workflow automation | Open-source + AI |
| 5 | ZenML | ML pipelines | Pipeline orchestration |

### 8. How Can This Tool Be Improved? How Active Is Development?

Temporal is actively developed by Temporal Technologies with frequent releases. Key improvements for AI use cases include adding LLM-specific activity templates, improving Python SDK maturity, providing AI agent workflow examples, adding native LLM observability hooks, and simplifying the developer experience for teams new to durable execution. More documentation for AI/LLM use cases would help adoption.

### 9. Official Maintainer Contacts

Temporal is maintained by Temporal Technologies Inc. GitHub: https://github.com/temporalio/temporal. Website: https://temporal.io. Documentation: https://docs.temporal.io. Temporal Cloud: https://cloud.temporal.io. Community: Slack, GitHub discussions.

### 10. General Usage Guidance

Use Temporal if your AI agent workflows require durable execution — surviving crashes, running for hours/days, and automatically retrying failures. It is the most reliable execution platform for long-running agent systems. For simpler agent orchestration, evaluate LangGraph or CrewAI. Start with `temporal server start-dev` for local development. For production, use Temporal Cloud or self-host with a managed database. Pair with Langfuse for LLM-specific observability.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
