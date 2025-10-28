# 1. Find all of the numbers from 1–1000 that are divisible by 8

numbers = [x for x in range(1, 1001) if x % 8 == 0]

print("Numbers divisible by 8 from 1-1000 are:", numbers)