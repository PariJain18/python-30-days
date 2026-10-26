import csv

students = [
    ["Name", "Marks"],
    ["Aman", 80],
    ["Riya", 90],
    ["Rahul", 70],
    ["Priya", 85],
    ["Neha", 75],
    ["Karan", 88],
    ["Simran", 92],
    ["Vikas", 65],
    ["Pooja", 78],
    ["Rohit", 82]
]

with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

total = 0
count = 0


with open("marks.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        total += int(row[1])
        count += 1

average = total / count

print("Average Marks:", average)