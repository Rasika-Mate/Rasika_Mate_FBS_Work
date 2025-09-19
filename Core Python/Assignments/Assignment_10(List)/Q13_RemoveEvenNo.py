# 13 . WAP to print list after removing even numbers.

n = int(input("Enter number of elements in the list: "))

li = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    li += [num]

even_list = []
for num in li:
    if num % 2 != 0:  
        even_list += [num]

print("List after removing even numbers:", even_list)