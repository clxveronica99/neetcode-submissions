import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        columns = collections.defaultdict(set)
        for r in range(9):
            row = set()
            for c in range(9):
                curr = board[r][c]
                if curr != '.':
                    if curr in row:
                        return False
                    if curr in columns[c]:
                        return False
                    row.add(curr)
                    columns[c].add(curr)
        

        groups = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                i, j = r//3, c//3
                curr = board[r][c]
                if curr != '.':
                    if curr in groups[(i, j)]:
                        return False
                    groups[(i, j)].add(curr)
        return True
        

                
        