# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String

string = input("Enter a string: ")

# Count characters manually
char_count = 0
for ch in string:
    char_count += 1

# Count words manually
word_count = 0
in_word = False
for ch in string:
    if ch != ' ' and not in_word:
        in_word = True
        word_count += 1
    elif ch == ' ':
        in_word = False

print("Number of characters:", char_count)
print("Number of words:", word_count)