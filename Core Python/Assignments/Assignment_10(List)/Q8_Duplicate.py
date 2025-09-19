# 8. WAP to create a duplicate of an existing list. It should not point to same list.

li = [10, 20, 30, 40, 50]

duplicate_list = []

for item in li:
    duplicate_list += [item]  

print("Original list:", li)
print("Duplicate list:", duplicate_list)