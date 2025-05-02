"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {None: None}
        tmp = head

        while tmp:
            hash[tmp] = Node(tmp.val)
            tmp = tmp.next

        tmp = head

        while tmp:
            copy = hash[tmp]
            copy.next = hash[tmp.next]
            copy.random = hash[tmp.random]
            tmp = tmp.next

        return hash[head]