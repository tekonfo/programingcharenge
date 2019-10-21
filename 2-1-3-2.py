# https://atcoder.jp/contests/abc007/tasks/abc007_3
from collections import deque
import pprint

R, C = map(lambda x: int(x), input().split())
sy, sx = map(lambda x: int(x), input().split())
gy, gx = map(lambda x: int(x), input().split())
rab_map = []
rab_map.append([0 for _ in range(C + 1)])
for i in range(R):
    one_row = list(map(lambda x: 1 if x == "." else 0, list(input())))
    one_row.insert(0, 0)
    rab_map.append(one_row)

queue = deque([])
queue.append([sy, sx, 0])
ans = 0
while len(queue) > 0:
    current_queue = queue.pop()
    y = current_queue[0]
    x = current_queue[1]
    count = current_queue[2]
    # すでに到達した場所はcountにする
    if count > 1:
        rab_map[y][x] = count
    else:
        rab_map[y][x] = 2
    ans = count
    if gy == y and gx == x:
        break

    if 0 <= y - 1 and rab_map[y - 1][x] == 1:
        queue.appendleft([y - 1, x, count + 1])
    if y + 1 <= C - 1 and rab_map[y + 1][x] == 1:
        queue.appendleft([y + 1, x, count + 1])
    if 0 < x - 1 and rab_map[y][x - 1] == 1:
        queue.appendleft([y, x - 1, count + 1])
    if y + 1 <= C - 1 and rab_map[y][x + 1] == 1:
        queue.appendleft([y, x + 1, count + 1])

print(ans)
