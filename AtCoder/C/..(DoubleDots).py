from collections import deque
 
N,M=map(int,input().split())
 
graph=[[]for _ in range(N+1)]
 
for _ in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
 
dist=[-1]*(N+1)
dist[0]=0
dist[1]=0
 
D=deque()
D.append(1)
 
while D:
    V=D.popleft()
    for i in graph[V]:
        if dist[i]!=-1:
            continue
        dist[i]=V
        D.append(i)
 
print('Yes')
for j in dist[2:]:
    print(j)