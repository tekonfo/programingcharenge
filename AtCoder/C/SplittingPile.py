INF = 30000000000
N = int(input())
points = list(map(int, input().split()))
sums = [0]
for index in range(len(points)):
  sums.append(points[index]+sums[index])
ans = INF
last = sums[-1]
for s in sums[1:-1]:
  ans = min(ans, abs(last -s - s))
print(ans)