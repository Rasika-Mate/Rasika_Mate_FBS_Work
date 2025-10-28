# 2. Python Program to Remove the nth Index Character from a Non-Empty String

string = input("Enter a string: ")
n = int(input("Enter the index (n) of the character to remove: "))

# Check if index is valid
if n < 0 or n >= len(string):
    print("Invalid index!")
else:
    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]
    print("String after removing character at index", n, ":", new_string)