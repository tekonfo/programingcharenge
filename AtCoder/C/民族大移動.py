N, D, K = map(int, input().split())
ranges = [list(map(int, input().split())) for _ in range(D)]
towns = [list(map(int, input().split())) for _ in range(K)]
anss = [0 for _ in range(K)]
for day in range(D):
  left, right = ranges[day]
  for group in range(K):
    now, end = towns[group]
    if now == end:
      continue
    anss[group] += 1
    # 近づくのを表現するのが難しい
    if left <= now <= right:
      if now < end:
        if end < right:
          towns[group][0] = end
        else:
          towns[group][0] = right
      else:
        if left < end:
          towns[group][0] = end
        else:
          towns[group][0] = left

for ans in anss:
  print(ans)