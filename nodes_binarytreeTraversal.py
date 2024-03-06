class Node (object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if value <= self.data:
            # check if left node is empty, and if it is, insert the value
            if self.left is None:
                self.left = Node(value)
            # else if it's not empty, recursively call the insert method on the left node
            else:
                self.left.insert(value)
        else:  # value is greater than self.data AKA root node
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        # check if val is equal to the root node
        if value == self.data:
            return True
        # check if val is less than the root node a) if left node is empty, return False, b) else recursively call contains on the left node
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        # check if val is greater than the root node a) if right node is empty, return False, b) else recursively call contains on the right node
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    # in order traversal: left, root, right
    # pre order traversal: root, left, right
    # post order traversal: left, right, root
    def printInOrder(self):
        if self.left:
            # print(self.left.data)
            self.left.printInOrder()

        print(self.data)

        if self.right:
            # print(self.right.data)
            self.right.printInOrder()

    # this is a breadth first search, using a queue, to traverse the tree, level by level, from left to right, and print the nodes, starting from the root
    def countFullNodesIterative(root):
        # PSEUDOCODE
        """
        - check edge caase
        - create a count and a queue, and immediately append root to it
        - loop while queue is >0
            - node = queue.pop(0) ... get the FIFO element
            - check if node has .left and .right
                - if yes, add 1 to count
            - check if node has .left and .right and append them to the queue
        - return count

        """
        # Base Case
        if root is None:
            return 0

        # Create an empty queue for level order traversal
        queue = []

        # Enqueue Root and initialize count
        queue.append(root)

        count = 0  # initialize count for full nodes
        while (len(queue) > 0):
            node = queue.pop(0)

            # if it is full node then increment count
            if node.left is not None and node.right is not None:
                count = count+1

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)

        return count

    """ 
    Let us create Binary Tree as shown  
    """


root = Node(13)
root.left = Node(10)
root.right = Node(12)
root.left.right = Node(8)
root.left.right.left = Node(5)
root.left.right.right = Node(9)
root.right.right = Node(13)
root.right.right.left = Node(12)

print(Node.countFullNodesIterative(root))
