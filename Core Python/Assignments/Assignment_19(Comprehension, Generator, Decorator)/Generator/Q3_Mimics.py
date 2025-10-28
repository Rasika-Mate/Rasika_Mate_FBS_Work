# 3. Write a generator function that mimics the behavior of the built-in range() function. The generator should take start, stop, and step arguments and yield numbers within the specified range.

def my_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

for num in my_range(1, 10, 2):
    print(num, end=" ")