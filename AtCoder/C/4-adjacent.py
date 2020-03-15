from collections import Counter
N = int(input())
points = list(map(int, input().split()))
points = list(map(lambda i:i%4, points))
l = Counter(points)
if l[0] + int(l[2]/2) >= int(N/2):
  print('Yes')
else:
  print('No')