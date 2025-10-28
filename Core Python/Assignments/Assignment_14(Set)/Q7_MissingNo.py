# 7. Given two sets of numbers, WAP to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

missing_in_set2 = set1 - set2   # items in set1 but not in set2
missing_in_set1 = set2 - set1   # items in set2 but not in set1

print("Set 1:", set1)
print("Set 2:", set2)
print("Missing in Set 2:", missing_in_set2)
print("Missing in Set 1:", missing_in_set1)