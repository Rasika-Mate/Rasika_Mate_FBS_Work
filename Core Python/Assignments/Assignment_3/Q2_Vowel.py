# 2.WAP to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter any Alphabet: ")

# Method 1
if alphabet in "aeiouAEIOU":
    print("It is vowel")
else:
    print("It is Consonant")


# Method 2
if(alphabet == 'a' or alphabet == 'e' or alphabet =='i' or alphabet == 'o' or alphabet == 'u'):
    print("It is vowel")
else:
    print("It is Consonant")