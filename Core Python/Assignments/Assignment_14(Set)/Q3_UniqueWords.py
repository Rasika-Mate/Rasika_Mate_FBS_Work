# 3. WAP to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

lines = ["apple banana mango", "banana orange apple", "grapes mango apple"]

unique = set()  # Empty set for unique words
count = {}  # Empty dictionary for word count

for line in lines:
    words = line.split()
    for w in words:
        unique.add(w)              # add word to set
        count[w] = count.get(w, 0) + 1  # count word

print("Unique words:", unique)
print("Word frequency:")
for w in count:
    print(w, ":", count[w])