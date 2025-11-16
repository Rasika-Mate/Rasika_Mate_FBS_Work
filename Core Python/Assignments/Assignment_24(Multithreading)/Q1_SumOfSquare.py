# 1. Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the range equally among the threads, and each thread calculates the sum of squares for its range. Finally, combine the results to get the total sum of squares.

import threading

result = [0, 0, 0, 0]   # to store sum from each thread

def calc_square(start, end, index):
    s = 0
    for i in range(start, end + 1):
        s += i*i
    result[index] = s

t1 = threading.Thread(target=calc_square, args=(1, 25, 0))  # 4 threads for 4 parts
t2 = threading.Thread(target=calc_square, args=(26, 50, 1))
t3 = threading.Thread(target=calc_square, args=(51, 75, 2))
t4 = threading.Thread(target=calc_square, args=(76, 100, 3))

t1.start()  # start all threads
t2.start()
t3.start()
t4.start()

t1.join()   # wait for all to finish
t2.join()
t3.join()
t4.join()

total = sum(result)
print("Sum of squares from 1 to 100 =", total)