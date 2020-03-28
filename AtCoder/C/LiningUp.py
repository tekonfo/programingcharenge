import sys
"""
奇数の場合は0が一つと偶数番号が2個ずつ存在している
偶数の場合は奇数番号が2個ずつ並んでいる
それらの条件を満たす場合に、並び替えることが可能で、
"""

N = int(input())
L = list(map(int, input().split()))
number_dict = {}

for l in L:
  if l in number_dict:
    number_dict[l] += 1
  else:
    number_dict[l] = 1

if N%2 ==1:
  if 0 in number_dict and number_dict[0] != 1:
    print(0)
    sys.exit()
  number_dict.pop(0)
  ran = range(2, N, 2)
else:
  ran = range(1, N, 2)

# チェック
for i in ran:
  if i not in number_dict:
    print(0)
    sys.exit()
  if number_dict[i] != 2:
    print(0)
    sys.exit()
  number_dict.pop(i)


if len(number_dict.keys()) == 0:
  print(2**int(N/2))
else:
  print(0)