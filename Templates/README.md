# Templates

This folder stores reusable templates for guides, lab instructions, and content scaffolding.

## Use This Folder For

- Guide templates
- Lab instruction templates
- Scenario and demo scaffolding
- Metadata templates for asset organization
- Content structure templates

## Available Templates

- [demo-guide.md](demo-guide.md) - Template for creating demo guides
- [shared-knowledge-metadata.md](shared-knowledge-metadata.md) - Metadata template for Shared-Knowledge assets

## Content Guidance

- Keep templates minimal and easy to adapt
- Include placeholders for the fields contributors must fill in
- Prefer reusable structure over highly specific wording
- Templates should work across multiple domains when possible

## Templates vs Reference-Architectures

### Use Templates/ For:

Reusable **empty scaffolds** that contributors fill in:

- Document structure templates
- Lab instruction formats
- Metadata schemas
- Content organization patterns

Example: A blank demo guide template with sections like "Prerequisites", "Steps", "Validation"

### Use Shared-Knowledge/Reference-Architectures/ For:

Complete, **working implementations** of multi-domain patterns:

- Full architecture examples with code
- End-to-end solutions with Infrastructure as Code
- Production-ready implementations
- Multi-service integration patterns

Example: A complete RAG application with Azure OpenAI + AI Search + Fabric, including Bicep templates, application code, and deployment guide

### Quick Comparison

| Aspect | Templates/ | Shared-Knowledge/Reference-Architectures/ |
|--------|-----------|-------------------------------------------|
| Content | Empty scaffolds | Complete implementations |
| Purpose | Starting point for creating | Reference for understanding and adapting |
| Code | Placeholders or minimal examples | Full, working code |
| Usage | Copy and fill in | Study, adapt, or deploy as-is |
| Scope | Single asset type | Multi-service solution |

## Contributing New Templates

When adding a new template:

1. Ensure it's truly reusable across multiple assets or domains
2. Include clear instructions for using the template
3. Add placeholders in `[brackets]` or `{curly braces}` for fields to fill
4. Document what each section should contain
5. Update this README with a link to the new template