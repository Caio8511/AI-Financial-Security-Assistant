from datetime import datetime

LOG_FILE = "logs/security.log"

def save_log(level, message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{now}] {level.upper()} - {message}\n")