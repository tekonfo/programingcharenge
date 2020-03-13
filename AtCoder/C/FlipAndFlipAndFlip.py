import sys

N, M = map(int, input().split())
ans = N*M

# N,Mどちらかが1の時はとりあえず考えない
if N == 1 and M == 1:
  ans = 1
elif N == 1 or M == 1:
  ans -= 2 
else:
  # 四隅,境界線は正なので引く
  ans -= (N*2 + M*2 - 4)

print(ans)