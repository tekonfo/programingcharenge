N, M = map(int, input().split())
friends_set = [set([i]) for i in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  friends_set[a-1].add(b-1)
  friends_set[b-1].add(a-1)

for human_index in range(N):
  ans_list = []
  for friend in friends_set[human_index]:
    for i in friends_set[friend] - friends_set[human_index]:
      if human_index < i and [human_index, i] not in ans_list:
        ans_list.append([human_index, i])
      if human_index > i and [i, human_index] not in ans_list:
        ans_list.append([i, human_index])
  print(len(ans_list))
