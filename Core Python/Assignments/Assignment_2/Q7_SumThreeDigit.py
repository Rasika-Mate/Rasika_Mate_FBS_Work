# 7. Find the sum of three-digit number.

num = int(input('Enter three digit number: '))
# 456
d1 = num % 10    # 456%10= 6
num = num // 10  # 456//10= 45

d2 = num % 10    # 45%10= 5
num = num // 10  # 45//10= 4

d3 = num % 10    # 4%10= 4
num = num // 10  # 4//10= 0
print(f'Digit 1: {d1}, Digit 2: {d2}, Digit 3: {d3}')

sum = d1+d2+d3
print("Sum of Three Digit number is", sum)
