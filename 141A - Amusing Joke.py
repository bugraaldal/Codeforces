# https://codeforces.com/problemset/problem/141/A
def check_freq(word):
    freq = {}
    for ch in set(word):
        freq[ch] = word.count(ch)
    return freq


chx_name = input()
host = input()
mixed = input()
res = chx_name + host
print("YES" if check_freq(res) == check_freq(mixed) else "NO")
