class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
PSEUDOCODE:
- use a stack to go through the binary tree
- var count: to count full nodes
- edge case:
    - if root is None, return o
- push root to the queue
- loop through queue while > 0
    - queue.pop() --> node
    - check if node has left and right nodes, if yes, increment count
    - if node.left is not None
        - count ++
        - push it into the stack
    - if node.right is not None
        - count ++
        - push it into the queue
    - return count

"""


def countFullNodesInBinaryTree(root):
    count = 0
    stack = []

    if root is None:
        return 0

    stack.append(root)

    while (len(stack) > 0):
        # curr_node = Node()

        curr_node = stack.pop(0)  # pop from the front of the list

        if curr_node.left is not None and curr_node.right is not None:
            count += 1

        if curr_node.left is not None:
            stack.append(curr_node.left)

        if curr_node.right is not None:
            stack.append(curr_node.right)

    return count


def countFullNodesInBinaryTreeRecursive(root):
    count = 0

    if root is None:
        return 0

    if (root.left and root.right):
        count += 1

    count += (countFullNodesInBinaryTreeRecursive(root.left) +
              countFullNodesInBinaryTreeRecursive(root.right))

    return count


# Test cases
# 1. Empty tree
print(countFullNodesInBinaryTree(None))  # 0
print(countFullNodesInBinaryTreeRecursive(None))  # 0


# 2. Tree with one node
root = Node(1)
print(countFullNodesInBinaryTree(root))  # 0
print(countFullNodesInBinaryTreeRecursive(root))  # 0


# 3. Tree with 3 nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(countFullNodesInBinaryTree(root))  # 1
print(countFullNodesInBinaryTreeRecursive(root))  # 1


# 4. Tree with 7 nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(countFullNodesInBinaryTree(root))  # 3
print(countFullNodesInBinaryTreeRecursive(root))  # 3

# 5. Tree with incomplete nodes
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6)
root.right.right = Node(7)
print(countFullNodesInBinaryTree(root))  # 2
print(countFullNodesInBinaryTreeRecursive(root))  # 2
