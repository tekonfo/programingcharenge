from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 全然わからんかった
"""
The key idea here is that, for any given node, 
the number of pre-order nodes that must be sent to the recursive call of the left-subtree can be limited(subsetted) 
by using the number of nodes you find to the left of the current node from the in-order list.
The same applies for the right-subtree call as well.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        node = TreeNode(preorder[0])
        inorder_idx = inorder.index(preorder[0])
        preorder_idx = inorder_idx+1
        
        node.left = self.buildTree(preorder[1:preorder_idx], inorder[0:inorder_idx])
        node.right = self.buildTree(preorder[preorder_idx:], inorder[inorder_idx+1:])
        
        
        return node

sol = Solution()
node = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

node.left = node1
node.right = node2
node2.left = node3
node2.right = node4
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol.buildTree(preorder, inorder)