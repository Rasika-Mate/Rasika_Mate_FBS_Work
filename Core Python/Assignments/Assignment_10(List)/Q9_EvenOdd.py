# 9. WAP of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.

n = int(input("Enter the number of elements in the list: "))
li = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    li += [num]

even_list = []
odd_list = []

for num in li:
    if num % 2 == 0:
        even_list += [num]
    else:
        odd_list += [num]

print("Original list:", li)
print("Even elements list:", even_list)
print("Odd elements list:", odd_list)