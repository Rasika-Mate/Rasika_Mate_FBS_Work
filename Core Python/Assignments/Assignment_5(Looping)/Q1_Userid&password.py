# 1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.

userid = "admin"  # Predefined correct credentials
password = "1234"

for attempt in range(3):
    uid = input("Enter User ID: ")
    pwd = input("Enter Password: ")
    
    if(uid == userid and pwd == password):
        print("Login Successful")
        break
    else:
        print("Invalid credentials. Try again.")
else:
    print("3 attempts over, Program terminated.")