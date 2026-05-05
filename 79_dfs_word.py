from typing import List

from collections import defaultdict, Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        letters = list(word)
        flat_nodes = []
        mapping = dict()
        start_variants = []
        nodes = defaultdict(list)
        for i, line in enumerate(board):
            for j in range(len(line)):
                if board[i][j] in letters:
                    nodes[board[i][j]].append((i, j))
                    flat_nodes.append((i, j))
                    mapping[(i, j)] = board[i][j]
                    
                if board[i][j] == letters[0]:
                    start_variants.append((i,j))
        let_c = Counter(word)
        for lt in let_c:
            if lt not in nodes or let_c[lt] > len(nodes[lt]):
                return False
        visited = []
        def dfs(g, node, visited, path):
            # print(f'dfs{node}')
            if node in visited:
                return False
            if not path:
                return True
            visited.append(node)
            for neighboor in flat_nodes:
                if (((neighboor[0] == node[0] and abs(neighboor[1] - node[1]) == 1) or
                        (neighboor[1] == node[1] and abs(neighboor[0] - node[0]) == 1)) and
                        neighboor not in visited and path[0] == mapping[neighboor]):
                    if dfs(g, neighboor, visited[:], path[1:]):
                        return True
            return False
        if not start_variants:
            return False
        for start_variant in start_variants:
            visited = []
            if dfs(flat_nodes, start_variant, visited[:], word[1:]):
                return True
        return False
                    

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

board = [
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"],
    ["A","A","A","A","A","A"]
]
word = "AAAAAAAAAAAAAAa"

a = Solution()
print(a.exist(board, word))