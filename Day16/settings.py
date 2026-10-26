import json

settings = {
    "name": "Pari",
    "language": "Python",
    "theme": "dark"
}

with open("settings.json", "w") as file:
    json.dump(settings, file)

with open("settings.json", "r") as file:
    data = json.load(file)

print("Settings:", data)