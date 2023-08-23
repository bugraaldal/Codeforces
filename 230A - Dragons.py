# https://codeforces.com/problemset/problem/230/A
def sort(dragons: list):
    for i in range(len(dragons)):
        for j in range(i+1, len(dragons)):
            if dragons[i][0] > dragons[j][0]:
                dragons[i], dragons[j] = dragons[j], dragons[i]
            elif dragons[i][0] == dragons[j][0]:
                if dragons[i][1] < dragons[j][1]:
                    dragons[i], dragons[j] = dragons[j], dragons[i]
    return dragons

s, n = map(int, input().split(" "))
dragons = []
for _ in range(n):
    d_s, b = map(int, input().split(" "))
    dragons.append([d_s, b])
flag = False
dragons = sort(dragons)
for dragon in dragons:
    if s > dragon[0]:
        s += dragon[1]
        flag = True
    else:
        print("NO")
        flag = False
        break

if flag:
    print("YES")