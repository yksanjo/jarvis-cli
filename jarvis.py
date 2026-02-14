#!/usr/bin/env python3
"""
Jarvis CLI - Command Line Personal Assistant
"""

import sys
import json
import os
from datetime import datetime
from typing import List, Dict, Any

# Data storage file
DATA_FILE = os.path.expanduser("~/.jarvis_cli_data.json")

class JarvisCLI:
    def __init__(self):
        self.data = self.load_data()
    
    def load_data(self) -> Dict[str, Any]:
        """Load data from JSON file"""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {"tasks": [], "events": []}
    
    def save_data(self):
        """Save data to JSON file"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def print_header(self):
        """Print Jarvis header"""
        print("\n🤖 Jarvis CLI - Your Personal Assistant")
        print("=" * 40)
    
    def cmd_task(self, args: List[str]):
        """Task management commands"""
        if not args:
            self.task_list()
            return
        
        subcmd = args[0]
        
        if subcmd == "add":
            title = " ".join(args[1:])
            task = {
                "id": len(self.data["tasks"]) + 1,
                "title": title,
                "status": "pending",
                "created": datetime.now().isoformat()
            }
            self.data["tasks"].append(task)
            self.save_data()
            print(f"✅ Task added: {title}")
        
        elif subcmd == "list":
            self.task_list()
        
        elif subcmd == "done":
            if len(args) < 2:
                print("Usage: task done <id>")
                return
            task_id = int(args[1])
            for task in self.data["tasks"]:
                if task["id"] == task_id:
                    task["status"] = "completed"
                    task["completed"] = datetime.now().isoformat()
                    self.save_data()
                    print(f"✅ Task {task_id} marked as done!")
                    return
            print(f"❌ Task {task_id} not found")
        
        elif subcmd == "delete":
            if len(args) < 2:
                print("Usage: task delete <id>")
                return
            task_id = int(args[1])
            self.data["tasks"] = [t for t in self.data["tasks"] if t["id"] != task_id]
            self.save_data()
            print(f"🗑️ Task {task_id} deleted")
        
        else:
            print(f"Unknown task command: {subcmd}")
            print("Usage: task <add|list|done|delete>")
    
    def task_list(self):
        """List all tasks"""
        tasks = self.data["tasks"]
        if not tasks:
            print("📋 No tasks found")
            return
        
        print("\n📋 Tasks:")
        for task in tasks:
            status_icon = "✅" if task["status"] == "completed" else "⬜"
            print(f"  {status_icon} [{task['id']}] {task['title']}")
    
    def cmd_event(self, args: List[str]):
        """Quick event creation"""
        if not args:
            print("Usage: event <title>")
            return
        
        title = " ".join(args)
        event = {
            "id": len(self.data["events"]) + 1,
            "title": title,
            "created": datetime.now().isoformat()
        }
        self.data["events"].append(event)
        self.save_data()
        print(f"📅 Event added: {title}")
    
    def cmd_events(self, args: List[str]):
        """List events"""
        events = self.data["events"]
        if not events:
            print("📅 No events found")
            return
        
        print("\n📅 Events:")
        for event in events:
            print(f"  [{event['id']}] {event['title']}")
    
    def cmd_search(self, args: List[str]):
        """File search (basic implementation)"""
        if not args:
            print("Usage: search <query>")
            return
        
        query = " ".join(args).lower()
        print(f"\n🔍 Searching for: {query}")
        print("Note: Full file search requires file indexing setup")
        print("This is a placeholder for the search functionality")
    
    def cmd_chat(self, args: List[str]):
        """Chat with Jarvis"""
        if not args:
            print("Usage: chat <message>")
            return
        
        message = " ".join(args)
        print(f"\n👤 You: {message}")
        
        # Simulated response (connect to Ollama in production)
        responses = [
            f"I understand: '{message}'. How can I help you with that?",
            f"Got it! You're asking about '{message}'.",
            f"I'm here to help! What would you like to do regarding '{message}'?",
        ]
        import random
        response = random.choice(responses)
        print(f"🤖 Jarvis: {response}")
    
    def cmd_stats(self, args: List[str]):
        """Show statistics"""
        tasks = self.data["tasks"]
        completed = sum(1 for t in tasks if t["status"] == "completed")
        pending = len(tasks) - completed
        
        print("\n📊 Statistics:")
        print(f"  Total Tasks: {len(tasks)}")
        print(f"  Completed: {completed}")
        print(f"  Pending: {pending}")
        print(f"  Events: {len(self.data['events'])}")
    
    def cmd_help(self, args: List[str]):
        """Show help"""
        help_text = """
🤖 Jarvis CLI Commands:
        
  task add <title>     Add a new task
  task list            List all tasks
  task done <id>       Mark task as complete
  task delete <id>     Delete a task
  
  event <title>        Quick event creation
  events               List all events
  
  search <query>       Search files
  chat <message>       Chat with Jarvis
  
  stats                Show statistics
  help                 Show this help
        """
        print(help_text)
    
    def run(self, args: List[str]):
        """Run Jarvis CLI"""
        if not args:
            self.print_header()
            self.cmd_help([])
            return
        
        cmd = args[0]
        
        if cmd == "task":
            self.cmd_task(args[1:])
        elif cmd == "event":
            self.cmd_event(args[1:])
        elif cmd == "events":
            self.cmd_events(args[1:])
        elif cmd == "search":
            self.cmd_search(args[1:])
        elif cmd == "chat":
            self.cmd_chat(args[1:])
        elif cmd == "stats":
            self.cmd_stats(args[1:])
        elif cmd == "help":
            self.cmd_help(args[1:])
        else:
            print(f"Unknown command: {cmd}")
            print("Type 'help' for available commands")

def main():
    jarvis = JarvisCLI()
    jarvis.run(sys.argv[1:])

if __name__ == "__main__":
    main()
