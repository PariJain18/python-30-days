student={
    "Aman":{"Math": 80, "Python": 90, "English":70},
    "Riya":{"Math": 75, "Python": 85, "English":80},
    "Siya":{"Math": 90, "Python": 95, "English":85}
}
for name,marks in student.items():

    total=sum(marks.values())
    count=len(marks)
    average= total /count
    print(name,"Average:",average)