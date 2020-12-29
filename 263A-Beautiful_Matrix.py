# https://codeforces.com/problemset/problem/263/A
n = 5
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    if 1 in a[i]:
        count = abs(2 - a[i].index(1)) + abs(2 - i)
        print(count)
        break
