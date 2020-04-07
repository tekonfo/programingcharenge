# from itertools import combinations
# from itertools import combinations_with_replacement
# N = int(input())
# lists = list(map(int, input().split()))
# ans = []
# tmp = []
# for i in range(len(lists)):
#   tmp.append(i+1)
#   if i == len(lists) - 1:
#     combi = combinations_with_replacement(tmp, 2)
#     for a,b in combi:
#       if a <= b:
#         ans.append(tuple([a,b]))
#     break
#   # 次が大きくなければ、ここで処理
#   if lists[i] >= lists[i+1]:
#     combi = combinations_with_replacement(tmp, 2)
#     for a,b in combi:
#       if a <= b:
#         ans.append(tuple([a,b]))
#     tmp = []
# print(len(ans))



N = int(input())
A = list(map(int, input().split()))
p = 0
ans = 1
for i in range(1, N):
    if A[i]<=A[i-1]:
        p = i
    ans += i-p+1
print(ans)