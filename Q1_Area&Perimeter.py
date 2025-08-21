# 1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:)
# Formula: Area of Rectangle= l*b, Area of Semi_Circle= 0.5*3.14*r*r
# Perimeter of Rectangle= 2(l+b), Perimeter of Circle= 2*3.14*r

l = int(input("Enter Length: "))
b = int(input("Enter Breadth: "))
r = int(input("Enter Radius: "))

area_rec = l*b
area_semicir = 0.5*3.14*r*r
total_area = area_rec+area_semicir
peri = 2*(l+b)+(3.14*r)
print("Total area is",total_area)
print("Perimeter is",peri)