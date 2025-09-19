# 1. WAP to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sum_of_factorials(n):
    if n == 0:
        return 0
    return factorial(n) + sum_of_factorials(n - 1)
n=int(input("Enter number: "))
print(sum_of_factorials(n))