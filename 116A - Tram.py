# https://codeforces.com/problemset/problem/116/A
n_stops = int(input())
total_tram = 0
tram_list = []
for _ in range(n_stops):
    out_tram, in_tram = map(int, input().split(" "))
    total_tram = total_tram + in_tram - out_tram
    tram_list.append(total_tram)
print(max(tram_list))
