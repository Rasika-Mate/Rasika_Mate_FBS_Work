# 3. Python Program to Sort the List According to the Second Element in Sublist

lst = [[1, 5], [3, 2], [4, 8], [2, 1]]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i][1] > lst[j][1]:
            lst[i], lst[j] = lst[j], lst[i]  # swap

print("Sorted list based on second element:", lst)