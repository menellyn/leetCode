# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        x = 1 
        num1 = 0
        num2 = 0

        while l1 or l2:
            if l1:
                num1 += l1.val*x
                l1 = l1.next

            if l2:
                num2 += l2.val*x
                l2 = l2.next

            x *= 10

        res = num1 + num2
        tmp = ListNode()
        head = tmp

        if res == 0:
            return head

        while res:
            n = res % 10
            res //= 10
            tmp.next = ListNode(val=n)
            tmp = tmp.next

        return head.next
