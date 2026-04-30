"""1466. Reorder Routes to Make All Paths Lead to the City Zero.

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
"""
from typing import List



class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = dict()
        g_reversed = dict()
        for node_from, node_to in connections:
            if node_from in g:
                g[node_from].add(node_to)
            else:
                g[node_from] = {node_to}
            if node_to in g_reversed:
                g_reversed[node_to].add(node_from)
            else:
                g_reversed[node_to] = {node_from}
        stack = [0]
        changes = 0
        visited = set()
        while stack:
            current_dest = stack.pop()
            visited.add(current_dest)
            neighbors = g.get(current_dest, set()) | g_reversed.get(current_dest, set())
            for ngb in neighbors:
                if ngb not in visited:
                    stack.append(ngb)
                    if current_dest in g_reversed.get(ngb, set()):
                        changes += 1
        return changes

n = 6

connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
s = Solution()
print(s.minReorder(n, connections))
