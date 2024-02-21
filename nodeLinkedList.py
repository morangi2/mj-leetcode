# ILLUSTRAION: https://www.youtube.com/watch?v=WwfhLC16bis

class ListNode(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def countNodes(head):
        # assume head != null ... in this case, count
        count = 1
        current = head

        while (current.next != None):
            count += 1
            current = current.next

        return count


print(ListNode.countNodes(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))  # 4

# this is a singly linked list
# 1 -> 2 -> 3 -> 4 -> None

# for a doubly linked list, we would have a previous pointer, since it goes both ways
# 1 <-> 2 <-> 3 <-> 4 <-> None
# so the dunder init would be
# def __init__(self, data=0, next=None, previous=None):
#     self.data = data
#     self.next = next
#     self.previous = previous
