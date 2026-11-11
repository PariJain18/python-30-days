class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount


m1 = Money(500)
m2 = Money(300)
m3 = Money(500)

result = m1 + m2

print("Total Money:", result.amount)
print(m1 == m2)
print(m1 == m3)