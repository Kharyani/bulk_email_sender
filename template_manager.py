import json

def load_templates(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error loading templates:", e)
        return {}

def apply_template(template, data):
    try:
        return template.format(**data)
    except KeyError as e:
        return f"Missing field: {e}"