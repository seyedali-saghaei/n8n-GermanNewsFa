# Changelog

## 2026-08-13

### Added

- Production Python helpers for Persian TTS and FFmpeg-based scene/final video rendering.
- Python dependency declaration for Edge TTS.
- Local news-to-video workflow using Ollama, ComfyUI, Persian TTS, and FFmpeg.
- Webhook handoff from hosted n8n to the local video pipeline.
- ComfyUI history polling, completion validation, and timeout handling.
- Scene rendering, concatenation, background music, intro/outro, final validation, and Telegram delivery.
- Documentation for the hybrid hosted/local architecture and security model.

### Changed

- Made FFmpeg, FFprobe, and Windows font paths configurable through environment variables while preserving current defaults.
- Expanded ignore rules for generated media, runtime folders, Python caches, and local AI model output.
- Updated the hosted `GermanNewsFa` workflow to the current 102-node export.
- Replaced the temporary Cloudflare tunnel URL with `GERMAN_NEWS_VIDEO_WEBHOOK_URL`.
- Removed deployment-specific n8n credential references from public workflow exports.

### Known limitations

- Full video generation may take more than one hour on the current local setup.
- Local commands and paths are currently Windows-oriented.
