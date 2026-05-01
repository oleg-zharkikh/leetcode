"""133. Clone Graph"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self):
        return f'Node({self.val}, {[node.val for node in self.neighbors]})'


from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if not node.neighbors:
            return Node(node.val)
        g = dict()
        visited = set()
        queue = [node]
        while queue:
            current_node = queue.pop(0)
            visited.add(current_node.val)
            # print(f'Current node {current_node.val}. Added to visited')
            g[current_node.val] = [ngb.val for ngb in current_node.neighbors]
            for ngb in current_node.neighbors:
                # print(f'Current neighboor {ngb.val}...', end='')
                if ngb.val not in visited:
                    # print(f'adding for visiting')
                    queue.append(ngb)
        new_nodes = [Node(i+1) for i in range(len(g.keys()))]        
        for idx, node in enumerate(new_nodes, start=1):
            for node_num in g[idx]:
                node.neighbors.append(new_nodes[node_num-1])
        return new_nodes[0]


edges = [[2,4],[1,3],[2,4],[1,3]]

nodes = [Node(i+1) for i in range(len(edges))]
for idx, node in enumerate(nodes):
    for node_num in edges[idx]:
        node.neighbors.append(nodes[node_num-1])

print('input:')
for node in nodes:
    print(node)


s = Solution()
print(s.cloneGraph(nodes[0]))