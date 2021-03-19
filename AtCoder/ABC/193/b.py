# O(N)になるはず

ans = 1e10

n = int(input())
for i in range(n):
    # aは徒歩A分、pはP円, xは在庫
    a, p, x = map(int, input().split())

    # 入力は全て整数なので、徒歩の数分だけ在庫が減る
    if x - a <= 0:
        continue

    if ans > p:
        ans = p

if ans != 1e10:
    print(ans)
else:
    print(-1)
