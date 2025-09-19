# 3. WAP to reverse a given number using recursive function.

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    rem = num % 10
    rev = rev * 10 + rem
    return reverse_num(num // 10, rev)

num = int(input("Enter a number: "))
reversed_number = reverse_num(num)
print(f"Reversed Number: {reversed_number}")