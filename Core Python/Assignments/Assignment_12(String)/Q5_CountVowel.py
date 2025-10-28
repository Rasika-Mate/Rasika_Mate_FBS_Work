# 5. Python Program to Count the Number of Vowels in a String

string = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)