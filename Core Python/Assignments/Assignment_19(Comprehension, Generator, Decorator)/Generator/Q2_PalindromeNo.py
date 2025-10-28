# 2. Implement a generator function that yields palindrome numbers. Palindromes are numbers that read the same backward as forward (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindrome_numbers():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

count = 10  # print first 10 palindrome numbers
gen = palindrome_numbers()
for _ in range(count):
    print(next(gen), end=" ")