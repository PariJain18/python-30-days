class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1


e1 = Employee("Pari")
e2 = Employee("Riya")
e3 = Employee("Priya")

print("Employee 1:", e1.name)
print("Employee 2:", e2.name)
print("Employee 3:", e3.name)

print("Total Employees:", Employee.total_employees)