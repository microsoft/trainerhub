# Tips-and-Tricks

Quick wins, shortcuts, and troubleshooting guides for cross-domain scenarios.

## Purpose

Share practical knowledge that improves daily work efficiency across multiple domains.

This is the place for battle-tested solutions, time-saving techniques, and "I wish I'd known this sooner" moments that don't warrant a full demo but provide immediate value.

## What Belongs Here

**Included:**

- Quick troubleshooting guides (cross-domain issues)
- Keyboard shortcuts and productivity tips
- Configuration tricks and optimization techniques
- Common pitfalls and how to avoid them
- Time-saving workarounds
- Little-known features that provide big value
- Cross-domain patterns and practices

**Not Included:**

- Domain-specific tips → Use domain Best-Practices folders
- Full demos or complex walkthroughs → Use domain Demos or other Shared-Knowledge folders
- Deprecated workarounds that no longer apply
- Opinionated practices without clear benefit

## Content Format

Keep tips concise and actionable:

- **One clear problem or goal per tip**
- **Quick context** - Why is this useful?
- **Step-by-step solution** - What exactly to do
- **Expected outcome** - What success looks like
- **Related resources** - Links to deeper documentation if needed

## Organization

Organize by category or domain applicability:

- **General** - Applies to all work
- **Azure** - Cross-service Azure tips
- **Development** - Coding and tooling
- **Training Delivery** - Lab and demo execution
- **Troubleshooting** - Common issues and fixes

## Contribution Guidelines

- Use English as the default language for new content
- Keep tips short and focused (under 500 words ideally)
- Include concrete examples or commands
- Test tips before sharing to ensure accuracy
- Update or remove tips that become obsolete
- Credit original source if applicable

## Quality Standards

Good tips are:

- **Specific** - Clear problem and solution
- **Tested** - Verified to work
- **Valuable** - Saves meaningful time or effort
- **Current** - Based on current product behavior

## Examples

### Quick Troubleshooting

- "VSCode Copilot not suggesting code: Check extension authentication"
- "Azure CLI hanging on login: Clear token cache with `az account clear`"

### Productivity Tips

- "Speed up azd deployments: Use `--no-prompt` for non-interactive execution"
- "Find large files in repo: `git ls-files | xargs ls -lh | sort -k5 -rh | head -20`"

### Configuration Tricks

- "Prevent accidental production deployments: Use Azure Policy to enforce tags"
- "Speed up Docker builds: Layer your dependencies before application code"

### Common Pitfalls

- "Bicep deployment fails: Check for resource name conflicts across scopes"
- "GitHub Actions timeout: Increase timeout in workflow file or optimize steps"
