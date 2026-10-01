numbers=input("Enter number:").split()
unique_numbers=[]
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
        print("Original list:",numbers)
        print("Unique list:",unique_numbers) 