import sys

S = input()
T = input()
alpha_map = {}
talpha_map = {}
for i in range(len(S)):
  s = S[i]
  t = T[i]
  if s in alpha_map.keys():
    if alpha_map[s] != t:
      print("No")
      sys.exit()
  if t in talpha_map.keys():
    if talpha_map[t] != s:
      print("No")
      sys.exit()
  alpha_map[s] = t
  talpha_map[t] = s
print("Yes")