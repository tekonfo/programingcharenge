from typing import List
from queue import LifoQueue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class childTuple:
    def __init__(self, node, depth, is_start_right):
        self.node = node
        self.depth = depth
        self.is_start_right = is_start_right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 幅優先探索
        # スタックを使って実装するか
        queue = LifoQueue()
        dic = {}

        if root == None:
            return {}

        # rootの処理
        dic[0] = [root.val]
        queue.put(childTuple(root.left, 1, True))
        queue.put(childTuple(root.right, 1, True))

        while not queue.empty():
            tmp_queue = LifoQueue()
            while not queue.empty():
                node = queue.get()
                if node.node == None:
                    continue

                if node.depth in dic:
                    dic[node.depth].append(node.node.val)
                else:
                    dic[node.depth] = [node.node.val]

                if node.is_start_right:
                    tmp_queue.put(childTuple(node.node.right, node.depth+1, False))
                    tmp_queue.put(childTuple(node.node.left, node.depth+1, False))
                else:
                    tmp_queue.put(childTuple(node.node.left, node.depth+1, True))
                    tmp_queue.put(childTuple(node.node.right, node.depth+1, True))
            queue = tmp_queue

        ans = []
        for i in sorted(dic.keys()):
            ans.append(dic[i])
        return ans

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

print(sol.zigzagLevelOrder(node))