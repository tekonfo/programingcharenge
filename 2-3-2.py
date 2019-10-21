def make_array(n, array):
    if(n == 0):
        return array
    return make_array(n - 1, [array] * 7)


# サイコロの数, 出た目の積
N, D = (int(x) for x in input().split())
# N次元配列作成, 初期値は0
saikoro_lists = [[0 for i in range(7)] for j in range(7)]
print(saikoro_lists)
# 0 ~ 5
for a in range(1, 7):
    for b in range(1, 7):
        saikoro_lists[a][b] = a * b

print(saikoro_lists)
