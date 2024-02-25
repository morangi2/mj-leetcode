"""
Given a linked list, delete the middle node. If the list is even length, delete the node at the start of the second half of the list.

/*
  * You may assume the node class is:
  
  * class LLNode {
  *   constructor(value, next = null) {
  *     this.value = value;
  *     this.next = next;
  *   }
  * }
  */

  """


class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def deleteMiddleNode(head):
    # your code here
    """
    PSEUDOCODE:
    - use the concept of slow and fast; slow moves one step, fast moves two steps ahead... when fast is at the end, slow will be in the middle
    - update the pointer of slow.next to be slow.next.next
    """

    slow = head
    fast = head

    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

    # at this point, fast is at the end, slow is in the middle
    slow.next = slow.next.next

    return head.next


# 1 -> 2 -> 4 -> 5
print(deleteMiddleNode(LLNode(1, LLNode(2, LLNode(3, LLNode(4, LLNode(5)))))))
