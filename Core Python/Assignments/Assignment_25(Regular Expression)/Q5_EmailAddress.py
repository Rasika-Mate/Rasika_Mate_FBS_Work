# 5. Write a Python function that takes an email address as input and uses a regular expression to validate if it is a valid email address. The function should return True for valid emails and False for invalid ones.

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

print(validate_email("rasika123@gmail.com"))   # True
print(validate_email("hello.world@domain.co")) # True
print(validate_email("wrong@domain"))          # False
print(validate_email("abc@@gmail.com"))        # False