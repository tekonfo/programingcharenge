from typing import List

# ブルートフォース
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0

#         select_amounts = []
#         for index in range(len(nums)):
#             tmp = [i for i in range(index, len(nums)) if nums[i] > nums[index]]
#             select_amounts.append(len(tmp))
    
#         count = 0

#         while True:
#             print(select_amounts)
#             index = select_amounts.index(max(select_amounts))
#             count += 1
#             if index == len(select_amounts) - 1 or select_amounts[index] == 0:
#                 return count
#             select_amounts = [num for num in select_amounts[index+1:] if num < select_amounts[index]]


# DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        lis = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] >= nums[j] and lis[i] <= lis[j]:
                    lis[i] = lis[j] + 1
        return max(lis)

sol = Solution()
nums = [4,10,4,3,8,9]
print(sol.lengthOfLIS(nums))