def A():
    V, T, S, D = map(int, input().split())
    vanish_start = V * T
    vanish_end = V * S
    if vanish_start <= D <= vanish_end:
        print('No')
    else:
        print('Yes')

# 0が先頭に来たらどうしよう
# 一つも整数がない場合はどうしよう
def B():
    N, X = map(int, input().split())
    As = list(map(int, input().split()))

    Bs = []
    for i in range(N):
        if As[i] == X:
            continue
        Bs.append(str(As[i]))
    if len(Bs) == 0:
        print('')
    else:
        print(' '.join(Bs))
