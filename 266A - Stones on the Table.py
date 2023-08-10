# https://codeforces.com/problemset/problem/266/A
n_stones = int(input())
stones = list(input())
count = 0
for i in range(n_stones):
    try:
        if stones[i] == stones[i+1]:
            count += 1
    except:
        pass
print(count)