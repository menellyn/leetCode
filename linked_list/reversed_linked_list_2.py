# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        new_list = ListNode()
        new_head = new_list
        i = 1
        while head:
            while i <= right and i >= left:
                if i == left:
                    left_node = ListNode(head.val)
                    new_list.next = left_node
                    head = head.next
                elif i == right:
                    node = ListNode(head.val)
                    node.next = new_list.next
                    new_list.next = node
                    head = head.next
                    new_list = left_node
                else:
                    node = ListNode(head.val)
                    node.next = new_list.next
                    new_list.next = node
                    head = head.next
                i += 1
            if head:
                new_list.next = ListNode(head.val)
                head = head.next
                new_list = new_list.next
                i += 1

        return new_head.next