# 8. WAP to Count the Frequency of Words Appearing in a String Using a Dictionary

text = "python is easy and python is programming language"

words = text.split()    # Split the string into words
freq_dict = {}  # Initialize an empty dictionary
for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1
print("Word Frequency:", freq_dict)