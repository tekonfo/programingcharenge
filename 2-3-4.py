n, k = map(int, input().split())
dp = [[1e9] * (n + 1) for _ in range(n + 1)]

dp[0][0] = 0
num = 0
win = 0
for i in range(n):
    a = int(input())
    for j in range(i + 1):
        if num != 0:
            win = a * dp[i][j] // num
        dp[i + 1][j + 1] = min(dp[i][j] + win + 1, dp[i][j + 1])
    num += a
print(dp)

ans = 0
for i in range(n, -1, -1):
    if dp[n][i] <= k:
        ans = i
        break
if k == num:
    ans = 1
print(ans)
