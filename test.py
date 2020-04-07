from fabric.colors import green
from collections import Counter
print(green("This text is green!"))
path = 'lorem.txt'

with open(path) as f:
    s = f.read()
    words = s.split()
    word_counts = Counter(words)
    over_two_counts = []
    for word,count in word_counts.items():
      if count >= 2:
        over_two_counts.append(word)
    print(over_two_counts)