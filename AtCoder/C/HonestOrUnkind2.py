# N = int(input())
# true_humans = []

# for i in range(2**3):
#     ls = [False for n in range(N)]
#     for j in range(len(ls)):
#         if (i >> j) & 1:
#             ls[j] = True
#     true_humans.append(ls)    
    

# testimonys = []
# for n in range(N):
#   A = int(input())
#   tmp = {}
#   for a in range(A):
#     x, y = map(int, input().split())
#     y = bool(y)
#     tmp[x] = y
#   testimonys.append(tmp)

# true_mem = 0

# for humans in true_humans:
#   flg = True
#   for human_index in range(len(humans)):
#     is_true_man = humans[human_index]
#     values = testimonys[human_index]
#     for key, value in values.items():
#       value = value if is_true_man else not value
#       if value != humans[key-1]:
#         flg = False
#         break
#     if not flg:
#       break
#   if flg:
#     true_mem = max(true_mem, sum([1 for i in humans if i == True]))
  
# print(true_mem)
  



import itertools
 
n = int(input())
l =[]
 
for _ in range(n):
  a = int(input())
  m = []
  for _ in range(a):
    xn, yn = map(int, input().split())
    m.append([xn-1, yn])
  l.append(m)
 
for i in itertools.product([1, 0], repeat=n):
  i = list(i)
  flg = 0
  for j in range(n):
    for x, y in l[j]:
      if i[j] == 1 and i[x] != y:
        flg += 1
        break
  if flg == 0:
    break
    
print(sum(i))