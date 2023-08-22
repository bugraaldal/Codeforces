# https://codeforces.com/problemset/problem/677/A
_, h_fence = map(int, input().split(" "))
heights = list(map(int, input().split(" ")))
width = 0
for h in heights:
    if h <= h_fence:
        width += 1
    else:
        width += 2
print(width)
