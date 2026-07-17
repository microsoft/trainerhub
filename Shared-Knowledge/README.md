# Shared-Knowledge

Cross-domain assets and team contributions that don't fit into specific domain folders.

## Purpose

Shared-Knowledge provides a home for valuable assets that:

- Span multiple domains (AI, Fabric, GitHub, Copilot)
- Are still being evaluated for domain assignment
- Support team-wide learning and collaboration
- Represent emerging technologies or experimental work

This structure complements the domain-first organization by handling edge cases and accelerating contribution velocity.

## When to Use Shared-Knowledge

**Use Shared-Knowledge when:**

- Content applies to multiple domains equally
- You're unsure which domain fits best (temporary staging)
- Content is experimental or for emerging technologies
- Asset is for team-wide learning events (Learning Day)
- Tool or utility helps across all domains

**Use domain folders when:**

- Content clearly serves one domain's scope
- Asset follows established domain patterns
- Material is production-ready and domain-specific

## Folder Structure

```text
Shared-Knowledge/
├─ Learning-Day/              # Learning Day materials (demos, code, guides)
├─ Community-Contributions/   # Team contributions awaiting domain assignment
├─ Useful-Tools/              # Cross-domain scripts and utilities
├─ Emerging-Technologies/     # Experimental and preview content
├─ Tips-and-Tricks/           # Quick wins and troubleshooting guides
└─ Reference-Architectures/   # Multi-domain architecture patterns
```

## Folder Descriptions

### [Learning-Day](Learning-Day/)

Materials from team Learning Day events including runnable demos, code samples, and practical guides.

**Best for**: Learning session assets with executable components

### [Community-Contributions](Community-Contributions/)

Team member contributions that span multiple domains or are awaiting domain assignment.

**Best for**: Quick contributions, experiments, cross-domain utilities

**Review cycle**: Every 90 days to determine migration or archive

### [Useful-Tools](Useful-Tools/)

Cross-domain scripts, utilities, and automation tools for trainer productivity.

**Best for**: Repository maintenance, training delivery helpers, multi-domain diagnostics

### [Emerging-Technologies](Emerging-Technologies/)

Experimental content for preview features and technologies not yet in main domains.

**Best for**: Preview evaluations, beta features, proof-of-concepts

**Review cycle**: Every 90 days to determine graduation or archive

### [Tips-and-Tricks](Tips-and-Tricks/)

Quick wins, shortcuts, and troubleshooting guides for cross-domain scenarios.

**Best for**: Concise, actionable solutions; productivity hacks; common pitfall fixes

### [Reference-Architectures](Reference-Architectures/)

Complete architecture patterns with diagrams and implementation code spanning multiple domains.

**Best for**: Multi-domain solutions, enterprise patterns, end-to-end implementations

**Requirement**: Must include both diagrams and working implementation code

## Contribution Guidelines

### General Rules

- Use English as the default language for new content
- Follow the same quality standards as domain folders
- Add metadata indicating applicable domains when practical
- Include clear README files with purpose and usage
- Keep assets reproducible in clean environments

### Migration Expectations

Content in Shared-Knowledge is not permanent. Regularly review for migration opportunities:

1. **Move to domain folder** - When content becomes domain-specific or stable
2. **Stay in Shared-Knowledge** - When truly cross-domain or still experimental
3. **Archive** - When no longer relevant or superseded

### Metadata

For assets in Shared-Knowledge, consider adding metadata:

- Title and purpose
- Author or contributor
- Applicable domains (AI, Fabric, GitHub, Copilot, or All)
- Lifecycle status (Experimental, Stable, Archive)
- Last updated date
- Tags for discoverability

Use the [metadata template](../Templates/shared-knowledge-metadata.md) when creating new assets.

## Relationship with Domain Folders

Shared-Knowledge complements domain folders but should not duplicate them:

| Content Type | Shared-Knowledge | Domain Folder |
| ------------- | ---------------- | ------------- |
| Single-domain demo | ❌ No | ✅ Yes |
| Multi-domain architecture | ✅ Yes | ❌ No |
| Domain-specific code | ❌ No | ✅ Yes |
| Cross-domain utility | ✅ Yes | ❌ No |
| Domain best practice | ❌ No | ✅ Yes |
| Experimental preview | ✅ Yes (temporarily) | ❌ No |
| Learning Day asset | ✅ Yes (initially) | ✅ Yes (after migration) |

## Relationship with SharePoint

**GitHub (Shared-Knowledge)** is for:

- Executable assets: demos, code, scripts
- Architecture implementations with IaC
- Reusable tools and utilities
- Version-controlled content

**SharePoint** is for:

- Presentation slides and recordings
- Broad knowledge articles
- Team documentation
- General guides without code

## Governance

### Review Cycles

- **Community-Contributions**: Review every 90 days
- **Emerging-Technologies**: Review every 90 days
- **Other folders**: Review as needed

### Quality Standards

All Shared-Knowledge assets should meet the same standards as domain content:

- Clear purpose and scope
- Reproducible in clean environments
- Documented prerequisites and validation
- English as default language
- Maintained and updated

### Archive Criteria

Content should be archived or deleted when:

- No longer maintained or relevant
- Superseded by better alternatives
- Preview features cancelled
- Migrated to domain folders
- No team usage for 6+ months

## Examples by Folder

**Learning-Day**: "RAG implementation demo from Q2 Learning Day"

**Community-Contributions**: "Multi-domain cost calculator script"

**Useful-Tools**: "Training environment cleanup automation"

**Emerging-Technologies**: "Azure OpenAI GPT-5 preview evaluation"

**Tips-and-Tricks**: "Fix: azd deployment hanging on infrastructure provisioning"

**Reference-Architectures**: "Secure AI + Analytics Platform (OpenAI + AI Search + Fabric)"

## Questions?

For guidance on which folder to use or whether content belongs in Shared-Knowledge vs. a domain folder, refer to [CONTRIBUTING.md](../CONTRIBUTING.md) or ask the team.
