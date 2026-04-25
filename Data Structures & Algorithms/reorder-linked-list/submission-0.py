# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        listn = []
        curr = head

        while curr:
            listn.append(curr)
            curr = curr.next
        
        # now we have a list of nodes, link them back
        l = 0
        r =len(listn)-1

         # 2. 从头开始，两两互相接
        while l < r:
            # 左边 接 右边
            listn[l].next = listn[r]
            # 左指针前进
            l += 1
            # 右边 接 新的左边
            listn[r].next = listn[l]
            # 右指针后退
            r -= 1
        
        # 关键：最后中点节点断掉，避免成环
        listn[l].next = None