import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
count = 0
# ソートして
for b in B:
  upeer_b = N - bisect.bisect_right(C, b)
  downer_b = bisect.bisect_left(A, b)
  count += upeer_b * downer_b

# for c in C:
#   under_c = bisect.bisect_left(B, c)
#   for b in B[:under_c]:
#     under_b = bisect.bisect_left(A, b)
#     count += under_b

print(count)
