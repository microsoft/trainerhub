<p align="center">
<img src="./images/trainerhub-banner2.png" alt="CAIP Knowledge" width="100%">
</p>

# CAIP-Knowledge

CAIP-Knowledge is a domain-based knowledge hub for trainer assets, organized by product area instead of content type.

## Purpose

- Improve discoverability and reuse through domain-based organization
- Manage courses, demos, scenarios, code, and best practices in one place
- Accelerate onboarding for new contributors

## Shared Mission for CAIP MTTs

CAIP-Knowledge is a shared CAIP Knowledge Repository for CAIP MTTs.

Its primary goal is to help MTTs contribute, discover, and reuse high-value assets across the team.

Our current priority is to collect and share useful assets quickly, then refine information architecture over time based on real usage and feedback.

## Structure Principles

- Domain-first: AI, Fabric, GitHub, Copilot
- Each domain uses the same subfolder template
- Course assets are organized by official course code under `Courses/`
- Cross-domain and experimental assets use `Shared-Knowledge/`
- Shared templates are centrally managed in root `Templates/`
- Structure is intentionally flexible and will evolve as new asset types and contribution patterns emerge.

## GitHub and SharePoint: Complementary Roles

GitHub and SharePoint serve different but complementary purposes:

### GitHub (Reusable, Structured Assets)

Use GitHub for versioned, reusable assets such as:

- demos
- skills
- agents
- markdown content
- code samples
- scripts
- templates
- best practices

### SharePoint (Broader Knowledge and Team Documentation)

Use SharePoint for broader documentation and knowledge-sharing such as:

- guides
- team documentation
- Learning Day content
- recordings
- general knowledge articles

In short: GitHub is the execution-ready asset library; SharePoint is the wider team knowledge hub.

## Repository Structure

```text
.
├─ AI/
│  ├─ Courses/
│  ├─ Demos/
│  ├─ Industry-Use-Cases/
│  ├─ Customer-Scenarios/
│  ├─ Skills/
│  ├─ Code/
│  └─ Best-Practices/
├─ Fabric/
│  ├─ Courses/
│  ├─ Demos/
│  ├─ Industry-Use-Cases/
│  ├─ Customer-Scenarios/
│  ├─ Skills/
│  ├─ Code/
│  └─ Best-Practices/
├─ GitHub/
│  ├─ Courses/
│  ├─ Demos/
│  ├─ Industry-Use-Cases/
│  ├─ Customer-Scenarios/
│  ├─ Skills/
│  ├─ Code/
│  └─ Best-Practices/
├─ Copilot/
│  ├─ Courses/
│  ├─ Demos/
│  ├─ Industry-Use-Cases/
│  ├─ Customer-Scenarios/
│  ├─ Skills/
│  ├─ Code/
│  └─ Best-Practices/
├─ Shared-Knowledge/
│  ├─ Learning-Day/
│  ├─ Community-Contributions/
│  ├─ Useful-Tools/
│  ├─ Emerging-Technologies/
│  ├─ Tips-and-Tricks/
│  └─ Reference-Architectures/
└─ Templates/
```

## Domain Folders

- [AI/](AI/)
- [Fabric/](Fabric/)
- [GitHub/](GitHub/)
- [Copilot/](Copilot/)

## Shared-Knowledge

[Shared-Knowledge/](Shared-Knowledge/) contains cross-domain assets and team contributions that don't fit into specific domain folders.

**Use Shared-Knowledge for:**

- Content spanning multiple domains
- Team Learning Day materials with executable components
- Cross-domain utilities and tools
- Emerging technologies and experimental content
- Quick troubleshooting tips and productivity hacks
- Multi-domain reference architectures

**Use domain folders for:**

- Content clearly tied to one domain
- Production-ready, domain-specific assets

See [Shared-Knowledge/README.md](Shared-Knowledge/README.md) for detailed guidance.

## Templates

- [Templates/](Templates/)

## Quick Contribution Guide

1. Choose the target domain first.
2. Select the appropriate category subfolder inside that domain.
3. Include reproducible steps and validation criteria for new content.
4. Update the domain README and templates together when needed.

## Contribution and Governance (Lightweight)

We keep governance lightweight to encourage contribution while maintaining quality:

- Contribution expectations: follow repository conventions and include reproducible guidance.
- Update process: submit changes through pull requests.
- Review and approval: at least one reviewer from the relevant domain should validate clarity and reusability.
- Access management: repository maintainers manage write/admin permissions and reviewer coverage.
- Operational guidance: see [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [WORKBOARD.md](WORKBOARD.md).

Detailed policies can be expanded as the repository matures.

## Notes

- This repository currently uses a domain-based structure to improve discoverability and reuse.
- The structure is expected to evolve based on community feedback, contribution patterns, and asset growth.
- For detailed operating guidance, refer to each domain `README.md` first.
