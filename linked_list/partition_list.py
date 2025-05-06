# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ge_head = ListNode()
        lt_head = ListNode()
        ge_tmp = ge_head
        lt_tmp = lt_head

        while head:
            if head.val < x:
                lt_tmp.next = ListNode(head.val)
                lt_tmp = lt_tmp.next
            else:
                ge_tmp.next = ListNode(head.val)
                ge_tmp = ge_tmp.next

            head = head.next

        lt_tmp.next  = ge_head.next

        return lt_head.next