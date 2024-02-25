class ListNode(object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    # determine if there's a cycle
    def cycle(head):
        slow = head
        fast = head
        met = False

        # checks if fast is not empty and fast.next is not empty
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                met = True
                return met

        return met

    def cycleMeetPoint(head):
        slow = head
        fast = head
        met = False

        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                met = True
                break

        if not met:
            return None
        else:
            slow = head
            while (slow != fast):
                slow = slow.next
                fast = fast.next

        return slow


print(ListNode.cycle(ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5)))))))  # False
print(ListNode.cycleMeetPoint(ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5)))))))  # None

# true case
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b

print(ListNode.cycle(a))  # True
print(ListNode.cycleMeetPoint(a).data)  # 2

# this is also known as Floyd's cycle-finding algorithm
# ILLUSION: https://www.youtube.com/watch?v=PvrxZaH_eZ4
