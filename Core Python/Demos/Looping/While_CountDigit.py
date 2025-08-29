num = int(input("Enter Number: "))

temp = num
count = 0
while(temp > 0):
    count += 1
    digit = temp % 10
    temp = temp // 10
print("Total No. of digits are:", count)