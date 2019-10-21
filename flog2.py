INF = 1000
N, K = map(lambda x: int(x), input().split())
h = list(map(lambda x: int(x), input().split()))
# DP 配列全体を「DP の種類に応じた初期値」で初期化
# dp[i] はノードiにたどり着くまでの最小コスト
dp = [INF for _ in range(N)]

# 初期条件を入力
dp[0] = 0
dp[1] = abs(h[0] - h[1])

# ループを回す
# 今回は配るDP
for i in range(0, N):
    for k in range(K):
        if i + k >= N:
            continue
        print(i, k)
        dp[i + k] = min(dp[i + k], dp[i] + abs(h[i] - h[i + k]))

# テーブルから解を得て出力
print(dp)
