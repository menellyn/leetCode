# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = ListNode()
        l = new_head
        sz = 0
        tmp = head

        while tmp:
            sz += 1
            tmp = tmp.next

        ptr = head
        for _ in range(sz - n):
            new_head.next = ListNode(ptr.val)
            new_head = new_head.next
            ptr = ptr.next

        ptr = ptr.next

        for _ in range(n - 1):
            new_head.next = ListNode(ptr.val)
            new_head = new_head.next
            ptr = ptr.next

        return l.next