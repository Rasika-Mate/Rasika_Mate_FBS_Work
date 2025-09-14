for i in range(5):
    # print spaces
    for j in range(5 - i - 1):
        print(" ", end=" ")
    # print stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()  