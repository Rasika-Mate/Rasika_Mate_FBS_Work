# 3. WAP to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# a. 1+ 2 + 3 + 4+..... + n
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter Number: "))
print("Sum:", sum_natural(n))


# b. 1!+ 2! + 3! + 4!+..... + n!
def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

def sum_factorials(n):
    total = 0
    for i in range(1, n+1):
        total += factorial(i)
    return total

n = int(input("Enter Number: "))
print("Sum of Factorials:", sum_factorials(n))


# c. 1^1 + 2^2 + 3^3+ ...... n^n
def sum_powers(n):
    total = 0
    for i in range(1, n+1):
        total += i ** i
    return total

n = int(input("Enter Number: "))
print("Sum of Powers:", sum_powers(n))