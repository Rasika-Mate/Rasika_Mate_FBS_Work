# 7. WAP to check if user has entered correct userid and password.

userid = "admin"
password = "123"

id= input("Enter User ID: ")
pwd = input("Enter Password: ")

if(id == userid and pwd == password):
    print("Login Successfull")
else:
    print("Invalid user ID and Password")