products = [
    {"name": "Laptop", "price": 50000, "category": "Electronics", "stock": 5},
    {"name": "Mouse", "price": 500, "category": "Electronics", "stock": 10},
    {"name": "Keyboard", "price":1000, "category": "Electronics", "stock": 0},
    {"name": "Shirt", "price": 800, "category": "Clothing", "stock": 8},
    {"name": "Jeans", "price": 1500, "category": "Clothing", "stock": 4},
    {"name": "Shoes", "price": 2000, "category": "Footwear", "stock": 0},
    {"name": "Book", "price": 300, "category": "Stationery", "stock": 15},
    {"name": "Pen", "price": 20, "category": "Stationery", "stock": 50}
]

print("NAME\tPRICE\tCATEGORY\tSTOCK")

for product in products:
    print(
        product["name"],
        product["price"],
        product["category"],
        product["stock"],
        sep="\t"
    )


category = input("\nEnter category: ")

for product in products:
    if product["category"]== category:
        print(product)


sorted_products = sorted(products, key=lambda x: x["price"])

print("\nProducts sorted by price:")

for product in sorted_products:
    print(product["name"], product["price"])


print("\nOut of stock products:")

for product in products:
    if product["stock"] == 0:
        print(product["name"])

total = 0

for product in products:
    total = total + product["price"] * product["stock"]

print("\nTotal inventory value:", total)