# Identity: Check if two variables are actually same object in memory

# 1. is
x = 10
y = 20
z = 10
l1 = [1,2,3] 
l2 = [1,2,3]
print(x is y)
print(x is z)
print(l1 is l2) # same values but diff memory

# 2. is not
print(x is not y)
print(x is not z)
print(l1 is not l2)