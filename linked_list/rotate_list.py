# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        
        tmp = head
        sz = 0
        while tmp:
            tmp = tmp.next
            sz += 1

        k = k % sz
        for _ in range(k):
            tmp = head
            while tmp.next.next:
                tmp = tmp.next

            prev = tmp
            last = tmp.next
            first = last
            first.next = head
            prev.next = None
            head = first

        return head