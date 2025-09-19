# 7. WAP to create a new list from existing list which contains cube of each number of list.

li = [1, 2, 3, 4, 5]

cube_list = []

for num in li:
    cube = num * num * num  
    cube_list += [cube]     

print("Original list:", li)
print("List of cubes:", cube_list)