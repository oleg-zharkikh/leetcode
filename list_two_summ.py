

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printl(n:ListNode):
    node = n
    while node != None:
        print(node.val, sep='')
        node = node.next
    print()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        nn = head
        h1 = l1
        h2 = l2
        flag = False
        while h1 != None and h2 != None:
            cv = h1.val + h2.val
            if flag:
                cv += 1
                flag = False
            if cv > 9:
                flag = True
                cv = cv - 10
            nn.val = cv
            if h1.next != None and h2.next != None:
                nn.next = ListNode()
           
            nn = nn.next
            h1 = h1.next
            h2 = h2.next
        cn = None
        if h1 != None:
            cn = h1
            nn.next = ListNode()
            nn = nn.next
        elif h2 != None:
            cn = h2
            nn.next = ListNode()
            nn = nn.next
        while cn != None:
            cv = cn.val
            if flag:
                cv += 1
                flag = False
            if cv > 9:
                flag = True
                cv = cv - 10
            nn.val = cv
            if cv.next != None:
                nn.next = ListNode()
            nn = nn.next
            cn = cn.next
        return head

l1 = ListNode(3, None)
l2 = ListNode(4, l1)
l3 = ListNode(2, l2)
printl(l3)

p1 = ListNode(4, None)
p2 = ListNode(6, p1)
p3 = ListNode(5, p2)
s = Solution()
h = s.addTwoNumbers(l3,p3)

printl(h)