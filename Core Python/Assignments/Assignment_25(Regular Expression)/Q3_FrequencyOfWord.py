# 3. Develop a function that counts the occurrences of each word in a given text. Use regular expressions to split the text into words and then count the frequency of each word.

import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())    # Use regex to split text into words

    word_count = {}
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1

    return word_count

text = "Python is easy to learn and Python is High programming language!"
print(count_words(text))