# https://codeforces.com/problemset/problem/344/A
magnet_count = int(input())
magnets = ""
for _ in range(magnet_count):
    magnets += str(input())
print(magnets.count("00")+magnets.count("11")+1)
