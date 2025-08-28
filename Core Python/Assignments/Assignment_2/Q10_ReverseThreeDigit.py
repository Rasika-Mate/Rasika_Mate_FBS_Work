# 10. WAP to reverse three-digit number

num = int(input('Enter three-digit number: '))

d1 = num % 10    
num = num // 10  
d2 = num % 10    
num = num // 10  
d3 = num % 10    
num = num // 10  

rev_digit = (d1*100)+(d2*10)+d3
print(rev_digit)