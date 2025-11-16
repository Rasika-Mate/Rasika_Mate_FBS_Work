# 2. Create two threads, one printing even numbers and the other printing odd numbers from 1 to 10. Ensure proper synchronization to alternate between even and odd numbers.

import threading

lock = threading.Condition()
turn = "odd"  

def print_odd():
    global turn
    for i in range(1, 11, 2):  
        with lock:
            while turn != "odd":
                lock.wait()
            print(i)
            turn = "even"
            lock.notify()

def print_even():
    global turn
    for i in range(2, 11, 2):  
        with lock:
            while turn != "even":
                lock.wait()
            print(i)
            turn = "odd"
            lock.notify()

t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

t1.start()
t2.start()

t1.join()
t2.join()