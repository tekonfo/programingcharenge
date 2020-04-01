import sys
from itertools import product
N, K = map(int, input().split())
selects = [list(map(int, input().split())) for _ in range(N)]
patterns = product([i for i in range(K)], repeat=N)
for pattern in patterns:
  tmp = selects[0][pattern[0]]
  for index in range(1, N):
    tmp = tmp ^ selects[index][pattern[index]]
  if tmp == 0:
    print("Found")
    sys.exit()

print("Nothing")

