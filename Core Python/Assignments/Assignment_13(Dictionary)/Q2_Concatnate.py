# 2. Python Program to Concatenate Two Dictionaries Into One

dic1 = {'name': 'Rasika', 'age': 22}
dic2 = {'course': 'B.Tech', 'college': 'PCCoE'}

# Method 1 (Python 3.9+): Using | operator
dic3 = dic1 | dic2
print("Concatenated Dictionary:", dic3)

# Method 2
# dic3 = dic1.copy()  # Create a copy so original dic1 is not changed
# dic3.update(dic2)
# print("Concatenated Dictionary:", dic3)