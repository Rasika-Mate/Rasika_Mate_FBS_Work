# WAP to input all sides of a triangle and check whether triangle is valid or not.
# Triangle Inequality Theorem: if sum of any two sides is greater than the third side then Valid Triangle.

s1 = float(input("Enter First side: "))
s2 = float(input("Enter Second side: "))
s3 = float(input("Enter Third side: "))

if(s1+s2>s3 and s1+s3>s2 and s3+s2>s1):
    print("It is Valid Triangle")
else:

    print("Not Valid Triangle.")
