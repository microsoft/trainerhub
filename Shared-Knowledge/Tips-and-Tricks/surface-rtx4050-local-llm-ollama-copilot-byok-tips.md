# Surface RTX4050 Local LLM Tips with Ollama and GitHub Copilot BYOK

## Summary

This note is for teammates who usually work on Surface laptops and want to try running a local LLM with Ollama before using it in GitHub Copilot BYOK.

We tried it out on the Surface machines that most MTTs actually use day to day, and the idea was simple: get a local LLM running on the NVIDIA GPU, then see how far we could take it inside GitHub Copilot. What we found was pretty clear. The default GitHub-provided model still gave the best overall speed and output quality, while the larger local models were often slower than expected.

In particular, once the model got too large for the RTX 4050 6 GB GPU, it started spilling work over to the CPU and the experience became noticeably sluggish. Because of that, we had to use a Modelfile to tune the parameters a bit and keep the model in a range that actually feels practical on this hardware.

It also gives a quick look at:

- a known-good setup path
- model selection guidance for RTX 4050 6 GB VRAM
- practical usage tips for Copilot Chat and Agent Plan
- a known limitation for Start implementation in the current BYOK flow

## Scope

This document covers:

- Local Ollama setup validation for Surface + NVIDIA
- Practical model choices for coding tasks
- Copilot BYOK usage pattern that works today
- Current Agent Mode limitation and workaround

This document does not cover:

- Enterprise deployment or team policy rollout
- Full benchmark methodology across all models
- Official product root-cause confirmation from engineering teams

## Tested Environment

| Area | Value |
| --- | --- |
| Device | Surface Laptop Studio 2 |
| CPU | Intel i7-13800H |
| RAM | 32 GB |
| GPU | NVIDIA RTX 4050 Laptop (6 GB VRAM) |
| OS | Windows 11 Pro |
| NVIDIA Driver | 591.55 |
| CUDA | 13.1 |
| VS Code | 1.129.1 |
| Copilot Extension | Latest at test time |
| Ollama | Latest at test time |

## Prerequisites & Installation

Before starting, ensure you have the following installed:

### 1. NVIDIA Driver & CUDA

- Download latest NVIDIA driver: [NVIDIA Driver Downloads](https://www.nvidia.com/Download/driverDetails.aspx)
- For RTX 4050 Laptop on Windows: search `RTX 4050` and select your OS
- CUDA Toolkit (optional for Ollama, but recommended): [CUDA Toolkit Downloads](https://developer.nvidia.com/cuda-downloads)
  - Ollama will auto-detect CUDA for GPU acceleration

### 2. Ollama

- Download from: [ollama.com](https://ollama.com)
- Windows installer available
- After install, verify with: `ollama --version`
- Ollama will run as a local service on `http://localhost:11434`

### 3. VS Code

- Download from: [code.visualstudio.com](https://code.visualstudio.com)
- Install the GitHub Copilot extension (see next step)

### 4. GitHub Copilot Extension

- Open VS Code
- Go to Extensions (Ctrl+Shift+X)
- Search for "GitHub Copilot"
- Install the official extension by GitHub

### Quick Validation

```powershell
# Check NVIDIA GPU
nvidia-smi

# Check Ollama
ollama --version

# Verify Ollama service is running (should return version info)
Invoke-WebRequest -Uri "http://localhost:11434/api/version"
```

If any tool is missing, follow the links above to install it first.

## Quick Start on Surface

1. Validate GPU and runtime:

```powershell
nvidia-smi
ollama --version
```

1. Confirm local models are available:

```powershell
ollama list
```

1. In VS Code, register Ollama provider in Language Models.
1. In Copilot Chat, pick an Ollama BYOK model.
1. Use BYOK model for chat and planning tasks first.

## Model Tips for RTX 4050 (6 GB VRAM)

### Practical Recommendation

- Default coding model: `qwen3:4b` or `qwen3:4b-coding`
- Reason: best speed/quality balance in this hardware profile

### Observed Model Behavior

| Model | Practical Result | Note |
| --- | --- | --- |
| `gemma4:12b` | Not recommended for daily use | High quality, but too slow on 6 GB VRAM |
| `qwen3:8b` | Usable, somewhat slow | CPU offload observed |
| `qwen3:4b` | Recommended | Fits GPU better, faster response |

## Useful Modelfile Profiles

### Fast Profile

```text
FROM qwen3:4b

PARAMETER num_ctx 8192
```

### Coding Profile

```text
FROM qwen3:4b

PARAMETER num_ctx 8192
PARAMETER temperature 0.2
PARAMETER top_p 0.9
PARAMETER top_k 20
PARAMETER repeat_penalty 1.05
```

### Think Profile

```text
FROM qwen3:4b

PARAMETER num_ctx 8192
PARAMETER temperature 0.7
PARAMETER top_p 0.95
PARAMETER top_k 40
PARAMETER repeat_penalty 1.05
```

Create model command:

```powershell
ollama create <your-model-name> -f Modelfile
```

## Copilot BYOK Usage Pattern (What Works Well)

- Copilot Chat with Ollama BYOK works.
- Agent Plan generation with Ollama BYOK works.
- This is a good flow for ideation, scaffolding plans, and code review drafts.

## Known Limitation: Agent Start Implementation

In the tested setup, Agent Mode fails at Start implementation with:

```text
No utility model is configured for 'copilot-utility-small'
while the selected main agent model is BYOK.
```

### What Was Checked

The same issue reproduced with multiple BYOK model choices:

- `qwen3:4b`
- `qwen3.5:4b`
- `qwen3:4b-coding`

This indicates it is likely not a single-model issue.

## Workaround (Current)

Use a hybrid flow:

1. Keep Ollama BYOK for planning and local chat tasks.
2. For Start implementation, use a supported utility model path in Copilot.

3. If needed, split execution:

   - Step A: Plan with BYOK model.
   - Step B: Switch model configuration for implementation run.

## Validation Checklist

- [ ] `nvidia-smi` shows the expected NVIDIA GPU.
- [ ] `ollama list` shows intended local models.
- [ ] Copilot can select Ollama model for chat.
- [ ] Agent Plan works with BYOK model.
- [ ] Start implementation behavior is verified and recorded.

## Version Delta

- **2026-07-20**: Reframed from issue-only note to Surface-focused local LLM tips with known limitation section.

## Last Verified

- **Date**: 2026-07-20
- **Status**: Reproducible in tested environment
