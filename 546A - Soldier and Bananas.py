# https://codeforces.com/problemset/problem/546/A
k, n, w = input().split(" ")
sum_of = int(w)*(int(w)+1)/2
res = int(int(n) - (sum_of*int(k)))
if int(abs(res)) == int(res):
    print("0")
else:
    print(int(abs(res)))
