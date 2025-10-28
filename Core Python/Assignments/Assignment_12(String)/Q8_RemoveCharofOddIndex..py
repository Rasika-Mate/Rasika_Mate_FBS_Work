# 8. Python Program to Remove the Characters of Odd Index Values in a String

string = input("Enter a string: ")

new_string = string[::2] # Keep only characters at even indices

print("String after removing odd-index characters:", new_string)