N = int(input())
AList = list(map(int, input().split()))
sumFee = 0

# 全てを回った時の料金を求める
sumFee += abs(AList[0])
for i in range(1, N):
  sumFee += abs(AList[i] - AList[i - 1])
sumFee += abs(AList[N-1])

# Iを抜かした時の料金を求める
for i in range(N):
  low_i = abs(AList[i] - AList[i-1]) if i != 0 else abs(AList[0])
  high_i = abs(AList[i + 1] - AList[i]) if i != N - 1 else abs(AList[N-1])
  if i == 0 :
    mix_i = abs(AList[i + 1])
  elif i == N - 1 :
    mix_i = abs(AList[i - 1])
  else:
    mix_i = abs(AList[i + 1] - AList[i - 1])
  
  print(sumFee - low_i - high_i + mix_i)


# 
# n=int(input())
# l=[0]+list(map(int,input().split()))+[0]
# f=lambda x,y:abs(l[x]-l[y])
# s=sum(f(i+1,i) for i in range(n+1))
# for i in range(n): print(s-f(i+1,i)-f(i+2,i+1)+f(i+2,i))