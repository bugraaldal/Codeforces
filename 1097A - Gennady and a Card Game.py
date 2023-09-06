rank, suit = list(input())
cards = input().split(" ")
flag = False
for card in cards:
    if rank in card or suit in card:
        print("YES")
        flag = True
        break

if flag == False:
    print("NO")
