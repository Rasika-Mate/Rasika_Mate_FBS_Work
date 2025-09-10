# 2. WAP to print all odd numbers until n.

# Method 1- While Loop
n = int(input("Enter Number: "))
i = 1
while i <= n:
    print(i)
    i+=2

# Method 2- For Loop
n = int(input("Enter Number: "))
for i in range(1, n+1, 2):  
    print(i, end=" ")