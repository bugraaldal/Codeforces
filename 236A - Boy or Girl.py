# https://codeforces.com/problemset/problem/236/A
""" This problem is actually hilarious. """
def split(word):
    return list(word)


x = 0
nickname = input()
nickname_check_list = split(nickname)
for each_char in range(len(nickname_check_list)):
    if nickname_check_list.count(nickname_check_list[x]) > 1:
        nickname_check_list.remove(nickname_check_list[x])
    elif nickname_check_list.count(nickname_check_list[x]) == 1:
        x += 1
if len(nickname_check_list) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
