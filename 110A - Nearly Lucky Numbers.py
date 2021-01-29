# https://codeforces.com/problemset/problem/110/A
inputlist = list(input())
x = 0
for ch in inputlist:
    if ch == "4" or ch == "7":
        x += 1
if x == 1:
    print("NO")
elif x == 4 or x == 7:
    print("YES")
else:
    print("NO")
