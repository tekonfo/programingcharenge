path = 'input.txt'
path_w = 'output.txt'
tmp_count = 0
list = []

with open(path) as f:
    for s_line in f:
        if tmp_count == 0:
            N, M = map(lambda x: int(x), s_line.split())
            tmp_count += 1
            continue
        list.append(int(s_line))

# 逆順にソート
list.sort(reverse=True)

sum = 0
for _ in range(4):
    for i in range(N):
        if sum + list[i] < M:
            sum = sum + list[i]
            break


with open(path_w, mode='w') as f:
    f.write(str(sum))
