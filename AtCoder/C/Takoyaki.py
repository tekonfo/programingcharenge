import sys
from collections import deque
T = int(input())
N = int(input())
items = list(map(int, input().split()))
M = int(input())
humans = list(map(int, input().split()))
item_queue = deque()
human_queue = deque()

# 各種追加
for i in items:
  item_queue.append(i)

for i in humans:
  human_queue.append(i)
  
# print("human: {}".format(human_queue))
# print("item: {}".format(item_queue))
  
# お客さんにたこ焼きを売る
while len(human_queue) > 0 and len(item_queue) > 0:
  i = human_queue[0]
  item = item_queue.popleft()
  if i < item:
    print("no")
    sys.exit()

  if i <= item + T:
    human_queue.popleft()
  # print("human: {}".format(human_queue))
  # print("item: {}".format(item_queue))

if(len(human_queue) > 0):
  print("no")
else:
  print("yes")