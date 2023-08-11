# https://codeforces.com/problemset/problem/977/A
n, k = map(int, input().split(" "))
for _ in range(k):
    if list(str(int(n)))[-1] != "0":
        n -= 1
    else:
        n = n / 10
print(int(n))