# from collections import deque
# R, C = map(int, input().split())
# sy, sx = map(lambda x: int(x)-1, input().split())
# gy, gx = map(lambda x: int(x)-1, input().split())
# mize = [list(input()) for _ in range(R)]
# q = deque()
# q.append((sy, sx, 0))
# ans = 0
# while q:
#   y, x, count = q.popleft()
#   if y == gy and x == gx:
#     ans = count
#     break
#   mize[y][x] = count
#   for nx,ny in [[-1,0],[1,0],[0,-1],[0,1]]:
#     if 0<=nx+x<C and 0<=ny+y<R and mize[y+ny][x+nx] == '.':
#       q.append((y+ny, x+nx, count+1))
  
# print(ans)

from collections import deque
 
def next(x):
    return [[x[0]-1,x[1]],[x[0]+1,x[1]],[x[0],x[1]-1],[x[0],x[1]+1]]
 
R,C = list(map(int, input().split()))
s = list(map(int, input().split()))
g = list(map(int, input().split()))
c = []
for i in range(R):
    a = list(input())
    c.append(a)
 
q = deque()
q.append([s[0]-1,s[1]-1])
c[s[0]-1][s[1]-1] = 0
 
while len(q)>0:
    r = q.pop()
    for t in next(r):
        if c[t[0]][t[1]] == '.':
            q.appendleft(t)
            c[t[0]][t[1]] = c[r[0]][r[1]] + 1
 
print(c[g[0]-1][g[1]-1])