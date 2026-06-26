# GermanNewsFa – AI Media & Language Learning Automation Platform

GermanNewsFa is a modular AI automation platform built with **n8n**.
It automates multilingual German news publishing, daily calendar content, and German language-learning posts for Persian-speaking audiences.

The project combines **AI translation**, **RSS aggregation**, **Telegram publishing**, **Google Sheets-based content management**, and **scheduled automation workflows** into one structured media automation system.

---

## Overview

GermanNewsFa is not only a news translation workflow.
It is a multi-workflow automation platform with three main modules:

1. **AI News Automation**
2. **Daily Calendar Automation**
3. **German Language Learning Automation**

The goal is to provide Persian-speaking users with:

* German and international news in Persian
* Daily cultural/calendar content from Germany
* Practical German learning material
* Weekly German dialogs for real-life language practice

---

## Main Features

### AI News Automation

* Collects German news from multiple RSS sources
* Cleans and normalizes article content
* Extracts article images where available
* Filters and processes news items
* Uses AI for translation and summarization
* Supports OpenAI and Gemini-based processing
* Builds Telegram-ready Persian content
* Handles Telegram caption limits
* Splits long texts into safe Telegram chunks
* Supports RTL Persian formatting
* Adds source links and inline buttons

---

### Daily Calendar Automation

* Runs automatically every morning
* Selects a German landmark or location
* Downloads an image from Wikimedia
* Generates a Persian daily greeting
* Shows Jalali date
* Shows Gregorian date
* Shows Berlin time
* Adds German public holiday information where available
* Publishes the result to Telegram

---

### German Learning – Daily Sentence

This workflow publishes one practical German sentence per day.

It uses Google Sheets as a simple content database and includes:

* German sentence
* Persian translation
* Learning level, for example A1–B1
* German keyword
* Persian keyword translation
* Telegram publishing
* Automatic `Published = TRUE` update after successful posting

---

### German Learning – Weekly Dialog

This workflow publishes one weekly German dialog.

It includes:

* German dialog text
* Persian translation
* Practical phrases
* Learning level
* Weekly Telegram post
* Google Sheets-based publishing status management

---

## Architecture

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
│   ├── Random German Place Selection
│   ├── Wikimedia Image Download
│   ├── Jalali/Gregorian Date Builder
│   └── Telegram Publishing
│
└── German Learning Automation
    ├── Daily Sentence Workflow
    ├── Weekly Dialog Workflow
    ├── Google Sheets Content Database
    └── Telegram Publishing
```

---

## Project Structure

```text
n8n-GermanNewsFa/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
│
├── workflows/
│   ├── GermanNewsFa.json
│   ├── Gemini-single-call-legacy.json
│   └── GermanLearning/
│       ├── DailySentence.json
│       └── WeeklyDialog.json
│
├── docs/
│   └── screenshots/
│
├── assets/
└── images/
```

---

## Workflows

### 1. `GermanNewsFa.json`

Main production workflow for AI-powered German news processing and Telegram publishing.

Core responsibilities:

* RSS ingestion
* News preprocessing
* Translation pipeline
* Summary generation
* Telegram formatting
* Image-aware publishing
* Long-text chunking

---

### 2. `Gemini-single-call-legacy.json`

Legacy workflow kept for reference.

This version was focused on Gemini-based single-call translation and batching logic.

It is useful for showing the evolution from an experimental workflow to a larger automation platform.

---

### 3. `GermanLearning/DailySentence.json`

Publishes one daily German learning sentence from Google Sheets to Telegram.

Content fields:

* `ID`
* `German`
* `Persian`
* `KeywordGerman`
* `KeywordPersian`
* `Level`
* `Published`

---

### 4. `GermanLearning/WeeklyDialog.json`

Publishes one weekly German dialog from Google Sheets to Telegram.

Content fields:

* `ID`
* `Title`
* `GermanDialog`
* `PersianDialog`
* `Vocabulary`
* `Keywords`
* `Level`
* `Published`

---

## Tech Stack

* n8n
* JavaScript
* OpenAI API
* Google Gemini API
* Telegram Bot API
* Google Sheets
* RSS Feeds
* HTTP Requests
* JSON Workflow Exports
* Git / GitHub

---

## AI & Automation Concepts Used

* Workflow automation
* Prompt-based content transformation
* Multilingual translation pipeline
* Persian RTL text handling
* Telegram message formatting
* Content chunking
* Scheduled automation
* Google Sheets as a lightweight CMS
* Persistent publishing state
* Modular workflow design

---

## Configuration

Before importing or running the workflows, configure the following services:

### Required

* n8n instance
* Telegram Bot
* Telegram Channel or Group ID
* Google Sheets OAuth credentials
* OpenAI or Gemini API credentials

### Recommended Environment Variables

Use environment variables or n8n credentials instead of hardcoding secrets.

```text
TELEGRAM_CHAT_ID=your_chat_id
TELEGRAM_BOT_TOKEN=your_bot_token
GOOGLE_SHEET_ID=your_google_sheet_id
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

