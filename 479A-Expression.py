# https://codeforces.com/problemset/problem/479/A
a = int(input())
b = int(input())
c = int(input())
my_list = [a*b*c, a+b*c, a*(b+c), (a+b)*c, a+b+c]
print(max(my_list))
