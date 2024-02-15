class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# Time complexity: O(n)
# Space complexity: O(1)

# Example:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 5 -> 4 -> 3 -> 2 -> 1 -> None

# 1 -> 2 -> 3 -> 4 -> None
# 4 -> 3 -> 2 -> 1 -> None


print(reverseLinkedList([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
