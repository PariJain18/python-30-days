def even_generator(limit):
    for num in range(0, limit + 1, 2):
        yield num


for number in even_generator(10):
    print(number)