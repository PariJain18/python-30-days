class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }


p1 = Product("Headphones", 500, 5)
p1.display()