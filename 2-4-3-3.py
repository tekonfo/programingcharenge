from unionfind import UnionFind

N, K, L = map(lambda x: int(x), input().split())

road_ways = []
rail_ways = []

for _ in range(K):
    road_ways.append(list(map(lambda x: int(x) - 1, input().split())))
for _ in range(L):
    rail_ways.append(list(map(lambda x: int(x) - 1, input().split())))
print(road_ways, rail_ways)

# 道路、鉄道を記録するUnionFind宣言
road_unionfind = UnionFind(N)
rail_unionfind = UnionFind(N)

# UnionFindを鉄道、道路それぞれで作成
for k in range(K):
    road_unionfind.unite(road_ways[k][0], road_ways[k][1])
for l in range(L):
    rail_unionfind.unite(rail_ways[l][0], rail_ways[l][1])

ans = [0 for _ in range(N)]
for n in range(N):
    # 自分自身は必ず一致しているので１スタート
    sum = 0
    for k in range(N):
        # 鉄道、道路のどちらでも繋がっているならインクリメント
        if road_unionfind.same(n, k) and rail_unionfind.same(n, k):
            sum += 1
    ans[n] = sum

print(*ans)
