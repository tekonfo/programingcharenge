# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def calcMax(self, root: TreeNode, depth: int) -> int:
        print(root.val, depth)
        if root.left:
            left_max = self.calcMax(root.left, depth+1)
        else:
            left_max = depth

        if root.right:
            right_max = self.calcMax(root.right, depth+1)
        else:
            right_max = depth
        
        return max(left_max, right_max)

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.calcMax(root, 1)

sol = Solution()
node = TreeNode(0)
node1 = TreeNode(2)
node2 = TreeNode(4)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(-1)
node6 = TreeNode(5)
node7 = TreeNode(1)
node8 = TreeNode(6)
node9 = TreeNode(8)

node.left = node1
node.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.right = node8
node5.right = node9

print(sol.maxDepth(node))