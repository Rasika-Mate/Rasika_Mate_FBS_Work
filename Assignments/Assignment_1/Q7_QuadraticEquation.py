# WAP to Find the Roots of a Quadratic Equation

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

ans=(b*b)-(4*a*c)
ans=ans**0.5
root1=(-b+ans)/(2*a)
root2=(-b-ans)/(2*a)
print("Root1 is",root1)
print("Root2 is",root2)