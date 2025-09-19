# 4. WAP to find sum of n numbers using recursion.

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1) 

n = int(input("Enter Number: "))
total = sum_n(n)
print(f"Sum of first {n} numbers is: {total}")