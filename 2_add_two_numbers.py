from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printl(head: ListNode, sep: str = ', '):
    node = head
    while node is not None:
        print(node.val, sep=sep)
        node = node.next
    print()


class Solution:
    """The solution of # 2 problem."""

    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """Add the two numbers and return the sum as a linked list."""
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        sum_number = ListNode(0, None)
        head = sum_number
        add_to_next = 0
        while l1 is not None or l2 is not None or add_to_next:
            sum_number.val = ((getattr(l1, 'val', 0)
                               + getattr(l2, 'val', 0) + add_to_next) % 10)
            add_to_next = int(
                ((getattr(l1, 'val', 0)
                  + getattr(l2, 'val', 0) + add_to_next) > 9))
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 is not None or l2 is not None or add_to_next:
                sum_number.next = ListNode(0, None)
                sum_number = sum_number.next
        return head


l1 = ListNode(3, None)
l2 = ListNode(4, l1)
l3 = ListNode(2, l2)
printl(l3)

p1 = ListNode(4, None)
p2 = ListNode(6, p1)
p3 = ListNode(5, p2)
printl(p3)
s = Solution()
h = s.addTwoNumbers(l3, p3)
printl(h)
