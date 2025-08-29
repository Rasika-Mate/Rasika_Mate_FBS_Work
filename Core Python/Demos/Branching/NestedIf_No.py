num = int(input("Enter Number: "))
if(num >= 0):
    if(num > 50):
        if(num > 100):
            print(f"{num} is greater than 100")
        else:
            print(f"{num} is in 51-100 category")
    else:
        print(f"{num} is in 0-50 category")
else: 
    print(f"{num} is less than 0")