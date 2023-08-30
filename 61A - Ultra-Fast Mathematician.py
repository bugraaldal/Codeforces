# https://codeforces.com/problemset/problem/61/A
a = input("")
b = input("")
output = ""
for i, k in zip(a, b):
    if i == k:
        output += "0"
    else:
        output += "1"
print(output)
