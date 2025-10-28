# 2. Create a class Distance with data members as km,m and cm and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
        print("Constructor called...")

    def __del__(self):
        print("Destructor called...")

    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm
        return Distance(km, m, cm)

    def __sub__(self, other):
        km = self.km - other.km
        m = self.m - other.m
        cm = self.cm - other.cm
        return Distance(km, m, cm)

d1 = Distance(5, 300, 40)
d2 = Distance(3, 200, 30)

print("First Distance:", d1.km, "km", d1.m, "m", d1.cm, "cm")
print("Second Distance:", d2.km, "km", d2.m, "m", d2.cm, "cm")

add_result = d1 + d2
sub_result = d1 - d2

print("\nAfter Addition:", add_result.km, "km", add_result.m, "m", add_result.cm, "cm")
print("After Subtraction:", sub_result.km, "km", sub_result.m, "m", sub_result.cm, "cm")