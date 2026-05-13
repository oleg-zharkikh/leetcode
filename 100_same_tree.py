from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        the_same = True
        def in_order(node_1: Optional[TreeNode], node_2: Optional[TreeNode]):
            nonlocal the_same
            if not the_same:
                return
            if not node_1 and not node_2:
                return
            elif (not node_1 and node_2) or (node_1 and not node_2):
                the_same = False
                return

            in_order(node_1.left, node_2.left)

            if node_1.val != node_2.val:
                the_same = False
                return

            in_order(node_1.right, node_2.right)

        in_order(p, q)
        return the_same


def print_tree(node):
    if not node:
        return

    print_tree(node.left)
    print(node.val)
    print_tree(node.right)


    
def list_to_tree(data):
    
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    queue = [root]
    current_item = 1
    n = len(data)

    while queue and current_item < n:
        node = queue.pop(0)

        if current_item < n:
            value = data[current_item]
            current_item += 1
            if value is not None:
                node.left = TreeNode(value)
                queue.append(node.left)

        if current_item < n:
            value = data[current_item]
            current_item += 1
            if value is not None:
                node.right = TreeNode(value)
                queue.append(node.right)
    return root


null = None
p = [1,2]
q = [1,null,2]


p_bt = list_to_tree(p)
q_bt = list_to_tree(q)

a = Solution()

print(a.isSameTree(p_bt, q_bt))
