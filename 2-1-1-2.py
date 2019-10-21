# https://atcoder.jp/contests/abc002/tasks/abc002_4
class Tree():
    def __init__(self, n, costs):
        self.left
        self.right


def make_tree(count, from_id_lists):
    for i in range(len(relation_map)):
        if relation_map[i] == [from_id, count]:
            make_tree(count+1, )

    make_tree(count+1, from_id, 0)


N, M = map(lambda x: int(x), input().split())
relation_map = []
for i in range(1, N + 1):
    relation_map.append([0, i])
max_count = 0
# relation_map作成
for _ in range(N):
    a = list(map(lambda x: int(x + 1), input().split()))
    relation_map.append(a)

make_tree(0, 0)
