# 15. Python Program to find larger string without using built-in functions.

str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

count1 = 0
for ch in str1:
    count1 += 1

count2 = 0
for ch in str2:
    count2 += 1

if count1 > count2:
    print("Larger string is:", str1)
elif count2 > count1:
    print("Larger string is:", str2)
else:
    print("Both strings are of equal length.")