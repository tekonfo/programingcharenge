# 逆から読んでみる
# ちょっと休憩


def check(string):
  l = len(string)

  if l == 0:
    return True
  
  if l < 5:
    return False

  if string[0:5] == 'dream':
    if check(string[5:]):
      return True
    if l >= 7 and string[0:7] == 'dreamer':
      if check(string[7:]):
        return True
  elif string[0:5] == 'erase':
    if check(string[5:]):
      return True
    if l >= 6 and string[0:6] == 'eraser':
      if check(string[6:]):
        return True
  
  return False

S = input()
if check(S):
  print("YES")
else:
  print("NO")
