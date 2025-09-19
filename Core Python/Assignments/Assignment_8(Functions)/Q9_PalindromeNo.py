# 9. WAP check if entered number is a palindrome or not.

def reverseNo(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

def checkPalindromeNo(num):
    if num == reverseNo(num):
        print(f"{num} is a Palindrome number")
    else:
        print(f"{num} is Not a Palindrome number")

n = int(input("Enter a number: "))
checkPalindromeNo(n)