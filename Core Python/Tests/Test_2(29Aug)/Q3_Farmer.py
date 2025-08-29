# 3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle length is 50m and breadth is 40.. If cost of barbed wire is 35Rs/m then calculate total cost of fencing the field

l = 50
b = 40
r = 20
cost = 35
times = 5

perimeter = (2*l)+b+(3.14*r)
total_length = perimeter*times
total_cost = total_length*cost
print(f"Total cost of fencing {total_cost} Rs")