# 12. WAP to create three lists of numbers, their squares and cubes

n = int(input("Enter number of elements: "))

numbers = []
squares = []
cubes = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers += [num]
    squares += [num * num]
    cubes += [num * num * num]

print("Numbers list:", numbers)
print("Squares list:", squares)
print("Cubes list:", cubes)