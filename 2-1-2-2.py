# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

def remove_one_island(height, weight):
    if island_map[height][weight] == 1:
        island_map[height][weight] = 0
        for s in range(-1, 2):
            for i in range(-1, 2):
                if 0 <= height+s and height+s <= h-1 and 0 <= weight+i and weight+i <= w-1:
                    remove_one_island(height+s, weight+i)


while True:
    w, h = map(lambda x: int(x), input().split())
    island_map = []
    if w == 0 and h == 0:
        exit()
    for i in range(h):
        island_map.append(list(map(lambda x: int(x), input().split())))

    count = 0
    for s in range(h):
        for i in range(w):
            if island_map[s][i] == 1:
                count += 1
                remove_one_island(s, i)

    print(count)
