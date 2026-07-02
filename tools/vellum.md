# Vellum

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Enterprise Orchestration
- **License**: Proprietary
- **Region**: N/A
- **Tier**: A
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> McKinsey, Coframe; experimentation, evaluation, deployment; A/B testing; SOC 2; 99.998% uptime

---

## Overview

Vellum is an enterprise-grade LLMOps platform that enables companies to build, deploy, and monitor production-ready AI applications through unified workflow automation, prompt engineering, and evaluation infrastructure. Founded roughly 2021–2022 and backed by Y Combinator, Vellum closed a $20 million Series A in July 2025 led by Leaders Fund, bringing total funding to approximately $29.5 million. Named customers include McKinsey and Coframe, and the platform advertises 99.998% uptime.

Vellum's platform covers the full AI development lifecycle: prompt engineering with version control, visual workflow orchestration, document retrieval (RAG), quantitative evaluation, and A/B testing. It is designed for both technical engineers and non-technical team members (product managers, domain experts) to collaborate on AI systems. Vellum serves as a fast proxy to LLM providers, allowing version-controlled prompt modifications without code changes, while gathering model inputs, outputs, and user feedback to build testing datasets. The platform is entirely proprietary and cloud-hosted, with an Enterprise tier offering VPC installation and on-premises deployment options.

Vellum is rated 4.8 out of 5 on Capterra, with users praising its visual workflow builder, deployment speed, and support quality. The most common criticism is a learning curve for advanced features and pricing that jumps steeply from free to paid tiers.

---

## Setup Experience

| Step | Metric | Value | Notes |
|------|--------|-------|-------|
| Time to first result | `git clone` to working | N/A | Cloud SaaS only; no local installation path for non-Enterprise tiers |
| Dependency count | Direct + transitive | N/A | Managed service; operators do not see dependencies |
| Docker required? | Yes / No | No | Enterprise tier offers VPC install; no Docker-based self-hosting for Free/Pro |
| Language runtime | Required version | N/A | Cloud platform; SDK clients available in Python and TypeScript |
| Auth complexity | API key / OAuth / None | API key + SSO (Enterprise) | Standard SaaS signup; Enterprise adds SAML/SSO |
| First-run failure rate | Smoke gate pass/fail | ⏳ TBD | Web-based onboarding; no local smoke gate applicable |

### Setup commands (expected)
```bash
# No local installation for Free/Pro tiers.
# Sign up at https://vellum.ai and obtain an API key.
# Install the Python SDK:
pip install vellum-ai
# Or the TypeScript SDK:
npm install @vellum-ai/vellum-client
```

### Known sharp edges
- **Steep pricing jump:** The transition from Free ($0) to Pro ($500/month) is abrupt. Free and Pro are both capped at 5 users; teams with 6+ users must negotiate Enterprise pricing.
- **Usage hard limits:** There is no pay-as-you-go overage for daily executions. Hitting the daily prompt or workflow limit means waiting until the next day or upgrading.
- **Learning curve:** Users on Capterra and TrustRadius consistently report that mastering advanced features (bulk execution, complex evaluation logic) requires patience and training.
- **Model costs separate:** Vellum does not mark up LLM API calls, but you must budget for provider costs (OpenAI, Anthropic, etc.) on top of platform fees.
- **Not a general automation tool:** Vellum is purpose-built for LLM orchestration; it does not replace general workflow automation tools like n8n or Zapier for CRM, email, or ERP integrations.

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

> Raw results JSON: `benchmarks/llmops-platforms-vellum-<date>.json`

---

## Bug Notes

### Smoke gate findings
- Not yet tested (cloud-only platform, no local smoke gate applicable)

### Known issues (from community / docs)
- Steep free-to-paid pricing cliff: The jump from Free ($0) to Pro ($500/month) is abrupt. Both tiers cap at 5 users, so teams with 6 members must immediately negotiate Enterprise pricing. This is a frequent complaint on Capterra and TrustRadius.
- Learning curve for advanced features: Users consistently report that mastering bulk execution, evaluation logic, and complex workflow branching requires patience. The platform's depth creates friction for teams expecting a simple prompt-management tool.
- Usage hard limits without overage: Unlike consumption-based platforms, Vellum stops execution when daily limits are hit. This creates production risk for apps with variable traffic.
- Pricing opacity: Vellum does not list pricing on its public website. Accurate pricing is only visible inside a Vellum account, which complicates budget planning and procurement.
- Limited general automation: Vellum is narrowly focused on LLM orchestration. Teams needing CRM, email, ERP, or general business-process automation must integrate separate tools (e.g., n8n, Zapier).
- Model costs are separate: Vellum does not mark up LLM API calls, but this also means total cost of ownership is unpredictable when using expensive models (e.g., GPT-4-turbo, Claude 3 Opus).

