#  Recursive factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


#  Sum of a list
def list_sum(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + list_sum(numbers[1:])


#  String reverse
def reverse_string(text):
    if text == "":
        return text
    return reverse_string(text[1:]) + text[0]


print(factorial(5))
print(list_sum([10, 20, 30]))
print(reverse_string("hello"))