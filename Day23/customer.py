from cart import Cart


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = Cart()

    def display_customer(self):
        print("Customer:", self.name)
        print("Email:", self.email)

    def checkout(self):
        print("Customer:", self.name)
        self.cart.checkout()