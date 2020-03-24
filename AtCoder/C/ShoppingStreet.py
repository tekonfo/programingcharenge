INF = 100000000000

from itertools import product
N = int(input())
is_opens = []
all_open = [0 for i in range(10)]

for n in range(N):
  l = list(map(int, input().split()))
  for i in range(len(l)):
    all_open[i] = 1 if l[i] == 1 else all_open[i] 
  is_opens.append(l)
must_true = set([i for i in range(len(all_open)) if all_open[i] == 0])

values = []
for n in range(N):
  values.append(list(map(int, input().split())))

patterns = product([0,1], repeat=10)
ans = -INF
for pattern in patterns:
  trues = set([i for i in range(len(pattern)) if pattern[i] == 1])
  if not must_true.issubset(trues) or trues == set():
    continue 

  tmp = 0
  for n in range(N):
    count = sum([1 for i in range(10) if pattern[i] == 1 and pattern[i] == is_opens[n][i]])
    value = values[n][count]
    tmp += value
  ans = max(ans, tmp)

print(ans)
  
