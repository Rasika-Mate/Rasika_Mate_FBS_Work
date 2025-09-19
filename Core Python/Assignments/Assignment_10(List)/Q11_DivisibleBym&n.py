# 11. WAP to print all numbers which are divisible by m and n in the list.

ele = int(input("Enter number of elements in the list: "))

li = []
for i in range(ele):
    num = int(input(f"Enter element {i+1}: "))
    li += [num]  

m = int(input("Enter first divisor (m): "))
n = int(input("Enter second divisor (n): "))

divisible_list = []
for num in li:
    if num % m == 0 and num % n == 0:
        divisible_list += [num]

print("Numbers divisible by", m, "and", n, ":", divisible_list)