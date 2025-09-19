# 7. WAP to find sum of digits of a number.

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

n = int(input("Enter a Number: "))
print("Sum of Digits:", sum_of_digits(n))