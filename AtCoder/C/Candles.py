"""
はじめ全探索するところがOを意識すればもう少し納得感のいく回答を作ることができた
０からスタートするところで難しく考えすぎた

"""
INF = 1000000000
N, K = list(map(int, input().split()))
items = list(map(int, input().split()))

mi = INF

for l_index in range(N-K+1):
  left = items[l_index]
  right = items[l_index+K-1]

  if right <= 0:
    mi = min(mi, 0-left)
  elif left >= 0:
    mi = min(mi, right)
  else:
    min_l = min(0-left, right)
    mi = min(mi, (0-left) + right + min_l)

print(mi)