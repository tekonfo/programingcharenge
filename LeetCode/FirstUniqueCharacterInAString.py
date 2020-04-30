from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == '':
            return -1
        l = Counter(s)
        for i in range(len(s)):
            if l[s[i]] == 1:
                return i
        return -1


sol = Solution()
s = "loveleetcode"
print(sol.firstUniqChar(s))