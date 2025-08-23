# 8. WAP to swap two numbers using third variable.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before Swapping")
print("First Number=",num1)
print("Second Number=",num2)

temp = num1 # Third Variable 
num1 = num2
num2 = temp

print("\nAfter Swapping")
print("First Number=",num1)
print("Second Number=",num2)
