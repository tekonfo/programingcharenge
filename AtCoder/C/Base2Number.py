# ToDo
# まだ正味よくわかってない

N=int(input())
if N==0:
  print(0)
  exit()
  
S=''
while N!=0:
  if N%2==0:
    S='0'+S
    N//=-2
  else:
    S='1'+S
    N-=1
    N//=-2
print(S)