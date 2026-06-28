import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        subBoxes = {}
        
        for i in range(9):
            rows[i] = []
            cols[i] = []
            subBoxes[i] = []

        for i in range(9):  
            for j in range(9):
                if board[i][j] != '.':
                    rows.get(i).append(board[i][j])
                    cols.get(j).append(board[i][j])
                    subBoxes.get( math.floor(i / 3) * 3 + math.floor(j / 3) ).append(board[i][j])
        
        print(rows)
        print(cols)
        print(subBoxes)

        for i in range(9):
            if len(set(rows[i])) != len(rows[i]) or len(set(cols[i])) != len(cols[i])  or len(set(subBoxes[i])) != len(subBoxes[i]) :
                return False
        
        return True

        