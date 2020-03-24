import math
N = int(input())

stations = []
for n in range(N-1):
  tmp = tuple(map(int, input().split()))
  stations.append(tmp)

for index in range(len(stations)):
  time = 0
  sum_time = 0
  for c, s, f in stations[index:]:
    if time <= s:
      time = s + c
    else:
      diff = time - s
      count = math.ceil(diff/f)
      time = s + f*count + c
  print(time)
print(0)