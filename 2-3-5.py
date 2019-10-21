INF = 1000
# int N, M, L, X, A[10101], dp[10101][1010];
# //---------------------------------------------------------------------------------------------------
# void _main() {
#     cin >> N >> M >> L >> X;
#     rep(i, 0, N) cin >> A[i];
#
#     rep(i, 0, N + 1) rep(j, 0, M) dp[i][j] = inf;
#     dp[0][0] = 1;
#
#     rep(i, 0, N) rep(j, 0, M) {
#         if (M <= j + A[i]) {
#             int x = A[i];
#             int d = 0;
#
#             d++;
#             x -= M - j;
#
#             d += x / M;
#             x %= M;
#
#             chmin(dp[i + 1][x], dp[i][j] + d);
#         }
#         else chmin(dp[i + 1][j + A[i]], dp[i][j]);
#         chmin(dp[i + 1][j], dp[i][j]);
#     }
#
#     if (dp[N][L] <= X) printf("Yes\n");
#     else printf("No\n");


#     cin >> N >> M >> L >> X;
#     rep(i, 0, N) cin >> A[i];

#     rep(i, 0, N) rep(j, 0, M) {
#         if (M <= j + A[i]) {
#             int x = A[i];
#             int d = 0;
#
#             d++;
#             x -= M - j;
#
#             d += x / M;
#             x %= M;
#
#             chmin(dp[i + 1][x], dp[i][j] + d);
#         }
#         else chmin(dp[i + 1][j + A[i]], dp[i][j]);
#         chmin(dp[i + 1][j], dp[i][j]);
#     }
A = []
N, M, L, X = map(lambda x: int(x), input().split())
for i in range(N):
    A[i] = int(input())
dp = [[INF for _ in range(M)] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(M):
        if(M <= j + A[i]):
