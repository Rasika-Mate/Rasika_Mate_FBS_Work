# 2. WAP to accept 3 digit number. if 1st digit is double of second digit and half of 3rd digit then display "Yes you have done it!", otherwise display "Please try next time!".

num = int(input("Enter 3-digit Number: "))

first = num//100
second = (num//10)%10
third = num%10

if(first==2*second and first==third/2):
    print()
else:
    print("Please try next time!")