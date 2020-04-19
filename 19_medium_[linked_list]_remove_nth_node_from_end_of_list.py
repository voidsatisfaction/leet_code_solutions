# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        iter1, iter2 = head, head

        for _ in range(n-1):
            if iter2 == None:
                return head

            iter2 = iter2.next

        before_iter1 = None
        while iter2.next is not None:
            before_iter1 = iter1
            iter1 = iter1.next
            iter2 = iter2.next

        if iter1 is head:
            # Same with the condition that iter1 is head node
            head = iter1.next
        elif n == 1:
            # Same with the condition that iter1 is tail node
            before_iter1.next = None
        else:
            # Same with the condition that iter1 is in the middle of nodes
            before_iter1.next = iter1.next
            
        return head