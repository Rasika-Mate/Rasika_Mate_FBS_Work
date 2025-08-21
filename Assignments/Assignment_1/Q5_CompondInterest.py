# WAP to enter P, T, R and calculate Compound Interest
# Formula: P*(1+R/100)**t-P
# Where, P=Principle Amount, R=Rate of interest(%), T=Time(Years)

p = int(input('Enter Principle Amount: '))
r = int(input('Enter Rate: '))
t = int(input('Enter Time: '))

ci = p*(1+r/100)**t-p
print('Compound Interest is',ci)