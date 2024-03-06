class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertIntoBST(root, data):
    if not root:
        return Node(data)

    if data < root.data:  # move to the left side of BST
        if root.left is None:  # insert a node there
            root.left = Node(data)
        else:
            insertIntoBST(root.left, data)

    elif data > root.data:  # move to the right side of BST
        if root.right is None:
            root.right = Node(data)
        else:
            insertIntoBST(root.right, data)

    return root


def findMax(root):
    if root is None:
        return None

    curr_node = root

    while (curr_node.right is not None):
        curr_node = curr_node.right

    return curr_node.data


# Test cases
root = None
root = insertIntoBST(root, 2)
root = insertIntoBST(root, 1)
root = insertIntoBST(root, 3)
root = insertIntoBST(root, 6)
root = insertIntoBST(root, 5)

print(findMax(root))
