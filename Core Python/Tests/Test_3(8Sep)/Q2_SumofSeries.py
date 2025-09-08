# 2. WAP to calculate the sum of following series where n is input by user.
# 1/n!+2/n!+3/n!+4/n!+....N/N!

n = int(input("Enter Number: "))
sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i       
    sum = sum + (i / fact)

print("Sum of the series is:", sum)