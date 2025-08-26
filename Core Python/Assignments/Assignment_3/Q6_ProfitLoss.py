# 6. WAP to calculate profit or loss.

sp = int(input("Enter Selling Price: "))
cp = int(input("Enter Cost Price: "))

# Method 1
if(sp > cp):
    print("Profit")
else:
    print("Loss")

# Method 2
if sp > cp:
    profit = sp - cp
    print("Profit: ", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss: ", loss)
else:
    print("No Profit, No Loss")
