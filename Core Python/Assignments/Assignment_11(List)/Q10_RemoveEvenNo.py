# 10. WAP to print list after removing even numbers.

n = int(input("Enter the number of elements in the list: "))
lst = []

print("Enter the elements:")
for _ in range(n):
    lst.append(int(input()))

odd_list = []
for num in lst:
    if num % 2 != 0:
        odd_list += [num]  # add odd number to new list

print("List after removing even numbers:", odd_list)