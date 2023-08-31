# https://codeforces.com/problemset/problem/1373/B
n = int(input())
for _ in range(n):
    bin = input()
    zeros = bin.count("0")
    ones = bin.count("1")
    if min(zeros, ones) % 2 == 0:
        print("NET")
    else:
        print("DA")
