# 4. Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall.
# (Note: 1. Below diagram is of two joint rooms. 2. It is upper view of building.)

interior_area = float(input("Enter the area of Interior walls: "))
interior_cost = float(input("Enter the Cost: "))
exterior_area = float(input("Enter the area of Exterior walls: "))
exterior_cost = float(input("Enter the Cost: "))

int_cost = interior_cost*interior_area
ext_cost = exterior_cost*exterior_area
painting_cost = int_cost+ext_cost
print("Cost of painting is",painting_cost)