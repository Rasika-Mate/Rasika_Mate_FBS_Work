# 7. Python Program to Find the Intersection of Two Lists

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

intersection = [i for i in list1 if i in list2] # Find intersection using list comprehension

print("List 1:", list1)
print("List 2:", list2)
print("Intersection of Two Lists:", intersection)