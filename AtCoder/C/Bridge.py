n,m=map(int,input().split())
X=[]
M=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    X.append([a-1,b-1])
    M[a-1].append(b-1)
    M[b-1].append(a-1)
ans=0
 
def dfs(x,se):
    visited[x]=1
    for m in M[x]:
        if se!={x,m} and visited[m]==0:
            dfs(m,se)
 
for i in range(m):
    visited=[0]*n
    dfs(0,set(X[i]))
    if 0 in visited:
        ans+=1
print(ans)