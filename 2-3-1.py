# https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_B
def dp(i, j):
    if dp_list[i][j] != 0:
        return dp_list[i][j]
    if i == len(lists):
        return 0
    if j < lists[i][1]:
        dp_list[i][j] = dp(i + 1, j)
        return dp_list[i][j]
    else:
        dp_list[i][j] = max(dp(i + 1, j), dp(i + 1, j - lists[i][1]) + lists[i][0])
        return dp_list[i][j]


N, W = (int(x) for x in input().split())
# value, weightの順で並んでいる
lists = []
for i in range(N):
    lists.append(list(map(lambda x: int(x), input().split())))
dp_list = [[0 for i in range(W + 1)] for j in range(N + 1)]
print(dp(0, W))
