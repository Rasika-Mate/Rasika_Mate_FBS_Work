# 8. WAP find reverse of a number

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = int(input("Enter a Number: "))
print("Reverse of Number:", reverse_number(n))