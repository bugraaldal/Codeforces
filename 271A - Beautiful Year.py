# https://codeforces.com/problemset/problem/271/A
year = int(input())
counts = []
while True:
    year += 1
    for digit in str(year):
        counts.append(str(year).count(digit))
    if max(counts) == 1:
        print(year)
        break
    else:
        counts.clear()

            
            