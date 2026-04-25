# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 虚拟头节点：防止删除第一个节点出错
        dummy = ListNode()
        dummy.next = head
        
        # 快慢指针都从 dummy 开始
        fast = dummy
        slow = dummy
        
        # ----------------------
        # 第一步：快指针先走 n 步
        # ----------------------
        for i in range(n):
            fast = fast.next
        
        # ----------------------
        # 第二步：一起走，直到快指针到底
        # ----------------------
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        # ----------------------
        # 第三步：删除节点
        # ----------------------
        slow.next = slow.next.next
        
        return dummy.next