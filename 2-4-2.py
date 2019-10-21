from collections import Counter
import random

N = int(input())
s = []
for n in range(N):
    s.append(input())

M = int(input())
T = []
for m in range(M):
    T.append(input())

# 単語数が辞書で帰ってくる
count_s = Counter(s)

for t in range(len(T)):
    if T[t] in count_s:
        count_s[T[t]] -= 1
    else:
        count_s[T[t]] = -1

count_s[str(random.random())] = 0

print(max(count_s.values()))
