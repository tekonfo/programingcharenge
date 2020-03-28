N, X, Y = map(int, input().split())
dic = [0 for _ in range(N-1)]

for f in range(1,  N):
  for t in range(f+1, N+1):
    print(f,t)
    if f <= X and Y <= t:
      d = (X - f) + (t - Y)
    else:
      d = t-f-1
    print(d)
    dic[d] += 1

print("")

for d in dic:
  print(d)