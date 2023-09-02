_ = input()
welfares = list(map(int, input().split(" ")))
count = 0
for i in welfares:
    count += max(welfares) - i
print(count)
