N, M = map(lambda x: int(x), input().split())
lists = []
for i in range(M):
  lists.append(list(map(lambda x: int(x), input().split())))

used_lists  = [0 for i in range(M)]
used_points = [0 for i in range(N)]

dp_lists = []
for i in range(N + 1):
  dp_lists.append([0 for t in range(N + 1)])

len_lists = []
for i in range(N + 1):
  len_lists.append([0 for t in range(N + 1)])
for i in lists:
  len_lists[i[0]][i[1]] = i[2]
  len_lists[i[1]][i[0]] = i[2]

# 全ての頂点間の最短距離をだす
#for i in range(N - 1):
#  for t in range(i + 1, N)
from_point = 1
used_lists[1] =
while True:
  v = -1
  for i in range(1, N + 1):
    v = i if == 0 and (v == -1 or v > len_lists[from_point][i])
  used_points[v] = 1


  # to_pointに使った辺をカウントする
  dp_lists =
  from_point = to_point

# 使っていない編の数を数える
# print(used_list.count(0))
