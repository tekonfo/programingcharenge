N = int(input())
points = list(map(int, input().split()))
even_points = [points[index] for index in range(len(points)) if index % 2 == 0]
odd_points = [points[index] for index in range(len(points)) if index % 2 == 1]

if N % 2 == 0:
  odd_points = list(reversed(odd_points))
  odd_points.extend(even_points)
  ans = odd_points
else:
  even_points = list(reversed(even_points))
  even_points.extend(odd_points)
  ans = even_points

ans = list(map(str, ans))
print(' '.join(ans))