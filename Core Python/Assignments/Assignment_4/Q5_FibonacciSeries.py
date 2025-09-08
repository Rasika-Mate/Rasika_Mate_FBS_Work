# 5. WAP to print Fibonacci series upto n.

num = int(input("How many Fibonacci numbers you want?: "))
a = -1
b = 1
for i in range(num):
    c = a+b
    print(c, end=' ')
    a = b
    b = c
    # a,b = b,c