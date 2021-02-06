# https://codeforces.com/problemset/problem/43/A
from collections import Counter, OrderedDict
import operator
lines = int(input())
unsorted = Counter([input() for _ in range(lines)]).items()
sorted_tuples = sorted(unsorted, key=operator.itemgetter(1), reverse=True)
sorted_dict = OrderedDict()
for k, v in sorted_tuples:
    sorted_dict[k] = v
print(list(sorted_dict.keys())[0])
