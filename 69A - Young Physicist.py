# https://codeforces.com/problemset/problem/69/A
lines = int(input())
xs, ys, zs = [], [], []
for i in range(0, lines):
    coords = input()
    x, y, z = coords.split(" ")
    xs.append(int(x))
    ys.append(int(y))
    zs.append(int(z))
if sum(xs) == 0 and sum(ys) == 0 and sum(zs) == 0:
    print("YES")
else:
    print("NO")
