from operator import mul
from functools import reduce
from collections import Counter
from itertools import combinations

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = int(input())
items = list(map(int, input().split()))
counts = Counter(items)
cobinations = {}
count_sum = 0

for key,value in counts.items():
  if value not in cobinations:
    if value > 1:
      count = cmb(value, 2)
      cobinations[value] = count
    else:
      cobinations[value] = 0
  count_sum+=cobinations[value]

for key in items:
  value = counts[key]
  if value - 1 not in cobinations:
    if value - 1 > 1:
      # tmp_key = list(range(value-1))
      # count = len(list(combinations(tmp_key, 2)))
      # cobinations[value-1] = count
      count = cmb(value-1, 2)
      cobinations[value-1] = count
    else:
      cobinations[value-1] = 0
  
  before = cobinations[value]
  after = cobinations[value-1]
  print(count_sum - before + after)

