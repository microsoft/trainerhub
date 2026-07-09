# CAIP-Knowledge

CAIP-Knowledge is a domain-based knowledge hub for trainer assets, organized by product area instead of content type.

## Purpose

- Improve discoverability and reuse through domain-based organization
- Manage courses, demos, scenarios, code, and best practices in one place
- Accelerate onboarding for new contributors

## Structure Principles

- Domain-first: AI, Fabric, GitHub, Copilot
- Each domain uses the same subfolder template
- Course assets are organized by official course code under `Courses/`
- Shared templates are centrally managed in root `Templates/`

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
└─ Templates/
```

## Domain Folders

- [AI/](AI/)
- [Fabric/](Fabric/)
- [GitHub/](GitHub/)
- [Copilot/](Copilot/)
- [Templates/](Templates/)

## Quick Contribution Guide

1. Choose the target domain first.
2. Select the appropriate category subfolder inside that domain.
3. Include reproducible steps and validation criteria for new content.
4. Update the domain README and templates together when needed.

## Notes

- This repository uses a domain-based structure as the official standard.
- For detailed operating guidance, refer to each domain `README.md` first.

