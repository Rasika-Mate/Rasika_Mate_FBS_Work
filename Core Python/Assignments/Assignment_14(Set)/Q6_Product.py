# 6. WAP to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

nums = [2, 3, 5, 7, 1, 9, 4]
unique = set(nums)
max_product = 0
pair = ()

for a in unique:
    for b in unique:
        if a != b:
            if a * b > max_product:
                max_product = a * b
                pair = (a, b)

print("Numbers:", nums)
print("Pair with maximum product:", pair)
print("Maximum Product:", max_product)