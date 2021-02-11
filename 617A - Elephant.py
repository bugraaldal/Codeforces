# https://codeforces.com/problemset/problem/617/A
friend_loc = int(input())
five_step = friend_loc//5
if friend_loc > 5 and friend_loc % 5 != 0:
    print(five_step + 1)
elif friend_loc > 5 and friend_loc % 5 == 0:
    print(five_step)
else:
    print(1)
