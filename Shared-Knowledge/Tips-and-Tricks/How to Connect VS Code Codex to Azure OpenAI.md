# How to Connect VS Code Codex to Azure OpenAI

As MTTs, we are increasingly getting opportunities to work not only with Copilot, but also with coding agents such as Codex.

While exploring Codex myself, I tested how to configure **VS Code Codex to use a model deployed in Azure OpenAI**. I thought this could also be useful for other MTTs who want to experiment with Codex while using Azure OpenAI, so I decided to document and share the setup process.

This guide walks through how to configure VS Code Codex to use **your Azure OpenAI deployment instead of the default OpenAI endpoint**.

> **Note:** This is a practical guide based on my own testing with VS Code, Codex, and Azure OpenAI, along with Microsoft official documentation.

---

## Prerequisites

Before starting, make sure you have the following:

- Visual Studio Code installed
- OpenAI Codex extension installed
- An Azure OpenAI resource
- An Azure OpenAI API key
- An Azure OpenAI model deployment that supports the Responses API

> Codex uses the Azure OpenAI Responses API, so make sure the model and deployment you plan to use support the Responses API.

---

## 1. Deploy an Azure OpenAI Model

In Microsoft Foundry, deploy an Azure OpenAI model that supports the Responses API.

For example:

- Model: `gpt-5.5`
- Deployment name: `my-gpt-5.5`

After deployment, make sure you have the following information:

- Azure OpenAI endpoint
- Model deployment name
- Azure OpenAI API key

Example endpoint:

```text
https://<resource-name>.openai.azure.com
```

> **Important:** The `model` value in the Codex configuration should be the **Azure deployment name**, not necessarily the original model name.
>
> For example, if you deploy `gpt-5.5` using the deployment name `my-gpt-5.5`, configure Codex with `model = "my-gpt-5.5"`.

---
<img width="1415" height="653" alt="image" src="https://github.com/user-attachments/assets/ee86db6d-273b-43dd-91ef-f5d27aa77192" />

## 2. Store the API Key in a Local Environment Variable

On Windows, you can store the Azure OpenAI API key as a user-level environment variable using PowerShell.

> **Important security requirement:** Store the API key in an environment variable. Never place the API key directly in `config.toml`, any other configuration file, or source control. The configuration should contain only the environment variable name through `env_key`.

Run:

```powershell
:SetEnvironmentVariable(
    "AZURE_OPENAI_API_KEY",
    "<Azure OpenAI API Key>",
    "User"
)
```

Do not include `<` or `>` when entering the actual API key.

For example, if your API key is `abc123`, use:

```powershell
:SetEnvironmentVariable(
    "AZURE_OPENAI_API_KEY",
    "abc123",
    "User"
)
```

You can open a new PowerShell window and verify that the environment variable is available:

```powershell
$env:AZURE_OPENAI_API_KEY
```

> **Security recommendation:** Do not store the API key directly in `config.toml` or commit it to a Git repository. The `env_key` setting should reference the name of the environment variable containing the API key.
>
> **Recommended after setup:** Because the API key is stored in a user-level environment variable, sign out of Windows and sign back in whenever possible before starting VS Code again. This helps ensure that VS Code and Codex receive the updated environment variable. At a minimum, completely close and restart VS Code.

---

## 3. Configure Codex `config.toml`

Codex uses the `config.toml` file to configure the model and model provider.

On Windows, the configuration file is typically located at:

```text
C:\Users\<username>\.codex\config.toml
```

Configure the model settings as follows:

```toml
model = "my-gpt-5.5"
model_provider = "azure"
model_reasoning_effort = "medium"

[model_providers.azure]
name = "Azure OpenAI"
base_url = "https://<resource-name>.openai.azure.com/openai/v1"
env_key = "AZURE_OPENAI_API_KEY"
wire_api = "responses"
```

Here is what each setting means:

| Setting | Description |
|---|---|
| `model` | Azure OpenAI model deployment name |
| `model_provider` | Model provider configuration to use |
| `model_reasoning_effort` | Reasoning effort level for supported models |
| `base_url` | Azure OpenAI endpoint with `/openai/v1` appended |
| `env_key` | Name of the environment variable containing the API key |
| `wire_api` | API used by Codex, in this case the Responses API |

