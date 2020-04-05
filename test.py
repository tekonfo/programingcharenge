# import sys
# K = int(input())
# anss = [set([str(i) for i in range(1,10)])]
# count = 9
# if K <= 9:
#   print(K)
#   sys.exit()

# for i in range(1, 15):
#   origin = anss[i-1]
#   ans = []
#   for j in range(10):
#     print(j, ans)
#     l = list(origin)
#     for index in range(len(l)):
#       word = l[index]
#       if abs(int(word[-1]) - j) <= 1:
#         tmp = str(int(word+str(j)))
#         if tmp[0] == '0':
#           continue
#         count+=1
#         if count == K:
#           print(tmp)
#           sys.exit()
#         if tmp not in ans:
#           ans.append(tmp)
#       if abs(int(word[0]) - j) <= 1:
#         if str(j) == '0':
#           continue
#         tmp = str(int(str(j)+word))
#         count+=1
#         if count == K:
#           print(tmp)
#           sys.exit()
#         if tmp not in ans:
#           print("append: {}".format(tmp))
#           ans.append(tmp)
#   anss.append(set(ans))
#   print(anss)

import sys
K = int(input())
anss = [[i for i in range(1,10)]]
count = 9
if K <= 9:
  print(K)
  sys.exit()
for i in range(1,15):
  ans = []
  # これは昇順に並んでいるはず
  origin = anss[i-1]
  for o in origin:
    s = str(o)
    for j in range(10):
      if abs(int(s[-1]) - j) <= 1:
        a = int(s+str(j))
        count += 1
        if count == K:
          print(a)
          sys.exit()
        ans.append(a)
  anss.append(ans)


