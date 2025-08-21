# WAP to enter P, T, R and calculate simple Interest.
# Formula: P*R*T/100
# Where, P=Principle Amount, R=Rate of interest(%), T=Time(Years)

p = int(input('Enter Principle Amount: '))
r = int(input('Enter Rate: '))
t = int(input('Enter Time: '))

si = p*r*t/100
print('Simple Interest is',si)