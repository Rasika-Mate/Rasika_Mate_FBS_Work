# 1. WAP to Put Even and Odd elements of a List into two Different Lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
odd_list = []

for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Original List:", numbers)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)