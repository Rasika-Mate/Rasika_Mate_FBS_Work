# 2. Find all of the numbers from 1–1000 that have a 6 in them

numbers = [x for x in range(1, 1001) if '6' in str(x)]

print("Numbers from 1 to 1000 that contain the digit 6 are:", numbers)