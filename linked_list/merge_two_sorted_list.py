# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return list1

        tmp = ListNode()
        head = tmp

        while list1 or list2:
            if not list1:
                tmp.next = list2
                break
            elif not list2:
                tmp.next = list1
                break

            if list1.val < list2.val:
                tmp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tmp.next = ListNode(list2.val)
                list2 = list2.next

            tmp = tmp.next

        return head.next