# UnionFind
class UnionFind(object):
    # 親を表す配列 木はこの配列で表現する
    par = []
    rank = []

    def __init__(self, arg):
        super(UnionFind, self).__init__()
        self.par = [i for i in range(arg)]
        self.rank = [0 for i in range(arg)]

    # 木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # xとyの属する集合を結合
    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        else:
            self.par[root_x] = root_y
            # それぞれの高さが一致する場合のみrankを更新する
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)
