class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""
PSEUDOCODE
- edge case;
    - if root is None, return 0
- recursively call maxDepth on the left node
- recursivelt call maxDepth on the right node
- check which one is greater, and return it + 1
"""


def maxDepthRecursive(root):

    if root is None:
        return 0

    left_depth = maxDepthRecursive(root.left)
    right_depth = maxDepthRecursive(root.right)

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1


"""
PSEUDOCODE for non-recursive
- edge case;
    - if root is None, return 0
- vars; stack, depth
- append root to the stack
- loop stack while not empty
    - get the number of nodes at the current level in the stack and store in a variable == len(stack)
    - loop through the nodes at the current level == nodeCountAtCurrentLevel > 0
        - pop(0) from the front of the stack
            - if node.left is not none
                -- append to stack
            - if node.right is not none
                -- append to stack
            - decrement nodeCountAtCurrentLevel by 1 so that we can move to the next node in this level
        - increment depth by 1
- return depth
"""


def maxDepth(root):

    if root is None:
        return 0

    stack = []
    depth_count = 0

    stack.append(root)

    while stack:
        nodeCountAtCurrentLevel = len(stack)

        while nodeCountAtCurrentLevel > 0:

            curr_node = stack.pop(0)

            if curr_node.left is not None:
                stack.append(curr_node.left)

            if curr_node.right is not None:
                stack.append(curr_node.right)

            nodeCountAtCurrentLevel -= 1

        depth_count += 1

    return depth_count


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(maxDepthRecursive(root))  # 3
print(maxDepth(root))
