# https://codeforces.com/contest/520/problem/A
def check_freq(x):
    freq = {}
    for c in set(x):
        freq[c] = x.count(c)
    return freq


_ = input()
word = input().lower()
if len(check_freq(word)) == 26:
    print("YES")
else:
    print("NO")
