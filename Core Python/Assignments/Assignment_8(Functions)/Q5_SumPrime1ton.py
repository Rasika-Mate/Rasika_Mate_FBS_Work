# 5. Sum of all prime numbers between 1 to n

def is_prime(num):
    for i in range(2,num):
        sum = 0
        if(num%i==0):
            print(f"{num} is not a Prime Number")
        break
    else:
        sum += i
        print(f"{num} is a Prime Number")
num = int(input("Enter Number: "))
is_prime(num)