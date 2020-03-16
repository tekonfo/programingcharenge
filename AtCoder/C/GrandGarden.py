N = int(input())
h = list(map(int, input().split()))

count = 0

while any(h):
  lists = [i for i, x in enumerate(h) if x > 0]
  i  = lists[0]
  start = i
  end = i
  while end + 1 < N and h[end + 1] > 0:
    end += 1
  for index in range(start, end + 1):
    h[index] -= 1
  count += 1

print(count)