## Security Notice

This repository should not contain real credentials.

Before committing workflow exports, replace sensitive values such as:

```text
chatId
webhookId
credential IDs
Google Sheet IDs
Telegram Bot Tokens
API Keys
OAuth IDs
```

with placeholders such as:

```text
YOUR_TELEGRAM_CHAT_ID
YOUR_WEBHOOK_ID
YOUR_GOOGLE_SHEET_ID
YOUR_CREDENTIAL_ID
YOUR_API_KEY
```

---

## Example Output

### News Post

```text
📰 German news title in Persian

Persian summary of the article...

🔗 Continue reading
@German_news_fa
```

### Daily Calendar Post

```text
☀️ سلام، صبح بخیر

🏛 تصویر روز
دروازه براندنبورگ — برلین

📅 تاریخ شمسی | تاریخ میلادی
⏰ به وقت برلین

@German_news_fa
```

### German Learning Sentence

```text
🇩🇪 آلمانی کاربردی برای زندگی در آلمان

📘 جمله روز

🏷 سطح: A1-B1

🇩🇪
German sentence

🇮🇷
Persian translation

🔹 #واژه_امروز

German keyword = Persian keyword
```

### Weekly Dialog

```text
🎭 دیالوگ هفته

📍 Dialog title
🏷 سطح: A1-B1

متن آلمانی

German dialog

────────────

ترجمه فارسی

Persian translation

────────────

🔹 عبارت‌های کاربردی

Useful phrases
```

---

## Roadmap

* [x] RSS-based German news automation
* [x] Persian Telegram publishing
* [x] Daily German calendar post
* [x] Google Sheets-based German learning content
* [x] Daily sentence automation
* [x] Weekly dialog automation
* [ ] Add X/Twitter publishing
* [ ] Add Instagram publishing
* [ ] Add podcast script generation
* [ ] Add dashboard for article analytics
* [ ] Add Supabase/PostgreSQL storage
* [ ] Add Docker deployment
* [ ] Add automated error monitoring
* [ ] Add RAG-based archive search

---

## Design Decisions

### Why n8n?

n8n was selected because it allows fast integration between APIs, RSS feeds, LLM providers, Google Sheets, and Telegram while still supporting custom JavaScript logic.

### Why Google Sheets?

Google Sheets works as a simple lightweight CMS for educational content.
It allows easy editing of sentences and dialogs without changing the workflow itself.

### Why Telegram?

Telegram is well suited for Persian-speaking audiences and supports rich media posts, captions, inline links, and automated channel publishing.

### Why Modular Workflows?

The project is split into independent workflows so that news automation, calendar posts, and language-learning posts can be maintained separately.

---

## Author

**Seyedali Saghaei**
Development Engineer | Software Engineering | AI Automation | n8n | LLM Workflows

---

## License

This project is licensed under the terms defined in the `LICENSE` file.
