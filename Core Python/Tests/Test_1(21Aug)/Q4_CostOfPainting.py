# 4. Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall.
# (Note: 1. Below diagram is of two joint rooms. 2. It is upper view of building.)

area = float(input("Enter area of one wall: "))
ci = float(input("Enter cost per sq.m for Interior: "))
ce = float(input("Enter cost per sq.m for Exterior: "))

# 8 interior walls
int_cost = 8*area*ci

# 7 exterior walls (1 common wall not painted)
ext_cost = 7*area*ce

print("Total Painting Cost is", int_cost + ext_cost)