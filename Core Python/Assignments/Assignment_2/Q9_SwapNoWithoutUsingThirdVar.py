# 9. WAP to swap two numbers without using third variable.

# First Approach
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f'\nBefore Swapping - x: {x}, y:{y}')

x,y = y,x
print(f'After Swapping - x: {x}, y:{y}')


# Second Approach
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f'Before Swapping - num1: {num1}, num2:{num2}')

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f'After Swapping - num1: {num1}, num2:{num2}')


# Third Approch
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f'Before Swapping - num1: {num1}, num2:{num2}')

num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2
print(f'After Swapping - num1: {num1}, num2:{num2}')
