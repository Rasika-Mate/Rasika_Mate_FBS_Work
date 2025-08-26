# 8. WAP to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random

userid = "admin"
password = "1234"

id= input("Enter User ID: ")
pwd = input("Enter Password: ")

if(id == userid and pwd == password):
    print("Login Successfull")
    
    captcha = random.randint(1111, 9999)
    print("\nCaptcha=", captcha)
    enter = int(input("Enter above Captcha: "))
    
    if(enter == captcha):
        print("Success")
    else: 
        print("Captcha is not matched")
else:
    print("Invalid user ID and Password")