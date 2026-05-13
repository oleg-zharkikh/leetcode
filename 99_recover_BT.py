from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        first = second = None
        prev = None

        def in_order(node: Optional[TreeNode]):
            nonlocal prev, first, second
            if not node:
                return
            in_order(node.left)

            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
            prev = node

            in_order(node.right)

        in_order(root)
        first.val, second.val = second.val, first.val



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
data=[3,1,4,null,null,2]

root = list_to_tree(data)

a = Solution()
a.recoverTree(root)
