# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
                dummy = node = ListNode()

                while list1 and list2:
                    if list1.val < list2.val:
                        node.next = list1
                        list1 = list1.next
                    else:
                        node.next = list2
                        list2 = list2.next
                    node = node.next

                node.next = list1 or list2

                return dummy.next
            while len(lists)>1:
                merged = []
                for i in range(0, len(lists), 2):
                    print(i, len(lists))
                    l1 = lists[i] 
                    l2 = lists[i+1] if i+1 <len(lists) else None

                    merged.append(mergeTwoLists(l1, l2))
                lists = merged

            
            return lists[0] if lists else None