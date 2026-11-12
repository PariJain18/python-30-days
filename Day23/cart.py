class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        count = self.items.count(product)

        if count < product.stock:
            self.items.append(product)
            print(product.name, "added to cart")
        else:
            print("Product is out of stock")

    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(product_name, "removed from cart")
                return

        print("Product not found")

    def show_cart(self):
        if not self.items:
            print("Cart is empty")
            return

        for product in self.items:
            print(product.name, "-", product.price)

    def total_price(self):
        total = 0

        for product in self.items:
            total += product.price

        return total

    def checkout(self):
        if not self.items:
            print("Cart is empty")
            return

        for product in self.items:
            product.stock -= 1

        print("Total Bill:", self.total_price())
        self.items.clear()
        print("Order placed successfully!")