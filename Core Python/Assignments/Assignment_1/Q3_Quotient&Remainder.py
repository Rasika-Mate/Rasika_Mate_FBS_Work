# WAP to find quotient and remainder of two numbers
# Floor Division (//) ----> Quotient
# Modulus Operator (%) ---> Remainder

dividend = int(input('Enter Dividend: '))
divisor = int(input('Enter Divisor: '))

Q = dividend // divisor
R = dividend % divisor
print(f'Quotient is {Q}')
print(f'Remainder is {R}')