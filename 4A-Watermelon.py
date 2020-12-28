# https://codeforces.com/problemset/problem/4/A
""" In order to buy a watermelon that is sliceable to two even parts, we must buy a watermelan which has the weights of an even number.
    Except the number 2 because it can only be divided 1/1. """
w = int(input())
if w % 2 == 0 and w != 2:
    print("YES")
else:
    print("NO")
