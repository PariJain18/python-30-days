import json
from product import Product
from customer import Customer


# Create Products
p1 = Product("Headphones", 500, 5)
p2 = Product("Bag", 800, 3)

products = [p1, p2]


# Create Customer
customer = Customer("Pari", "pari@gmail.com")


# Add Products to Cart
customer.cart.add_product(p1)
customer.cart.add_product(p2)


# Display Customer Details
customer.display_customer()


# Display Cart
print("\nMy Cart:")
customer.cart.show_cart()


# Calculate Total Price
print("\nTotal Price:", customer.cart.total_price())


# Save Data in JSON
def save_data(products, customer):
    data = {
        "products": [p.to_dict() for p in products],
        "customer": {
            "name": customer.name,
            "email": customer.email,
            "cart": [p.name for p in customer.cart.items]
        }
    }

    with open("shop_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")


# Load Data from JSON
def load_data():
    try:
        with open("shop_data.json", "r") as file:
            data = json.load(file)

        print("Data loaded successfully!")
        return data

    except FileNotFoundError:
        print("No saved data found")
        return None


# Save Shopping Data
save_data(products, customer)


# Checkout
customer.checkout()


# Save Updated Stock
save_data(products, customer)


# Load Saved Data
saved_data = load_data()

print(saved_data)