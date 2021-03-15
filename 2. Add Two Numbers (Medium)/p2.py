# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = ListNode()
        n = s
        x = 0
        while l1 or l2:
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next
            if x >= 10:
                n.val = x - 10
                x = 1
            else:
                n.val = x
                x = 0
            if l1 or l2:
                n.next = ListNode()
                n = n.next
        if x == 1:
            n.next = ListNode()
            n = n.next
            n.val = x
        return s
