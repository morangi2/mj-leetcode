class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
QUESTION:
Given a binary tree, find the height, that is the length of the path from the root to the deepest leaf node.
"""

"""
PSEUDOCODE:
- BFS
- Edge cases:
    - if root is None... return 0
    - if root.left is None and root.right is None ... return 1
- vars:
    - stack; to hold the node data in a FIFO order (.pop(0))
    - curr == root ... to traverse the tree
    - count = 0... to count depth
- append root to stack
- loop while stack is not None:
    - .pop(0) on stack to get node that was inserted first
    - if node.left AND node.right:
        - increment count
    - if node.left:
        - append node.left to stack
    - if node.right is not None:
        - append node.riht to stack
    
- return count
        
"""


def treeHeightRecursive(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    lSide = treeHeightRecursive(root.left)
    rSide = treeHeightRecursive(root.right)

    result = 1 + max(lSide, rSide)

    return result


def treeHeight(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    stack = []
    count = 0

    stack.append(root)

    while stack:
        node_count_at_current_level = len(stack)

        while node_count_at_current_level > 0:  # there's at least one node at the current level, loop through them

            curr_node = stack.pop(0)

            if curr_node.left is not None:
                stack.append(curr_node.left)

            if curr_node.right is not None:
                stack.append(curr_node.right)

            node_count_at_current_level -= 1

        count += 1

    return count

# test cases
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /
# 6
# height = 4
# 1 -> 2 -> 4 -> 6


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(6)
root.left.right = Node(5)
print(treeHeight(root))  # 4
print(treeHeightRecursive(root))

#       1
#      / \
#     2   3
#    / \
#   4   5
#  /
# 6
#  \
#   7
# height = 5
# 1 -> 2 -> 4 -> 6 -> 7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(6)
root.left.right = Node(5)
root.left.left.left.right = Node(7)
print(treeHeight(root))  # 5
print(treeHeightRecursive(root))  # 5

# edge case
root = None
print(treeHeight(root))  # 0
print(treeHeightRecursive(root))

# edge case
root = Node(1)
print(treeHeight(root))  # 1
print(treeHeightRecursive(root))

# edge case
root = Node(1)
root.left = Node(2)
print(treeHeight(root))  # 2
print(treeHeightRecursive(root))
