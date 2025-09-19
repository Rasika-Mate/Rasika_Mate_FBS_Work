# 10. WAP to check if entered year is a leap year or not.

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

y = int(input("Enter Year: "))
if is_leap_year(y):
    print(y, "is a Leap Year")
else:
    print(y, "is Not a Leap Year")