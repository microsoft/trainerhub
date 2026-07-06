# trainerhub

trainerhub is a shared repository for training assets, demos, scenarios, code samples, and reusable content for technical trainers.

## Purpose

- Reuse practical training assets across teams
- Reduce duplicated effort when creating hands-on content
- Keep demo and lab quality consistent
- Support fast iteration on trainer workflows and delivery materials

## Language Policy

1. English by default: Use English as the default language for new repository content.
2. Multilingual support: Non-English content is allowed when it improves audience reach, local delivery quality, or training outcomes.
3. Scope: This applies to README files, docs, templates, PR titles and descriptions, issue content, and code comments.
4. Practical guidance: When adding non-English content, include an English summary or bilingual headings when practical.
5. Team usage: English is the baseline for shared content so contributors across regions can collaborate consistently.
6. Automation: CI may provide language-policy guidance for consistency, but it does not block multilingual contributions.

## Repository Structure

```
.
├─ Courses/
│  ├─ AI-3026/
│  ├─ AI-3016/
│  ├─ GH-300/
│  └─ PL-7008/
├─ Demos/
│  ├─ AI/
│  ├─ Copilot/
│  ├─ Foundry/
│  └─ Fabric/
├─ Agents/
│  ├─ Trainer Skills/
│  ├─ Copilot Studio/
│  └─ Custom Agents/
├─ Scenarios/
│  ├─ Customer Stories/
│  ├─ Industry Use Cases/
│  └─ Field Examples/
├─ Code/
│  ├─ Samples/
│  ├─ Snippets/
│  └─ Scripts/
├─ Learning-Day/
│  ├─ 20260703/
│  │  ├─ Docs/
│  │  └─ Recordings/
│  └─ 20260807/
│     ├─ Docs/
│     └─ Recordings/
├─ Best-Practices/
└─ Templates/
```

## Folder Guide

- [Courses/](Courses/): Course-specific assets and learning resources organized by official course code
- [Demos/](Demos/): Hands-on demos and runnable examples grouped by solution area
- [Agents/](Agents/): AI-powered trainer tools, assistants, and agent workflows
- [Scenarios/](Scenarios/): Story-driven references for customer and field usage contexts
- [Code/](Code/): Reusable implementation assets and utilities
- [Learning-Day/](Learning-Day/): Session-based knowledge archive by date
- [Best-Practices/](Best-Practices/): Curated best practices, checklists, and standards
- [Templates/](Templates/): Reusable templates for guides, lab instructions, and content scaffolding

## Contribution Guidelines

Contributors are encouraged to add demos, agents, and templates that are practical, reusable, and easy for other trainers to adopt.

### Adding Content

- Place new material in the most relevant folder.
- Add a short README when a folder needs setup or usage instructions.
- Keep examples reproducible and easy to validate.
- Prefer reusable templates and shared assets when possible.

## Folder Structure Principles

- Group by capability first (Courses, Demos, Agents, Scenarios, Code, Learning-Day, Best-Practices, Templates)
- Keep nesting shallow (prefer 2-3 levels)
- One clear purpose per folder
- Store shared assets in a local `assets/` folder when needed

## Naming Conventions

- Follow the established repository folder names as defined above
- Keep names short, specific, and searchable
- Use consistent suffixes where useful:
	- `-demo`
	- `-agent`
	- `-template`
- Avoid version numbers in folder names unless required by release policy

## Quick Start for Contributors

- Add or update content in the appropriate folder
- Reuse existing templates from `Templates/` whenever possible
- Keep instructions practical and testable
- Open a pull request with a short summary of:
	- what was added
	- who it is for
	- how to validate it

## GitHub Codespaces

This repository includes a default dev container configuration for GitHub Codespaces.

### Open in Codespaces

1. Open the repository on GitHub.
2. Select **Code** > **Codespaces** > **Create codespace on main**.
3. Wait for the container setup to complete.

### Included setup

- Base image: `mcr.microsoft.com/devcontainers/universal:2`
- Recommended VS Code extensions for Azure, Python, PowerShell, and Markdown

## Notes

- This repository contains multiple demos, scenarios, and course assets, so run steps are defined per folder.
- Check each demo or agent folder README for prerequisites and execution commands.

## Scalability Recommendations

To keep this repository maintainable as contributions grow:

1. Add folder-level `README.md` files in `Courses/`, `Demos/`, `Agents/`, `Scenarios/`, `Code/`, and `Templates/` to improve discoverability.
2. Introduce a lightweight metadata header format (owner, target audience, estimated duration, required tools) for demos, scenarios, and templates.
3. Add a simple contribution checklist in pull requests (reproducible steps, prerequisites, expected outcome validated).
4. Create tagging conventions for scenarios (for example: `foundry`, `copilot`, `rag`, `beginner`, `advanced`) to improve search and filtering.
5. Add a periodic cleanup process for stale items (archive or promote across `Scenarios/`, `Demos/`, `Agents/`, and `Courses/`).

## Collaboration Note

Prioritize clarity, reuse, and real training value over completeness.

