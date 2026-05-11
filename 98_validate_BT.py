from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return None
        
        def dfs_check(node: Optional[TreeNode], lt: int = None, gt: int = None):
            print(f'{node.val=} {lt=} {gt=}' if node else '')
            if node is None:
                return True
            if lt is not None and node.val >= lt:
                return False
            if gt is not None and node.val <= gt:
                return False
            if node.left and (node.left.val >= node.val):
                return False

            if node.right and (node.right.val <= node.val):
                return False
                
            if dfs_check(node.left, lt=min(node.val, lt) if lt else node.val, gt=gt) is False:
                return False
            if dfs_check(node.right, lt=lt, gt=max(node.val, gt) if gt else node.val)  is False:
                return False
            return True
        
        
        return dfs_check(root)



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
data=[5,4,6,null,null,3,7]

root = list_to_tree(data)

a = Solution()
print(a.isValidBST(root))