# 4. WAP to calculate the total cost of painting. The interior of building with four equal sized walls

length = float(input("Enter Length for wall: "))
height = float(input("Enter Height for wall: "))
cost = int(input("Enter Cost for per Sq: "))

area = 4*length*height
print("Total cost of painting is ", area*cost)