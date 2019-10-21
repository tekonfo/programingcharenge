# https://atcoder.jp/contests/abc007/tasks/abc007_3
from collections import deque

length = list(map(lambda x: int(x), input('length = ').split()))
start = list(map(lambda x: int(x), input('start = ').split()))
end = list(map(lambda x: int(x), input('end = ').split()))
maze = [[0 for column in range(length[0])] for row in range(length[1])]
for i in range(length[0]):
    # 壁は1, 何にもない箇所は0
    maze[i] = list(map(lambda x: 1 if x == '#' else 0, list(input(''))))
# スタートからどれくらいの距離なのかをqueueの末尾に記録する。
start_clock = 0
queue = deque([start])
ans = 0

while len(queue) < 1:
    target = queue.popleft()
    # 一致処理
    if target[0] == end[0] and target[1] == end[1]:
        ans = target[2]
        break
    for i in range(-1, 1):
        for k in range(-1, 1):
            if i == 0 and k == 0 or target[0] + i < 0 or target[0] + i > length[0] or target[1] + k < 0 or target[1] + k > length[1]:
                continue
            if maze[target[0] + i][target[1] + k] == 0:
                queue = deque([target[0] + i, target[1] + k, target[2] + 1])

print(ans)
