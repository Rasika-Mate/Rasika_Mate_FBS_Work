# 1. WAP to print all even numbers until n.

# Method 1- While Loop
n = int(input("Enter Number: "))
i = 2
while i <= n:
    print(i)
    i+=2

# Method 2- For Loop
n = int(input("Enter Number: "))
for i in range(2, n+1, 2):  
    print(i, end=" ")