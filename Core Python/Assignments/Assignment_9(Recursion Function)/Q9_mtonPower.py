# 9. WAP to calculate the m to the power n using recursion.

def power(m, n):
    if n == 0: 
        return 1
    elif n > 0:
        return m * power(m, n - 1)  # Recursive case for positive power
    else:
        return 1 / power(m, -n)     # Handle negative powers

m = float(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))

result = power(m, n)
print(f"{m}^{n} = {result}")