N, K = map(int, input().split())
points = list(map(int, input().split()))
ans = 0
tmp = sum(points[:K])
ans += tmp
for i in range(K, N):
  tmp += points[i]
  tmp -= points[i-K]
  ans += tmp
print(ans)
 