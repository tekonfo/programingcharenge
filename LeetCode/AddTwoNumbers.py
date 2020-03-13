from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ListNode2Arr(self, l: ListNode, arr: List) -> List:
        arr.insert(0, str(l.val))
        if l.next is not None:
            arr = self.ListNode2Arr(l.next, arr)
        return arr
    
    def Arr2ListNode(self, arr: List):
      root_node = ListNode(arr[0])
      arr.pop(0)
      prev_l = root_node
      for a in arr:
        l = ListNode(a)
        prev_l.next = l
        prev_l = l
      return root_node
      
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # まず、二つのリストを整数に変換する
        a1 = self.ListNode2Arr(l1, [])
        a2 = self.ListNode2Arr(l2, [])
        
        a1 = int(''.join(a1))
        a2 = int(''.join(a2))

        # 二つの整数を足し合わせる
        a3 = list(map(lambda x: int(x), list(str(a1 + a2))))
        a3.reverse()

        # リストを再変換する
        l3 = self.Arr2ListNode(a3)
        return l3

if __name__ == "__main__":
    a1 = ListNode(2)
    a2 = ListNode(4)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3

    b1 = ListNode(5)
    b2 = ListNode(6)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3

    sol = Solution()
    l3 = sol.addTwoNumbers(a1, b1)