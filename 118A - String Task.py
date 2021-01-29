# https://codeforces.com/problemset/problem/118/A
""" Taking the input and removing the vowels, then adding the dots (There were double dots at first.) """
word = input("").lower()
no_Vowel = word.translate({ord(change): None for change in "aoyeui"})
no_Vowels = f".{no_Vowel}"
points = ".".join(no_Vowels).replace("..", ".")
print(points.lower())
