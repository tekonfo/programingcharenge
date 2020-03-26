def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N =int(input())

facters = {}

for i in range(1, N+1):
  # 約数を求める
  arr = factorization(i)
  for key,value in arr:
    if key in facters:
      facters[key] += value
    else:
      facters[key] = value

ans = 1

facters.pop(1)

for value in facters.values():
  ans *= value + 1 
  ans = ans % (10**9 + 7)
print(ans)