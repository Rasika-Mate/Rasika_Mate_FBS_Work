# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

beg = int(input("Enter beginning of Range: "))
end = int(input("Enter Ending of Range: "))

for num in range(beg, end+1):
    if(num%2!=0 and num%3!=0):
        print(num)