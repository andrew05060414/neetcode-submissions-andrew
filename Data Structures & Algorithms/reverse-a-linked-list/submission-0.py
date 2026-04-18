# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr: # 1 -> 2 -> 3 -> 4
            next_node = curr.next # next -> 2
            curr.next = prev  # 1 -> None
            prev = curr
            curr = next_node
        return prev
