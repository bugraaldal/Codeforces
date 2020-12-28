# https://codeforces.com/problemset/problem/1/A
# Getting the sides of the rectangle and the profuct of the remainder
import math
x = input()
x = x.split()
m = int(x[0])
n = int(x[1])
a = int(x[2])
remainder1 = m/a
remainder1 = math.ceil(remainder1)
remainder2 = n/a
remainder2 = math.ceil(remainder2)
print(remainder2*remainder1)
