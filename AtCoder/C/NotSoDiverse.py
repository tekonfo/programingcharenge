from collections import Counter
N,K=map(int,input().split())
A = list(map(int,input().split()))
L = Counter(A)
count = len(L.keys()) - K if len(L.keys()) - K > 0 else 0
ans = 0
for c in range(count):
  mi_k = min(L, key=L.get)
  ans+=L[mi_k]
  L.pop(mi_k)

print(ans)