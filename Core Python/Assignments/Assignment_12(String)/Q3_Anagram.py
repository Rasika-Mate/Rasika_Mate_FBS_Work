# 3. Python Program to Detect if Two Strings are Anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase for fair comparison
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check lengths first
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # Manually compare character counts
    count1 = {}
    count2 = {}

    for ch in str1:
        if ch in count1:
            count1[ch] += 1
        else:
            count1[ch] = 1

    for ch in str2:
        if ch in count2:
            count2[ch] += 1
        else:
            count2[ch] = 1

    if count1 == count2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")