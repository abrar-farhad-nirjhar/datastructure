class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Left {self.left.value if self.left else None}  Value {self.value} Right {self.right.value if self.right else None}"
    


class Heap:
    def __init__(self, root=None):
        self.root = root

    
    def insert_node(self, node, order):
        if not self.root:
            self.root = node
            return
        
    def __iter__(self):
        order = [self.root]
        while order:
            current = order.pop(0)
            if current.left:
                order.append(current.left)
            if current.right:
                order.append(current.right)
            yield current


heap = Heap()


for i in range(10):
    heap.insert_node(Node(i))

heap.insert_node(Node(-1))

def print_tree(node, level=0):
    if not node:
        return
    
    print_tree(node.right, level+1)
    print(" "*level, node.value)
    print_tree(node.left, level+1)

print_tree(heap.root)
