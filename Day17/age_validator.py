class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age!")

    print("Valid age")

except ValueError:
    print("Please enter a valid number.")

except InvalidAgeError as e:
    print(e)