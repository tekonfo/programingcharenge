from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dicts = {}
    for word in strs:
      sort_word = ''.join(sorted(word))
      print(sort_word)
      if sort_word in dicts:
        dicts[sort_word].append(word)
      else:
        dicts[sort_word] = [word]
    return list(dicts.values())

lists = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(lists))