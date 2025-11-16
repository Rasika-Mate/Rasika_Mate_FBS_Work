# 1. Develop a function that takes a text and a list of forbidden words. Replace all occurrences of these forbidden words with asterisks (*) using regular expressions.

import re

def censor_text(text, forbidden_words):
    for word in forbidden_words:
        pattern = re.compile(word, re.IGNORECASE)   # Create a regex pattern that matches the word (case-insensitive)
        text = pattern.sub('*' * len(word), text)   # Replace each character of the word with '*'
    return text

text = "Python is amazing and Java is powerful."
forbidden = ["python", "java"]
result = censor_text(text, forbidden)
print(result)