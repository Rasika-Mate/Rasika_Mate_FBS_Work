# 6. Python Program to Find the Union of two Lists

list1 = [1, 2, 3]
list2 = [3, 4, 5, 6]

union_list = list1[:]   # Start with all elements of list1

for item in list2:  # Add elements from list2 if not already in union_list
    if item not in union_list:
        union_list += [item]  # add element
print("Union of the two lists:", union_list)