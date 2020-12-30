# https://codeforces.com/problemset/problem/59/A
vasyaInput = input()
upperLetter, lowerLetter = 0, 0
for ch in vasyaInput:
    if ch.isupper():
        upperLetter += 1
    elif ch.islower():
        lowerLetter += 1
if lowerLetter >= upperLetter:
    print(vasyaInput.lower())
else:
    print(vasyaInput.upper())
