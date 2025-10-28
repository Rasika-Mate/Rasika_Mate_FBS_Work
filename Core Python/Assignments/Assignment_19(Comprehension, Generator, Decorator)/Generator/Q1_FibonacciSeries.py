# 1. We want to generate Fibonacci numbers up to a certain limit. Instead of computing and storing the entire sequence in memory, create generator to yield Fibonacci numbers one by one, conserving memory and allowing for easy iteration.

def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

n = int(input("Enter the limit for Fibonacci sequence: "))
for num in fibonacci(n):
    print(num, end=" ")