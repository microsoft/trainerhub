# Contributing Guide

Thank you for contributing to CAIP-Knowledge.

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

## How to Add a Demo

1. Select the target domain folder: `AI/`, `Fabric/`, `GitHub/`, or `Copilot/`.
2. Create or choose the correct folder under `Demos/` in that domain.
3. Add a local README that explains objective, prerequisites, setup, and validation.
4. Keep the demo reproducible in a clean environment.

## Folder Structure Rules

- Group by domain first: AI, Fabric, GitHub, Copilot
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
