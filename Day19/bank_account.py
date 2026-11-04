class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.amount = balance

    def deposit(self, money):
        self.amount += money
        print("Money deposited:", money)

    def withdraw(self, money):
        if money <= self.amount:
            self.amount -= money
            print("Money withdrawn:", money)
        else:
            print("Insufficient balance")

    def balance(self):
        return self.amount


b1 = BankAccount("Pari", 1000)

b1.deposit(500)
b1.withdraw(200)

print("Account Holder:", b1.name)
print("Current Balance:", b1.balance())