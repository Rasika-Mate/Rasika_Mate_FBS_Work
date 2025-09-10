# 4. WAP to print factorial of a number.abs

num = int(input("Enter Number: "))
i = 1
fact = 1
while(i <= num):
    fact *= i
    i += 1
print("Factorial Number: ", fact)