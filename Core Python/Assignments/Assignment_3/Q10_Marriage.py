# 10. WAP to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter Gender(M/F): ")
age = int(input("Enter Age: "))

if(gender == 'M' or gender == 'F'):
    if(age >= 21):
        print("Eligible for Marriage!")
    else:
        print("Not eligible for Marriage")
else:
    if(age > 17):
        print("Eligible for Marriage!")
    else:
        print("Not eligible for Marriage")