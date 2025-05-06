class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._head = self.Node(-1, -1)
        self._tail = self.Node(-1, -1)
        self._head.next = self._tail
        self._tail.prev = self._head

    def insert(self, node) -> None:
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

    def remove(self, node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self._cache:
            node = self._cache[key]
            self.remove(node)
            self.insert(node)
            self._cache[key] = self._head.next
            return node.val  
        return -1    
        
    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            self.remove(node)
        elif len(self._cache) == self._capacity:
            deleted = self._tail.prev
            del self._cache[deleted.key]
            self.remove(deleted)

        self.insert(self.Node(key, value))
        self._cache[key] = self._head.next
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)