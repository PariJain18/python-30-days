from dataclasses import dataclass

@dataclass
class Rectangle:
    length: int
    width: int

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r1 = Rectangle(10, 5)

print("Length:", r1.length)
print("Width:", r1.width)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())