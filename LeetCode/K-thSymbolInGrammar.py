class Solution:
    mapping = ((0, 1), (1, 0))

    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        return self.mapping[self.kthGrammar(N - 1, K // 2 + K % 2)][(K - 1) % 2]

sol = Solution()
N = 3
K = 2
print(sol.kthGrammar(N, K))