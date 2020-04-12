from typing import List, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def appendVal(self, root: TreeNode, deep_level, dic) -> Dict:
        if deep_level in dic:
            dic[deep_level].append(root.val)
        else:
            dic[deep_level] = [root.val]

        if root.left != None:
            self.appendVal(root.left, deep_level + 1, dic)

        if root.right != None:
            self.appendVal(root.right, deep_level + 1, dic)
        
        return dic
        

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        dic = {}
        if root == None:
            return []
        
        dic = self.appendVal(root, 0, dic)
        ans = []
        for i in sorted(dic.keys()):
            ans.append(dic[i])
        return ans


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

print(sol.levelOrder(node))





        