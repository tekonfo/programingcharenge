count = 0
x = int(input())
count = int(x/11)
x -= count*11
if x == 0:
  print(2*count)
elif x <= 6:
  print(2*count+1)
else:
  print(2*count+2)