# より簡単な問題から考えていく

# k = 0の場合をまず考える
# その場合は、N*(N-1)*(N-1)...のようになる。

# k= xの場合を考える
# グループの色の割当：N＊（Nー1）^(N-x-1)
# これは、つながっている数字である隣同士のブロックである場合に、一つのブロックとして見なすとこのようになる
# グループの分け方：N-1コンビネーションxで求められる

mod = 998244353
 
n, m, k = map(int, input().split())
count = 0
 
comb = 1
for i in range(k + 1):
  # グループの色の割当方
  tmp = comb * m * pow(m-1, n-i-1, mod) % mod
  count = (count + tmp) % mod
  # コンビネーションの計算方法
  # ここよくわからん！！！
  comb = comb * (n - i - 1) * pow(i+1, mod-2, mod) % mod
  print(comb)
print(count)