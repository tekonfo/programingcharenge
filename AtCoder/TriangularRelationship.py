from itertools import product
N,K=map(int, input().split())

num = [0 for k in range(K)]

# Nの範囲の中で、Kで割った時のあまりがxになる数がどれくらいあるのかをカウントする
for n in range(1, N+1):
  num[n%K] += 1

ans = 0

for a in range(len(num)):
  b = (K-a) % K
  c = (K-a) % K
  if (b + c) % K == 0:
    ans += num[a] * num[b] * num[c]

print(ans)
