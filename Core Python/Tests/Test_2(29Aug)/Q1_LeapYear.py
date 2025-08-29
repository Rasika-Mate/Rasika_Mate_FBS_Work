# 1. WAP to accept year from user and check if it is a Leap Year or not

year = int(input("Enter Year: "))

if(year%4==0):
    print("It is a Leap year!")
    if(year%100==0):
        print("It is a Leap year!")
        if(year%400==0):
            print("It is a Leap year!")
else:
    print("It is not a Leap year")