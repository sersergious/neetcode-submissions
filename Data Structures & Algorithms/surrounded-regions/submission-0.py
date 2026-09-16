class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        unsurrounded = set()

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or (r, c) in unsurrounded or board[r][c] != 'O'):
                return
            
            unsurrounded.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        # capture all unsurrounded 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in (0, ROWS - 1) or c in (0, COLS - 1)):
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in unsurrounded:
                    board[r][c] = "X"

                    

