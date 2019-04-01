# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def decode(node: ListNode):
            i = 1
            while node is not None:
                yield node.val * i
                i *= 10
                node = node.next
        
        def encode(i: int):
            temp = None
            for val in str(i):
                node = ListNode(val)
                node.next = temp
                temp = node
            return node
        
        i1 = sum(decode(l1))
        i2 = sum(decode(l2))
        
        return encode(i1 + i2)


n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)
m1.next = m2
m2.next = m3

solution = Solution()
it = solution.addTwoNumbers(n1, m1)

while it.next is not None:
	print(it.val)
	it = it.next
print(it.val)