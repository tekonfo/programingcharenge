from collections import deque
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        found = [False] *(len(s)+1)
        found[0] = True
        for i in range(0, len(s)+1):
            for j in range(0, i):
                if found[j] and s[j:i] in words:
                    found[i] = True
        return found[len(s)] 

sol = Solution()
s = 'catsandog'
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s, wordDict))