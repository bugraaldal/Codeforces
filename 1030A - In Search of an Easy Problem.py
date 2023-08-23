# https://codeforces.com/problemset/problem/1030/A
_ = input()
answers = list(map(int, input().split(" ")))
print("EASY" if (not(any(answers))) else "HARD")
