# https://codeforces.com/problemset/problem/282/A
times = int(input())
val = 0
for _ in range(0, times):
    X = input()
    val += 1 if "+" in X else -1
print(val)
