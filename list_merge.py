
class LinkedList:
  
    def __init__(self):
        self.head = None
        self.tail = None

    def iterate(self):
        print('--Start iterate--')
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_item
        print('--End iterate--')

    def append(self, value):
        new_node = Node(value)
        if self.tail is not None:
            self.tail.next_item = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if value == current_node.value:
                return True
            current_node = current_node.next_item
        return False

    def get_value_by_index(self, index):
        if self.head is None:
            return
        current_node = self.head
        index_counter = 0
        while index_counter < index:               
            index_counter += 1
            current_node = current_node.next_item
            if current_node is None:
                return
        return current_node.value
            
    def remove(self, index):
        if self.head is None:
            return
        current_node = self.head
        if index == 0:
            self.head = self.head.next_item
        else:
            index_counter = 0
            while index_counter < index:               
                index_counter += 1
                previous_node = current_node
                current_node = current_node.next_item
                if current_node is None:
                    return
            previous_node.next_item = current_node.next_item

        del current_node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def iterate(self,node:ListNode):
        print('--Start iterate--')
        current_node = node
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next_item
        print('--End iterate--')

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        



node2 = ListNode(4, None)
node1 = ListNode(2, node2)
node0 = ListNode(1, node1)

n2 = ListNode(4, None)
n1 = ListNode(3, n3)
n0 = ListNode(1, n2)

a = Solution()
a.mergeTwoLists(node0, n0)