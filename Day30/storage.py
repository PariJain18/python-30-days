import json
import os

FILE_NAME = "habits.json"


def load_habits():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_habits(habits):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(habits, file, indent=4)
    except OSError:
        print("Error saving habits!")