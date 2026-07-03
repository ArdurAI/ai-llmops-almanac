# Coze


[![Agent Frameworks](https://img.shields.io/badge/Also_in-Agent_Frameworks-blue)](https://github.com/ArdurAI/ai-agent-framework-almanac) [![Infrastructure](https://img.shields.io/badge/Also_in-Infrastructure-blue)](https://github.com/ArdurAI/ai-infrastructure-almanac)

- **Category**: LLMOps Platforms & Workflow Automation
- **Type**: No-code
- **License**: Proprietary
- **Region**: N/A
- **Tier**: B
- **First Triaged**: 2026-06-16
- **Last Updated**: 2026-06-16

> ByteDance; 100K+ bots; zero-code Bot builder; Doubao model; multi-channel publish

---

## Overview

ByteDance; 100K+ bots; zero-code Bot builder; Doubao model; multi-channel publish

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

> Raw results JSON: `benchmarks/llmops-platforms-coze-<date>.json`

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

Coze is ByteDance's no-code AI bot builder that enables users to create, deploy, and monetize AI chatbots and agents across multiple platforms without coding. It provides a visual interface for building conversational agents with plugin support, knowledge bases, workflow orchestration, and multi-channel deployment (Discord, Telegram, Slack, web). The platform is particularly popular in the Asian market and offers a generous free tier.

### 2. Gotchas of Using This Tool

Coze is a proprietary platform by ByteDance, raising data privacy concerns especially for users outside China who may be uncomfortable with ByteDance's data practices. The platform's availability and feature parity vary significantly between the Chinese (coze.cn) and international (coze.com) versions. API rate limits and model availability differ by region. The platform's terms of service regarding bot ownership and monetization are complex.

### 3. Limitations

Coze's international version has fewer features and model options compared to the Chinese version. The platform does not provide self-hosting, code-level access, or an open-source option. Advanced customization is limited to what the visual builder and plugin system expose. Integration with enterprise systems (SSO, audit logging, RBAC) is not available on lower tiers. The platform's LLM provider is primarily ByteDance's models with limited support for external providers.

### 4. How Secure Is This Tool?

Coze is operated by ByteDance, which means data is processed under ByteDance's privacy policies and jurisdictional requirements. The platform does not prominently document SOC 2, ISO 27001, or HIPAA compliance for the international version. Teams in regulated industries or government sectors should carefully evaluate data residency and privacy implications. No public CVEs are associated with the platform, but the closed-source nature limits independent security review.

### 5. Usefulness to General Public and Non-Technical Users

**Rating: 8/10.** Coze is one of the most accessible no-code AI bot builders — non-technical users can create functional bots in minutes through the visual interface. The learning curve is minimal for basic bot creation.

### 6. What Does This Tool Solve That Others Don't?

Coze uniquely combines no-code bot building with a plugin marketplace and multi-channel deployment in a single free platform, backed by ByteDance's infrastructure. Its deep integration with ByteDance's LLM ecosystem (Doubao models) provides cost-effective inference. The platform's monetization features for bot creators differentiate it from purely enterprise-focused alternatives.

### 7. How Does This Tool Rank Compared to Others?

| Rank | Tool | Focus | Strength |
|------|------|-------|----------|
| 1 | Dify | LLM app builder | Open-source |
| 2 | Coze | No-code bot builder | Free + multi-channel |
| 3 | Voiceflow | Conversational design | Visual + LLM |
| 4 | Botpress | Enterprise chatbots | NLU + LLM hybrid |
| 5 | Flowise | Visual LLM flows | LangChain-native |

### 8. How Can This Tool Be Improved? How Active Is Development?

Coze is actively developed by ByteDance with frequent feature updates. Key improvements include feature parity between international and Chinese versions, transparent data privacy policies, expanded external LLM provider support, enterprise features (SSO, audit logging), and an open API for deeper integration. Clear documentation on bot ownership and data handling would build trust.

### 9. Official Maintainer Contacts

Coze is maintained by ByteDance. Website: https://www.coze.com (international) and https://www.coze.cn (China). Documentation is available on the platform. No public GitHub repository or community Discord is documented for the international version.

### 10. General Usage Guidance

Use Coze if you need to quickly build and deploy AI chatbots without coding, especially in the consumer or SMB space. Carefully evaluate data privacy implications if operating outside China. For enterprise use, evaluate Dify (open-source, self-hostable) or Botpress (SOC 2 compliant) instead. The free tier is excellent for prototyping and small-scale deployment.

## License

Content for this page is licensed CC BY 4.0 — share and adapt with attribution to **ArdurAI / LLMOps Platforms & Workflow Automation Almanac**.