### Example configuration

If your Azure OpenAI resource is named `my-openai-resource` and your model deployment is named `my-gpt-5.5`, the configuration would look like this:

```toml
model = "my-gpt-5.5"
model_provider = "azure"
model_reasoning_effort = "medium"

[model_providers.azure]
name = "Azure OpenAI"
base_url = "https://my-openai-resource.openai.azure.com/openai/v1"
env_key = "AZURE_OPENAI_API_KEY"
wire_api = "responses"
```

> When using the Azure OpenAI v1 API, include `/openai/v1` in the `base_url`.

---

## 4. Windows and WSL Considerations

For running the Codex CLI on Windows, the official documentation describes using **Windows 11 with WSL2**.

The VS Code Codex extension uses the Codex `config.toml` configuration.

If you are also using WSL, keep the following points in mind:

- The required environment variable must be available in the environment where Codex runs.
- The VS Code Codex extension must also be able to access the required environment variable.
- If you use WSL, you may also need to set the environment variable on the Windows host so that the VS Code extension can access it.
- Changes to environment variables might not be visible to an already running VS Code process.

---

## 5. Restart VS Code and Test the Connection

After configuring the environment variable and `config.toml`, completely restart VS Code so that the new environment variable is available to the process.

1. Close all VS Code windows.
2. If necessary, check Task Manager and close any remaining VS Code processes.
3. Start VS Code again.
4. Open a new conversation in Codex.
5. Enter a simple test prompt.

For example:

```text
Do not modify any files in the current workspace.
Just reply with:
"Azure OpenAI connection test successful"
```

If Codex responds successfully, the basic Azure OpenAI connection configuration is working.

---

## Troubleshooting

| Error or Symptom | Possible Cause and Resolution |
|---|---|
| `Missing environment variable: AZURE_OPENAI_API_KEY` | The environment variable is not configured or is not available to the existing VS Code process. Completely restart VS Code. If necessary, sign out of Windows and sign back in. |
| `The requested operation is unsupported.` | Check whether the model and deployment you are using support the Responses API. |
| `401 Unauthorized` | Verify that the Azure OpenAI API key is correct. |
| `403 Forbidden` | Verify that the credentials being used have access to the Azure OpenAI resource. |
| `404` or `deployment not found` | Verify the `base_url` and make sure the `model` value matches the actual Azure deployment name. |
| Works in CLI but not in VS Code | Check whether the environment variable is available to the VS Code process and restart VS Code completely. |
| Model is deployed but does not work with Codex | Verify that the model and deployment support the Responses API. |

---

## Quick Checklist

If the connection does not work, check these five things first:

1. **Does the model support the Responses API?**
2. **Does the `model` value match the actual Azure deployment name?**
3. **Does the `base_url` end with `/openai/v1`?**
4. **Does `env_key` match the environment variable containing your API key?**
5. **Did you completely restart VS Code after configuring the environment variable?**

Example:

```toml
model = "my-gpt-5.5"
model_provider = "azure"

[model_providers.azure]
name = "Azure OpenAI"
base_url = "https://my-openai-resource.openai.azure.com/openai/v1"
env_key = "AZURE_OPENAI_API_KEY"
wire_api = "responses"
```

---

## Additional Notes

- The `model` value in `config.toml` should match the actual **Azure deployment name**.
- The model name and deployment name do not have to be the same.
- Include `/openai/v1` at the end of the Azure OpenAI `base_url`.
- Set `wire_api` to `responses`.
- Store the API key in an environment variable instead of directly in the configuration file.
- Verify that the model you plan to use supports the Responses API.
- After changing the configuration, it is a good idea to test it in a new Codex conversation rather than continuing an existing conversation.

---

## Official Documentation

Always review the latest Microsoft official documentation before configuring or troubleshooting Codex with Azure OpenAI. Product requirements and configuration details may change, so use the links below as the authoritative source.

- [Codex with Azure OpenAI in Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/codex)
- [Azure OpenAI Responses API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/responses)
