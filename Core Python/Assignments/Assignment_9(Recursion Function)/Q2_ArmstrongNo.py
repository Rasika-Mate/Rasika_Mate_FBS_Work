# 2. WAP to check if given number is Armstrong or not using recursive function.

def digit_cnt(num):
    if num == 0:
        return 0
    return 1 + digit_cnt(num // 10)

def sum_of_power(num, cnt):
    if num == 0:
        return 0
    rem = num % 10
    return (rem ** cnt) + sum_of_power(num // 10, cnt)

def is_armstrong(num):
    cnt = digit_cnt(num)
    s = sum_of_power(num, cnt)
    if s == num:
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is not an Armstrong Number")

num = int(input("Enter Number: "))
is_armstrong(num)