import sys
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

for a,b,c in points:
  if c>0:
    a,b,c
    break

f = lambda x, y: abs(a-x) + abs(b-y)

for i in range(101):
  for j in range(101):
    height = f(i, j) + c
    flg = True
    for x, y, h in points:
      # if height != max(h + f(x, y), 0):
      # これだとダメだった。コーナーケースがダメになるパターンってわからないことが多いから、問題文を忠実に実装するのがベター
      if h != max(height - abs(x-i) - abs(y-j) , 0):
        flg = False
        break
    if flg:
      print(i, j, height)
      sys.exit()

