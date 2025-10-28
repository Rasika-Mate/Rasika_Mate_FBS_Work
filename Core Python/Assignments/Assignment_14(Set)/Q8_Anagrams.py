# 8. WAP to find all the anagrams and group them together from a given list of strings.

words = ["listen", "silent", "enlist", "hello", "below", "elbow"]

groups = {}

for w in words:
    key = ''.join(sorted(w))   # sort the letters to get common key
    groups.setdefault(key, []).append(w)

print("Words:", words)
print("Anagram Groups:")

for g in groups.values():
    print(g)