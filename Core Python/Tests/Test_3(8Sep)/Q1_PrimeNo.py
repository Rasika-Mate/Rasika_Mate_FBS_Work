# 1. WAP to print first n prime numbers

n = int(input("Enter how many prime numbers you want: "))
count = 0            
num = 2

for num in range(2, 1000):  
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
        if count == n:  
            break