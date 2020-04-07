import sys
from collections import Counter


def to_red(word):
  return "\033[41m" + word + "\033[0m"


args = sys.argv
path = args[1]

s = ""

with open(path) as f:
  s = f.read()

# 二回以上出てくる文字列を調べる
tmp_s = s.replace('.', '')
tmp_s = tmp_s.replace(',', '')
words = tmp_s.split()
word_counts = Counter(words)
over_two_counts = []
for word,count in word_counts.items():
  if count >= 2:
    over_two_counts.append(word)

# 出力
answer = []
is_dot = False
words = s.split()
for index in range(len(words)):
  word = words[index]
  if word in over_two_counts:
    word = to_red(word)
  # **. のように.や,で終わる文字列についても処理する
  elif word[-1] == '.' and word[:len(word)-1] in over_two_counts:
    word = to_red(word[:len(word)-1]) + '.'
  elif word[-1] == ',' and word[:len(word)-1] in over_two_counts:
    word = to_red(word[:len(word)-1]) + ','
  answer.append(word)

ans = ' '.join(answer)
print(ans)
  

