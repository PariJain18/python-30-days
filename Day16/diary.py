from datetime import date

entry = input("Write your diary entry: ")

with open("diary.txt", "a") as file:
    file.write(str(date.today()) + " - " + entry + "\n")

print("Diary entry saved successfully!")

with open("diary.txt", "r") as file:
    print(file.read())