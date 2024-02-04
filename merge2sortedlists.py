# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first, create a new ListNode object to serve as the head of the merged list
# then, create a new ListNode object to serve as the current pointer
# while list1 and list2 are not empty, compare the first elements of list1 and list2
# add the smaller of the two to the merged list
# move the current pointer to the next element
# repeat the process until list1 and list2 are empty
# add the remaining elements of list1 or list2 to the merged list
# return the merged list


def merge2SortedLists(list1, list2):
    head = ListNode()
    current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 or list2

    return head.next

# Time complexity: O(n + m)
# Space complexity: O(1)


print(merge2SortedLists([1, 2, 4], [1, 3, 4]))  # [1, 1, 2, 3, 4, 4]
