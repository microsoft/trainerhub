# Contributing Guide

Thank you for contributing to CAIP-Knowledge.

## Scope of This Guide

For shared mission, repository design principles, and GitHub/SharePoint positioning, refer to [README.md](README.md).

This document focuses on day-to-day contribution execution.

## Rule 1: English by Default

Use English as the default language for new content.

This repository supports multilingual content when needed.

This includes:

- Documentation and README files
- Templates and lab instructions
- Pull request titles and descriptions
- Issue titles and descriptions
- Code comments
- Commit messages

Allowed exceptions:

- Official product names and trademarks
- External quoted text that must remain unchanged

If you add non-English content, include an English summary when practical so global contributors can follow.

English is the baseline for shared repository content so contributors across regions can work from the same default.

## How to Add an Asset

1. Determine if the asset belongs in a domain folder or Shared-Knowledge (see decision guide below).
2. If domain-specific: Select the target domain folder: `AI/`, `Fabric/`, `GitHub/`, or `Copilot/`.
3. If cross-domain or uncertain: Select the appropriate `Shared-Knowledge/` subfolder.
4. Select the category folder that best matches the asset type.
5. Create or choose the correct subfolder in that category.
6. Add a local README that explains objective, prerequisites, setup, and validation.
7. Keep the asset reproducible in a clean environment.

## Domain vs Shared-Knowledge Decision Guide

Use this guide to determine where your contribution belongs:

### Use Domain Folders When

- ✅ Content clearly serves one domain's scope
- ✅ Asset is production-ready and domain-specific
- ✅ Follows established domain patterns
- ✅ Examples: AI-specific demo, Fabric-only code sample, GitHub workflow, Copilot skill

### Use Shared-Knowledge When

- ✅ Content applies to multiple domains equally
- ✅ Asset is experimental or for emerging technologies
- ✅ Material is from team Learning Day events
- ✅ Tool or utility helps across all domains
- ✅ Temporary staging while determining domain fit

### Quick Decision Table

| Content Type | Location |
| ------------ | -------- |
| AI-specific demo | `AI/Demos/` |
| Multi-domain architecture | `Shared-Knowledge/Reference-Architectures/` |
| Fabric code sample | `Fabric/Code/` |
| Cross-domain utility script | `Shared-Knowledge/Useful-Tools/` |
| GitHub course lab | `GitHub/Courses/{course-code}/` |
| Learning Day demo | `Shared-Knowledge/Learning-Day/` (initially) |
| Experimental preview feature | `Shared-Knowledge/Emerging-Technologies/` |
| Domain best practice | `{Domain}/Best-Practices/` |
| Quick troubleshooting tip | `Shared-Knowledge/Tips-and-Tricks/` |

For detailed Shared-Knowledge guidance, see [Shared-Knowledge/README.md](Shared-Knowledge/README.md).

## Migrating Content from Shared-Knowledge

Content in Shared-Knowledge is not permanent. When contributing to or reviewing Shared-Knowledge:

**Move to domain folder when:**

- Asset becomes clearly domain-specific
- Content is stable and production-ready
- Team usage shows it serves primarily one domain

**Keep in Shared-Knowledge when:**

- Asset truly spans multiple domains
- Still experimental or under active development
- Provides cross-domain value

**Archive when:**

- No longer maintained or relevant
- Superseded by better alternatives
- Preview features cancelled

## Folder Structure Rules

- Group by domain first: AI, Fabric, GitHub, Copilot
- Use Shared-Knowledge for cross-domain or experimental content
- Use the common domain template: Courses, Demos, Industry-Use-Cases, Customer-Scenarios, Skills, Code, Best-Practices
- Keep depth shallow when possible
- Keep one clear purpose per folder

## Naming Conventions

- Keep top-level and category folder names consistent with the repository standard
- Use official course codes under each `Courses/` folder
- Keep names short and descriptive for content subfolders

Examples:

- foundry-rag-demo
- copilot-trainer-agent
- lab-instructions-template

## Pull Request Checklist

Before opening a PR, confirm:

- English is used as the default language for new content
- Non-English content includes English context when practical
- Steps are clear and testable
- Naming follows repository conventions
- README or usage docs are updated if needed
- A reviewer from the relevant domain is requested
- If structure or categorization changed, related README/docs are updated in the same PR
