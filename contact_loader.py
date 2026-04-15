import csv
import json

def load_csv(file_path):
    contacts = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except Exception as e:
        print("Error loading CSV:", e)
    return contacts


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error loading JSON:", e)
        return []