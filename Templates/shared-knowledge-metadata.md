# Shared-Knowledge Asset Metadata Template

Use this template to provide metadata for assets in the Shared-Knowledge folder.

Copy this template to the top of your asset's README.md or create a separate `metadata.md` file.

---

## Asset Metadata

**Title**: [Clear, descriptive title]

**Author/Contributor**: [Name or team]

**Created**: [YYYY-MM-DD]

**Last Updated**: [YYYY-MM-DD]

**Applicable Domains**: [Select all that apply]
- [ ] AI
- [ ] Fabric
- [ ] GitHub
- [ ] Copilot
- [ ] All / Cross-domain

**Lifecycle Status**: [Select one]
- [ ] Experimental - Under active development, may change frequently
- [ ] Stable - Production-ready, tested, and documented
- [ ] Deprecated - No longer recommended, consider alternatives
- [ ] Archive - No longer maintained

**Category**: [Select the Shared-Knowledge subfolder]
- [ ] Learning-Day
- [ ] Community-Contributions
- [ ] Useful-Tools
- [ ] Emerging-Technologies
- [ ] Tips-and-Tricks
- [ ] Reference-Architectures

**Tags**: [Comma-separated keywords for discoverability]

Example: `azure, automation, cost-optimization, troubleshooting`

---

## Asset Description

**Purpose**: [What problem does this solve? What value does it provide?]

**Prerequisites**: [What's needed to use this asset?]

- Tool/SDK requirements
- Access permissions
- Environment setup
- Knowledge prerequisites

**Quick Start**: [Brief instructions to get started]

1. [First step]
2. [Second step]
3. [Third step]

**Expected Outcome**: [What success looks like]

**Known Limitations**: [Any constraints, edge cases, or known issues]

**Migration Considerations**: [If applicable, conditions for moving this to a domain folder]

**Related Resources**: [Links to documentation, related assets, or dependencies]

---

## Template Usage Notes

### When to Use This Template

- Adding new content to any Shared-Knowledge subfolder
- Updating existing Shared-Knowledge assets
- Migrating content from domain folders to Shared-Knowledge

### Optional vs Required Fields

**Required**:
- Title
- Last Updated
- Applicable Domains
- Lifecycle Status
- Category
- Purpose
- Quick Start

**Recommended**:
- Author/Contributor (for follow-up questions)
- Tags (for discoverability)
- Prerequisites (for reproducibility)
- Expected Outcome (for validation)

**Optional**:
- Known Limitations
- Migration Considerations
- Related Resources

### Maintenance

- Update "Last Updated" whenever content changes
- Review "Lifecycle Status" regularly (at least every 90 days for Experimental)
- Update "Migration Considerations" when domain fit becomes clear
- Mark as "Deprecated" before archiving to give users notice

### Examples

#### Example 1: Cross-Domain Tool

```markdown
**Title**: Multi-Domain Cost Analysis Script

**Author/Contributor**: Cost Optimization Team

**Created**: 2026-01-15

**Last Updated**: 2026-07-18

**Applicable Domains**: All / Cross-domain

**Lifecycle Status**: Stable

**Category**: Useful-Tools

**Tags**: azure, cost-optimization, reporting, automation

**Purpose**: Generate cost reports across AI, Fabric, and other Azure services with breakdown by domain and resource type.
```

#### Example 2: Learning Day Content

```markdown
**Title**: Learning Day: RAG Implementation with AI Search

**Author/Contributor**: Learning Day Q2 2026

**Created**: 2026-04-15

**Last Updated**: 2026-04-15

**Applicable Domains**: AI

**Lifecycle Status**: Stable

**Category**: Learning-Day

**Tags**: azure-openai, ai-search, rag, demo

**Purpose**: Hands-on demo of Retrieval-Augmented Generation using Azure OpenAI and AI Search.

**Migration Considerations**: Consider moving to AI/Demos/ if widely reused beyond Learning Day context.
```

#### Example 3: Emerging Technology

```markdown
**Title**: Azure OpenAI GPT-5 Preview Evaluation

**Author/Contributor**: Early Adopters Team

**Created**: 2026-07-01

**Last Updated**: 2026-07-18

**Applicable Domains**: AI

**Lifecycle Status**: Experimental

**Category**: Emerging-Technologies

**Tags**: azure-openai, gpt-5, preview, evaluation

**Purpose**: Evaluate GPT-5 preview capabilities for training scenarios.

**Migration Considerations**: Move to AI/Demos/ once GPT-5 reaches GA and demo is finalized.
```
