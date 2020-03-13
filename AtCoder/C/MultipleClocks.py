def lcm(x, y):
  return (x * y) // fractions.gcd(x, y)

import fractions
N=int(input())
t=[int(input()) for _ in range(N)]
ans = 1
for item in t:
  ans = lcm(ans, item)
print(int(ans))