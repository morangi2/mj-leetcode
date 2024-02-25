class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    # determine if there's a cycle
    def findIntersection(array1, array2):
        # put the nodes of array1 in a dict
        # rem to use dummy List nodes
        # traverse array2 while comparing with nodes in array1 in the dict
        # if equal, retrun that node

        vals = {}
        dummyA = array1
        dummyB = array2

        while dummyA:
            vals[dummyA] = dummyA.data
            dummyA = dummyA.next

        while dummyB:
            if dummyB in vals:
                return print(dummyB.data)
            dummyB = dummyB.next

        return None


# let's test using ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
b = ListNode(5, ListNode(6, ListNode(
    7, ListNode(8, ListNode(9)))))
print(ListNode.findIntersection(a, b))  # None
