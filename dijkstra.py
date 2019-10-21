INF = 10000

class Dijkstra():

    def __init__(self, n, costs):
        self.node_count = n
        self.costs = costs
        self.used = [False for i in range(n)]
        # total_costはスタート地点から添字までへの最短距離を記録するもの
        self.total_cost = [0 for i in range(n)]

    def return_cost(self):
        while True:
            # 一番小さい経路の発見
            for i in range(self.node_count):
                min_value_point = -1
                if not self.used[i] and min_value_point == -1 and self.costs[i] < self.costs[min_value_point]:
                    min_value_point = i
                    print(min_value_point)
            if min_value_point == -1:
                break

            self.used[min_value_point] = True

            for i in range(self.node_count):
                if self.total_cost[i] > self.costs[min_value_point][i] + self.total_cost[min_value_point]:
                    self.total_cost[i] = self.costs[min_value_point][i] + self.total_cost[min_value_point]

        return self.total_cost[self.node_count - 1]


route = [
    [INF, 2, 3, INF, INF, INF],
    [2, INF, 4, 3, 5, INF],
    [3, 4, INF, 6, 4, INF],
    [INF, 3, 6, INF, 1, 5],
    [INF, 5, 4, 1, INF, 3],
    [INF, INF, INF, 5, 3, INF]]

dijkstra = Dijkstra(len(route), route)
print(dijkstra.return_cost())
