# 2. WAP that takes a list of strings as input and returns a new list containing the uppercase versions of the strings using list comprehension.

words = input("Enter strings separated by space: ").split()

uppercase_words = [word.upper() for word in words]

print("Uppercase List:", uppercase_words)