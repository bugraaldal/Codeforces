# https://codeforces.com/problemset/problem/486/A
# Time:  O(1)
# Space: O(1)
n = int(input())
if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)

"""
Exceeds time limit
Time:  O(n)
Space: O(1)
num = int(input())
calc = 0
for track, i in enumerate(range(1, num + 1)):
    if track % 2 == 0:
        calc -= i
    else:
        calc += i

print(calc)
"""
