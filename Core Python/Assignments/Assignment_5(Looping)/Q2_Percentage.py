# 2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.

n = int(input("Enter number of students: "))
total = 0

for i in range(1, n+1):
    print(f"\nStudent {i}:")
    s1 = int(input(" Enter marks of Subject 1: "))
    s2 = int(input(" Enter marks of Subject 2: "))
    s3 = int(input(" Enter marks of Subject 3: "))
    s4 = int(input(" Enter marks of Subject 4: "))
    s5 = int(input(" Enter marks of Subject 5: "))
    percentage = (s1+s2+s3+s4+s5)/5
    print(" Percentage:", percentage, "%")
    total += percentage

avg = total / n
print("\nAverage Percentage of Class:", avg, "%")