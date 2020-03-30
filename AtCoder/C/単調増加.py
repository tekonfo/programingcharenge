from itertools import combinations

N = int(input())
items = list(map(int, input().split()))
is_ups = []
tmp = 0
for index in range(1, len(items)):
  tmp+=1
  if items[index-1] >= items[index]:
    is_ups.append(tmp)
    tmp=0

if items[-2] <= items[-1]:
  is_ups[-1] += 1
else:
  is_ups.append(1)

ans = 0

for count in is_ups:
  ans += count
  ans += len(list(combinations(range(count),2)))

print(ans)