# https://codeforces.com/problemset/problem/1742/A
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split(" ")))
    nums.sort()
    if nums[0] + nums[1] == nums[2]:
        print("YES")
    else:
        print("NO")
