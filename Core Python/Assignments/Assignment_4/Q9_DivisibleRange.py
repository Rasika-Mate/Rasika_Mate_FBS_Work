# 9. WAP to print all numbers in a range divisible by a given number.

beg = int(input("Enter beginning of Range: "))
end = int(input("Enter Ending of Range: "))
div = int(input("Enter the number to check divisibility: "))

print(f"Numbers divisible by {div} are: ")

for i in range(beg, end+1):
    if i % div == 0:
        print(i, end=" ")