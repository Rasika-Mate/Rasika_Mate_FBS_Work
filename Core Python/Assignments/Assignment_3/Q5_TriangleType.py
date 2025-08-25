# 5. WAP to check whether the triangle is Equilateral, Isosceles or Scalene triangle.
# Equilateral- All three sides are equal
# Isosceles- Any two sides are equal
# Scalene- All three sides are different (s1!=s2, s1!=s3, s2!=s3)

s1 = int(input("Enter First side: "))
s2 = int(input("Enter Second side: "))
s3 = int(input("Enter Third side: "))

if(s1==s2==s3):
    print("It is Euqilateral Triangle")

elif(s1==s2 or s1==s3 or s2==s3):
    print("It is Isosceles Triangle")

else:
    print("It is Scalene Triangle")