class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
    
    def __repr__(self):
        return f"Parent {self.parent if self.parent else None} Left {self.left.value if self.left else None}  Value {self.value} Right {self.right.value if self.right else None}"
    


class Heap:
    def __init__(self, root=None):
        self.root = root
    
    def insert_node(self, node):
        if not self.root:
            print(f"setting root to node {node}")
            self.root = node
            return

        print(f"root is {self.root}")
        order = [self.root]
        while order:
            current = order.pop(0)
            print(f"looking at {current}")
            if not current.left:
                print(f"current has no left, setting {current} left to {node}")
                current.left = node
                node.parent = current
                break
            if not current.right:
                print(f"current has no right, setting {current} right to {node}")
                current.right = node
                node.parent = current
                break
            order.append(current.left)
            order.append(current.right)

        self._bubble_up(node)


    def _bubble_up(self, node):
        while node:
            print(f"bubbling up {node}")
            parent = node.parent
            print(f"parent is {parent}")
            if parent and parent.value > node.value:
                print(f"swapping {parent} and {node}")
                parent.value, node.value = node.value, parent.value
                node = parent
            else:
                break


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

heap.insert_node(Node(1.1))
heap.insert_node(Node(1.3))


def print_tree(node, level=0):
    if not node:
        return

    print_tree(node.right, level + 1)

    print(" " * (4 * level) + f"{node.value}")

    print_tree(node.left, level + 1)

print_tree(heap.root)