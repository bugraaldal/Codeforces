# https://codeforces.com/problemset/problem/791/A
a, b = list(map(int, input().split(" "))) # Limak, Bob; a < b
y_count = 0
while True:
    a = a * 3
    b = b * 2
    y_count += 1
    if a > b:
        print(y_count)
        break
    else:
        pass