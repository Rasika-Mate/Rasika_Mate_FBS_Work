rows=5
for i in range(1, rows + 1):
        for j in range(rows - i):
            print("  ", end="")
       
        for k in range(i,i*2):
            print(k, end=" ")
           
        for l in range(2*i - 2, i - 1, -1):
            print(l, end=" ")
        print()