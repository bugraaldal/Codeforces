# https://codeforces.com/contest/1858/problem/0
# https://codeforces.com/problemset/problem/1858/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    r1 = a + (c // 2) + (c % 2)
    r2 = b + (c // 2)
    if r1 > r2:
        print("First")
    else:
        print("Second")
"""
Exceeds time limit on pretest 2:
n_test = int(input())
for _ in range(n_test):
    a, b, c = map(int, str(input()).split(" "))
    total_buttons = a + b + c
    for i in range(total_buttons):
        if a == 0:
            if c == 0:
                print("Second")
                break
            else:
                c -=1
        else:
            a -= 1
        
        if b == 0:
            if c == 0:
                print("First")
                break
            else:
                c -= 1
        else:
            b -= 1
"""