for i in range(1, 6):
    for j in range(i, 6):
        if(j == 5 or j == i or i==1):
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()