# https://codeforces.com/problemset/problem/71/A

n = int(input()) # Get the lenght of the word.

for i in range(0, n):
    x = str(input())
    l = len(x)
    # if the lenght of the word is bigger than 10, get the first and the last letter
    # and then mend it all together.
    if l > 10:
        print(f"{x[0]}{l-2}{x[l-1]}")
    else:
        print(x)
