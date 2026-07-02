# Langdock

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: LLMOps Platform
- **License**: Proprietary
- **Region**: N/A
- **Tier**: B
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> Europe; enterprise LLM platform; compliance-focused; EU AI Act ready

---

## Overview

Europe; enterprise LLM platform; compliance-focused; EU AI Act ready

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

> Raw results JSON: `benchmarks/llmops-platforms-langdock-<date>.json`

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

LangDock is a platform for building, deploying, and managing internal AI assistants and chatbots for enterprise use cases. It provides a visual interface for creating conversational AI tools that can access company knowledge bases, integrate with internal systems, and enforce access controls. The platform is useful for organizations that want to deploy AI assistants to employees without exposing sensitive internal data to public AI services.

### 2. Gotchas of Using This Tool

LangDock is a proprietary platform with limited public documentation and no open-source option. The platform's integration ecosystem is narrow compared to more established alternatives. Pricing is not transparent. The smaller community means fewer community-contributed templates and integration patterns. Evaluation and observability features are not well-documented.

### 3. Limitations

LangDock's capabilities for complex multi-agent orchestration are limited compared to dedicated frameworks. The platform's model provider support is not well-documented. Self-hosting is not available, which may be a blocker for regulated industries. Integration with existing CI/CD and observability stacks requires custom work. The platform's scalability under high concurrent load is not documented.

### 4. How Secure Is This Tool?

LangDock operates as a cloud-hosted SaaS platform targeting enterprise use cases. Specific compliance certifications (SOC 2, ISO 27001) are not prominently documented in public materials. The closed-source nature limits independent security auditing. Teams should request security documentation and review data processing practices before deploying with sensitive internal data. No public CVEs are associated.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 4/10.** LangDock aims at enterprise internal use with a visual interface, making it somewhat accessible to semi-technical users. Non-technical users would need support for initial setup and integration.

### 6. What Does This Tool Solve That Others Don't?

LangDock differentiates by focusing specifically on internal enterprise AI assistants with access control and knowledge base integration. The platform's emphasis on secure, internal deployment addresses organizations' concerns about sensitive data exposure to public AI services. The visual builder for internal assistants is tailored to enterprise IT and operations teams.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Dify | LLM app builder | Open-source |
| 2 | Botpress | Enterprise chatbots | NLU + LLM |
| 3 | Voiceflow | Conversational design | Visual + LLM |
| 4 | LangDock | Internal AI assistants | Enterprise security |
| 5 | Coze | No-code bot builder | Free tier |

### 8. How Can This Tool Be Improved? How Active Is Development?

LangDock's development activity is difficult to assess without public repositories. Key improvements include publishing compliance certifications, expanding documentation, adding self-hosting, expanding integrations, and providing transparent pricing. A free trial and community edition would help teams evaluate the platform.

### 9. Official Maintainer Contacts

LangDock is maintained by the LangDock team. No public GitHub repository or community channel is documented. The primary contact is through the official LangDock website.

### 10. General Usage Guidance

Consider LangDock if you need a platform for internal enterprise AI assistants with access control. Evaluate Dify (open-source, self-hostable) and Botpress (SOC 2 compliant) as alternatives. Request security documentation and a trial before committing. The platform is best suited for organizations that prioritize internal deployment over external customer-facing applications.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
