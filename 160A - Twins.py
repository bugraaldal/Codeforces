# https://codeforces.com/problemset/problem/160/A
_ = input()
coins = list(map(int, input().split(" ")))
coins.sort(reverse=True)
total = 0
for i in range(len(coins)):
    total += coins[i]
    try:
        if total > sum(coins[i + 1 :]):
            print(i + 1)
            break
    except IndexError:
        print(len(coins))