### Workarounds documented
- Budget for Enterprise negotiation early if team size exceeds 5 users.
- Use Vellum's evaluation and bulk-execution features during the Free tier to validate ROI before committing to Pro.
- Architect integrations with general automation tools (n8n, Make) for non-LLM business logic.

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
- **Free (Startup):** $0 — 50 prompt executions/day, 25 workflow executions/day, up to 5 users, 10K pages RAG indexing, 180 min max workflow runtime. No RBAC, no VPC, no SSO.
- **Pro:** $500/month — 5,000 prompt executions/day, 250 workflow executions/day, up to 5 users, RBAC, external monitoring integrations (Datadog, webhooks), enterprise-grade support. **Note:** user cap remains at 5.
- **Enterprise:** Custom pricing — unlimited/custom usage, unlimited users, VPC install, on-premises deployment, SSO, BAA/DPA, custom SLAs, HIPAA compliance via BAA.
- **Alternative docs pricing (Vellum.ai/docs/pricing):** Base free with pay-as-you-go credits; Pro from $50/mo plus machine-size and storage add-ons. **Discrepancy warning:** third-party pricing cards and official docs may differ; verify current terms with Vellum sales directly.

### Cost at scale
| Scale | Estimated Cost | Notes |
|-------|---------------|-------|
| Small (1-5 users) | $0–$500/mo | Free or Pro tier (5-user hard ceiling) |
| Medium (6-25 users) | $2,000–$10,000/mo | Enterprise negotiation required for 6+ users |
| Large (100+ users) | $10,000–$50,000+/mo | Enterprise with VPC, custom SLAs, dedicated support |
| Enterprise | Custom | Annual contract, typically tens of thousands per year |

### Hidden costs
- **LLM provider costs:** Vellum passes through model costs at cost; OpenAI/Anthropic/Google bills are separate and can exceed platform fees.
- **VPC infrastructure:** Enterprise VPC install requires customer's own cloud infrastructure (AWS/GCP/Azure) and DevOps time.
- **Training/onboarding:** Reviewers note a learning curve for advanced features; budget for internal training or professional services.
- **Storage overages:** RAG and document indexing may require additional storage tiers beyond the base plan.

---

## Data Sovereignty

| Property | Status | Notes |
|----------|--------|-------|
| Self-hostable | Partial | Enterprise tier offers VPC install and on-premises deployment; Free/Pro are cloud-only |
| Open source | No | Proprietary platform; no source code available |
| Audit trail | Yes | Detailed audit logs included in Enterprise tier |
| Data residency controls | Partial | Enterprise VPC keeps data within customer cloud perimeter; standard tiers use Vellum-managed infrastructure |
| On-premise deployment | Partial | Enterprise only; requires custom negotiation |
| Export format | JSON / API | Prompts, workflows, and datasets exportable via API |

---

## Security & Compliance

| Standard | Status | Notes |
|----------|--------|-------|
| SOC 2 | Yes | Enterprise tier includes SOC 2 attestation |
| GDPR | Yes | Enterprise includes DPA; platform is designed for EU data protection requirements |
| HIPAA | Yes (Enterprise) | HIPAA compliance via BAA available on Enterprise tier only |
| ISO 27001 | ⏳ TBD | Not publicly attested |
| EU AI Act | ⏳ TBD | Compliance posture not documented |
| FedRAMP | No | Not listed |

---

## Related Tools

### Tier A peers in same category
- [Dify](dify.md)
- [Flowise](flowise.md)
- [n8n](n8n.md)
- [PromptLayer](promptlayer.md)
- [Pezzo](pezzo.md)
- [Braintrust](braintrust.md)
- [Zapier](zapier.md)
- [Make](make.md)

### Complementary tools
- **Datadog** — External monitoring integration available on Pro/Enterprise tiers
- **OpenAI / Anthropic / Google** — LLM providers; Vellum acts as a proxy and evaluation layer
- **n8n** — General workflow automation; pair with Vellum when you need non-LLM business logic (CRM, email, database operations)

### Alternatives to consider
- **HumanLoop (now Anthropic)** — Enterprise prompt management and evaluation; choose if you are already in the Anthropic ecosystem
- **Dify** — Open-source alternative with self-hosting; choose if budget constraints or data residency requirements make $500/mo Pro tier unaffordable
- **PromptLayer** — Lighter-weight prompt management; choose if you only need prompt versioning and observability, not full workflow orchestration
- **LangSmith** — Deep LangChain integration; choose if your entire stack is built on LangChain and you need native tracing

