from datetime import datetime
import os

def log_transaction(message):
    # Ensure logs are written inside "data/log.txt"
    log_path = os.path.join("data", "log.txt")

    # Create folder if it doesn’t exist (optional safety)
    os.makedirs("data", exist_ok=True)

    # Add timestamp and log message
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_path, "a") as log_file:
        log_file.write(log_entry)
