# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d
import pprint

INF = 10000


def dijkstra(map, start):
    length = len(map)
    answer = [INF for i in range(length)]
    used = [False for i in range(length)]
    answer[start] = 0

    while True:
        # pprint.pprint(answer)
        v = -1

        # 使われていない経路の中で最小のものをだす
        # ここで次に行く点が決定する
        for i in range(length):
            if used[i] is False and (v == -1 or answer[v] > answer[i]):
                v = i

        if v == -1:
            break
        used[v] = True

        # 最小経路をだす
        for i in range(length):
            answer[i] = min(answer[i], answer[v] + map[i][v])

    # return array
    return answer


N, M, S, T = map(lambda x: int(x), input().split())
yen_map = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
sunuku_map = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    u, v, a, b = map(lambda x: int(x), input().split())
    # 逆の道順でも同じコストにする
    yen_map[u][v] = a
    yen_map[v][u] = a
    sunuku_map[u][v] = b
    sunuku_map[v][u] = b

yen_ans = dijkstra(yen_map, S)
sunuku_ans = dijkstra(sunuku_map, S)
pprint.pprint(yen_ans)
pprint.pprint(sunuku_ans)
