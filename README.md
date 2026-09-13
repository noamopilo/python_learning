# 🐍 Python Learning

A collection of small Python projects built while learning the language — a mix of games, automation scripts, and API-powered tools, based on tutorials and personal experiments.

## 📋 Table of Contents

- [About](#about)
- [Projects](#projects)
  - [🎮 Games](#-games)
  - [🛠️ Utilities & Automation](#️-utilities--automation)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Notes & Known Issues](#notes--known-issues)
- [Project Structure](#project-structure)

## About

This repo is a personal sandbox for learning Python. Each file is a self-contained mini-project, so you can jump straight to whichever script interests you without needing to understand the rest of the repo.

## Projects

### 🎮 Games

| File | Description |
|------|-------------|
| `dice_rolling_game.py` | Simulates rolling one or more dice. |
| `number_guessing_game.py` | Guess a randomly generated number with feedback (higher/lower). |
| `rock_paper-scissor.py` | Classic Rock–Paper–Scissors against the computer. |
| `snake.py` | The classic Snake game. |
| `word_guessing_game.py` | Hangman-style word guessing game. |
| `games/` | Additional in-progress game scripts. |

### 🛠️ Utilities & Automation

| File | Description | Key libraries |
|------|-------------|----------------|
| `email_sender.py` | Sends an email via Gmail's SMTP server, with the sender's password loaded from a `.env` file. | `smtplib`, `python-dotenv` |
| `ip_geolocator.py` | Looks up the geographic location of an IP address (country, city, timezone) and can display the country's flag. | `requests`, `Pillow`, `tkinter` |
| `link_shortner.py` | Shortens a URL and lets you set a custom alias using the cutt.ly API. | `requests` |
| `pdfmerger.py` | Merges every PDF found in a local `pdfs/` folder into a single PDF. | `PyPDF2` |
| `qr_code_generator.py` | Generates a QR code from text or a URL and saves it as a PNG. | `qrcode`, `Pillow` |
| `randpass.py` | Generates a random password. | — |
| `web-searcher.py` | Placeholder for a web search script (work in progress). | — |
| `ytdwnld.py` | Downloads a YouTube video in the highest available resolution. | `pytubefix` |

## Getting Started

### Prerequisites

- Python 3.9 or higher
- `pip` for installing dependencies

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/noamopilo/python_learning.git
   cd python_learning
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```

3. Install the dependencies used across the scripts:
   ```bash
   pip install requests Pillow qrcode PyPDF2 python-dotenv pytubefix
   ```
   > Not every script needs every library — check the table above to see which one(s) a specific script needs.

## Usage

Most scripts are meant to be run directly and will prompt you for input in the terminal:

```bash
python number_guessing_game.py
```

A few scripts take command-line arguments instead, for example:

```bash
python ytdwnld.py "https://www.youtube.com/watch?v=your-video-id"
```

Scripts that call an external API (`ip_geolocator.py`, `link_shortner.py`) currently need a valid API key to work — see the note below.

## Notes & Known Issues

This repo is a learning project, so a few things are still rough around the edges:

- **API keys**: `ip_geolocator.py` and `link_shortner.py` currently have API keys hardcoded in the file. For anything beyond personal experimentation, move these into a `.env` file (like `email_sender.py` already does) and load them with `python-dotenv` instead.
- **Hardcoded local paths**: `ytdwnld.py` (download folder) and `pdfmerger.py` (source PDF folder) point to specific local folder paths. Update these to match your own machine before running them.
- **`web-searcher.py`** is currently an empty placeholder for a future project.
- **`.env`** is committed to the repo as an example — replace its contents with your own secrets and make sure real credentials are never pushed.

## Project Structure

```
python_learning/
├── games/                      # Extra/in-progress game scripts
├── dice_rolling_game.py
├── email_sender.py
├── ip_geolocator.py
├── link_shortner.py
├── number_guessing_game.py
├── pdfmerger.py
├── qr_code_generator.py
├── randpass.py
├── rock_paper-scissor.py
├── snake.py
├── web-searcher.py
├── word_guessing_game.py
├── ytdwnld.py
├── .env
├── .gitignore
└── README.md
```

---

*A personal Python learning journey — new mini-projects are added as new concepts are explored.*
