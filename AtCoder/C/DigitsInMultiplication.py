import math
N=int(input())
# rootを求める
# 二分探索すればいいのか！！！
root_n = int(math.sqrt(N))
up_n = root_n
up_ans = 0
keta = lambda x: len(str(x))
while up_n <= N:
  if N % up_n == 0:
    pair = int(N/up_n)
    # 桁数を求める
    up_ans = max(keta(pair), keta(up_n))
    break
  else:
    up_n-=1

print(up_ans)

