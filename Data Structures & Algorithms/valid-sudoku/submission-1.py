class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time taken: 

        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)

        for i in range(len(board)):
            row = board[i]
            
            for j in range(len(row)):
                if row[j] != ".":
                    rows[i].append(row[j])
                    cols[j].append(row[j])
                    boxes[(i // 3) * 3 + j // 3].append(row[j])
        
        print(boxes)
        for i in range(9):
            if len(cols[i]) != len(set(cols[i])) or len(rows[i]) != len(set(rows[i])) or  len(boxes[i]) != len(set(boxes[i])):
                return False

        return True