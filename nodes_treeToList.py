class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
PSEUDOCODE:
- edge case:
    - if root is None, return -1
- in-order traversal: left --> root --> right
- vars:
    - stack, node_list
- append root to stack
- append root.data to node_list
- traverse stack while not None
    - .pop(0) on the stack
    - check if .left is not None
        - append .left to stack
        - append .left.data to node_list
    - check if .right is not None
        - append .right to stack
        - append. right.data to node_list
- return node_list
"""


def treeToListInOrderTraversal(root):
    if root is None:
        return []  # Return an empty list for an empty tree

    # Recursive traversal
    result = []

    # Recursive call to the left side returns a list of nodes in order
    leftSide = treeToListInOrderTraversal(root.left)
    result.extend(leftSide)  # Add the left side to the result list

    result.append(root.data)  # Add the root to the result list

    # Recursive call to the right side returns a list of nodes in order and we add it to the result list
    rightSide = treeToListInOrderTraversal(root.right)
    result.extend(rightSide)

    return result


# Test cases
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

print(treeToListInOrderTraversal(root))  # [3, 5, 7, 10, 12, 15, 18]
