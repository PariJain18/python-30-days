class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display(self):
        super().display()
        print("Course:", self.course)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print("Subject:", self.subject)


student1 = Student("Pari", 20, "BCA")
teacher1 = Teacher("Riya", 30, "Python")

print("Student Details:")
student1.display()

print("\nTeacher Details:")
teacher1.display()