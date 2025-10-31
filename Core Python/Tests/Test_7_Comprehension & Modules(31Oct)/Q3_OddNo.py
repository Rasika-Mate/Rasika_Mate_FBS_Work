# 3. WAP that generates a list of odd numbers from 1 to 50 using list comprehension and filters out the even numbers

odd_no = [n for n in range(1, 51) if n % 2 != 0]

print("Odd numbers from 1-50:", odd_no)