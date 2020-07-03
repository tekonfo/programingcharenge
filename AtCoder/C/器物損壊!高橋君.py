# # https://code3kaku.hatenablog.com/entry/2018/12/06/221212
# # ここの図示がわかりやすい

# from collections import deque

# INF = 10000000000

# H, W = map(int, input().split())
# is_checked = [[False for _ in range(W)] for _ in range(H)]
# min_break_board = [[INF for _ in range(W)] for _ in range(H)]
# up_down_left_light = [[-1,0], [1,0], [0,-1], [0,1]]

# board = []
# for h in range(H):
#     line = list(input())

#     if 's' in line:
#         start = [h, line.index('s')]
#     if 'g' in line:
#         goal = [h, line.index('g')]
#     board.append(line)

# queue = deque()
# min_break_board[start[0]][start[1]] = 0
# queue.appendleft([start[0], start[1], 0])

# c = 0

# while queue:
#     # BFSだから先入先出し
#     y, x, count = queue.popleft()
#     if is_checked[y][x]:
#         continue

#     if board[y][x] == '#':
#         count += 1
#     min_break_board[y][x] = min(min_break_board[y][x], count)

#     is_checked[y][x] = True

#     # 周りのものを更新する
#     for ver, axi in up_down_left_light:
#         tmp_y = ver + y
#         tmp_x = axi + x
#         if 0 <= tmp_y <= H - 1 and 0 <= tmp_x <= W - 1:
#             prev = min_break_board[tmp_y][tmp_x]
#             if board[tmp_y][tmp_x] == "#":
#                 min_break_board[tmp_y][tmp_x] = min(min_break_board[tmp_y][tmp_x], count+1)
#             else:
#                 min_break_board[tmp_y][tmp_x] = min(min_break_board[tmp_y][tmp_x], count)

#     # 周りの点で到達していないものがあればキューにいれる
#     # 周りのものを更新する
#     for ver, axi in up_down_left_light:
#         tmp_y = ver + y
#         tmp_x = axi + x
#         if 0 <= tmp_y <= H - 1 and 0 <= tmp_x <= W - 1 and not is_checked[tmp_y][tmp_x]:
#             queue.append([tmp_y, tmp_x, count])

# if 0 <= min_break_board[goal[0]][goal[1]] <= 2:
#     print("Yes")
# else:
#     print("No")

from collections import deque
 
def solve(h, w, c):
    s=c.index('s')
    g=c.index('g')
    d=(-w-6,-1,1,w+6)
    v=set()
    chk=deque([(0,s)])
    while chk:
        b,x=chk.popleft()
        if x==g:
            return True
        if x in v:
            continue
        v.add(x)
        for dx in d:
            nx=x+dx
            if nx in v:
                continue
            if c[nx]=='#':
                if b<2:
                    chk.append((b+1,nx))
            else:
                chk.appendleft((b,nx))
    return False
 
h,w=map(int,input().split())
c='#'*(w+6)*3
c+=''.join('###'+input()+'###' for _ in range(h))
c+='#'*(w+6)*3
print('YES' if solve(h,w,c) else 'NO')