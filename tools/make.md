# Make

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Workflow Automation
- **License**: Proprietary
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> 1,000+ integrations (3,000+ apps); visual canvas builder; filters, routers, iterators; error handling; AI agents; credit-based pricing; SOC 2 Type II, SOC 3, GDPR; founded 2012 as Integromat, rebranded 2022

---

## Overview

Make (formerly Integromat) is a visual automation platform founded in 2012 in Prague and rebranded to Make in 2022 after acquisition by Celonis. It connects over 3,000 apps through a visual scenario builder where users drag and drop modules onto a canvas, connecting them with arrows to represent data flow. Unlike Zapier's linear step model, Make uses a graph-based visual interface that naturally handles branching, iteration, routers, filters, and error handling — making it well-suited for complex, multi-path workflows that would become unwieldy in a linear builder. The platform supports JavaScript and Python via the Make Code app for custom transformations, and added native AI agents and AI toolkit integrations (OpenAI, Anthropic, Google AI) in 2025.

Make's credit-based billing model charges one credit per module execution (trigger, action, filter, router, or data transformation). This means costs scale transparently with workflow complexity — a 10-step scenario running 100 times consumes 1,000 credits. The model is predictable for simple workflows but can escalate unexpectedly when scenarios include many conditional branches or frequent polling triggers. Some actions cost more than one credit: Make Code uses 2 credits per second of execution, and AI-related actions can consume additional credits. Make offers a genuine free tier with 1,000 credits/month and 2 active scenarios (no time limit), making it one of the more accessible starting points for automation experimentation.

Make's enterprise tier adds SSO (Azure AD, Okta, Google Workspace), advanced security, 24/7 support, and an on-prem agent for local/SAP connectivity. However, Make has no fully self-hosted deployment option — it is cloud-only. This makes it unsuitable for organizations with strict data residency requirements or HIPAA-regulated workflows. The visual canvas, while powerful, has a steeper learning curve than Zapier's linear builder; Make's own support team has suggested roughly 19 hours of Make Academy training before building production workflows. Teams that need complex visual logic, are comfortable with a learning curve, and do not require self-hosting typically find Make a better value than Zapier at moderate-to-high volumes.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | Sign-up to first scenario | ~10-20 minutes | Web-based visual builder; no install for cloud |
| Dependency count | N/A | 0 | Cloud-native; optional Make CLI for deployment |
| Docker required? | Yes / No | No | Fully managed SaaS; no self-hosted option |
| Language runtime | Required version | N/A | Optional JS/Python via Make Code app module |
| Auth complexity | API key / OAuth / None | OAuth / API key | Per-app connection credentials; OAuth for most SaaS |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | |

### Setup commands (expected)
```bash
# No local installation required; sign up at make.com
# Optional: Make CLI for organization management
npm install -g @make/cli
make login
```

### Known sharp edges
- **No self-hosted option**: Make is cloud-only; data processed through Make's AWS infrastructure (US or EU Dublin), with no on-prem or air-gapped deployment
- **Credit model surprises**: every module execution costs a credit, including triggers, filters, routers, and error paths; complex scenarios burn credits faster than expected
- **HIPAA non-compliant**: Make does not sign BAAs and does not support PHI processing in its cloud environment
- **Steeper learning curve**: the visual canvas is powerful but requires understanding of data types, iterators, aggregators, and routers; Make Academy training recommended (~19 hours)
- **Limited error recovery**: resuming failed scenario runs often requires manual intervention; auto-retry capabilities are less robust than enterprise iPaaS tools
- **RBAC limitations**: role-based access applies mainly to scenario builders/authors; no native end-user role differentiation within automation execution contexts
- **Data isolation**: managed via separate team workspaces and credential scopes, not enforced at the tenant level natively

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

> Raw results JSON: `benchmarks/llmops-platforms-make-<date>.json`

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
- **Free:** $0/month — 1,000 credits/month, 2 active scenarios, 15-minute minimum interval, routers & filters, 3,000+ apps, visual builder, forum support; no time limit
- **Core:** $9–$12/month (annual) — 10,000 credits/month, Make API access, 1-minute interval, unlimited active scenarios, increased data transfer
- **Pro:** $16–$21/month (annual) — 10,000 credits/month, full-text execution log search, custom variables, priority scenario execution
- **Teams:** $29–$38/month (annual) — 10,000 credits/month, scenario templates, team roles, shared workspaces, collaboration features
- **Enterprise:** Custom pricing — custom credits, advanced security (SSO, 2FA enforcement, domain claim), 24/7 enterprise support, Value Engineering team, enterprise app integrations, custom functions, on-prem agent for local/SAP connectivity, overage protection

- **Credit packs**: scalable from 20k up to 8M+ credits/month; annual billing saves ~15%+
- **Unused credits**: monthly credits do not roll over; some yearly prepaid plans offer 12-month validity
- **AI agent costs**: workflows with AI agents can consume 43–50+ credits per execution (Small model), significantly more than classic workflows

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
| Self-hostable | No | Cloud-only SaaS; no self-hosted or on-prem deployment option |
| Open source | No | Proprietary; owned by Celonis since 2020 acquisition |
| Audit trail | Yes | Execution logs, user actions, scenario changes logged; configurable retention on Enterprise |
| Data residency controls | Partial | EU data center (Dublin) available; no full data residency or region-locking controls beyond hosting region choice |
| On-premise deployment | No | Enterprise on-prem agent connects to local/SAP systems but core engine remains cloud-hosted |
| Export format | JSON, CSV | Scenario blueprints exportable as JSON; execution data exportable as CSV |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Type II and SOC 3 certified; annual audits; hosted on AWS EC2 private instances |
| GDPR | Yes | Compliant; DPA available; EU data center in Dublin |
| HIPAA | No | Not HIPAA-compliant; does not sign BAAs; PHI should not flow through Make |
| ISO 27001 | Yes | Certified (as of post-2020 acquisition by Celonis) |
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
- [Zapier](zapier.md) — broader app coverage for simple linear workflows; good to run alongside Make for long-tail integrations
- [n8n](n8n.md) — self-hosted alternative when Make's cloud-only model violates data sovereignty requirements
- [Braintrust](braintrust.md) — evaluation and observability for AI agent steps within Make scenarios
- [Gumloop](gumloop.md) — AI-native automation when Make's bolt-on AI modules are insufficient

### Alternatives to consider
- [Zapier](zapier.md) when the team is non-technical and needs the simplest possible setup with the broadest app coverage
- [n8n](n8n.md) when self-hosting, data residency, or open-source flexibility is required
- [Gumloop](gumloop.md) when AI-native workflows with model-agnostic routing and agentic reasoning are needed
- Workato or MuleSoft when enterprise governance, HIPAA compliance, or advanced audit requirements are mandatory

---

## Links

- Official site: [https://www.make.com](https://www.make.com)
- GitHub: [https://github.com/integromat](https://github.com/integromat)
- Documentation: [https://www.make.com/en/help](https://www.make.com/en/help)
- Community / Forum: [https://www.make.com/en/community](https://www.make.com/en/community)
- Security & Compliance: [https://www.make.com/en/security](https://www.make.com/en/security)
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
