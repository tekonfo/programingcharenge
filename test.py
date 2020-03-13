import math
N, M = map(int, input().split())

t = 100 * (N - M) + 1900 * M

ans = t * (2 ** M)

print(int(ans))