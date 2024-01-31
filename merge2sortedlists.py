class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(l1, l2):

        l1: ListNode
        l2: ListNode
        # rtype: ListNode

        head = ListNode()
        current = head

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next  # advance current at the end of each loop

        current.next = l1 or l2  # if l1 is not empty, current.next = l1, else current.next = l2

        return head.next


""" def arrtolinkedlist(arr):
    res = [ListNode(x) for x in arr]
    for i in range(len(res) - 1):
        res[i].next = res[i + 1]
    return res[0]

ln1 = arrtolinkedlist(array1)

ln2 = arrtolinkedlist(array2) """

    array1 = [1, 2, 4]
    array2 = [1, 3, 4]

    print(Solution().mergeTwoLists(array1, array2))
    # to run use: python3 merge2sortedlists.py
