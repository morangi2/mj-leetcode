class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
PSEUDOCODE:
- edge cases:
    - if root is None ... return -1
- min values are always to the left...
- assign root to a temp curr node
- loop while curr.left node is not null
    - curr = curr.next
- return curr.data
"""


def findMin(root):
    if root is None:
        return -1

    curr_node = root

    while (curr_node.left is not None):
        curr_node = curr_node.left

    return curr_node.data


def findMax(root):
    if root is None:
        return -1

    curr_node = root

    while (curr_node.right is not None):
        curr_node = curr_node.right

    return curr_node.data


# Test cases
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

print(findMin(root))  # 3
print(findMax(root))  # 18
