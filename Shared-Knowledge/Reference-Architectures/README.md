# Reference-Architectures

Architecture patterns with diagrams and implementation code spanning multiple domains.

## Purpose

Provide complete, production-quality reference architectures that demonstrate best practices across multiple Azure services and domains.

These are end-to-end patterns showing how different services work together, not individual service examples.

## What Belongs Here

**Included:**

- Multi-domain architecture patterns (e.g., AI + Fabric + GitHub)
- Complete implementations with Infrastructure as Code
- Architecture diagrams with accompanying code
- End-to-end solutions crossing service boundaries
- Enterprise patterns (networking, security, compliance)
- Multi-region or complex topologies

**Not Included:**

- Single-service examples → Use domain Code or Demos folders
- Single-domain architectures → Use domain Best-Practices folders
- Diagrams without implementation code
- Incomplete or proof-of-concept only patterns

## Architecture Components

Each reference architecture should include:

### 1. Overview Document

- Business scenario and requirements
- Architecture decisions and rationale
- Technology stack and Azure services used
- Prerequisites and assumptions

### 2. Architecture Diagram

- Mermaid diagrams in markdown (preferred for version control)
- Or exported images with source files
- Clear component relationships
- Data flow and integration points

### 3. Implementation Code

- Infrastructure as Code (Bicep or Terraform preferred)
- Configuration files
- Application code if applicable
- Deployment scripts

### 4. Deployment Guide

- Step-by-step deployment instructions
- Validation and testing steps
- Troubleshooting common issues
- Cleanup instructions

### 5. Operational Considerations

- Monitoring and observability setup
- Security and compliance notes
- Cost estimation and optimization
- Scaling considerations

## Contribution Guidelines

- Use English as the default language for new content
- Follow Azure Well-Architected Framework principles
- Include cost estimation when practical
- Document security considerations and RBAC requirements
- Provide both development and production configurations
- Test deployment in clean environment before submitting

## Quality Standards

Reference architectures should be:

- **Complete** - All components documented and implemented
- **Production-ready** - Includes security, monitoring, reliability
- **Well-documented** - Clear explanations and rationale
- **Tested** - Verified deployment in clean environment
- **Maintained** - Updated when services or best practices change

## Single-Domain vs Multi-Domain

**Use Reference-Architectures for:**

- Solutions spanning AI + Fabric
- Solutions spanning GitHub + Azure services
- Solutions spanning Copilot + other domains
- Enterprise patterns involving multiple service categories

**Use domain folders for:**

- AI-only architectures → AI/Best-Practices
- Fabric-only data patterns → Fabric/Best-Practices
- GitHub-only workflows → GitHub/Best-Practices
- Copilot-only integrations → Copilot/Best-Practices

## Examples

- **RAG + Analytics Pipeline**: Azure OpenAI + AI Search + Fabric Lakehouse
- **Secure AI Workload**: Hub-spoke network + Private endpoints + AI services + Key Vault
- **Multi-region Intelligent App**: Functions + Cosmos DB + OpenAI + Front Door
- **MLOps Pipeline**: GitHub Actions + Azure ML + Container Registry + AKS
- **Enterprise Data Platform**: Synapse + Fabric + AI services + Purview
