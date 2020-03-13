from typing import List

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    if n == 0:
      return []

    patterns = set()
    patterns.add("")
    for i in range(n):
      nextPatterns = set()
      for pat in patterns:
        if len(pat) == 0:
          nextPatterns.add("()")
          continue
        for index in range(len(pat)):
          # これ””の時大丈夫なのかは微妙
          nextPatterns.add(pat[:index] + "()" + pat[index:])
      patterns = nextPatterns
    return(list(patterns))
      
    

n = 10
sol = Solution()
print(sol.generateParenthesis(n))