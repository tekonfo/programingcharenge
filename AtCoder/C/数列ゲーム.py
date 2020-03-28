def calc(start, end):
  a = 0
  t = 0
  # startが奇数→青木くんは偶数の列
  if start % 2 == 1:
    a = even_sum[end] - even_sum[start]
    t = odd_sum[end] - odd_sum[start]
  else:
    t = even_sum[end] - even_sum[start]
    a = odd_sum[end] - odd_sum[start]
  return a, t 


N = int(input())
L = list(map(int, input().split()))

odd_sum = [0 for _ in range(N)]
even_sum = [0 for _ in range(N)]

# 偶数、奇数番号の二つの累積和を先に計算しておく
for i in range(N):
  if i % 2 == 1:
    even_sum[i] = even_sum[i-1] + L[i]
    odd_sum[i] = odd_sum[i-1]
  else:
    even_sum[i] = even_sum[i-1]
    odd_sum[i] = odd_sum[i-1] + L[i]

print(odd_sum, even_sum)

a_ans = 0
t_and = 0

# 高橋くんの選択する丸を決める
for i in range(N):
  a_max = 0
  t_max = 0
  # 青木くんの選択する丸を決める
  for s in range(N):
    if i == s:
      continue
    if i < s:
      a, t = calc(i, s)
    else:
      a, t = calc(s, i)
    # ここ一番左のっていう制約無視してない？
    if a_max < a and t_max < t:
      a_max = a
      t_max = t

print(a_ans)


  

