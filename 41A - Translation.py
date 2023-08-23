# https://codeforces.com/problemset/problem/41/A
# Realized that there was a simpler answer
word = str(input())
translated = str(input())
if translated[::-1] == word:
    print("YES")
else:
    print("NO")

# Old solution:
"""
word = str(input())
translated = str(input())
final = "".join([e for e in ([translated[i:i+1]
                              for i in range(0, len(word))][::-1])])
if final == word:
    print("YES")
else:
    print("NO")
"""
