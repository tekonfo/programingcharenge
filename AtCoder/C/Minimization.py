import math,sys

N, K = map(int, input().split())
window = K - 1
A = list(map(int, input().split()))
# mi_index = A.index(min(A))
# left_count = math.ceil(mi_index / (K - 1))
# right_count = math.ceil((N - (mi_index + 1)) / (K - 1))
# left = mi_index
# right = mi_index
# while left > 0 or right < N-1:
#   if left >= 0 and left > window:
#     left -= window
#   elif N - 1 - right >= window:
#     right += window
  
#   print(left, right)


l = K
count = 1
if l >= N:
  print(count)
  sys.exit()
  
while l < N:
  l += K - 1
  count += 1

print(count)