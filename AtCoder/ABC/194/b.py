n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]

for i in range(n):
  a[i],b[i] = map(int, input().split())

## 1eXは10のX乗の意味
## 総当りで計算しても時間的には大丈夫
ans = 1e6+5
for i in range(n):
  for j in range(n):
    ans = min(ans, a[i]+b[j] if i==j else max(a[i], b[j]))

print(ans)
