from collections import Counter

N = int(input())
lines = list(map(int, input().split()))

l = Counter(lines)

l = {k:v for k,v in l.items() if v>=2}

if len(l.keys()) <= 1:
  print(0)
else:
  anss = list(l.keys())
  ma  = max(anss)
  ma2 = sorted(anss)[-2]
  print(ma * ma2 if l[ma] < 4 else ma ** 2)
