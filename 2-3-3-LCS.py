import pdb;


# iはlistsの添字
def lcs(x, y):
    if x == len(X) - 1 or y == len(Y) - 1:
        return memo[x][y]
    if X[x] == Y[y]:
        memo[x + 1][y + 1] = max(memo[x][y] + 1, lcs(x + 1, y), lcs(x, y + 1))
    else:
        memo[x + 1][y + 1] = max(lcs(x + 1, y), lcs(x, y + 1))
    return memo[x][y]

  # for (int i = 0; i < S.size(); ++i) {
  #   for (int j = 0; j < T.size(); ++j) {
  #     if (S[i] == T[j]) dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1);
  #     dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j]);
  #     dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1]);
  #   }
  # }

n = int(input())
lists = []
for i in range(n):
    X = input()
    Y = input()
    memo = [[0 for i in range(len(Y))] for j in range(len(X))]
    lcs(0, 0)
    print(memo)
    print(memo[len(X) - 1][len(Y) - 1])
