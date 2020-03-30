
INF = 10 ** 10
N = int(input())
ans = [0 for i in range(33)]

count = 0
while N != 0 or count == 10:
  val = INF

  if N > 0:
    index = 0
  else: 
    index = 1

  while abs(N - -2**index) >= val:
    val = abs(N - -2**index)
    index += 2

  print(index)

  count += 1
  ans[index] = 1
  N -= -2**index
  print("N*{}".format(N))
print(ans)



  

