N,M=map(int,input().split())

lists = [[] for _ in range(N)]
items = [list(map(int, input().split())) for _ in range(M)]
for p, y in items:
  lists[p-1].append(y)

dic = {}

for n in range(N):
  lists[n].sort()  

for n in range(N):
  l = lists[n]
  count = 1
  for i in l:
    dic[i] = count
    count+=1

for p, y in items:
  #ToDo これどういう書き方？
  print("{:06g}{:06g}".format(p,dic[y]))