from datetime import datetime

def log_change(change_type, file_path, log_file="logs/changes.log"):
    """Logs a detected change into the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {change_type}: {file_path}\n"
    with open(log_file, "a") as f:
        f.write(entry)
