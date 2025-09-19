# 7. WAP to find sum of digits using recursion.

def sum_of_digits(num):
    if num == 0:
        return 0
    return (num % 10) + sum_of_digits(num // 10)

n = int(input("Enter a Number: "))
print("Sum of Digits:", sum_of_digits(n))