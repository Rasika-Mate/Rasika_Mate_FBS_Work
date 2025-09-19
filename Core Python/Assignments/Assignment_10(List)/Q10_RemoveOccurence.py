# 10. WAP to remove all occurrences of a given element in the list.

li = [10, 20, 30, 20, 40, 20, 50]
ele = int(input("Enter the element to remove: "))
new_list = []

for num in li:
    if num != ele:
        new_list += [num]

print("List after removing element", ele, ":", new_list)