from itertools import product
S = input()
len_s = len(S)
patterns = product([0,1], repeat=len(S) - 1)

ans = 0

for pattern in patterns:
  tmp_st = ''
  for i in range(len_s):
    tmp_st += S[i]
    if i <= len_s-2 and pattern[i]:
      ans += int(tmp_st)
      tmp_st = ''
  ans += int(tmp_st)

print(ans)

