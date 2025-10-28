# 2. WAP to remove the intersection of a second set with a first set.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}

inter = set1.difference_update(set2)
print("Set-1 after removing intersection with Set-2:",set1)