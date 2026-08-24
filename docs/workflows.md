# Workflow Inventory

## `GermanNewsFa.json`

Hosted news and publishing workflow. The current export contains 102 nodes covering RSS ingestion, article extraction, normalization, semantic duplicate filtering, OpenAI/Gemini translation, importance filtering, Telegram and X publishing, German-learning content, Reddit content, and forwarding selected news to the local video workflow.

Deployment-specific credential references are removed from the repository export. Configure all credentials again after importing the workflow.

## `GenerateVideoGermanNewsFa.json`

Local video-production workflow with 38 nodes. It receives news through a webhook and orchestrates Ollama, ComfyUI, Persian TTS, FFmpeg, intro/outro processing, background music, validation, cleanup, and Telegram delivery.

The ComfyUI stage uses history polling, completion checks, and a timeout path. Local commands are prepared in dedicated Code nodes and executed only in the local self-hosted n8n instance.

## Import order

1. Import and configure `GenerateVideoGermanNewsFa.json` on the local n8n instance.
2. Activate its production webhook and publish only that path through a named Cloudflare Tunnel.
3. Configure the fixed webhook URL in the hosted n8n instance.
4. Import or update `GermanNewsFa.json` on the hosted instance.
5. Test with one manually selected news item before enabling scheduled execution.

## Repository policy

Workflow exports in this repository contain logic and node configuration, but no usable credentials. Runtime assets, generated media, local models, execution folders, and secrets are excluded from version control.
