# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

numbers = [x for x in range(1, 1001) if any(x % d == 0 for d in range(2, 10))]

print("Numbers divisible by any single digit (2–9):", numbers)