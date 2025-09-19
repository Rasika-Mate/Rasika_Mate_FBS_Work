# 3. WAP to find the second largest element in the list.

li = [10, 20, 30, 40, 50]
max_no = li[0]
second_max = li[0]

for i in li:
    if i > max_no:
        second_max = max_no
        max_no = i
    elif i > second_max and i != max_no:
        second_max = i

print("Second largest element:", second_max)