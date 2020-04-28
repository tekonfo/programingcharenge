from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = Counter(nums)
        most_common = l.most_common()
        ans = []
        for i in range(k):
            ans.append(most_common[i][0])
        return ans
            
        