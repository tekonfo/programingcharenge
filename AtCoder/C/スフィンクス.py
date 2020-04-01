N, M = map(int, input().split())
rouzin_count = 1
ans = []
# 老人が一人のとき
for adult_count in range(N):
  baby_count = N - adult_count - rouzin_count
  if rouzin_count * 3 + baby_count * 4 + adult_count * 2 == M:
    ans.append([adult_count, rouzin_count, baby_count])

# 老人が０人のとき
rouzin_count = 0
for adult_count in range(N+1):
  baby_count = N - adult_count - rouzin_count
  if rouzin_count * 3 + baby_count * 4 + adult_count * 2 == M:
    ans.append([adult_count, rouzin_count, baby_count])

if len(ans) > 0:
  print(' '.join(list(map(str, ans[0]))))
else:
  print(' '.join(['-1','-1','-1']))