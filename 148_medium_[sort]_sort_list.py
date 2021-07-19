class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        mid = self._get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self._merge(left, right)

    def _merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = tail = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1

        return head.next

    def _get_mid(self, head: ListNode) -> ListNode:
        mid_previous = None
        while head and head.next:
            mid_previous = head if mid_previous is None else mid_previous.next
            head = head.next.next
        mid = mid_previous.next
        mid_previous.next = None
        return mid
