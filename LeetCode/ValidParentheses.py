import queue

open_brackets = ['[', '{', '(']
close_brackets = [']', '}', ')']
brackets_sets = [('[', ']'), ('{', '}'), ('(', ')')]

class Solution:
  def isValid(self, s: str) -> bool:
    lifo_queue = queue.LifoQueue()
    for i in s:
      if i in open_brackets:
        lifo_queue.put(i)
      elif i in close_brackets:
        if lifo_queue.empty():
          return False
        last_open = lifo_queue.get()
        if not (last_open, i) in brackets_sets:
          return False
    if not lifo_queue.empty():
      return False
    return True

string = "{[]}"
sol = Solution()
if sol.isValid(string):
  print("true")
else:
  print("false")
