# Jarvis CLI - Command Line Personal Assistant

A powerful CLI-based personal AI assistant that runs in your terminal. Privacy-first, local-only, and designed for developers.

## Features

- 🖥️ **Terminal-First** - Full control from your command line
- 🤖 **Local LLM** - Connects to Ollama for AI responses
- 📝 **Task Management** - Create, list, and manage tasks
- 📅 **Quick Events** - Fast calendar event creation
- 🔍 **File Search** - Search files from CLI
- 🎯 **Productivity** - Designed for developers

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Start Jarvis CLI
python jarvis.py

# Or use individual commands
python jarvis.py task add "Buy groceries"
python jarvis.py task list
python jarvis.py event "Meeting at 3pm"
python jarvis.py search "document"
python jarvis.py chat "Hello Jarvis"
```

## Commands

- `task add <title>` - Add a new task
- `task list` - List all tasks
- `task done <id>` - Mark task as complete
- `event <title>` - Quick event creation
- `search <query>` - Search files
- `chat <message>` - Chat with Jarvis
- `help` - Show help message

## Requirements

- Python 3.9+
- Ollama (optional, for AI features)

## License

MIT
