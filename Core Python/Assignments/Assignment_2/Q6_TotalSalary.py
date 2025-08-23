# 6. WAP to calculate total salary of employee based on basic, da-10% of basic. ta-12% of basic, hra 15% of basic.

bs = float(input("Enter Basic Salary: "))

da = 0.10*bs # 10% = (10/100) 
ta = 0.12*bs # 12% = (12/100)
hra = 0.15*bs # 15% = (15/100)

totalSalary = bs+da+ta+hra
print("Total Salary of Employee is", totalSalary)
