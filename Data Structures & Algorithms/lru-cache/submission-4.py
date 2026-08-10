class Node:
    def __init__(self, key: int, val: int):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left   
   
    # we insert from the right
    def insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next        

    # we delete from the leftmost
    # --> i was wrong, we remove the actual node
    def delete(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next 
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.delete(node)
        self.insert(node)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            nodeToDel = self.left.next
            self.delete(nodeToDel)
            del self.cache[nodeToDel.key]
        
        
