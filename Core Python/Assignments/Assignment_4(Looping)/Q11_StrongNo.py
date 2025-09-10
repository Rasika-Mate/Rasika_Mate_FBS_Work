# 11. WAP to check if given number Strong Number.
# 145 → 1! + 4! + 5! = 1 + 24 + 120 = 145

num = int(input("Enter a number: "))
original_num = num  
sum_fact = 0 

while num > 0:
    digit = num % 10        
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    sum_fact += fact        
    num //= 10              

if sum_fact == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is NOT a Strong Number")