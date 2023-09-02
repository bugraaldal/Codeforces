n = int(input())
for _ in range(n):
    runners = list(map(int, input().split(" ")))
    timur = runners[0]
    runners.sort(reverse=True)
    print(runners.index(timur))


