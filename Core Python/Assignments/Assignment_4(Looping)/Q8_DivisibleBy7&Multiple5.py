# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

beg = int(input("Enter beginning of Range: "))
end = int(input("Enter Ending of Range: "))

for num in range(beg, end+1):
    if(num%7==0 and num%5==0):
        print(num)