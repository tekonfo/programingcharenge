class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        def get_max(nums: List[int]) -> int:
            anss = [0 for _ in range(len(nums))]
            anss[0] = nums[0]
            anss[1] = max(nums[0],nums[1])
            for index in range(2, len(nums)):
                anss[index] = max(anss[index-1], anss[index-2] + nums[index])
            return max(anss)
        return max(get_max(nums[:-1]),get_max(nums[1:]))
        
            
            
            