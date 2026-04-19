# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 定义结果链表的虚拟头节点（非常好用，避免空指针）
        dummy = ListNode()
        current = dummy # current 用来往后拼接节点

    # 两个指针分别指向两个输入链表的头部
        p1 = list1
        p2 = list2

    # 只要两个指针都没走完，就继续比较
        while p1 != None and p2 != None:
            if p1.val < p2.val:
            # 取 p1 这个节点
                current.next = p1
                p1 = p1.next
            else:
            # 取 p2 这个节点
                current.next = p2
                p2 = p2.next
            
        # 结果链表的指针也往后走
            current = current.next

    # 一个链表走完了，把剩下的直接接上
        if p1 == None:
            current.next = p2
        else:
            current.next = p1

    # 返回真正的头节点
        return dummy.next