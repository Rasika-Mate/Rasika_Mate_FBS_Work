# 9. WAP to create three lists of numbers, their squares and cubes

n = int(input("Enter the number of elements: "))

numbers = []
squares = []
cubes = []

for i in range(1, n+1):
    numbers += [i]
    squares += [i**2]
    cubes += [i**3]

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)