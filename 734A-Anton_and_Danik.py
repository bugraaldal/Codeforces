# https://codeforces.com/problemset/problem/734/A
_ = int(input())
Matches = input()
Anton, Danik = Matches.count("A"), Matches.count("D")
if Anton == Danik:
    print("Friendship")
elif Anton > Danik:
    print("Anton")
else:
    print("Danik")
