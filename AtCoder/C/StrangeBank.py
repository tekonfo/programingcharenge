N = int(input())
dp = [i for i in range(100000+1)]
arr_6 = [6**i for i in range(11)]
arr_9 = [9**i for i in range(11)]
for index in range(100000+1):
  tmp = [v for v in arr_6 if index >= v]
  if len(tmp) != 0:
    tmp = tmp[-1]
    dp[index] = min(dp[index], dp[index - tmp] + 1)

  tmp = [v for v in arr_9 if index >= v]
  if len(tmp) != 0:
    tmp = tmp[-1]
    dp[index] = min(dp[index], dp[index - tmp] + 1)

print(dp[N])

# 間違っているパターン
# N = int(input())
# dp = [i for i in range(100000+1)]
# arr_6 = [6**i for i in range(11)]
# arr_9 = [9**i for i in range(11)]
# for index in range(100000+1):
#   tmp = [v for v in arr_6 if index >= v]
#   if len(tmp) == 0:
#     continue
#   tmp = tmp[-1]
#   dp[index] = min(dp[index], dp[index - tmp] + 1)
# # これforを分割してしまうと、9の最小のパターン→6の最小のパターンの場合をカバーできなくなる
# for index in range(100000+1):
#   tmp = [v for v in arr_9 if index >= v]
#   if len(tmp) == 0:
#     continue
#   tmp = tmp[-1]
#   dp[index] = min(dp[index], dp[index - tmp] + 1)
# print(dp[N])

