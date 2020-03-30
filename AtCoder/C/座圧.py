N = int(input())
items = [int(input()) for _ in range(N)]
d = {v: i for i, v in enumerate(sorted(list(set(items))))}
for item in items:
  print(d[item])