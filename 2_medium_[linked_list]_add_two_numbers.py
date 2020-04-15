# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode(None)
        iterator = answer
        carry = 0

        node1 = l1
        node2 = l2
        while True:
            digit_val = carry

            if node1 is None and node2 is None:
                if digit_val == 0:
                    break
            elif node1 is None:
                digit_val += node2.val
                node2 = node2.next
            elif node2 is None:
                digit_val += node1.val
                node1 = node1.next
            else:
                digit_val += (node1.val + node2.val)
                node1 = node1.next
                node2 = node2.next

            carry, digit_val = divmod(digit_val, 10)

            iterator.next = ListNode(digit_val)
            iterator = iterator.next

        return answer.next