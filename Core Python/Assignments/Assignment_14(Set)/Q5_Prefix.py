# 5. WAP to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "flow", "flight"]
prefix = ""

for i in range(len(words[0])):         # loop through each letter of first word
    s = set(word[i] for word in words if i < len(word))
    if len(s) == 1:                    # all letters same
        prefix += words[0][i]
    else:
        break

print("Words:", words)
print("Longest Common Prefix:", prefix)