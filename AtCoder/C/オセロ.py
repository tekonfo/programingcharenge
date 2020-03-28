N, Q = map(int, input().split())
L = [0 for _ in range(N)]

# いもす法で解く
for q in range(Q):
  l, r = map(int, input().split())
  L[l-1] += 1
  if N <= r:
    continue
  L[r] -= 1 

newL = [0 for _ in range(N)]
newL[0] = L[0]
# 累積和計算
for i in range(1, N):
  newL[i] =  newL[i-1] + L[i]

ans = ['1' if l % 2 == 1 else '0' for l in newL ]
ans = ''.join(ans)
print(ans)