---

## Links

- Official site: [https://vellum.ai](https://vellum.ai)
- Documentation: [https://docs.vellum.ai](https://docs.vellum.ai)
- Pricing docs: [https://www.vellum.ai/docs/pricing](https://www.vellum.ai/docs/pricing)
- GitHub: ⏳ (no public core repository; proprietary platform)
- Community / Discord: ⏳ (no public community Discord found)
- Capterra reviews: [https://www.capterra.com/p/232074/Vellum-AI/](https://www.capterra.com/p/232074/Vellum-AI/)
- Benchmark adapter: ⏳ (link to harness repo when available)

---

## Changelog

| Date | Event | Notes |
|------|-------|-------|
| 2026-06-16 | First triaged | Added to roster, deep-dive template created |
| | | |

---

## Deep Analysis

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

Vellum is a comprehensive LLM application development platform that provides prompt engineering, workflow building, semantic search (RAG), model evaluation, and deployment in a single product. It targets product teams that want to build, test, and deploy LLM features without deep engineering investment. The platform's workflow builder enables complex multi-step AI pipelines, and the free tier (50 prompt executions/day, 25 workflow executions/day) makes it accessible for prototyping.

### 2. Gotchas of Using This Tool

Vellum is a proprietary platform with no public open-source repository and no self-hosting option. The free tier has strict limits (no RBAC, no VPC, no SSO) that push teams toward paid plans quickly. The workflow builder, while visual, can become complex for multi-step pipelines and debugging visual workflows is harder than debugging code. Pricing scales with execution volume, which can be unpredictable for high-traffic applications. The platform's model provider coverage may not include all specialized models.

### 3. Limitations

Vellum lacks the observability depth of Langfuse or LangSmith (deep tracing, cost analytics). The evaluation framework is focused on Vellum's workflow model rather than framework-agnostic evaluation. Agent tracing and multi-agent monitoring are limited. The platform does not provide a public API for programmatic workflow management beyond the SDK. Advanced features (VPC, SSO, RBAC) are enterprise-only. The community is smaller than open-source alternatives.

### 4. How Secure Is This Tool?

Vellum operates as a cloud-hosted SaaS platform. The platform offers VPC deployment and SSO on enterprise plans. Specific compliance certifications (SOC 2, ISO 27001, HIPAA) should be verified with the vendor. Data is encrypted at rest and in transit. No public CVEs are documented. Teams in regulated industries should evaluate enterprise features and review data processing agreements. The proprietary nature limits independent security auditing.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 6/10.** Vellum's visual workflow builder and prompt engineering tools make LLM application development accessible to semi-technical product teams. Non-technical users can prototype simple features, though complex workflows require engineering support.

### 6. What Does This Tool Solve That Others Don't?

Vellum's unique strength is providing a comprehensive product suite — prompt engineering, workflow building, RAG, evaluation, and deployment — in a single platform designed for product teams rather than just engineers. The workflow builder for multi-step AI pipelines with conditional logic and branching is more capable than simple prompt management tools. The model-agnostic approach with evaluation tools helps teams choose optimal models.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Langfuse | Open-source observability | Self-hostable |
| 2 | LangSmith | Full LLMOps | Ecosystem depth |
| 3 | Braintrust | Evaluation | Eval workflows |
| 4 | Vellum | Prompt + workflow builder | Product team focus |
| 5 | Humanloop | Collaborative prompts | Human evaluation |

### 8. How Can This Tool Be Improved? How Active Is Development?

Vellum is actively developed with regular feature updates. Key improvements include adding self-hosting options, expanding the free tier, deepening observability features, adding agent tracing, improving documentation, expanding model provider coverage, and providing more transparent pricing. More integrations with popular frameworks would reduce integration friction.

### 9. Official Maintainer Contacts

Vellum is maintained by Vellum AI Inc. Website: https://vellum.ai. Documentation: https://docs.vellum.ai. Pricing: https://www.vellum.ai/docs/pricing. No public GitHub repository (proprietary).

### 10. General Usage Guidance

Use Vellum if you are a product team that wants to build, test, and deploy LLM features with a visual workflow builder. The free tier is good for prototyping. For open-source self-hosting, evaluate Langfuse. For deeper evaluation workflows, evaluate Braintrust. For code-first development, evaluate LangChain. Evaluate the enterprise plan for VPC, SSO, and compliance features.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
