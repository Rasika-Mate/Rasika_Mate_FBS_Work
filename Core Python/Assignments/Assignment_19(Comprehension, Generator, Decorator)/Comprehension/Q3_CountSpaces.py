# 3. Count the number of spaces in a string (take input from user)

text = input("Enter a string: ")

space_count = len([ch for ch in text if ch == ' '])

print("Number of spaces in the string:", space_count)