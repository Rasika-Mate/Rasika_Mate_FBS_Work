# 5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

li = [10, 20, 30, 40, 20, 50, 20]
print(li)

num = int(input("Enter a number to check: "))
count = 0  

for i in li:
    if i == num:
        count += 1

if count > 0:
    print(f"{num} is present in the list {count} time(s).")
else:
    print(f"{num} is not present in the list.")