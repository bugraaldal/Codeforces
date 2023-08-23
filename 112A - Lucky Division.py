# https://codeforces.com/problemset/problem/122/A
def check_lucky(val):
    check = False
    if len(str(val)) < 2:
        if val == 4 or val == 7:
            check = True
    else:
        val = list(set(str(val)))
        if len(val) != 2:
            check = False
        else:
            if (val[0] == "4" or val[0] == "7") and (val[1] == "4" or val[1] == "7"):
                check = True
            else:
                check = False
    return check 

n = int(input())
set_check = False
for i in range(1,n+1):
    check_num = check_lucky(i)
    if check_num:
        if n % i == 0:
            print("YES")
            set_check = True
            break
if not set_check:
    print("NO")
