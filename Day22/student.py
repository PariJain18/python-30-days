class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, {self.marks})"


s1 = Student("Pari", 20, 85)

print(s1)
print(repr(s1))