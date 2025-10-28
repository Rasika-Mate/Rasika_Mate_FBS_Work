# 14. Python Program to count the occurrences of ach word in a string.

string = input("Enter a string: ")

words = string.split()   # split the string into words
word_count = {}          # empty dictionary

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word occurrences:")
for word, count in word_count.items():
    print(word, ":", count)