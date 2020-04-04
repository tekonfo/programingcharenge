S=input()
K=int(input())
l = []
for alpha in [chr(i) for i in range(97, 97+26)]:
  indexs = [k for k, v in enumerate(list(S)) if v == alpha]
  for index in indexs:
    for j in range(index,min(index+6,len(S)+1)):
      sub_s = S[index:j]
      l.append(sub_s)
  l = sorted(list(set(l)))
  if '' in l:
    l.remove('')
  if len(l) >= K:
    break
print(l[K-1])
