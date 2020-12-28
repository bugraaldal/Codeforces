# https://codeforces.com/problemset/problem/231/A
shoould_Answer = 0
surness = int(input())
for inputs in range(0, surness):
    surness = str(input())
    ones, zeros = surness.count("1"), surness.count("0")
    if ones > zeros:
        shoould_Answer += 1
print(shoould_Answer)
