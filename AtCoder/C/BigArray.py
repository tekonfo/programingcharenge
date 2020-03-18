import sys
N, K = map(int, input().split())
arr = [0 for _ in range(10**5 + 1)]
su = 0
ans = 0

for n in range(N):
  a, b = map(int, input().split())
  arr[a] += b
  
for i in range(1, 10**5+1):
  su += arr[i]
  if su >= K:
    ans = i
    break
print(ans)