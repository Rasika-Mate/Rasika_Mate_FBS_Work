# 5. Find all of the words in a string that are less than 5 letters (take input from user)

text = input("Enter a sentence: ")

short_words = [word for word in text.split() if len(word) < 5]

print("Words with less than 5 letters:", short_words)