# Hybrid News-to-Video Pipeline

## Current status

The project now combines a hosted news workflow with a local AI media pipeline. The hosted n8n instance selects and prepares German news. A webhook forwards suitable items to a local n8n instance, which creates a Persian vertical news video.

## Architecture

1. The hosted `GermanNewsFa` workflow reads RSS feeds, extracts article content, filters duplicates, evaluates importance, generates Persian news copy, and publishes regular posts.
2. The `Send News To Video Workflow` node forwards selected news to the local webhook configured through `GERMAN_NEWS_VIDEO_WEBHOOK_URL`.
3. The local `GenerateVideoGermanNewsFa` workflow creates and validates a three-scene storyboard with Ollama.
4. ComfyUI generates one image per scene. The workflow polls ComfyUI history instead of relying on one long fixed wait and stops with a controlled timeout.
5. Local text-to-speech creates Persian narration.
6. FFmpeg renders the scenes, joins them, adds background music, and inserts intro/outro assets.
7. The completed video is validated and sent to Telegram.

## Local components

| Component | Responsibility |
| --- | --- |
| n8n | Local workflow orchestration |
| Ollama | Local storyboard generation |
| ComfyUI | AI image generation |
| FFmpeg | Scene rendering and final video assembly |
| Cloudflare Tunnel | Temporary inbound connection from hosted n8n |
| Telegram | Final video delivery |

## Required configuration

- Import `workflows/GenerateVideoGermanNewsFa.json` into the local n8n instance.
- Configure Ollama and Telegram credentials after import. Credential IDs are intentionally not stored in Git.
- Provide the hosted workflow with `GERMAN_NEWS_VIDEO_WEBHOOK_URL`.
- Start ComfyUI on `http://127.0.0.1:8188` or update the corresponding HTTP Request nodes.
- Make FFmpeg and all local rendering scripts available to the n8n process.
- Allow only the local directories that the workflow needs through `N8N_RESTRICT_FILE_ACCESS_TO`.

## Security rules

- Never commit API keys, Telegram tokens, OAuth secrets, `.env` files, or n8n credential exports.
- Treat Cloudflare quick-tunnel URLs as temporary values.
- Keep generated images, audio files, video files, model weights, and execution folders outside Git.
- Use n8n Credentials or environment variables for secrets and deployment-specific URLs.

## Known limitations

- A complete video run can take more than one hour depending on Ollama and ComfyUI performance.
- Cloudflare quick-tunnel URLs change after restart unless a named tunnel is configured.
- The workflow currently assumes Windows-oriented local commands and paths.
- Model availability and GPU memory directly affect generation time and reliability.

## Next improvements

- Replace the temporary tunnel with a stable authenticated endpoint.
- Add bounded retries around ComfyUI, TTS, and rendering failures.
- Record execution duration per stage to identify the main bottleneck.
- Move deployment-specific paths and service URLs into environment variables.
- Add an automated JSON validation and secret scan for exported workflows.
