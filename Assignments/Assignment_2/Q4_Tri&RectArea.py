# 4. WAP to calculate area of triangle and rectangle
# Formula: Traingle= 1/2(b*h), Rectangle= l*b

heigth = float(input("Enter Height for Triangle: "))
base = float(input("Enter Base for Triangle: "))
area_t = ((1/2)*(base*heigth))
print("Area of Triangle is", area_t)

length = float(input("Enter Length for Reactangle: "))
breadth = float(input("Enter Breadth for Reactangle: "))
area_r = length*breadth
print("Area of Rectangle is", area_r)