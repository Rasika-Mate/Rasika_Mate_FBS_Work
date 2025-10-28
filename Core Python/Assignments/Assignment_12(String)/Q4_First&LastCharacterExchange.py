# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

string = input("Enter a string: ")

# Check if string length is at least 2
if len(string) <= 1:
    new_string = string
else:
    new_string = string[-1] + string[1:-1] + string[0]

print("String after exchanging first and last characters:", new_string)