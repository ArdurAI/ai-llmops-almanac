# BISHENG

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: Enterprise Platform
- **License**: Open Source
- **Region**: N/A
- **Tier**: B
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> China; 'Proudly made by Chinese'; Fortune 500 deployments; open-source alternative to Dify

---

## Overview

China; 'Proudly made by Chinese'; Fortune 500 deployments; open-source alternative to Dify

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

> Raw results JSON: `benchmarks/llmops-platforms-bisheng-<date>.json`

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

> **Authored by Team Ardur** — Researched and compiled as part of the ArdurAI LLMOps Platforms & Workflow Automation Almanac. Licensed under CC BY 4.0.

### 1. How Is This Tool Useful?

Bisheng is an open-source enterprise-grade LLM application development platform designed for building production-ready AI agents, RAG systems, and document processing workflows. It emphasizes visual workflow building with a drag-and-drop interface while providing the depth needed for enterprise deployment, including role-based access control, audit logging, and multi-tenant support. The platform is particularly strong in the Chinese enterprise market.

### 2. Gotchas of Using This Tool

Bisheng's documentation and community resources are predominantly in Chinese, creating a language barrier for English-speaking teams. The platform requires significant infrastructure (Docker, multiple containers) for deployment, and setup complexity is higher than Dify or Flowise. No public GitHub repository link is documented in the almanac, making it difficult to assess code quality and community activity independently.

### 3. Limitations

Bisheng's international community presence is limited compared to Dify or Flowise, meaning fewer English tutorials and community integrations. The platform's model provider integrations are skewed toward Chinese LLM providers (Zhipu, Qwen, Baichuan) with slower adoption of Western models. Advanced features like multi-agent orchestration are less mature than dedicated frameworks like CrewAI or LangGraph.

### 4. How Secure Is This Tool?

Bisheng is open-source under Apache 2.0, allowing independent security review if the repository is accessible. The platform supports enterprise security features including RBAC, audit logging, and on-premise deployment. However, no public SOC 2, ISO 27001, or compliance certifications are documented. Teams should verify the security posture of the specific deployment configuration and review container security settings.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 3/10.** While Bisheng offers a visual interface, the Chinese-language documentation and enterprise-focused features make it inaccessible to most non-technical users outside its target market.

### 6. What Does This Tool Solve That Others Don't?

Bisheng differentiates by combining enterprise governance features (RBAC, audit logging, multi-tenancy) with a visual workflow builder, targeting the Chinese enterprise market where data sovereignty and on-premise deployment are critical. Its deep integration with Chinese LLM providers and document processing pipelines for complex Chinese-language documents fills a niche underserved by Western platforms.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Dify | LLM app builder | Global ecosystem |
| 2 | Flowise | Visual LLM builder | LangChain-native |
| 3 | Langflow | Visual flows | IBM-backed |
| 4 | Bisheng | Enterprise (China) | RBAC + audit |
| 5 | FastGPT | RAG platform | Chinese market |

### 8. How Can This Tool Be Improved? How Active Is Development?

Development activity appears active based on the project's web presence, though without a publicly documented GitHub repository, commit frequency is hard to verify. Key improvements include English-language documentation, broader international model provider support, simplified deployment options, and a public community channel. Open-sourcing or linking the existing repository would build international trust.

### 9. Official Maintainer Contacts

Bisheng is maintained by the Bisheng team (China). No public GitHub repository, Discord, or community forum is documented in English-language sources. The primary contact channel is through the official Bisheng website.

### 10. General Usage Guidance

Consider Bisheng if you are building enterprise LLM applications in the Chinese market or need deep Chinese-language document processing. For international teams, evaluate Dify or Flowise first for their larger English-speaking communities and broader model provider support. Verify the repository's accessibility and activity before committing to the platform.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
