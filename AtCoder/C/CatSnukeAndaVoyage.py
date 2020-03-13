import sys

N, M = map(int, input().split())
canMove = [[] for _ in range(N+1)]
for m in range(M):
  a, b = map(int, input().split())
  canMove[a].append(b)

for key in canMove[1]:
  if N in canMove[key]:
    print('POSSIBLE')
    sys.exit()

print('IMPOSSIBLE')