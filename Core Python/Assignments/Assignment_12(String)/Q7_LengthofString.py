# 7. Python Program to Calculate the Length of a String Without Using a Library Function

string = input("Enter a string: ")
count = 0

for char in string:
    count += 1
print("Length of the string:", count)