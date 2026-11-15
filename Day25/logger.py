def logger(func):
    def wrapper(*args, **kwargs):
        print("Function called:", func.__name__)
        print("Arguments:", args)

        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    print("Result:", a + b)


add(10, 20)