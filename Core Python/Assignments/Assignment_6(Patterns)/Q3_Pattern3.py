for i in range(4):
    print(" " * (4 - i), end="")
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1) 
    print() 