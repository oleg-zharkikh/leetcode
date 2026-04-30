"""841. Keys and Rooms.

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.   
"""


from typing import List


class Solution:
    @staticmethod
    def dfs(g, node, visited):
        if node in visited:
            return
        visited.add(node)
        keys = g[node]
        for room in keys:
            Solution.dfs(g, room, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        current_room = 0
        visited = set()
        Solution.dfs(rooms, current_room, visited)
        return len(visited) == len(rooms)


rooms = [[1,3],[3,0,1],[2],[0]]
s = Solution()
print(s.canVisitAllRooms(rooms))
