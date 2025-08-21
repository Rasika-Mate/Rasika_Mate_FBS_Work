# WAP to input two angles from user and find third angle of the triangle.
# Formula: angle1+angle2+angle3 = 180

a1 = int(input('Enter First angle: '))
a2 = int(input('Enter Second angle: '))

a3= 180-(a1+a2)
print("Third Angle is",a3)