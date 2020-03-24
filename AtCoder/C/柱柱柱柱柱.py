func = lambda x, y: int(abs(x - y))
N = int(input())
trees = list(map(int, input().split()))
dp = [0 for i in range(N)]
dp[1] = func(trees[1], trees[0])
for index in range(2, N):
  b_1 = dp[index - 1] + func(trees[index - 1], trees[index])
  b_2 = dp[index - 2] + func(trees[index - 2], trees[index])
  dp[index] = min(b_1, b_2)
print(dp[N-1])