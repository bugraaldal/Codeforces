# https://codeforces.com/problemset/problem/705/A

word = ""
times = int(input())
if times == 1:
    print("I hate it")
else:
    for x in range(0, times):
        if x == times-1:
            if x % 2 == 0:
                word += " that I hate it"
            else:
                word += " that I love it"
        elif x % 2 == 0:
            word += " that I hate"
        else:
            word += " that I love"
    print(word[6:])
