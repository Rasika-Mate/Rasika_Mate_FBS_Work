# 4. Implement a producer-consumer problem with a limited buffer of size 5. Create two producer threads and two consumer threads. Producers produce items, and consumers consume them. Ensure proper synchronization to avoid buffer overflows or underflows.

import threading
import time
import random

buffer = []
BUFFER_SIZE = 5

lock = threading.Condition()

def producer(id):
    while True:
        item = random.randint(1, 100)

        with lock:
            while len(buffer) == BUFFER_SIZE:     # buffer full
                lock.wait()

            buffer.append(item)
            print(f"Producer {id} produced:", item, "| Buffer:", buffer)

            lock.notify_all()

        time.sleep(random.uniform(0.5, 1.5))      # slow down producer

def consumer(id):
    while True:
        with lock:
            while len(buffer) == 0:               # buffer empty
                lock.wait()
            
            item = buffer.pop(0)
            print(f"Consumer {id} consumed:", item, "| Buffer:", buffer)

            lock.notify_all()

        time.sleep(random.uniform(0.5, 1.5))      # slow down consumer

p1 = threading.Thread(target=producer, args=(1,))
p2 = threading.Thread(target=producer, args=(2,))
c1 = threading.Thread(target=consumer, args=(1,))
c2 = threading.Thread(target=consumer, args=(2,))

p1.start()
p2.start()
c1.start()
c2.start()