# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def decode(node: ListNode):
            i = 1
            while node is not None:
                yield node.val * i
                i *= 10
                node = node.next

        def encode(i: int):
            node = None
            next_node = None
            for val in str(i):
                node = ListNode(int(val))
                node.next = next_node
                next_node = node
            return node

        i1 = sum(decode(l1))
        i2 = sum(decode(l2))

        return encode(i1 + i2)
