from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check is the tree symmetric."""
        nodes = []        

        def in_order(node, nf):
            if not node:
                return
            in_order(node.left, 'l')
            nodes.append(f'{node.val}{nf}')
            in_order(node.right, 'r')
        in_order(root, '')
        X = lambda a, b: 0 if a[:-1] == b[:-1] and a[-1] != b[-1] else 1
        r = [X(nodes[i], nodes[len(nodes) - i - 1]) for i in range(len(nodes) // 2)]
        return all([i == 0 for i in r])


def print_tree(node):
    """In-order traversal and print the values of nodes."""
    if not node:
        return

    print_tree(node.left)
    print(node.val)
    print_tree(node.right)


def list_to_tree(data):
    """Make tree from the list of levels (leetcode test examples)."""
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
# d = [1,2,2,3,4,4,3]  # true
# d = [1,2,2,null,3,null,3]  # false
d = [1, 0]


root = list_to_tree(d)

a = Solution()

# print_tree(root)
print(a.isSymmetric(root))
