# this one was tough, skipping to come back to it later
"""
PROMPT:
Given a binary tree, convert this to a doubly linked list in the order of the in-order traversal. 
This operation should be done in place, not creating any new data structure.
You must re-use the node's left pointer as the pointer to the previous node in the list 
and the right pointer should be the next node in the list.

At the end, return a pointer the first node in the list.
"""


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
PSEUDOCODE:
- edge cases..
- we'll attempt this recursively
- in-oder == left, root, right
- vars:
    result []
- recurs through left side; lSide = fn(root.left)
- extend result with lSide
- append result with node.data
- extend result with rSide
- return result
"""


def treeToListInOrderTraversal(root):
    if root is None:
        return []

    result = []

    leftSide = treeToListInOrderTraversal(root.left)
    result.extend(leftSide)

    result.append(root.data)

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

# space complexity: O(n) where n is the number of nodes in the tree because we are storing the nodes in a list and the list will have n elements
# time complexity: O(n) where n is the number of nodes in the tree because we are visiting each node once
