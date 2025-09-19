# 2. WAP to find maximum and minimum element in a list.

li = [10, 20, 30, 40, 50]
max_no = li[0]
min_no = li[0]

for i in li:
    if i > max_no:
        max_no = i
    if i < min_no:
        min_no = i

print("Maximum Number:", max_no)
print("Minimum Number:", min_no)