# 4. Sum of all odd numbers between 1 to n

def sum_odd(n):
    total = 0
    for i in range(1, n+1, 2):  
        total += i
    return total

n = int(input("Enter Number: "))
print("Sum of odd numbers:", sum_odd(n))