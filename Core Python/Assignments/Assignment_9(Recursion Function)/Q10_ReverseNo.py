# 10. WAP to reverse a number using recursion.

def reverse_num(num, rev=0):
    if num == 0:  
        return rev
    rem = num % 10
    rev = rev * 10 + rem
    return reverse_num(num // 10, rev)

n = int(input("Enter a number: "))
reversed_number = reverse_num(n)
print(f"Reversed Number: {reversed_number}")