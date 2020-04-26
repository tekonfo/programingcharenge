from collections import deque
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque([])
        for index in range(len(nums)):
            if nums[index] == 0:
                queue.append(index)
            elif nums[index] != 0 and len(queue) != 0:
                i = queue.popleft()
                tmp = nums[index]
                nums[index] = 0
                nums[i] = tmp
                queue.append(index)
                            
sol = Solution()
nums = [0,0,0,0,4,5,6]
sol.moveZeroes(nums)