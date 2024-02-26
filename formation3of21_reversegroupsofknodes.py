class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverseInGroupsOfK(head, k):
    # your code here
    """
    PSEUDOCODE:
    - 
    """
    if head is None or head.next is None or k == 1:
        return head

    # we need 2 pointers, so that we can make changes to the pointers without loosing our position
    prev = head
    curr = prev.next

    # below is to ensure that the 1st node points to null when it's the last node after reversal
    prev.next = None

    # now count out k Nodes to reverse
    count = 1
    last = prev

    while (curr and count < k):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        count += 1

    # now, we've reversed up to k nodes
    # if there's anything remaining, reverse that and set it as the next node of the last of the current set

    if curr:
        last.next = reverseInGroupsOfK(curr, k)

    return prev
