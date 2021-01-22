# https://codeforces.com/contest/469/problem/A
final_list = []
check = 0
total_levels = int(input())
X = input().split(' ')
X = list(map(int, X))
Y = input().split(' ')
Y = list(map(int, Y))

for i in range(1, X[0]+1):
    final_list.append(X[i])
for i in range(1, Y[0]+1):
    final_list.append(Y[i])


for i in range(1, total_levels+1):
    if (not(i in final_list)):
        check = 1
        print("Oh, my keyboard!")
        break

if (check == 0):
    print("I become the guy.")

# I have no idea why the code below doesn't work
# and the why test 27's answer is "Oh my keyboard"
"""
total_lvl = int(input())
k = 0
final_list = []
X = input().split(" ")
Y = input().split(" ")
set_X = (set(map(int, X)))
set_Y = (set(map(int, Y)))
collective_pass = (set_X | set_Y)
all_levels = [x for x in range(1, total_lvl+1)]
for items in collective_pass:
    if items != 0:
        final_list.append(items)

for item in zip(all_levels, final_list):
    if item[0] == item[1]:
        k += 1
if k == total_lvl:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
"""
