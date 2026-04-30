"""547. Number of Provinces.

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

[[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""
from typing import List


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if isConnected is None or len(isConnected) == 0:
            return 0
        if len(isConnected) != len(isConnected[0]):
            return 0
        visited = set()
        groups = 0
        for g_node in range(len(isConnected)):
            if g_node in visited:
                continue
            stack = [g_node]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for neighbor in range(len(isConnected)):
                        if isConnected[node][neighbor] == 1:
                            stack.append(neighbor)
            groups += 1
        return groups


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
s = Solution()
print(s.findCircleNum(isConnected))
