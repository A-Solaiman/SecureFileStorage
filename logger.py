import os
from datetime import datetime

LOG_FILE = "actions.log"

def log_action(username, action_type, file_name):
    """Logs an action to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | User: {username} | Action: {action_type} | File: {file_name}\n"

    # Append the log entry to the log file
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

    return f"Action logged: {log_entry.strip()}"

def view_logs():
    """Displays the log file content."""
    if not os.path.exists(LOG_FILE):
        return "No logs available."

    with open(LOG_FILE, "r") as log_file:
        return log_file.read()
