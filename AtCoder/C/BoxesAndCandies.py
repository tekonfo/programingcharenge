# def calc(ran, count, cans, X):
#   for n in ran:
#     if n == 0:
#       while cans[n+1] + cans[n] > X:
#         cans[n] -= 1
#         count += 1  
#       continue
#     if n + 1 == N:
#       while cans[n-1] + cans[n] > X:
#         cans[n] -= 1
#         count += 1  
#       continue
#     while cans[n-1] + cans[n] > X or cans[n+1] + cans[n] > X:
#       cans[n] -= 1
#       count += 1
#   return count, cans

# N, X = map(int, input().split())
# cans = list(map(int, input().split()))

# count = 0

# # odd_range = range(1, N, 2)
# # even_range = range(0, N, 2)
# # count, cans = calc(odd_range, count, cans, X)
# # count, cans = calc(even_range, count, cans, X)

# # even_count = count
# # print(min(odd_count, even_count))

# for i in range(0, N-1):
#   if cans[i] + cans[i+1] > X:
#     cans[i+1] -= X - cans[i]
#     count += 1
# print(count)
n, x = map(int, input().split())
l = list(map(int, input().split()))
 
y = 0
if l[0] > x:
    w = l[0] - x
    y += w
    l[0] -= w
 
for i in range(n-1):
    if l[i] + l[i+1] > x:
        z = l[i+1] + l[i] - x
        y += z
        l[i+1] -= z
 
print(y)