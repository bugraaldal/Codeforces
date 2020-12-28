# https://codeforces.com/problemset/problem/112/A
def split(word):
    return list(word)


s1 = input().lower()
s2 = input().lower()
s1_list = split(s1)
s2_list = split(s2)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if s1_list == s2_list:
    print(0)
else:
    for x in range(0, len(s2_list)):
        if alphabet.index(s1_list[x]) > alphabet.index(s2_list[x]):
            print(1)
            break
        elif alphabet.index(s1_list[x]) < alphabet.index(s2_list[x]):
            print(-1)
            break
