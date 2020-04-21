from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # inflection point is key
        left = 0
        right = len(nums)-1
        while left != right:
            if nums[left] < nums[right]:
                return nums[left]
            print(left,right)
            mid_index = int((left+right)/2)
            print(mid_index)
            if mid_index == len(nums) - 1 and nums[mid_index-1] > nums[mid_index]:
                return nums[mid_index]
            if mid_index == 0 and nums[mid_index] < nums[mid_index+1]:
                return nums[mid_index]
            if 0 < mid_index < len(nums) - 1 and nums[mid_index] < nums[mid_index+1] and nums[mid_index-1] > nums[mid_index]:
                return nums[mid_index]
            if nums[mid_index] >= nums[left]:
                left = mid_index + 1
            else:
                right = mid_index - 1
        print(left)
        return nums[left]


sol = Solution()
nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums))