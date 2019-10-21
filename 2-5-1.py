# 再帰の深さが1000を超えそうなときはこれをやっておく
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
es = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    es[a].append(b)
    es[b].append(a)

colors = [0 for i in range(N)]


# 頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse


def dfs(v, color):
    # 今いる点を着色
    colors[v] = color
    # 今の頂点から行けるところをチェック
    for to in es[v]:
        # 同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        # 未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    # 調べ終わったら矛盾がないのでTrue
    return True

# 2部グラフならTrue, そうでなければFalse


def is_bipartite():
    return dfs(0, 1)  # 頂点0を黒(1)で塗ってDFS開始


if is_bipartite():
    b = (sum(colors) + N) // 2
    w = N-b
    print(b*w - M)
else:
    all = N*(N-1) // 2
    print(all - M)
