class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(root, key):
    if root is None:
        return None

    curr_node = root

    if curr_node.data == key:
        return curr_node.data

    elif curr_node.data < key:
        # check the right side recursively
        return search(curr_node.right, key)

    elif curr_node.data > key:
        # search the left side of node
        return search(curr_node.left, key)


# test the search function
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print(search(root, 7))
# 7

print(search(root, 20))
# 20

print(search(root, 10))
# 10

# edge case
print(search(root, 25))
# None
