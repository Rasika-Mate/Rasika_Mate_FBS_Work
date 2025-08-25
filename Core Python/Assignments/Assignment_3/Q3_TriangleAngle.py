# 3. WAP to input angles of a triangle and check whether triangle is valid or not.
# Sum of angles must be 180°.

a1 = int(input("Enter First Angle: "))
a2 = int(input("Enter Second Angle: "))
a3 = int(input("Enter Third Angle: "))

if a1 > 0 and a2 > 0 and a3 > 0 and (a1 + a2 + a3 == 180):
    print("It is Valid Triangle")
else:
    print("Not Valid Triangle.")