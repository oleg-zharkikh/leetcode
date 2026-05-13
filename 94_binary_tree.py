from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result



from collections import deque
def list_to_tree(lst):
    
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    n = len(lst)

    while queue and i < n:
        node = queue.popleft()

        if i < n:
            val = lst[i]
            i += 1
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)

        # Правый потомок
        if i < n:
            val = lst[i]
            i += 1
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)

    return root



null = None
data=[1,2,3,4,5,null,8,null,null,6,7,9]

root = list_to_tree(data)

a = Solution()
print(a.inorderTraversal(root))