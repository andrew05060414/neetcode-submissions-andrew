# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # ----------------------
        # Step 1: 快慢指针找中点
        # ----------------------
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # ----------------------
        # Step 2: 反转后半段
        # ----------------------
        prev = None
        curr = slow.next  # 后半段的头
        slow.next = None  # 切断前后两段

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # ----------------------
        # Step 3: 交替合并两段
        # ----------------------
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2