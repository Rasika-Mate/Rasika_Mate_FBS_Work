# 6. WAP to calculate total salary of employee based on basic, da-10% of basic. ta-12% of basic, hra 15% of basic.

basicSalary = float(input("Enter Your Basic Salary: "))

da = ((10/100)*basicSalary)
ta = ((12/100)*basicSalary)
hra = ((15/100)*basicSalary)

totalSalary = basicSalary + da + ta + hra
print("Total salary is",totalSalary)