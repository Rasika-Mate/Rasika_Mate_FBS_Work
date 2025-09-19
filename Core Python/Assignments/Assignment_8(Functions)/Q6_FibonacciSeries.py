# 6. WAP to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacciSeries(num):
    a = 1
    b = 0
    for i in range(num):
        c = a + b
        print(c, end=' ')
        a,b = b,c
num = int(input("How many Fibonacci numbers you want?: "))
fibonacciSeries(num)