n=int(input())
a=list(map(int,input().split()))
ans=-10**18
for i in range(n):
  x=0
  y=-10**18
  for j in range(n):
    if i==j:
      continue
    tmp_x=sum(a[min(i,j):max(i,j)+1:2])
    tmp_y=sum(a[min(i,j)+1:max(i,j)+1:2])
    if tmp_y>y:
      y=tmp_y
      x=tmp_x
  ans=max(ans,x)
print(ans)