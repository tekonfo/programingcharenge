# N, M = map(int, input().split())
# X, Y = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))



# rounds = 0
# time = 0
# is_a = 1
# while True:
#   if is_a:
#     if len(A) == 0:
#       break

#     if time <= A[0]:
#       is_a = 0
#       time = A[0] + X
#     else:
#       A.pop(0)
#   else:
#     if len(B) == 0:
#       break

#     if time <= B[0]:
#       is_a = 1
#       time = B[0] + Y
#       rounds += 1
#     else:
#       B.pop(0)

# print(rounds)

import bisect
N,M=map(int,input().split(' '))
X,Y=map(int,input().split(' '))
A,B=[list(map(int,input().split(' '))) for _ in range(2)]
ans = 0
t=A[0]+X
while t <= B[-1]:
    t=B[bisect.bisect_left(B,t)]
    t+=Y
    ans += 1
    if t <=A[-1]:
        t = A[bisect.bisect_left(A,t)]+X
    else:
        break
print(ans)