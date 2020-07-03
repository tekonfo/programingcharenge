"""
https://atcoder.jp/contests/abc035/tasks/abc035_d

確かに各点を渡り歩く必要はない。
各点に最短経路で進み、そこからどれだけ報酬を得ることができるのかを考える
そうか、有向グラフだから行き道と帰り道が異なっている。
有向辺の向きを逆側にした際に帰り道が求まる。
答えの形、
1: 有向グラフの最短経路を求める
2: 辺の向きを逆転させ、最短経路を求める
3: それぞれの点において、得られる金額の最大値を求める
4: 結果を出力

ダイクストラさえきちんとできれば解ける
"""
INF = 10000000
N, M, T = map(int, input().split())
prices = list(map(int, input().split()))
# まずダイクストラをどうやって実装するのかを考えないといけない

# cost[u][v] はuからvの経路のコスト
cost = [[INF for _ in range(N)]for _ in range(N)]
rev_cost = [[INF for _ in range(N)]for _ in range(N)]
# 頂点sからの最短経路
d = [INF for _ in range(N)]
rev_d = [INF for _ in range(N)]
# 既に使われたのかのフラグ
used = [False for _ in range(N)]
rev_used = [False for _ in range(N)]

for m in range(M):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = c
    rev_cost[b-1][a-1] = c

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

d = dijkstra(0, cost, d, used)
rev_d = dijkstra(0, rev_cost, rev_d, rev_used)
max_price = 0
for n in range(N):
    remaining_time = T - (d[n] + rev_d[n])
    if remaining_time <= 0:
        continue
    max_price = max(max_price, remaining_time*prices[n])
print(max_price)
