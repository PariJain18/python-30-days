import pytest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square(n):
    return n * n


def cube(n):
    return n * n * n


def is_even(n):
    return n % 2 == 0


def factorial(n):
    if n < 0:
        raise ValueError("Negative number not allowed")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def maximum(a, b):
    return max(a, b)


def minimum(a, b):
    return min(a, b)


# 10 Pytest Tests


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5


def test_square():
    assert square(4) == 16


def test_cube():
    assert cube(3) == 27


def test_is_even():
    assert is_even(8) == True


def test_factorial():
    assert factorial(5) == 120


def test_maximum():
    assert maximum(10, 20) == 20


def test_minimum():
    assert minimum(10, 20) == 10


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
