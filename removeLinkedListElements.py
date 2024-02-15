
def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """

    # create a dummy node at the very beginning of the given linked list in case the head node needs to be removed
    temp = ListNode(0)
    # the next val will be the head of the linked list
    temp.next = head
    # we start at the head aka curr == head
    curr = head
    # prev is the temp node
    prev = temp

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next

    return temp.next
