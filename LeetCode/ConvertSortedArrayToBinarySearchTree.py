# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = int(len(nums)/2)
        node = TreeNode(nums[mid])
        if mid > 0:
            node.left = self.sortedArrayToBST(nums[:mid])
        if mid < len(nums)-1:
            node.right = self.sortedArrayToBST(nums[mid+1:])
        return node