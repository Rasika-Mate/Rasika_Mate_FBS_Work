# 6. WAP to remove duplicates from the list.

li = [10, 20, 30, 20, 40, 10, 50]

unique_list = []

for i in li:
    found = False
    for j in unique_list:
        if i == j:
            found = True
            break
    if not found:
        unique_list.append(i)

print("List after removing duplicates:", unique_list)