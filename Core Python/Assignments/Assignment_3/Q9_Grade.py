# 9. Input 5 subject marks from user and display grade (eg.First class,Second class ..)

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

total_marks = (m1+m2+m3+m4+m5)
per = (total_marks/500)*100

if(per >= 70):
    print("First Class")
elif(per >= 50):
    print("Second Class")
elif(per >= 35):
    print("Pass")
else:
    print("Fail")