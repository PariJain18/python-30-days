def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def fibonacci(n):
    series = []
    a = 0
    b = 1
    for i in range(n):
        series.append(a)
        temp = a + b
        a = b
        b = temp
    return series


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a