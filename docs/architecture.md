# Architecture

GermanNewsFa is designed as a modular n8n automation platform with separate workflows for news automation, daily calendar publishing, and German language learning.

## High-Level Architecture

```text
GermanNewsFa Platform
│
├── AI News Automation
│   ├── RSS Sources
│   ├── Article Cleaning
│   ├── Image Extraction
│   ├── AI Translation
│   ├── AI Summarization
│   ├── Telegram Payload Builder
│   └── Telegram Publishing
│
├── Daily Calendar Automation
│   ├── Schedule Trigger
│   ├── German Place Selection
│   ├── Wikimedia Image Download
│   ├── Jalali / Gregorian Date Builder
│   ├── Holiday Detection
│   └── Telegram Publishing
│
└── German Learning Automation
    ├── Daily Sentence Workflow
    ├── Weekly Dialog Workflow
    ├── Google Sheets Content Database
    └── Telegram Publishing


Module 1: AI News Automation

The main news workflow collects articles from German RSS sources, processes the content, transforms it with AI, and publishes Persian output to Telegram.

Main responsibilities:

RSS ingestion
Article normalization
HTML cleanup
Image extraction
AI-based translation
AI-based summarization
Telegram-safe message formatting
RTL Persian text support
Long-text chunking
Source attribution
Module 2: Daily Calendar Automation

The daily calendar workflow publishes a morning post with a German cultural or geographic reference.

Main responsibilities:

Scheduled morning trigger
Random German location selection
Wikimedia image download
Jalali date generation
Gregorian date generation
Berlin time display
Public holiday information
Telegram photo publishing
Module 3: German Learning Automation

The German learning workflows use Google Sheets as a lightweight content management system.

Daily Sentence

Publishes one practical German sentence with Persian translation and keyword support.

Weekly Dialog

Publishes one longer German dialog with Persian translation and useful expressions.

Shared Design Principles
Modular workflows instead of one monolithic automation
Google Sheets as lightweight CMS for learning content
Telegram as the main publishing channel
AI providers abstracted through workflow configuration
Persian RTL formatting handled before publishing
Sensitive credentials managed through n8n credentials