# 3. WAP to accept basic salary of n employee (n should be accepted from user). If basix salary is below 20000 then da=10%, ta=12% and hra=20. Based on this calculate the total salary of each employee and also total salary of all emp.

num = int(input("Enter Number of Employees: "))
total_all = 0

for i in range(1, num + 1):
    bs = int(input(f"Enter Basic salary of Employee {i}: "))

    if bs < 20000:
        total_salary = bs+(0.10*bs)+(0.12*bs)+(0.20*bs)
    else:
        total_salary = bs

    print("Total Salary of Employee", i, ":", total_salary)
    total_all += total_salary

print("\nTotal Salary of all employees:", total_all)