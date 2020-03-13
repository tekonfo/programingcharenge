divisor = 10**9 + 7

def frac(n):
  sum = 1
  for i in range(1,n+1):
    sum = sum * i % divisor
  return sum

import sys,fractions
N,M=map(int,input().split(' '))
# abs(N-M) > 1なら無理
if (abs(N-M) > 1):
  print(0)
  sys.exit()

# それぞれの階乗を求める
frac_n = frac(N)
frac_m = frac(M)

if N == M:
  ans = frac_m * frac_n * 2
else:
  ans = frac_n * frac_m

print(ans % (10**9 + 7))