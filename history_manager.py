import json
from datetime import datetime

HISTORY_FILE = "data/history.json"

def save_history(email, subject, status):
    try:
        with open(HISTORY_FILE, 'r') as file:
            history = json.load(file)
    except:
        history = []

    history.append({
        "email": email,
        "subject": subject,
        "status": status,
        "timestamp": str(datetime.now())
    })

    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file, indent=4)


def view_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            history = json.load(file)
            if not history:
                print("No history found.")
            for record in history:
                print(record)
    except Exception as e:
        print("Error reading history:", e)