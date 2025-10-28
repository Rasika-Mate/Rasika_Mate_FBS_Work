# 11. Python Program to replace every blank space with hyphen in a string.

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch == " ":
        result += "-"
    else:
        result += ch

print("String after replacing spaces with hyphens:")
print(result)