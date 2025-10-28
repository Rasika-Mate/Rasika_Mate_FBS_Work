# 13. Python Program to count number of digits and letters in a string.

string = input("Enter a string: ")
letters = 0
digits = 0

for char in string:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
print("Number of letters:", letters)
print("Number of digits:", digits)