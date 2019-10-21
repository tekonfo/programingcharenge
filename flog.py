INF = 1000
N = int(input())
h = list(map(lambda x: int(x), input().split()))
# DP 配列全体を「DP の種類に応じた初期値」で初期化
# dp[i] はノードiにたどり着くまでの最小コスト
dp = [INF for _ in range(N)]

# 初期条件を入力
dp[0] = 0
dp[1] = abs(h[0] - h[1])

# ループを回す
for i in range(0, N - 2):
    dp[i + 2] = min(dp[i + 1] + abs(h[i + 2] - h[i + 1]), dp[i] + abs(h[i + 2] - h[i]))

# テーブルから解を得て出力
print(dp[N - 1])
