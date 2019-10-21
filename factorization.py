from collections import Counter


#  [(要素, 出現回数), (要素, 出現回数)]というようなタプルのリストを作成する
def counter(array):
    return list(Counter(array).most_common())


# combを実装する
def comb_cal(n, r):
    tmp = 1
    for i in range(r):
        tmp *= (n - i)
    for i in range(r):
        tmp //= r - i
    return tmp


N, M = map(int, input().split())
MOD = 10 ** 9 + 7

frac = []

# 約数の列挙
while True:
    for i in range(2, int(M**(1/2))+1):
        if M % i == 0:  # 割り切れるかどうか
            frac.append(i)  # 配列に代入する
            M //= i  # 値で割る
            break  # 値を一回入れたらまたWhileに戻る
    break
if M > 1:
    frac.append(M)

c = counter(frac)

ans = 1
for x in c:
    ans *= (comb_cal(x[1] + N-1, x[1]) % MOD)
    ans %= MOD
print(ans)
