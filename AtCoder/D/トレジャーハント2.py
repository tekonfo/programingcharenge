from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from sys import stdin
nii=lambda:map(int,stdin.readline().split())
 
n,m,t=nii()
a_l=list(nii())
 
row,col,w=[],[],[]
for i in range(m):
  a,b,c=nii()
  row.append(a-1)
  col.append(b-1)
  w.append(c)
 
g=csr_matrix((w,(row,col)),shape=(n,n))
rg=csr_matrix((w,(col,row)),shape=(n,n))
 
d=dijkstra(g,indices=0)
rd=dijkstra(rg,indices=0)

ans=0
for i in range(n):
    t_ans=(t-(d[i]+rd[i]))*a_l[i]
    ans=max(ans,t_ans)
print(int(ans))