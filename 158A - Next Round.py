# https://codeforces.com/problemset/problem/158/A
n, k = list(map(int, input().split(" ")))
scores = list(map(int, input().split(" ")))
set_score = scores[k-1]
passed = [i for i in scores[:k] if i>0]
for i in range(k, n):
    if (scores[i] > 0) and (set_score == scores[i]):
        passed.append(scores[i])
print(len(passed))
        
