for i in range(5):
    # print spaces
    for j in range(5 - i - 1):
        print("  ", end="")  
    # print numbers
    num = 1
    for j in range(2 * i + 1):
        print(num, end=" ")
        num += 1
    print() 
