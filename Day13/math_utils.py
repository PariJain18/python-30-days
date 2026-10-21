
    # prime 
def is_prime(n):
    
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

    # factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

    # fibonacci
def fibonacci(n):
    series = []
    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        temp= a + b
        a=b
        b=temp

    return series

    # greatest common divisor 
def gcd(a, b):
 
    while b != 0:
        remaindar=a % b
        a=b
        b=remaindar
    return a


print(is_prime(7))
print(factorial(5))
print(fibonacci(13))
print(gcd(12, 18))
