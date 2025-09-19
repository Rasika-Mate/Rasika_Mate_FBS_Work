# 11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.
# 153--->Digits=3--->1³ + 5³ + 3³ = 153, 370,371,1634

def digit_cnt(num):
    cnt = 0
    while(num!=0):
        num = num//10
        cnt += 1
    return cnt

def sum_of_power(num,cnt):
    sum = 0
    while(num!=0):
        rem = num%10
        sum = sum + (rem**cnt)
        num = num//10
    return sum

def is_armstrong(num):  #Calling Function
    cnt = digit_cnt(num)    #Called Function
    sum = sum_of_power(num,cnt)
    if sum == num:
        print(f'{num} is a Armstrong Number')
    else:
        print(f'{num} is not Armstrong Number')

num = int(input("Enter Number: "))
is_armstrong(num)