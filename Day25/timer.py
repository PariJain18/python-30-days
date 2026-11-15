import time

def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print("Time taken:", end - start, "seconds")

    return wrapper


@timer
def say_hello():
    print("Hello Python!")


say_hello()