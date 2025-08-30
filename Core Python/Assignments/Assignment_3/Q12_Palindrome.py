# 12. WAP to check if given 3 digit number is a palindrome or not.
# For a 3-digit number, only the first and last digit matter.

num = int(input('Enter three-digit Number: '))

first = num // 100  # first digit
last = num % 10  # last digit

if first == last:
    print(num, "is a Palindrome Number")
else:
    print(num, "is Not a Palindrome Number")
