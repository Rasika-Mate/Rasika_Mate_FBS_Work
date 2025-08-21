# 9. WAP to swap two numbers without using third variable.

# First Approach
x = 10
y = 20
print(f'Before Swapping - x: {x}, y:{y}')

x,y = y,x
print(f'After Swapping - x: {x}, y:{y}')
num1 = int(input("Enter No1 = "))
num2 = int(input("Enter No2 = "))

# Second Approach
print("Num1 =",num1)
print("Num2 =",num2)

print("# First Approch")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("Num1 =",num1)
print("Num2 =",num2)


# Third Approch
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print("Num1 =",num1)
print("Num2 =",num2)

