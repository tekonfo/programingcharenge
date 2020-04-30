from typing import List
from queue import PriorityQueue

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        pq = PriorityQueue()
        
        for n1 in nums1:
            if not pq.empty() and k <= 0 and n1 + nums2[0] > -(pq.queue[0][0]):
            # Early break for nums1 if n1 + nums2[0] > top element in max heap
            # i.e. all other combinations after n1 and nums2[0] are also greater
            # so no need to iterate them
                break
            for n2 in nums2:
                if k > 0:
                    pq.put((-(n1 + n2), n1, n2))
                    k -= 1
                else:
                    topSum = -(pq.queue[0][0])
                    if n1 + n2 < topSum:
                        pq.get()
                        pq.put((-(n1 + n2), n1, n2))
                    else:
                        # All other combinations of n1 and elements of nums2 are greater so stop early
                        break
                        
        res = []
        while not pq.empty():
            sum, n1, n2 = pq.get()
            res.append([n1, n2])
            
        return res


nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10

sol = Solution()
print(sol.kSmallestPairs(nums1, nums2, k))        