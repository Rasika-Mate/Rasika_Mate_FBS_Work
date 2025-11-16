# 3. Implement two threads to print lowercase and uppercase alphabets concurrently from 'a' to 'z' and 'A' to 'Z'.

import threading
import string
import time

def print_lowercase():
    for ch in string.ascii_lowercase:   # a to z
        print(ch, end=" ")
        time.sleep(0.05)   

def print_uppercase():
    for ch in string.ascii_uppercase:   # A to Z
        print(ch, end=" ")
        time.sleep(0.05)

t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

t1.start()
t2.start()

t1.join()
t2.join()