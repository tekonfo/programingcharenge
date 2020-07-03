# cost[u][v] はuからvの経路のコスト
cost = [[INF for _ in range(N)]for _ in range(N)]
# 頂点sからの最短経路
d = [INF for _ in range(N)]
# 既に使われたのかのフラグ
used = [False for _ in range(N)]

# このやり方だとO(N**2)
def dijkstra(s, cost, d, used):
    d[s] = 0
    while (True):
        print(d)
        print(used)
        v = -1
        # 初めはゼロからスタートして、そこから最短経路の点を拾っていく
        for u in range(N):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break
        
        used[v] = True
        for u in range(N):
            d[u] = min(d[u], d[v] + cost[v][u])
    return d

dijkstra(0, cost, d, used)