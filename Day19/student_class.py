class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 80:
            return "A Grade"
        elif avg >= 60:
            return "B Grade"
        elif avg >= 40:
            return "C Grade"
        else:
            
            return "Fail"


s1 = Student("Pari", [80, 70, 90])

print("Name:", s1.name)
print("Average:", s1.average())
print("Grade:", s1.grade())