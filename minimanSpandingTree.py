INF = 10000


class MinSpandTree():
    def __init__(self, n, cost):
        self.v = n
        self.cost = cost
        self.used = [False for i in range(n)]
        self.mincost = [INF for i in range(n)]

    def prim(self):
        self.mincost[0] = 0
        ans = 0
        while True:
            v = -1
            for u in range(self.v):
                # print("u = {}, mincost[u] = {}, v = {}, mincost[v] = {}".format(u, self.mincost[u], v, self.mincost[v]))
                if not self.used[u] and (v == -1 or self.mincost[u] < self.mincost[v]):
                    # print("v changed to {}".format(u))
                    v = u

            if v == -1:
                break
            self.used[v] = True
            ans += self.mincost[v]

            # 経路に応じて最小を初期化する
            for u in range(self.v):
                # 新しくセットした経路から少ないコストの経路がないのかを探す、更新する
                self.mincost[u] = min(self.mincost[u], self.cost[v][u])
                # print(min(self.mincost[u], self.cost[v][u]))

        return ans


V, E = map(lambda x: int(x), input().split())
array = [[INF for i in range(V)] for i in range(V)]
for _ in range(E):
    a, b, cost = map(lambda x: int(x), input().split())
    array[a][b] = cost
    array[b][a] = cost
min_spand_tree = MinSpandTree(V, array)
print(min_spand_tree.prim())
